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

document.getElementById("Types").onchange = function() {
    sessionStorage.setItem('Types', document.getElementById("Types").value);
}
if (sessionStorage.getItem('Types')) {
    document.getElementById("Types").options[sessionStorage.getItem('Types')].selected = true;
}

document.getElementById("Format").onchange = function() {
    sessionStorage.setItem('Format', document.getElementById("Format").value);
}
if (sessionStorage.getItem('Format')) {
    document.getElementById("Format").options[sessionStorage.getItem('Format')].selected = true;
}

document.getElementById("Switches").onchange = function() {
    sessionStorage.setItem('Switches', document.getElementById("Switches").value);
}
if (sessionStorage.getItem('Switches')) {
    document.getElementById("Switches").options[sessionStorage.getItem('Switches')].selected = true;
}