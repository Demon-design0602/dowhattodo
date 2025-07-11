// Make user token globally available
window.currentUserToken = null;

document.addEventListener('DOMContentLoaded', () => {
    console.log("Auth script loaded.");
    const loginBtn = document.getElementById('login-btn');

    if (loginBtn) {
        console.log("Login button found.");
        try {
            firebase.auth().onAuthStateChanged(async (user) => {
                if (user) {
                    console.log("User is signed in:", user.displayName);
                    loginBtn.textContent = `Hi, ${user.displayName.split(' ')[0]}`;
                    window.currentUserToken = await user.getIdToken();
                    console.log("User token set.");

                    loginBtn.onclick = () => {
                        firebase.auth().signOut();
                    };

                } else {
                    console.log("User is signed out");
                    loginBtn.textContent = 'Sign In';
                    window.currentUserToken = null;
                    loginBtn.onclick = () => {
                        const provider = new firebase.auth.GoogleAuthProvider();
                        firebase.auth().signInWithPopup(provider).catch((error) => {
                            console.error("Firebase sign-in error:", error);
                            alert(`Error signing in: ${error.message}`);
                        });
                    }
                }
            });
        } catch (error) {
            console.error("Fatal Error: Firebase library not loaded or initialized correctly.", error);
            alert("Error: The authentication service could not be loaded. Check the console for details.");
        }
    } else {
        console.error("Error: Login button not found in the DOM.");
    }
});

