/**
 * @fileoverview Authentication class that has the user signup and signin logic
 * @imports formaDataToJson, validateResponse, readResponseAsJson,
 *      saveCurrentUser
 */

import {
  formDataToJson,
  validateResponse,
  readResponseAsJson,
  saveCurrentUser,
  alertError,
} from './helpers.js';


export default class Auth {
  constructor(form, url) {
    this.form = form;
    this.url = url;
  }

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

  validateForm() {
    if (this.form.checkValidity()) {
      this.sendData();
      return;
    }
    alert('Fix highlighted form error and submit again');
  }
}