function validateEmpty(value) {
    if (value.trim() === "") {
        alert("Please enter a value in the field.");
        return false;
    }
    return true;
}

function validateUsername(username) {
    var usernameRegex = /^(?=.*[a-z])(?=.*[A-Z])[a-zA-Z\d]{5,}$/;

    if (!usernameRegex.test(username)) {
        alert("Please enter a username that contains both uppercase and lowercase letters.");
        return false;
    }
    return true;
}

function validatePassword(password) {
    var passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;

    if (!passwordRegex.test(password)) {
        alert("Please enter a password with at least 8 characters, including one uppercase letter, one lowercase letter, and one digit.");
        return false;
    }
    return true;
}

function validateForm(event) {
    event.preventDefault(); // Prevent form from submitting

    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (!validateEmpty(username) || !validateEmpty(password)) {
        return false;
    }

    if (!validateUsername(username)) {
        return false;
    }

    if (!validatePassword(password)) {
        return false;
    }

    if (username === 'AshMhk' && password === 'AshMhk12345') {
        window.location.href = "/website"; // Correct redirection URL
    } else {
        alert("Entered username or password is wrong.");
        return false;
    }
}