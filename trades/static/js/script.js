document.addEventListener('DOMContentLoaded', function() {
    const backBtn = document.getElementById('backBtn');
    
    backBtn.addEventListener('click', function() {
        window.history.back(); // Navigates to the previous page in browser history
    });
    
    // Optional: Disable if no history (e.g., first page)
    if (window.history.length <= 1) {
        backBtn.disabled = true;
        backBtn.style.opacity = '0.5';
        backBtn.title = 'No previous page';
    }
});