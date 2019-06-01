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
   * shows a notification toast for when a user is registered successfully
   *
   * @memberof NotificationToast
   */
  successPartyRegistration() {
    const partyName = this.resp.data[0].party_name;
    this.snackBar.className = 'appear';
    // add the message to the toast notification
    this.snackBar.innerHTML = `${partyName} is now registered.`;
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
