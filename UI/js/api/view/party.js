/**
 * @fileoverview renders the DOM with parties details.
 * @exports renderEditParties
 */

/**
 * renders a table with the parties details and a button to launch
 * the edit party name form
 * @param {obj} parties JSON object containing parties details
 * @returns undefined - the function just gives a side effect
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

  // party list
  const tableBody = document.createElement('tbody');
  table.appendChild(tableBody);

  // loop through the parties detail & render the data to edit table
  parties.data.forEach(party => {
    let tableRow = tableBody.insertRow(0);
    let partyName = tableRow.insertCell(0);
    let partyAddress = tableRow.insertCell(1);
    let editButton = tableRow.insertCell(2);

    /**
     * create an edit button on the last cell of the party details row
     *
     * @param {int} id party identifier
     * @returns Div element with an edit party button
     */
    let createEditButton = id => {
      let buttonDiv = document.createElement('div');
      buttonDiv.classList.add('card--actions');
      // add an edit button the div with a data-party-attribute which
      // is the party id
      buttonDiv.innerHTML = `<button class="btn btn--primary" onclick="edit()" data-party-id='${id}'>
      <i class="fas fa-fw fa-edit"></i>&nbsp;Edit</button>`;

      return editButton.appendChild(buttonDiv);
    };
    // populate table cells with the party detail data
    partyName.innerHTML = `${party.party_name}`;
    partyAddress.innerHTML = `${party.hq_address}`;
    editButton = createEditButton(`${party.party_id}`);
  });
  return;
};
