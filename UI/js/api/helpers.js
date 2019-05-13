/**
 * @fileoverview contains variables and functions that ares shared
 * @exports base api URL, formDataToJson function
 *
 */

// ? create API base URL
export const baseURL = new URL('https://politico-cb.herokuapp.com');
export const ApiVersionPath = 'api/v2';

/**
 * @function {formDataToJson} creates a json string from form data
 * @param {obj} Form input values
 * @returns {json} json string with form data values and keys
 *
 */
export function formDataToJson(formData) {
  const JSONFormDataObj = {};
  // ? populate the json object with key-value pair
  formData.forEach((value, key) => {
    JSONFormDataObj[key] = value;
  });
  const formDataJSON = JSON.stringify(JSONFormDataObj);
  return formDataJSON;
}