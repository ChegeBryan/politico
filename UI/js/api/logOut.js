/**
 * @fileoverview constains the user logout logic
 */

import {
  signOutApiUrl,
  validateResponse
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
  }
  // clear the token fr om the client local storage
  return;
});
