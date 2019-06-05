import {
  OfficeAdminAccess
} from '../model/office.js';
import {
  officesApiUrl
} from '../helpers.js';

/**
 * @fileoverview Office registration controller
 */

const addOfficeBtn = document.querySelector('#add-office-btn');
addOfficeBtn.addEventListener('click', () => {
  const currentUserToken = localStorage.getItem('token');
  const officeRegistrationForm = document.querySelector('#add-office-form');
  const registerOffice = new OfficeAdminAccess(currentUserToken, officesApiUrl);
  registerOffice.addOffice(officeRegistrationForm);
});
