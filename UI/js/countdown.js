// Set the voting deadline date
var countDownDate = new Date("April 1, 2019 00:00:00").getTime();

var countdown = setInterval(function () {

  // todays date and time
  var now = new Date().getTime();

  // Find the time left before election ends
  var timeLeft = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
  var hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

  // Add leading zeros
  days = (days < 10) ? "0" + days : days;
  hours = (hours < 10) ? "0" + hours : hours;
  minutes = (minutes < 10) ? "0" + minutes : minutes;
  seconds = (seconds < 10) ? "0" + seconds : seconds;

  // output the variables to their respective html
  document.getElementById("days").innerHTML = days;
  document.getElementById("hours").innerHTML = hours;
  document.getElementById("minutes").innerHTML = minutes;
  document.getElementById("seconds").innerHTML = seconds;

  // If the count down is done output time to vote
  if (timeLeft < 0) {
    clearInterval(countdown);
    document.getElementsByClassName("time--lapse")[0].innerHTML = "Oops can't vote!!!";
  }
}, 1000);