/**
 * @fileoverview renders parties ot the DOM
 * @exports renderParties
 */

/**
 * @description populates parties table with party data
 * @param {json} parties list with the party details
 */
export const renderParties = parties => {
  // display a message when there is no party registered
  if (parties.data.length === 0) {
    const cardHeader = document.querySelector('.card--title');
    cardHeader.innerHTML = `Oops! No party has been registered yet.`;
    return;
  }
  const table = document.querySelector('#parties-table-list');
  const tableHeader = table.createTHead();
  const tableHeaderRow = tableHeader.insertRow(0);
  let nameHeader = tableHeaderRow.insertCell(0);
  let addressHeader = tableHeaderRow.insertCell(1);
  nameHeader.innerHTML = 'Party name';
  addressHeader.innerHTML = 'Headquarters';

  // party list
  const tableBody = document.createElement('tbody');
  table.appendChild(tableBody);

  // loop through the parties detail & render the data to edit table
  parties.data.forEach(party => {
    let tableRow = tableBody.insertRow(0);
    let partyName = tableRow.insertCell(0);
    let partyAddress = tableRow.insertCell(1);

    // populate table cells with the party detail data
    partyName.innerHTML = `${party.party_name}`;
    partyAddress.innerHTML = `${party.hq_address}`;
  });
  return;
};
