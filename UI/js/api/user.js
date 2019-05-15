/**
 * @fileoverview logic for fetch user registration api
 * @imports the base API URL, formDataToJson()
 */

import {
  baseURL,
  formDataToJson,
  validateResponse,
  readResponseAsJson,
  ApiVersionPath as version
} from './helpers.js';

// ? user registration API endpoint
const signupApiUrl = new URL(`${version}/auth/signup`, baseURL);

/**
 * @description  pop an alert message when the form submission erred
 * @function alertError
 * @param {obj} error the error message
 */
const alertError = error => alert(error.message);

/**
 * @description Saves the sighup user token to localstorage
 * @function saveCurrentUser
 * @param {json} response json object with the registered user details
 */
const saveCurrentUser = response => {
  const currentUserToken = response.data[0].token;
  localStorage.setItem('token', currentUserToken);
  window.location.replace('dashboard.html');
};

/**
 * @description submits signup form data to the server
 * @function registerUser
 */
function registerUser() {
  const formData = new FormData(document.getElementById('signup_form'));
  const data = formDataToJson(formData);
  const messageHeaders = new Headers({
    'Content-Type': 'application/json'
  });
  fetch(signupApiUrl, {
    method: 'POST',
    body: data,
    headers: messageHeaders
  })
    .then(validateResponse)
    .then(readResponseAsJson)
    .then(saveCurrentUser)
    .catch(alertError);
}

const signupBtn = document.getElementById('signup_btn');
signupBtn.addEventListener('click', registerUser);

// TODO : Validate form data.
