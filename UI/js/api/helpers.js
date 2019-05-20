/**
 * @fileoverview contains variables and functions that ares shared
 * @exports base api URL, formDataToJson function
 */

// ? create API base URL
export const baseURL = new URL('https://politico-cb.herokuapp.com');
export const ApiVersionPath = 'api/v2';

/**
 * @description creates a json string from form data
 * @function formDataToJson
 * @param {obj} formData Form input values
 * @returns {json} json string with form data values and keys
 * @exports formDataToJson function
 */
export const formDataToJson = formData => {
  const JSONFormDataObj = {};
  // ? populate the json object with key-value pair
  formData.forEach((value, key) => {
    JSONFormDataObj[key] = value;
  });
  const formDataJSON = JSON.stringify(JSONFormDataObj);
  return formDataJSON;
};

/**
 * @function checks error code and throws and appropriate error message
 * @param {obj} fetch api promise resolve value
 * @throws {obj} bad request error data conflict error depending on statusCode
 */
const checkErrorCode = response => {
  if (response.status == 400) {
    throw new Error('Correct highlighted form errors and try again.');
  } else if (response.status == 409) {
    throw new Error(
      'Looks like you are already registered. Login to continue.'
    );
  } else if (response.status === 404) {
    throw new Error('User not registered.');
  }
};

/**
 * @description fetch resolves successfully with status code 200-299
 * @function validates
 * @param {obj} response fetch api response object
 * @exports validateResponse function
 * @returns {obj} resolved object if successfully
 */
export const validateResponse = response => {
  if (!response.ok) {
    checkErrorCode(response);
    return;
  }
  return response;
};

/**
 * @description parses the fetch response as JSON
 * @function readResponseAsJson
 * @param {obj} fetch response promise object
 * @returns {json} response object parsed to JSON
 */
export const readResponseAsJson = response => response.json();