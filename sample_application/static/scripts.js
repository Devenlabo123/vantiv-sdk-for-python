function requireAuth(booleanValue) {
    var toCheck = document.querySelectorAll("table tr:nth-child(1) td:nth-child(1) input");
    toCheck.forEach(function(element) {
        if(booleanValue)
        {
            element.setAttribute('required', 'required');
        }
        else
        {
            element.removeAttribute('required');
        }
    });
}

function requireCapture(booleanValue) {
    var toCheck = document.querySelectorAll("table tr:nth-child(1) td:nth-child(2) input");
    toCheck.forEach(function(element) {
        if(booleanValue)
        {
            element.setAttribute('required', 'required');
        }
        else
        {
            element.removeAttribute('required');
        }
    });
}

window.onload = checkboxListeners;
function checkboxListeners() {
    var AuthCheck = document.querySelector("#auth_checkbox");
    var CaptureCheck = document.querySelector("#capture_checkbox");
    AuthCheck.addEventListener("change", function () {
        if(AuthCheck.checked)
        {
            requireAuth(true);
        }
        else
        {
            requireAuth(false);
        }
    });
    CaptureCheck.addEventListener("change", function () {
        if(CaptureCheck.checked)
        {
            requireCapture(true);
        }
        else
        {
            requireCapture(false);
        }
    })
}