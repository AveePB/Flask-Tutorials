document.addEventListener('DOMContentLoaded', function() {
    // Fetch HTML elements
    const followBtn = document.getElementById('follow-btn');
    const followingBtn = document.getElementById('following-btn');


    if (followBtn) { // If present
        followBtn.addEventListener('click', function() {
            // Prepare data
            const username = followBtn.getAttribute('username');
            const url = '/accounts/follow/';

            const formData = new FormData();
            formData.append('username', username);

            // Send request
            fetch(url, {
                method: 'POST',
                body: formData,
            })
            .then(response => {
                if (response.ok) {
                    return response.json(); // or response.text() for plain text responses
                }
                throw new Error('Network response was not ok.');
            })
            .then(data => {
                console.log('Success:', data);
                // Handle success (e.g., update UI)
                location.reload(); // Reload the page on success
            })
            .catch(error => {
                console.error('Error:', error);
                // Handle error (e.g., show an error message)
            });
        });
    }

    if (followingBtn) { // If present
        followingBtn.addEventListener('click', function() {
            // Prepare data
            const username = followingBtn.getAttribute('username');
            const url = `/accounts/unfollow/${username}/`

            // Send request
            fetch(url, {
                method: 'DELETE',
            })
            .then(response => {
                if (response.ok) {
                    console.log('Success');
                    location.reload(); // Reload the page on success
                    return;
                }
                throw new Error('Network response was not ok.');
            })
            .catch(error => {
                console.error('Error:', error);
                // Handle error (e.g., show an error message)
            });
        });
    }

});