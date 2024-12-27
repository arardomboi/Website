
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

// Test //
var testPassword = "dog";
console.log(hasNumber(testPassword));