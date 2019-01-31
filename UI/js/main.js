// function to toggle nav links display on mobile
function toggleNavlink() {
  var x = document.getElementsByClassName('navbar__collapse');
  if (x[0].className === 'navbar__collapse') {
    x[0].className += ' navbar__collapse--show';
  } else {
    x[0].className = 'navbar__collapse';
  }
}

// toggle showing and hiding password text
function showPassword() {
  var x = document.getElementById("pwd");
  x.type = "text";
}

function hidePassword() {
  var x = document.getElementById("pwd");
  x.type = 'password';
}

// toggle hiding and opening modal
var modal = document.getElementById("modal");
var overLay = document.getElementById("modal-overlay");
var closeButton = document.getElementsByClassName("modal--close")[0];
var openButton = document.getElementsByClassName("modal--open")[0];

closeButton.addEventListener("click",
  function () {
    modal.classList.toggle("show");
    overLay.classList.toggle("show");
  });

openButton.addEventListener("click",
  function () {
    modal.classList.toggle("show");
    overLay.classList.toggle("show");
  });

