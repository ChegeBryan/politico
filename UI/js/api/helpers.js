/**
 * @fileoverview contains variables and functions that ares shared
 * @exports base api URL, formDataToJson function
 */

// ? create API base URL
const BASE_URL = new URL('https://politico-cb.herokuapp.com');
const VERSION = 'api/v2';

// ? user registration API endpoint
export const signInApiUrl = new URL(`${VERSION}/auth/signin`, BASE_URL);
export const signUpApiUrl = new URL(`${VERSION}/auth/signup`, BASE_URL);

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
  if (response.status === 400) {
    throw new Error('Verify your inputs data are correct and try again.');
  } else if (response.status === 409) {
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
 * @exports readResponseAsJson function
 */
export const readResponseAsJson = response => response.json();

/**
 * @description Saves the signed up user token to localstorage
 * @function saveCurrentUser
 * @param {json} response json object with the registered user details
 * @exports saveCurrentUser function
 */
export const saveCurrentUser = response => {
  const currentUserToken = response.data[0].token;
  localStorage.setItem('token', currentUserToken);
  if (response.data[0].user[0].isAdmin) {
    window.location.replace('admin_dashboard.html');
    return;
  }
  window.location.replace('dashboard.html');
};

/**
 * @description  pop an alert message when the form submission erred
 * @function alertError
 * @param {obj} error the error message
 */
export const alertError = error => alert(error.message);
