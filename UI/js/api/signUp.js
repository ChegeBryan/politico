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
  const userSignUp = new Auth(signUpForm, signUpApiUrl);
  userSignUp.validateForm();
});
