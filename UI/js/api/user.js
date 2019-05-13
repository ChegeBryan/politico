/**
 * @fileoverview logic for fetch user registration api
 * @imports the base API URL, formDataToJson()
 */


import {
  baseURL,
  formDataToJson,
  validateResponse,
  readResponseAsJson,
  ApiVersionPath as version,
} from './helpers.js';


// ? user registration API endpoint
const signupApiUrl = new URL(`${version}/auth/signup`, baseURL);

/**
 * @function submits signup form data to the server
 *
 */
function registerUser() {
  const formData = new FormData(document.getElementById('signup-form'));
  const data = formDataToJson(formData);
  const messageHeaders = new Headers({
    'Content-Type': 'application/json'
  });
  fetch(signupApiUrl, {
      method: 'POST',
      body: data,
      Headers: messageHeaders
    })
    .then(validateResponse)
    .then(readResponseAsJson);
}