
function hasNumber(string) {
    return /\d/.test(string);
}

function hasSpecial(password) {
    let specialChars = /[`!@#$%^&*()_\-+=\[\]{};':"\\|,.<>\/?~ ]/;
    return specialChars.test(password);
}

function checkPassword(password) {
    if (password.length < 8 || !hasNumber(password) || !hasSpecial(password)) {
        return false;
    }
    return true;
}

function checkEmail(email) {
    let emailString = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailString.test(email);
}

// Test //
var testPassword = "dog";
console.log(hasNumber(testPassword));