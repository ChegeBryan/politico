/**
 * @fileoverview the party class model
 * @exports class party, PartyAdminAccess
 */

import {
  formDataToJson,
  validateResponse,
  alertError,
  readResponseAsJson,
} from '../helpers.js';
import {
  notificationToast,
} from '../view/notificationToast.js';
import {
  renderEditParties
} from '../view/party.js';


/**
 * Party class has the methods for fetch calls to the server
 * @class
 */
export class Party {
  /**
   * @constructs PArty class instance
   * @param {byte} user  logged in user token
   * @param {string} url parties API endpoint
   * @memberof Party
   */
  constructor(user, url) {
    this.user = user;
    this.url = url;
  }

  /**
   * gets all parties from the server
   *
   * @static
   * @param {string} url the GET parties api endpoint
   * @param {string} currentUser the current logged in user token
   * @memberof Party
   */
  static getParties(url, currentUser) {
    return fetch(url, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${currentUser}`
        },
      })
      .then(validateResponse)
      .then(readResponseAsJson)
      .catch(alertError)
  }

  // TODO: add method to render the the parties to DOM for normal user
}


/**
 * constains methods for actions done by an the admin user
 *
 * @export
 * @class PartyAdminAccess has methods only accessible by admin user
 * @extends {Party}
 */
export class PartyAdminAccess extends Party {

  /**
   * takes data from the register party form and send it to the server
   *
   * @param {element} form register party form from DOM
   * @memberof PartyAdminAccess
   */
  addParty(form) {
    const formData = new FormData(form);
    // generate the form data as json string
    const data = formDataToJson(formData);
    const requestHeaders = new Headers({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${this.user}`,
    });
    // send form data to the server
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

  /**
   * gets the parties to edit for and renders them to the DOM
   *
   * @static
   * @param {object} url Get parties endpoint
   * @param {string} currentUser currently logged in admin token
   * @memberof PartyAdminAccess
   */
  static editPartiesList(url, currentUser) {
    // call get parties method from Party class the promise returned
    super.getParties(url, currentUser)
      .then(renderEditParties)
  }

  /**
   * send the new name from form to the server
   *
   * @param {obj} form edit party name form
   * @memberof PartyAdminAccess
   */
  editPartyName(form) {
    const formData = new FormData(form);
    // generate the form data as json string
    const data = formDataToJson(formData);
    const requestHeaders = new Headers({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${this.user}`,
    });
    fetch(this.url, {
        method: 'PATCH',
        body: data,
        headers: requestHeaders,
      })
      .then(validateResponse)
      .catch(alertError)
  }

  // TODO: add method for rendering parties to delete.
  // TODO: add method for deleting party
}
