// On click functions
function downloadFile(fileId) {
    fetch(`/download/${fileId}`)
        .then(response => {
            if (!response.ok)
                throw new Error('Network response wasn\'t ok');

            // Check if the Content-Disposition header is present
            const contentDisposition = response.headers.get('Content-Disposition');
            let fileName = 'downloaded-file';  // Default fallback filename

            if (contentDisposition) {
                const matches = contentDisposition.match(/filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/);
                if (matches != null && matches[1])
                    fileName = matches[1].replace(/['"]/g, ''); // Remove any extra quotes
            }

            return response.blob().then(blob => ({ blob, fileName }));
        })
        .then(({ blob, fileName }) => {
            // Create a temporary link element
            const link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = fileName;  // Use the filename extracted or fallback name

            // Append the link to the body (required for Firefox)
            document.body.appendChild(link);
            link.click();  // Trigger the download
            link.remove();  // Remove the link from the document
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

function deleteFile(fileId) {
    fetch(`/delete/${fileId}`, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.status === 204) {
            alert('File deleted successfully!');
            location.reload(); 
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Event handler
function handleUploadForm (e) {
    e.preventDefault();
    const formData = new FormData(this);

    fetch("/upload", {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.status === 204)  {
            alert('File successfully uploaded!');
            this.reset();
        }
        else if (response.status === 409) 
            alert('File name is already taken!');
        else
            alert('Unexpected error occurred!');
        location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

document.getElementById('uploadForm').addEventListener('submit', handleUploadForm);