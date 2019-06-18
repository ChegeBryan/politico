/**
 * @fileoverview office application registration
 */

import {
  OfficeApplication
} from '../model/application.js';
import {
  applicationApiUrl
} from '../helpers.js';


const vieOfficeBtn = document.querySelector('#vie-office-btn');
vieOfficeBtn.addEventListener('click', () => {
  const currentUserToken = localStorage.getItem('token');
  const vieOfficeForm = document.querySelector('#vie-office-form');
  // check if the form data is valid before submiting
  if (vieOfficeForm.checkValidity()) {
    /**
     * OfficeApplication instance, to aceess add office application method
     * @instance
     */
    const vieOffice = new OfficeApplication(currentUserToken, applicationApiUrl);
    vieOffice.addOfficeApplication(vieOfficeForm);
    return;
  }
  alert('Fix highlighted form error and submit again');
});
