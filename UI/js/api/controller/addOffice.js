import {
  OfficeAdminAccess
} from '../model/office.js';
import {
  officesApiUrl
} from '../helpers.js';

/**
 * @fileoverview Office registration controller
 */


/**
 * listens for a click event the office name inputs
 * and automatically selects the office type
 */
const officeNameInputs = document.querySelectorAll('input[name="office_name"]');
officeNameInputs.forEach(officeNameInput => {
  // automatically select the office type based on checked office name
  officeNameInput.addEventListener('click', () => {
    if (officeNameInput.value === 'president') {
      const officeTypeInput = document.querySelector('input[value="federal"]');
      officeTypeInput.checked = true;
    } else if (officeNameInput.value === 'house of representatives' ||
      officeNameInput.value === 'senator') {
      const officeTypeInput = document.querySelector('input[value="congress"]');
      officeTypeInput.checked = true;
    } else if (officeNameInput.value === 'governor') {
      const officeTypeInput = document.querySelector('input[value="state"]');
      officeTypeInput.checked = true;
    }
  });
});

const addOfficeBtn = document.querySelector('#add-office-btn');
addOfficeBtn.addEventListener('click', () => {
  const currentUserToken = localStorage.getItem('token');
  const officeRegistrationForm = document.querySelector('#add-office-form');
  const registerOffice = new OfficeAdminAccess(currentUserToken, officesApiUrl);
  registerOffice.addOffice(officeRegistrationForm);
});
