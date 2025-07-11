document.addEventListener('DOMContentLoaded', () => {
    const historyBtn = document.getElementById('history-btn');
    const modal = document.getElementById('history-modal');
    const closeBtn = document.querySelector('.close-button');
    const historyContainer = document.getElementById('history-container');

    const showModal = (show) => modal.classList.toggle('is-hidden', !show);

    historyBtn.addEventListener('click', async () => {
        if (!window.currentUserToken) {
            alert("You must be signed in to view your history.");
            return;
        }

        try {
            const headers = new Headers({ 'Authorization': `Bearer ${window.currentUserToken}` });
            const response = await fetch('/history', { headers });
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

