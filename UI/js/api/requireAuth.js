/**
 * @fileoverview loads before the body contents of a page are loaded
 */

/**
 * @description IIEF called when a page is accessed.
 * it checks if theres a authorization token at the client
 * before the page is loaded
 */
(() => {
  const authToken = localStorage.getItem('token');
  if (!authToken) {
    // if no token was found prompt user to sign-in
    window.location.replace('signin.html');
  }
})();
