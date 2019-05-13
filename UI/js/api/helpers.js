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
 * @exports formDataToJson function
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

/**
 * @function validates fetch resolves successfully with status code 200-299
 * @params {obj} fetch api response object
 * @exports validateResponse function
 * @returns {obj} resolved object if successfully
 */
export function validateResponse(response) {
  if (!response.ok) {
    throw new Error(response.statusText);
  }
  return response;
}

/**
 * @function parses the fetch response as JSON
 * @param {obj} fetch response promise object
 * @returns {json} response object parsed to JSON
 */
export const readResponseAsJson = response => response.json();