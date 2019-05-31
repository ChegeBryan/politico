/**
 * @fileoverview renders the DOM with parties details.
 * @exports renderEditParties
 */

/**
 * renders a table with the parties details and a button to launch
 * the edit party name form
 * @param {obj} parties JSON object containing parties details
 */
export const renderEditParties = parties => {
  const table = document.querySelector('#editTable');
  const tableHeader = table.createTHead();
  const tableHeaderRow = tableHeader.insertRow(0);
  let nameHeader = tableHeaderRow.insertCell(0);
  let addressHeader = tableHeaderRow.insertCell(1);
  let actionHeader = tableHeaderRow.insertCell(2);
  nameHeader.innerHTML = 'Party name';
  addressHeader.innerHTML = 'Headquarters';
  actionHeader.innerHTML = 'Edit name';

  // TODO: feed the DOM with the party details.
};
