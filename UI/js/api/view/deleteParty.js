/**
 * renders a table with the parties details and a button to
 * the remove party
 * @param {obj} parties JSON object containing parties details
 * @returns undefined - the function just gives a side effect
 */

export const renderDeleteParties = parties => {
  // display a message when there is no party registered
  if (parties.data.length === 0) {
    const cardHeader = document.querySelector('.card--title');
    cardHeader.innerHTML = `Oops! No party has been registered yet.`;
    return;
  }
  const table = document.querySelector('#delete-party-table');
  const tableHeader = table.createTHead();
  const tableHeaderRow = tableHeader.insertRow(0);
  let nameHeader = tableHeaderRow.insertCell(0);
  let addressHeader = tableHeaderRow.insertCell(1);
  let buttonHeader = tableHeaderRow.insertCell(2);
  nameHeader.innerHTML = 'Party name';
  addressHeader.innerHTML = 'Headquarters';
  buttonHeader.innerHTML = 'Click to delete';

  // party list
  const tableBody = document.createElement('tbody');
  table.appendChild(tableBody);

  // loop through the parties detail & render the data to edit table
  parties.data.forEach(party => {
    let tableRow = tableBody.insertRow(0);
    let partyName = tableRow.insertCell(0);
    let partyAddress = tableRow.insertCell(1);
    let editButtonCell = tableRow.insertCell(2);

    /**
     * create an delete button on the last cell of the party details row
     *
     * @param {int} id party identifier
     * @returns Div element with a delete party button
     */
    let createDeleteButton = id => {
      // create card--actioNS DIV
      let buttonDiv = document.createElement('div');
      buttonDiv.classList.add('card--actions');

      // add delete button
      let deleteBtn = document.createElement('button');
      deleteBtn.classList.add('btn', 'btn--danger');
      deleteBtn.setAttribute('data-party-id', id);
      deleteBtn.setAttribute('type', 'button');

      // insert button text after the icon node
      deleteBtn.innerHTML = `Dissolve party`;

      // insert button as a child node to button div
      buttonDiv.appendChild(deleteBtn);

      // insert card--actions div as child node to edit button table cell
      return editButtonCell.appendChild(buttonDiv);
    };
    // populate table cells with the party detail data
    partyName.innerHTML = `${party.party_name}`;
    partyAddress.innerHTML = `${party.hq_address}`;
    editButtonCell = createDeleteButton(`${party.party_id}`);
  });
};
