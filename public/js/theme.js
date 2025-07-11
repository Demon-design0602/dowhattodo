document.addEventListener('DOMContentLoaded', () => {
    console.log("Theme script loaded."); // For debugging
    const body = document.body;
    const newThemeSwitcher = document.getElementById('new-theme-switcher');

    if (newThemeSwitcher) {
        console.log("Theme switcher button found."); // For debugging
        newThemeSwitcher.addEventListener('click', () => {
            console.log("Theme switcher clicked."); // For debugging
            const currentTheme = body.dataset.theme;
            body.dataset.theme = currentTheme === 'dark' ? 'light' : 'dark';
        });
    } else {
        console.error("Error: Theme switcher button not found in the DOM.");
    }
});

