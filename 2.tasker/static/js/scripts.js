function removeTask(taskId) {
    // Send the request to the server to remove the task
    fetch(`/remove/${taskId}`, {
        method: 'DELETE',
    })
    .then(response => {
        if (response.status === 204) {
            alert('Task removed successfully!');
            location.reload(); // Reload the page to update the task list
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function handleAddTaskForm(event) {
    // Prevent the form from submitting the traditional way (reloading the page)
    event.preventDefault();

    // Prepare the data to send to the server
    var task_content = document.getElementById('taskInput').value; 
    var data = { content: task_content };

    fetch('/add', {
        method: 'POST', // Specify the request type
        headers: {
            'Content-Type': 'application/json' // Let the server know we're sending JSON
        },
        body: JSON.stringify(data) // Convert the JavaScript object to a JSON string
    })
    .then(response => {
        if (response.status === 204) {
            alert('Task added successfully!');
            location.reload(); // Reload the page to update the task list
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

document.getElementById('taskForm').addEventListener('submit', handleAddTaskForm);