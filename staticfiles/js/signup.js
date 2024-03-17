
   
  function onChange() {

    const password = document.querySelector('input[name=password1]');
    const confirm = document.querySelector('input[name=password2]');
    const errorMessage = document.getElementById('errorMessage');
    
    if (confirm.value === password.value) {
        confirm.setCustomValidity('');
        errorMessage.textContent = '';
    } else {
        confirm.setCustomValidity('Passwords do not match');
        errorMessage.textContent = 'Passwords do not match';
    }

    // Additional password validations
    if (password.value.length < 8) {
        errorMessage.textContent += ' Password must be at least 8 characters long';
    } 

}

let rmCheck = document.getElementById("rememberMe"),
    passwordInput = document.getElementById("password"),
    emailInput = document.getElementById("email");

if (localStorage.checkbox && localStorage.checkbox != "") {
  rmCheck.setAttribute("checked", "checked");
  emailInput.value = localStorage.username;
  passwordInput.value = localStorage.password;
} else {
  rmCheck.removeAttribute("checked");
  emailInput.value = "";
  passwordInput.value = "";
}

function lsRememberMe() {
  if (rmCheck.checked && emailInput.value != "" && passwordInput.value != "") {
    localStorage.username = emailInput.value;
    localStorage.password = passwordInput.value;
    localStorage.checkbox = rmCheck.value;
  } else {
    localStorage.username = "";
    localStorage.passoword = "";
    localStorage.checkbox = "";
  }
}


function toggleRememberMe() {
    var rememberMeCheckbox = document.getElementById("rememberMe");
    rememberMeCheckbox.checked = !rememberMeCheckbox.checked;
  }