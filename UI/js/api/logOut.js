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
logOutBtn.addEventListener('click', () => {
  // get the token from the local storage
  const currentUserToken = localStorage.getItem('token');
  if (currentUserToken) {
    fetch(signOutApiUrl, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${currentUserToken}`
        },
      })
      .then(validateResponse)
      .then(localStorage.removeItem('token')) // clear token from client localstorage
      .then(window.location.replace('signin.html'))
      .catch(alertError);
  }
});
