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
