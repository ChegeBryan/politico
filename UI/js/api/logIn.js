/**
 * @fileoverview contains logic specific to user login
 * @imports Auth class, signInApiUrl
 *
 */

import Auth from './auth.js'
import {
  signInApiUrl
} from './helpers.js'

// user login form submit button
const signInBtn = document.querySelector('#signin-btn');

/**
 * @event click create a user login instance from Auth class
 *  when a clicks login button
 */
signInBtn.addEventListener('click', () => {
  // create AUth class instance for user login
  const signInForm = document.querySelector('#signin-form');
  const userLogin = new Auth(signInForm, signInApiUrl);
  userLogin.validateForm()
});
