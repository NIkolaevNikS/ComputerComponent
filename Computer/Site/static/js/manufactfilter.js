document.getElementById('HyperX').onclick = function() {
    if(document.getElementById('HyperX').checked) {
    sessionStorage.setItem('HyperX', "true");
    } else {
    sessionStorage.setItem('HyperX', "false");
    }
}

if (sessionStorage.getItem('HyperX') == "true") {
  document.getElementById("HyperX").setAttribute('checked','checked');
}

document.getElementById('Logitech').onclick = function() {
    if(document.getElementById('Logitech').checked) {
    sessionStorage.setItem('Logitech', "true");
    } else {
    sessionStorage.setItem('Logitech', "false");
    }
}

if (sessionStorage.getItem('Logitech') == "true") {
  document.getElementById("Logitech").setAttribute('checked','checked');
}

document.getElementById('ZET GAMING').onclick = function() {
    if(document.getElementById('ZET GAMING').checked) {
    sessionStorage.setItem('ZET GAMING', "true");
    } else {
    sessionStorage.setItem('ZET GAMING', "false");
    }
}
if (sessionStorage.getItem('ZET GAMING') == "true") {
  document.getElementById("ZET GAMING").setAttribute('checked','checked');
}

document.getElementById('SteelSeries').onclick = function() {
    if(document.getElementById('SteelSeries').checked) {
    sessionStorage.setItem('SteelSeries', "true");
    } else {
    sessionStorage.setItem('SteelSeries', "false");
    }
}
if (sessionStorage.getItem('SteelSeries') == "true") {
  document.getElementById("SteelSeries").setAttribute('checked','checked');
}

document.getElementById('Razer').onclick = function() {
    if(document.getElementById('Razer').checked) {
    sessionStorage.setItem('Razer', "true");
    } else {
    sessionStorage.setItem('Razer', "false");
    }
}
if (sessionStorage.getItem('Razer') == "true") {
  document.getElementById("Razer").setAttribute('checked','checked');
}