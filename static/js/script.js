
// PhishGuard JavaScript

// Display a welcome message
function showWelcome() {
    alert("Welcome to PhishGuard!");
}

// Confirm an action
function confirmAction(message) {
    return confirm(message);
}

// Display a message on the page
function showMessage(elementId, message) {
    const element = document.getElementById(elementId);

    if (element) {
        element.textContent = message;
    }
}
