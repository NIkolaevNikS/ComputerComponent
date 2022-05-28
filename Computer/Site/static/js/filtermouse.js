document.getElementById("ConnectionInt").onchange = function() {
    sessionStorage.setItem('ConnectionInt', document.getElementById("ConnectionInt").value);
}
if (sessionStorage.getItem('ConnectionInt')) {
    document.getElementById("ConnectionInt").options[sessionStorage.getItem('ConnectionInt')].selected = true;
}

document.getElementById("ConnectType").onchange = function() {
    sessionStorage.setItem('ConnectType', document.getElementById("ConnectType").value);
}
if (sessionStorage.getItem('ConnectType')) {
    document.getElementById("ConnectType").options[sessionStorage.getItem('ConnectType')].selected = true;
}

document.getElementById("Sensers").onchange = function() {
    sessionStorage.setItem('Sensers', document.getElementById("Sensers").value);
}
if (sessionStorage.getItem('Sensers')) {
    document.getElementById("Sensers").options[sessionStorage.getItem('Sensers')].selected = true;
}

document.getElementById("Frequency").onchange = function() {
    sessionStorage.setItem('Frequency', document.getElementById("Frequency").value);
}
if (sessionStorage.getItem('Frequency')) {
    document.getElementById("Frequency").options[sessionStorage.getItem('Frequency')].selected = true;
}

document.getElementById("Dpi").onchange = function() {
    sessionStorage.setItem('Dpi', document.getElementById("Dpi").value);
}
if (sessionStorage.getItem('Dpi')) {
    document.getElementById("Dpi").options[sessionStorage.getItem('Dpi')].selected = true;
}

