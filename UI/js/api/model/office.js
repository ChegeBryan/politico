/**
 * @fileoverview office ajax calls
 * @exports OfficeAdminAccess
 */

import {
  formDataToJson,
  validateResponse,
  alertError,
  readResponseAsJson,
} from '../helpers.js';
import NotificationToast from '../view/notificationToast.js';
import {
  renderOffices
} from '../view/officeList.js';


/**
 * Office ajax calls common to both normal user and admin user
 *
 * @export
 * @class Office
 */
export class Office {
  /**
   * @constructs Office class instance
   * @param {string} user currently logged in user token
   * @param {string} url officeS API endpoint
   * @memberof Office
   */
  constructor(user, url) {
    this.user = user;
    this.url = url;
  }

  /**
   * fetches registered offices
   *
   * @static
   * @param {string} url get office endpoint url
   * @param {string} currentUser currently logged in user
   * @returns office list promise
   * @memberof Office
   */
  static getOffices(url, currentUser) {
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
   * renders returned offices to the DOM
   *
   * @static
   * @param {string} url get offices api endpoint url
   * @param {string} currentUser currently logged in user
   * @memberof Office
   */
  static officeList(url, currentUser) {
    this.getOffices(url, currentUser)
      .then(renderOffices);
  }
}


/**
 * contains APi calls that ate only accessbile to the admin
 *
 * @export OfficeAdminAccess
 * @class OfficeAdminAccess
 * @extends {Office}
 */
export class OfficeAdminAccess extends Office {
  /**
   * registers an office
   *
   * @param {object} form office registration form
   * @memberof OfficeAdminAccess
   */
  addOffice(form) {
    const formData = new FormData(form);
    const data = formDataToJson(formData);
    const requestHeaders = new Headers({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${this.user}`,
    });
    fetch(this.url, {
        method: 'POST',
        body: data,
        headers: requestHeaders,
      })
      .then(validateResponse)
      .then(readResponseAsJson)
      .then((res) => {
        let displayNotification = new NotificationToast(res);
        displayNotification.successOfficeRegistration();
      })
      .catch(alertError);
  }
}
