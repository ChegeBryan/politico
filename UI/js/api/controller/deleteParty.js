/**
 * @fileoverview handles DOM events on delete party page
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
  PartyAdminAccess.deletePartiesList(partiesApiUrl, currentUser);
}

/**
 * call the fetch parties method whenever the edit page is loaded
 * or refreshed
 * @event load
 */
window.addEventListener('load', fetchParties);


/**
 * delete party when the delete button against is clicked
 *
 * @param {string} partyId party to delete
 */
export const removeParty = partyId => {
  const currentUserTOken = localStorage.getItem('token');
  const partyToDeleteUrl = `${partiesApiUrl}/${partyId}`;
  PartyAdminAccess.deleteParty(partyToDeleteUrl, currentUserTOken);
}
