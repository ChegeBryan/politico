/**
 * @fileoverview validate the form input before from submission
 */

/**
 * @function validateInput is triggered when on blur on a input field
 *           it applies to an input field on data validation
 * @this inputfield input where the function was triggered
 */
function validateInput(input) {
  if (input.validity.valueMissing) {
    input.style.border = "1px solid red";
  } else if (input.validity.patternMismatch) {
    input.style.border = "1px solid red";
  } else if (input.validity.typeMismatch) {
    input.style.border = "1px solid red";
  } else {
    input.style.border = "1px solid green";
  }
}