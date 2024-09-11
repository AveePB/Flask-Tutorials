document.getElementById('logout-btn').addEventListener('click', function(event){
    event.preventDefault();

    fetch('/auth/logout/', {
        method: 'DELETE',
    })
    .then(response => {
        if (response.ok) {
            // If the response is successful, redirect to the home page
            window.location.href = '/'; // Redirect to home page
        } 
        else {
            // Handle the case where the logout fails
            console.error('Logout failed:', response.statusText);
            alert('Logout failed. Please try again.');
        }
    })
    .catch(error => {
        // Handle any network or other errors
        console.error('Logout error:', error);
        alert('An error occurred. Please try again.');
    });
});