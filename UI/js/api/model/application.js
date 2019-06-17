/**
 * @fileoverview application class model
 * @exports OfficeApplication class
 */

import {
  formDataToJson,
  validateResponse,
  readResponseAsJson,
  alertError,
} from '../helpers.js';


export class OfficeApplication {
  /**
   * @constructs Application class instance
   * @param {string} user logged in user token
   * @param {string} url Office application API endpoint
   * @memberof Application
   */
  constructor(user, url) {
    this.user = user;
    this.url = url;
  }

  /**
   * takes office application form data and sends it to the server
   *
   * @param {element} form office application form from DOM
   * @memberof OfficeApplication
   */
  addOfficeApplication(form) {
    const formData = new FormData(form);
    // generate the form data as json string
    const data = formDataToJson(formData);
    const requestHeaders = new Headers({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${this.user}`,
    });
    // send office application form data to server
    fetch(this.url, {
        method: 'POST',
        body: data,
        headers: requestHeaders,
      })
      .then(validateResponse)
      .then(readResponseAsJson)
      .catch(alertError);
  }
}
