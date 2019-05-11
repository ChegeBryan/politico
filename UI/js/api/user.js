/**
 * @function {formDataToJson} creates a json string from form data
 * @param {obj} Form input values
 * @returns {json} json string with form data values and keys
 *
 */
function formDataToJson(formData) {
  const JSONFormDataObj = {};
  // ? populate the json object with key-value pair
  formData.forEach((value, key) => {
    JSONFormDataObj[key] = value;
  });
  const formDataJSON = JSON.stringify(JSONFormDataObj);
  return formDataJSON;
}


/**
 *
 *
 */
function registerUser() {
  const formData = new FormData(document.getElementById('signup-form'));
  const data = formDataToJson(formData);
}