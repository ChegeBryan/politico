/**
 * @fileoverview initiates api call to render parties to DOM
 */
import {
  Party
} from '../model/party.js';
import {
  partiesApiUrl
} from '../helpers.js';


/**
 * @description fetches parties details from the server
 * and render the open opened window
 */
const fetchAllParties = () => {
  const currentUser = localStorage.getItem('token');
  // call the partyList to render parties
  Party.partiesList(partiesApiUrl, currentUser);
};

window.addEventListener('load', fetchAllParties);
