// Function to handle registration form submission
function handleRegisterForm(event) {
    // Prevent the form from submitting the traditional way (reloading the page)
    event.preventDefault();

    // Get the values from the form fields
    var username = document.getElementById('regUsername').value;
    var password = document.getElementById('regPassword').value;

    // Prepare the data to send to the server
    var data = {
        username: username,
        password: password
    };

    // Send the data to the server using fetch
    fetch('/register', {
        method: 'POST', // Specify the request type
        headers: {
            'Content-Type': 'application/json' // Let the server know we're sending JSON
        },
        body: JSON.stringify(data) // Convert the JavaScript object to a JSON string
    })
    .then(function(response) {
        return response.json(); // Parse the JSON from the server
    })
    .then(function(data) {
        // Update the webpage with the response from the server
        document.getElementById('response').innerText = data.message || data.error;
    });
}

// Function to handle login form submission
function handleLoginForm(event) {
    // Prevent the form from submitting the traditional way (reloading the page)
    event.preventDefault();

    // Get the values from the form fields
    var username = document.getElementById('loginUsername').value;
    var password = document.getElementById('loginPassword').value;

    // Prepare the data to send to the server
    var data = {
        username: username,
        password: password
    };

    // Send the data to the server using fetch
    fetch('/login', {
        method: 'POST', // Specify the request type
        headers: {
            'Content-Type': 'application/json' // Let the server know we're sending JSON
        },
        body: JSON.stringify(data) // Convert the JavaScript object to a JSON string
    })
    .then(function(response) {
        return response.json(); // Parse the JSON from the server
    })
    .then(function(data) {
        // Update the webpage with the response from the server
        document.getElementById('response').innerText = data.message || data.error;
    });
}

// Attach the event listeners to the forms when the page loads
document.getElementById('registerForm').addEventListener('submit', handleRegisterForm);
document.getElementById('loginForm').addEventListener('submit', handleLoginForm);
