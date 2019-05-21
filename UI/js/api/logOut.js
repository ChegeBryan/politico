/**
 * @fileoverview constains the user logout logic
 */

import {
  signOutApiUrl,
  validateResponse,
  alertError,
} from './helpers.js';

// get the logout button
const logOutBtn = document.querySelector('#logout-btn');
logOutBtn.addEventListener('click', async () => {
  // get the token from the local storage
  const currentUserToken = localStorage.getItem('token');
  if (currentUserToken) {
    /**
     * @description call fetch but wait for the promise to resolve
     *  before the low code is called i.e before a user is redirected
     */
    await fetch(signOutApiUrl, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${currentUserToken}`
        },
      })
      .then(validateResponse)
      .catch(alertError);
  }
  localStorage.removeItem('token');
  window.location.replace('signin.html');
});
