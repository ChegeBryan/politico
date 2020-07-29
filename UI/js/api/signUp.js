/**
 * @fileoverview contains logic specific to user login
 * @imports Auth class, signUpApiUrl
 *
 */

import Auth from './auth.js';
import {
  signUpApiUrl
} from './helpers.js';

// user login form submit button
const signUpBtn = document.querySelector('#signup-btn');

/**
 * @event click create a user registration instance from Auth class
 *  when a submits the registration form
 */
signUpBtn.addEventListener('click', () => {
  // create AUth class instance for user registration
  const signUpForm = document.querySelector('#signup-form');

  // check if the form data is valid before submiting
  if (signUpForm.checkValidity()) {
    /**
     * Auth instance, to access method for sending form data
     * party registration
     * @instance
     */
    const userSignUp = new Auth(signUpForm, signUpApiUrl);
    userSignUp.sendData();
    return;
  }
  alert('Fix highlighted form error and submit again');
});
