function redirectToThanks() {
    window.location.href = "/thanks";
}

document.addEventListener('DOMContentLoaded', (event) => {
    const form = document.querySelector('.card-details form');
    form.addEventListener('submit', function (e) {
        e.preventDefault();

        // Validate fields
        const cardNumber = document.getElementById('number').value;
        const expiryDate = document.getElementById('e-data').value;
        const cvv = document.getElementById('cvv').value;
        const email = document.getElementById('email').value;

        if (!validateCardNumber(cardNumber)) {
            alert("Invalid card number");
            return;
        }

        if (!validateExpiryDate(expiryDate)) {
            alert("Invalid expiry date. Format: MM/YY");
            return;
        }

        if (!validateCVV(cvv)) {
            alert("Invalid CVV. It should be 3 digits.");
            return;
        }

        if (!validateEmail(email)) {
            alert("Invalid email format.");
            return;
        }

        // If all fields are valid, redirect to the thanks page
        redirectToThanks();
    });
});

// Validate card number (simple Luhn Algorithm could be added for extra security)
function validateCardNumber(number) {
    const regex = /^[0-9]{16}$/; // Must be 16 digits
    return regex.test(number.replace(/\s+/g, ''));
}

// Validate expiry date (MM/YY format)
function validateExpiryDate(date) {
    const regex = /^(0[1-9]|1[0-2])\/([0-9]{2})$/; // MM/YY format
    if (!regex.test(date)) return false;

    const today = new Date();
    const month = parseInt(date.split('/')[0], 10);
    const year = parseInt('20' + date.split('/')[1], 10);
    const expiryDate = new Date(year, month);

    return expiryDate >= today;
}

// Validate CVV (3 digits)
function validateCVV(cvv) {
    const regex = /^[0-9]{3}$/; // CVV should be 3 digits
    return regex.test(cvv);
}

// Validate email
function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}