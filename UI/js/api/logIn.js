/**
 * @fileoverview contains logic specific to user login
 * @imports Auth class, signInApiUrl
 *
 */

import Auth from './auth.js';
import {
  signInApiUrl
} from './helpers.js';

// user login form submit button
const signInBtn = document.querySelector('#signin-btn');

/**
 * @event click create a user login instance from Auth class
 *  when a clicks login button
 */
signInBtn.addEventListener('click', () => {
  // create AUth class instance for user login
  const signInForm = document.querySelector('#signin-form');

  // check if the form data is valid before submiting
  if (signInForm.checkValidity()) {
    /**
     * Auth instance, to access method for sending form data
     * party registration
     * @instance
     */
    const userLogin = new Auth(signInForm, signInApiUrl);
    userLogin.sendData();
    return;
  }
  alert('Fix highlighted form error and submit again');
});
