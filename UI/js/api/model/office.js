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

  // TODO: add method to get registered offices
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
