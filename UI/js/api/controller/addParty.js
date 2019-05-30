/**
 * @fileoverview Party registration controller
 */

import {
  partiesApiUrl,
} from '../helpers.js';
import {
  PartyAdminAccess,
} from '../model/party.js';


const addPartyBtn = document.querySelector('#add-party-btn');
addPartyBtn.addEventListener('click', () => {
  // party registration form
  const currentUserToken = localStorage.getItem('token');
  const form = document.querySelector('#add-party-form');
  // check if the form data is valid before submiting
  if (form.checkValidity()) {
    /**
     * PartyAdminAccess instance, to aceess the add party method for party
     * party registration
     * @instance
     */
    const registerParty = new PartyAdminAccess(currentUserToken, partiesApiUrl);
    registerParty.addParty(form);
    return;
  }
  alert('Fix highlighted form error and submit again');
});
