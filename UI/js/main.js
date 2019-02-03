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


function closeModal() {
  modal.classList.toggle("show");
  overLay.classList.toggle("show");
}

function openModal() {
  modal.classList.toggle("show");
  overLay.classList.toggle("show");
}

window.onclick = function (event) {
  if (event.target == modal) {
    modal.classList.toggle("show");
    overLay.classList.toggle("show");
  }
}

var editTable = document.getElementsByClassName("edit__table")[0];
var editForm = document.getElementsByClassName("edit__form")[0];
function edit() {
  editTable.classList.toggle("hide");
  editForm.classList.toggle("hide");
}