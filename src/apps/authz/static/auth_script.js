// Ensures that listener is set after document is loaded
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const messageBox = document.getElementById('message-box');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission

        const xhr = new XMLHttpRequest();
        const formData = new FormData(form);

        xhr.open(form.method, form.action);
        
        xhr.onload = function () {
            if (xhr.status >= 200 && xhr.status < 300) {
                messageBox.textContent = 'Submission successful!';
                messageBox.className = 'message-box success'; // Add success class
                // Reload the page after a short delay to allow the user to see the message
                setTimeout(function () {
                    location.reload();
                }, 500); // 500 ms delay
            } else {
                const result = JSON.parse(xhr.responseText);
                messageBox.textContent = `Error: ${result.message}`;
                messageBox.className = 'message-box error'; // Add error class
            }
        };

        xhr.onerror = function () {
            messageBox.textContent = 'An error occurred.';
            messageBox.className = 'message-box error'; // Add error class
        };

        xhr.send(formData);
    });
});