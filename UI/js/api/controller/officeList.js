/**
 * @fileoverview initiates api call to render parties to DOM
 */


import {
  Office,
} from '../model/office.js';
import {
  officesApiUrl,
} from '../helpers.js';


/**
 * @description fetches offices details from the server
 * and render them on government offices page
 */
const fetchAllOffices = () => {
  const currentUser = localStorage.getItem('token');
  // call the officeList to render offices
  Office.officeList(officesApiUrl, currentUser);
};

window.addEventListener('load', fetchAllOffices);
