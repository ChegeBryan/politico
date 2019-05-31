/**
 * @fileoverview handles DOM events on edit party page
 */

import {
  PartyAdminAccess
} from "../model/party.js";
import {
  partiesApiUrl
} from "../helpers.js";

/**
 * @description fetches parties details from the server
 */
const fetchParties = () => {
  const currentUser = localStorage.getItem('token');
  // call the getParties from the Party class
  PartyAdminAccess.editPartiesList(partiesApiUrl, currentUser);
}

/**
 * call the fetch parties method whenever the edit page is loaded
 * or refreshed
 * @event load
 */
window.addEventListener('load', fetchParties);

const renamePartyBtn = document.querySelector('#rename-party-btn');
renamePartyBtn.addEventListener('click', () => {
  // party registration form
  const currentUserToken = localStorage.getItem('token');
  const form = document.querySelector('#rename-party-form');
  const partyId = renamePartyBtn.dataset.partyId;
  const renamePartyUrl = `${partiesApiUrl}/${partyId}/name`
  // check if the form data is valid before submiting
  if (form.checkValidity()) {
    /**
     * PartyAdminAccess instance, to aceess the edit party name method
     *
     * @instance
     */
    const renameParty = new PartyAdminAccess(currentUserToken, renamePartyUrl);
    renameParty.editPartyName(form)
    return;
  }
  alert('Fix highlighted form error and submit again');
});
