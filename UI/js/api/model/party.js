/**
 * @fileoverview the party class model
 * @exports class party
 */

import {
  formDataToJson,
  validateResponse,
  alertError,
  readResponseAsJson,
} from '../helpers.js';
import {
  notificationToast
} from '../view/notificationToast.js';

/**
 * Party class has the methods for fetch calls to the server
 * @class
 */
export default class Party {
  /**
   * @constructs PArty class instance
   * @param {byte} user  logged in user token
   * @param {string} url parties API endpoint
   * @param {object} [form=null] default value is set to null
   * for method calls that do not require a form element in the instance
   * @memberof Party
   */
  constructor(user, url, form = null) {
    this.user = user;
    this.url = url;
    this.form = form;
  }

  /**
   * takes data from the register party form and send it to the server
   * @memberof Party
   */
  addParty() {
    const formData = new FormData(this.form);
    // generate the form data as json string
    const data = formDataToJson(formData);
    const requestHeaders = new Headers({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${this.user}`,
    });
    // send data to the server
    fetch(this.url, {
        method: 'POST',
        body: data,
        headers: requestHeaders,
      })
      .then(validateResponse)
      .then(readResponseAsJson)
      .then(notificationToast)
      .catch(alertError);
  }
}
