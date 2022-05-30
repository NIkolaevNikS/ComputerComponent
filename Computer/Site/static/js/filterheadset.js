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

document.getElementById("Schemes").onchange = function() {
    sessionStorage.setItem('Schemes', document.getElementById("Schemes").value);
}
if (sessionStorage.getItem('Schemes')) {
    document.getElementById("Schemes").options[sessionStorage.getItem('Schemes')].selected = true;
}

document.getElementById("Hertz").onchange = function() {
    sessionStorage.setItem('Hertz', document.getElementById("Hertz").value);
}
if (sessionStorage.getItem('Hertz')) {
    document.getElementById("Hertz").options[sessionStorage.getItem('Hertz')].selected = true;
}

document.getElementById("Sens").onchange = function() {
    sessionStorage.setItem('Sens', document.getElementById("Sens").value);
}
if (sessionStorage.getItem('Sens')) {
    document.getElementById("Sens").options[sessionStorage.getItem('Sens')].selected = true;
}

document.getElementById("Set").onchange = function() {
    sessionStorage.setItem('Set', document.getElementById("Set").value);
}
if (sessionStorage.getItem('Set')) {
    document.getElementById("Set").options[sessionStorage.getItem('Set')].selected = true;
}

document.getElementById("minPrice").onchange = function() {
    sessionStorage.setItem('minPrice', document.getElementById("minPrice").value);
}
if (sessionStorage.getItem('minPrice')) {
    slider.noUiSlider.set(sessionStorage.getItem('minPrice'));
}

document.getElementById("maxPrice").onchange = function() {
    sessionStorage.setItem('maxPrice', document.getElementById("maxPrice").value);
}
if (sessionStorage.getItem('maxPrice')) {
    document.getElementById("maxPrice").value = sessionStorage.getItem('maxPrice');
}