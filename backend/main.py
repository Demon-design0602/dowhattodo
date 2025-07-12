import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import firebase_admin
from firebase_admin import credentials, firestore, auth
from datetime import datetime
import PIL.Image
from io import BytesIO

# --- Main Application Setup ---

# Initialize Flask App
app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

# Initialize Gemini API
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
    print("Gemini API configured successfully.")
except (KeyError, AttributeError):
    print("WARNING: Gemini API key not set.")
    model = None

# Initialize Firebase Admin SDK
try:
    # Use an absolute path to find the key file, which is more robust
    script_dir = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(script_dir, 'serviceAccountKey.json')
    
    if os.path.exists(key_path):
        cred = credentials.Certificate(key_path)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        print("Firebase Admin SDK configured successfully.")
    else:
        print("WARNING: serviceAccountKey.json not found. Running without Firebase.")
        db = None
except Exception as e:
    print(f"WARNING: Could not initialize Firebase Admin SDK: {e}")
    print("Running without Firebase authentication and storage.")
    db = None

@app.route('/')
def health_check():
    return "OK"

@app.route('/analyze', methods=['POST'])
def analyze_image():
    # First, check if the services are available
    if model is None:
        return jsonify({'error': 'The Gemini API is not configured on the server.'}), 503
    
    # Check if running in local development mode (no Firebase)
    local_dev_mode = db is None or os.environ.get('FLASK_ENV') == 'development'
    uid = "local_user"  # Default for local development
    
    if not local_dev_mode:
        # Production mode - require authentication
        if db is None:
            return jsonify({'error': 'The Firebase Database is not configured on the server.'}), 503
        
        # Get the user's ID token from the request header
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"error": "Missing or invalid Authorization header"}), 401
            
        id_token = auth_header.split('Bearer ')[1]
        try:
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token['uid']
        except Exception as e:
            return jsonify({"error": f"Unauthorized or invalid token: {e}"}), 401

    # Now, check for the image and prompt
    if 'prompt' not in request.form or 'image' not in request.files:
        return jsonify({'error': 'Missing prompt or image in the request.'}), 400

    prompt = request.form['prompt']
    image_file = request.files['image']

    try:
        # Open the image using Pillow to make sure it's valid.
        img = PIL.Image.open(image_file.stream)
    except Exception as e:
        return jsonify({'error': f'Invalid image file: {e}'}), 400

    try:
        # Send the prompt and image to the Gemini API.
        # Set temperature to 0 for deterministic, consistent results
        generation_config = {"temperature": 0.0}
        response = model.generate_content([prompt, img], generation_config=generation_config)
        response_text = response.parts[0].text

        # Find and parse the JSON from the model's response.
        print(f"Gemini response: {response_text}") # DEBUGGING
        try:
            # First, try to find a JSON code block
            start_index = response_text.find('```json')
            if start_index != -1:
                start_index += len('```json')
                end_index = response_text.rfind('```')
                json_string = response_text[start_index:end_index].strip()
            else:
                # If no code block, fall back to finding the first and last curly braces
                start_index = response_text.find('{')
                end_index = response_text.rfind('}')
                if start_index == -1 or end_index == -1:
                    raise ValueError("Could not find a valid JSON object in the Gemini response.")
                json_string = response_text[start_index:end_index+1]

            data = json.loads(json_string)
        except (json.JSONDecodeError, ValueError) as e:
            raise ValueError(f"Error parsing JSON from Gemini response: {e}") from e
        
        # Save the result to Firestore
        if db is not None:
            try:
                # Create a new document in the 'history' collection for the user
                doc_ref = db.collection('users').document(uid).collection('history').document()
                doc_ref.set({
                    "timestamp": datetime.utcnow(),
                    "results": data
                })
                print(f"Successfully saved analysis for user {uid}")
            except Exception as e:
                print(f"Error saving to Firestore: {e}") # Log error but don't fail the request

        # Return the parsed data as a proper JSON response.
        return jsonify(data)
    except Exception as e:
        # This will catch errors during the API call itself.
        return jsonify({'error': f'Error during Gemini API call: {e}'}), 500

@app.route('/history')
def history():
    if db is None:
        return jsonify({"error": "The Firebase Database is not configured on the server."}), 503

    try:
        id_token = request.headers.get('Authorization').split('Bearer ')[1]
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
    except Exception as e:
        return jsonify({"error": f"Unauthorized or invalid token: {e}"}), 401

    try:
        history_ref = db.collection('users').document(uid).collection('history').order_by('timestamp', direction=firestore.Query.DESCENDING).stream()
        history_data = [doc.to_dict() for doc in history_ref]
        return jsonify(history_data)
    except Exception as e:
        return jsonify({"error": f"Error fetching history: {e}"}), 500


# --- Server Start ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

