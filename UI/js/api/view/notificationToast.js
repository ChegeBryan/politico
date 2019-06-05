/**
 * @fileoverview creates notification toast
 * @exports class NotificationToast
 */

/**
 * creates a notification for various actions occuring on a page
 *
 * @export class NotificationToast
 * @class NotificationToast
 */
export default class NotificationToast {
  /**
   * @constructs NotificationToast creates an instance of NotificationToast class.
   * @param {json} resp the response JSON from calling resulting
   * from party registration API call
   * @memberof NotificationToast
   */
  constructor(resp) {
    this.resp = resp;
    this.snackBar = document.querySelector('#snackbar');
  }

  /**
   * gets the party name from the response
   * @returns party name
   */
  getPartyName() {
    return this.resp.data[0].party_name;
  }

  /**
   * adds the appear class to snackbar div showing the notification snackbar
   */
  showNotification() {
    this.snackBar.className = 'appear';
  }

  /**
   * shows a notification toast for when a user is registered successfully
   *
   * @memberof NotificationToast
   */
  successPartyRegistration() {
    this.showNotification();
    // add the message to the toast notification
    this.snackBar.innerHTML = `${this.getPartyName()} is now registered.`;
    this.hideNotification();
  }

  /**
   * shows a notification when a party has been renamed successfully
   *
   * @memberof NotificationToast
   */
  successPartyRename() {
    this.showNotification();
    // add the message to the toast notification
    this.snackBar.innerHTML = `Party name changed to ${this.getPartyName()}.`;
    this.hideNotification();
  }

  /**
   * display a notification when party is deleted successfully
   *
   * @memberof NotificationToast
   */
  successPartyDeletion() {
    this.showNotification();
    // add message to the toast notification
    this.snackBar.innerHTML = `${this.resp.data[0].message}`;
    this.hideNotification();
  }

  successOfficeRegistration() {
    this.showNotification();
    // add office name to the toast notification
    this.snackBar.innerHTML = `${this.resp.data[0].office_name} office registered to
    ${this.resp.data[0].office_type} offices.`;
    this.hideNotification();
  }

  /**
   * hide the notification bar when after 3 seconds it shows
   *
   * @memberof NotificationToast
   */
  hideNotification() {
    setTimeout(() => {
      // after 3 secs, remove the appear class and clear the innerhtml
      this.snackBar.className = this.snackBar.className.replace('appear', '');
      this.snackBar.innerHTML = '';
    }, 3000);
  }
}
