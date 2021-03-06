/**
 * @fileoverview the party class model
 * @exports class party, PartyAdminAccess
 */

import NotificationToast from '../view/notificationToast.js';
import {
  formDataToJson,
  validateResponse,
  alertError,
  readResponseAsJson,
} from '../helpers.js';
import {
  renderEditParties,
} from '../view/editParty.js';
import {
  renderDeleteParties,
} from '../view/deleteParty.js';
import {
  renderParties,
} from '../view/partyList.js';


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
      .catch(alertError);
  }

  /**
   * renders parties from the server on the DOM
   *
   * @static
   * @param {string} url get parties endpoint url
   * @param {string} currentUser currently logged in user token
   * @memberof Party
   */
  static partiesList(url, currentUser) {
    // call get parties method from Party class the promise returned
    this.getParties(url, currentUser)
      .then(renderParties);
  }
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
      .then(
        (res) => {
          let displayNotification = new NotificationToast(res);
          displayNotification.successPartyRegistration();
        }
      )
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
      .then(renderEditParties);
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
      .then(readResponseAsJson)
      .then(
        (res) => {
          const displayNotification = new NotificationToast(res);
          displayNotification.successPartyRename();
        }
      )
      .catch(alertError);
  }

  /**
   * gets the parties to delete and renders them to the DOM
   *
   * @static
   * @param {object} url Get parties endpoint
   * @param {string} currentUser currently logged in admin token
   * @memberof PartyAdminAccess
   */
  static deletePartiesList(url, currentUser) {
    // get parties fromthe server passing the response
    // to render the response to the DOM
    super.getParties(url, currentUser)
      .then(renderDeleteParties);
  }

  /**
   * Deletes a party the passed in party URL
   *
   * @param {String} url party url with party id on the URL
   * @param {*} currentUser currently logged in admin user token
   * @memberof PartyAdminAccess
   */
  static deleteParty(url, currentUser) {
    fetch(url, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${currentUser}`
        },
      })
      .then(validateResponse)
      .then(readResponseAsJson)
      .then((res) => {
        let displayNotification = new NotificationToast(res);
        displayNotification.successPartyDeletion();
        // wait for 3 seconds for notification to finish showing
        // then reload the page
        setTimeout(() => location.reload(), 3000);
      })
      .catch(alertError);
  }
}
