function changeBG() {
	let currentColour = document.getElementByID("main").style.color;
	if (currentColour == "white") {
		document.getElementByID("main").style.color = "black";
	} else {
		document.getElementByID("main").style.color = "white";
	}
}

function hasNumber(string) {
    return /\d/.test(string);
}
function checkPassword(password) {
    if (password.length < 8) { 
        return false;
    }
    if (!hasNumber(password)) {
        return false;
    }
    return true;
}

// test //
var testPassword = "dog";
console.log(hasNumber(testPassword));