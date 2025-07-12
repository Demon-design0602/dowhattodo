document.addEventListener('DOMContentLoaded', () => {
    const historyBtn = document.getElementById('history-btn');
    const modal = document.getElementById('history-modal');
    const closeBtn = document.querySelector('.close-button');
    const historyContainer = document.getElementById('history-container');

    const showModal = (show) => modal.classList.toggle('is-hidden', !show);

    historyBtn.addEventListener('click', async () => {
        // In local development mode, show a message since we don't have Firebase
        const isLocalDev = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
        
        if (isLocalDev) {
            // Show a modal with helpful information instead of just an alert
            historyContainer.innerHTML = `
                <div style="text-align: center; padding: 20px;">
                    <h3>🚀 Development Mode</h3>
                    <p>History feature is not available in local development mode.</p>
                    <p>In development mode, Firebase authentication and storage are disabled.</p>
                    <p><strong>You can still test the photo analysis feature!</strong></p>
                </div>
            `;
            showModal(true);
            return;
        }
        
        if (!window.currentUserToken) {
            alert("You must be signed in to view your history.");
            return;
        }

        try {
            const headers = new Headers({ 'Authorization': `Bearer ${window.currentUserToken}` });
            const apiUrl = 'https://asasasas3434.pythonanywhere.com/history';
            const response = await fetch(apiUrl, { headers });
            const historyData = await response.json();

            if (!response.ok) {
                throw new Error(historyData.error || "Could not fetch history.");
            }

            historyContainer.innerHTML = ''; // Clear previous history
            if (historyData.length === 0) {
                historyContainer.innerHTML = '<p>No history found.</p>';
            } else {
                historyData.forEach(item => {
                    const div = document.createElement('div');
                    div.className = 'history-item';
                    const timestamp = item.timestamp.seconds ? new Date(item.timestamp.seconds * 1000).toLocaleString() : new Date(item.timestamp).toLocaleString();
                    div.innerHTML = `<h4>Analysis from ${timestamp}</h4><p>Score: ${item.results.score} - ${item.results.summary}</p>`;
                    historyContainer.appendChild(div);
                });
            }
            showModal(true);

        } catch (error) {
            alert(`Error: ${error.message}`);
        }
    });

    closeBtn.addEventListener('click', () => showModal(false));
    window.addEventListener('click', (event) => {
        if (event.target === modal) showModal(false);
    });
});

