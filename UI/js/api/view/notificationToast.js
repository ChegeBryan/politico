/**
 * @fileoverview creates notification toast to notify user of operation
 *  completed successfully
 * @exports function notificationToast
 */

/**
 * @description shows the snackbar/toast when a party is successfully
 * registered
 * @param {json} resp the response JSON from calling resulting
 * from party registration API call
 */
export const notificationToast = resp => {
  const snackBar = document.querySelector('#snackbar');
  let partyName = resp.data[0].party_name;
  snackBar.className = 'appear';
  // add the message to the toast notification
  snackBar.innerHTML = `${partyName} is now registered.`;
  setTimeout(() => {
    // after 3 secs, remove the appear class and clear the innerhtml
    snackBar.className = snackBar.className.replace('appear', '');
    snackBar.innerHTML = '';
  }, 3000);
};
