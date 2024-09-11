document.addEventListener('DOMContentLoaded', function() {
    // Handle form submissions
    const forms = document.querySelectorAll('.form-container');

    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();

            const url = form.action;
            const method = form.method.toUpperCase();
            const formData = new FormData(form);

            fetch(url, {
                method: method,
                body: method === 'POST' ? formData : null,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': 'fake-token' // Adjust if CSRF protection is implemented
                }
            })
            .then(response => response.text().then(text => {
                let data = {};
                try {
                    data = JSON.parse(text);
                } catch {
                    data.message = text;
                }
                return { status: response.status, message: data.message };
            }))
            .then(result => {
                const messageBoxId = form.getAttribute('data-message-box');
                const messageBox = document.getElementById(messageBoxId);

                if (messageBox) {
                    // Clear previous classes
                    messageBox.classList.remove('success', 'error');
                    
                    // Add new class based on result status
                    if (result.status === 204) {
                        messageBox.classList.add('success');
                        messageBox.innerHTML = result.message || 'Operation completed.';
                        setTimeout(() => {
                            window.location.reload();
                        }, 500);
                    } else {
                        messageBox.classList.add('error');
                        messageBox.innerHTML = result.message || 'Operation failed.';
                    }
                    
                    // Clear form data
                    form.reset();
                }
            })
            .catch(error => {
                console.error('Error:', error);
                const messageBoxId = form.getAttribute('data-message-box');
                const messageBox = document.getElementById(messageBoxId);
                if (messageBox) {
                    messageBox.classList.remove('success', 'error');
                    messageBox.classList.add('error');
                    messageBox.innerHTML = 'An error occurred. Please try again.';
                }
            });
        });
    });

    // Password visibility toggle
    const togglePasswordButton = document.getElementById('toggle-password');
    const passwordField = document.getElementById('new-password');

    if (togglePasswordButton && passwordField) {
        togglePasswordButton.addEventListener('click', function() {
            const type = passwordField.type === 'password' ? 'text' : 'password';
            passwordField.type = type;
            togglePasswordButton.textContent = type === 'password' ? 'Show' : 'Hide';
        });
    } else {
        console.error('Toggle password button or password field not found');
    }
});
