document.addEventListener('DOMContentLoaded', () => {
    const getStartedBtn = document.getElementById('get-started-btn');
    const imageUpload = document.getElementById('image-upload');
    const heroSection = document.querySelector('.hero');
    const resultsSection = document.getElementById('results-section');
    const resultsContainer = document.getElementById('results-container');
    const analyzeAnotherBtn = document.getElementById('analyze-another-btn');
    const spinnerOverlay = document.getElementById('spinner-overlay');

    const PROMPT = `
    Analyze the facial symmetry and features of the person in this image.
    IMPORTANT: If the image does not contain a clear human face, you MUST respond with only the following JSON object and nothing else: {"error": "No human face was detected in the image."}
    
    If a human face is present, provide a response in JSON format with the following structure:
    {
      "score": <an integer between 1 and 100>,
      "summary": "<a brief, one-sentence summary of the analysis>",
      "analysis_points": [
        {
          "title": "<short title for the analysis point>",
          "description": "<a detailed paragraph explaining the analysis point>"
        },
        {
          "title": "<short title for a second analysis point>",
          "description": "<a detailed paragraph for the second point>"
        }
      ]
    }
    `;

    function showSpinner(show) {
        spinnerOverlay.classList.toggle('is-hidden', !show);
    }

    function displayErrorBox(errorMessage) {
        resultsContainer.innerHTML = ''; // Clear previous results
        
        const errorBox = document.createElement('div');
        errorBox.className = 'error-box';
        
        errorBox.innerHTML = `
            <div class="error-icon">🚫</div>
            <div class="error-title">No Human Face Detected</div>
            <div class="error-message">${errorMessage}</div>
            <div class="error-suggestions">
                <h4>💡 Tips for Better Results:</h4>
                <ul>
                    <li>Make sure the image contains a clear human face</li>
                    <li>Ensure good lighting in the photo</li>
                    <li>Face should be facing forward (not profile)</li>
                    <li>Remove sunglasses or face coverings</li>
                    <li>Try a different photo with better quality</li>
                </ul>
            </div>
            <button class="try-again-btn" onclick="document.getElementById('image-upload').click()">
                📷 Try Another Photo
            </button>
        `;
        
        resultsContainer.appendChild(errorBox);
        
        // Show results section with error
        heroSection.style.display = 'none';
        resultsSection.classList.remove('is-hidden');
        
        // Add some extra visual feedback
        setTimeout(() => {
            errorBox.style.transform = 'scale(1.02)';
            setTimeout(() => {
                errorBox.style.transform = 'scale(1)';
            }, 200);
        }, 600);
    }

    function displayResults(data) {
        // Before displaying results, check for the specific error from the AI
        if (data.error) {
            displayErrorBox(data.error);
            return;
        }

        resultsContainer.innerHTML = ''; // Clear previous results

        const scoreCard = document.createElement('div');
        scoreCard.className = 'result-card score-card';
        scoreCard.innerHTML = `<p class="score">${data.score}</p><p>${data.summary}</p>`;
        resultsContainer.appendChild(scoreCard);

        data.analysis_points.forEach(point => {
            const pointCard = document.createElement('div');
            pointCard.className = 'result-card';
            pointCard.innerHTML = `<h3>${point.title}</h3><p>${point.description}</p>`;
            resultsContainer.appendChild(pointCard);
        });

        heroSection.style.display = 'none';
        resultsSection.classList.remove('is-hidden');
    }

    if (getStartedBtn && imageUpload) {
        getStartedBtn.addEventListener('click', () => imageUpload.click());

        analyzeAnotherBtn.addEventListener('click', () => {
            resultsSection.classList.add('is-hidden');
            heroSection.style.display = 'flex';
        });

        imageUpload.addEventListener('change', async (event) => {
            if (imageUpload.files.length > 0) {
                showSpinner(true);
                const formData = new FormData();
                formData.append('image', imageUpload.files[0]);
                formData.append('prompt', PROMPT);

                try {
                    const headers = new Headers();
                    
                    // Add authorization header only if user token exists (production mode)
                    if (window.currentUserToken) {
                        headers.append('Authorization', `Bearer ${window.currentUserToken}`);
                    }

                    // Use local backend in development, remote in production
                    const apiUrl = window.location.hostname === 'localhost' ? 
                        'http://localhost:8080/analyze' : 
                        'https://asasasas3434.pythonanywhere.com/analyze';

                    const response = await fetch(apiUrl, { method: 'POST', headers: headers, body: formData });
                    const data = await response.json(); // The response is now clean JSON

                    if (!response.ok) {
                        // Use the 'error' field from the server's JSON response
                        throw new Error(`Server error (${response.status}): ${data.error || 'Unknown error'}`);
                    }

                    displayResults(data);

                } catch (error) {
                    console.error('Analysis Error:', error);
                    alert(`An error occurred during analysis:\n\n${error.message}`);
                } finally {
                    showSpinner(false);
                }
            }
        });
    }
});

