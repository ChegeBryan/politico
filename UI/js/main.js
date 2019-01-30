// function to toggle nav links display on mobile
function toggleNavlink() {
  var x = document.getElementsByClassName('navbar__collapse');
  if (x[0].className === 'navbar__collapse') {
    x[0].className += ' navbar__collapse--show';
  } else {
    x[0].className = 'navbar__collapse';
  }
}