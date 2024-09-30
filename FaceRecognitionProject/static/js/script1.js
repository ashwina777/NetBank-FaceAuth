function FaceAuthenticate() {
    fetch('/face_authenticate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (data.status === "success") {
            window.location.href = "/website";
        }
        else if(data.status === "failure"){
            window.location.href = "/login";
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}