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

    // Handle DELETE button clicks
    document.getElementById('delete-avatar-btn').addEventListener('click', function() {
        fetch('/accounts/avatar/', {
            method: 'DELETE',
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
            const messageBox = document.getElementById('avatar-message-box');
            if (messageBox) {
                // Clear previous classes
                messageBox.classList.remove('success', 'error');
                
                // Add new class based on result status
                if (result.status === 204) {
                    messageBox.classList.add('success');
                    messageBox.innerHTML = result.message || 'Avatar deleted.';
                    setTimeout(() => {
                        window.location.reload();
                    }, 500);
                } else {
                    messageBox.classList.add('error');
                    messageBox.innerHTML = result.message || 'Operation failed.';
                }
            }
        })
        .catch(error => {
            console.error('Error:', error);
            const messageBox = document.getElementById('avatar-message-box');
            if (messageBox) {
                messageBox.classList.remove('success', 'error');
                messageBox.classList.add('error');
                messageBox.innerHTML = 'An error occurred. Please try again.';
            }
        });
    });

    document.getElementById('delete-bio-btn').addEventListener('click', function() {
        fetch('/accounts/bio/', {
            method: 'DELETE',
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
            const messageBox = document.getElementById('bio-message-box');
            if (messageBox) {
                // Clear previous classes
                messageBox.classList.remove('success', 'error');
                
                // Add new class based on result status
                if (result.status === 204) {
                    messageBox.classList.add('success');
                    messageBox.innerHTML = result.message || 'Bio deleted.';
                    setTimeout(() => {
                        window.location.reload();
                    }, 500);
                } else {
                    messageBox.classList.add('error');
                    messageBox.innerHTML = result.message || 'Operation failed.';
                }
            }
        })
        .catch(error => {
            console.error('Error:', error);
            const messageBox = document.getElementById('bio-message-box');
            if (messageBox) {
                messageBox.classList.remove('success', 'error');
                messageBox.classList.add('error');
                messageBox.innerHTML = 'An error occurred. Please try again.';
            }
        });
    });
});
