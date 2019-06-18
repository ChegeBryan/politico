/**
 * @fileoverview Authentication class that has the user signup and signin logic
 * @imports formaDataToJson, validateResponse, readResponseAsJson,
 *      saveCurrentUser
 * @exports Auth
 */

import {
  formDataToJson,
  validateResponse,
  readResponseAsJson,
  saveCurrentUser,
  alertError,
} from './helpers.js';


export default class Auth {
  /**
   * Creates an instance of Auth.
   * @param {element} form signup form or log in form
   * @param {string} url user sign-in / sign-up url
   * @memberof Auth
   */
  constructor(form, url) {
    this.form = form;
    this.url = url;
  }

  /**
   * Send form data to server
   *
   * @memberof Auth
   */
  sendData() {
    const formData = new FormData(this.form);
    const data = formDataToJson(formData);
    const requestHeaders = new Headers({
      'Content-Type': 'application/json'
    });
    fetch(this.url, {
        method: 'POST',
        body: data,
        headers: requestHeaders
      })
      .then(validateResponse)
      .then(readResponseAsJson)
      .then(saveCurrentUser)
      .catch(alertError);
  }
}
