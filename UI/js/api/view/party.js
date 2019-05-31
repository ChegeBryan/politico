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
  // display a message when there is no party registered
  if (parties.data.length === 0) {
    const cardHeader = document.querySelector('.card--title');
    cardHeader.innerHTML = `Oops! No party has been registered yet.`;
    return;
  }
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
    let editButtonCell = tableRow.insertCell(2);

    /**
     * create an edit button on the last cell of the party details row
     *
     * @param {int} id party identifier
     * @returns Div element with an edit party button
     */
    let createEditButton = id => {
      // create card--actioNS DIV 
      let buttonDiv = document.createElement('div');
      buttonDiv.classList.add('card--actions');

      // add the edit button
      let editBtn = document.createElement('button');
      editBtn.classList.add('btn', 'btn--primary');
      editBtn.setAttribute('data-party-id', id);
      editBtn.setAttribute('type', 'button');

      // launch rename party form when buttin is clicked
      editBtn.addEventListener('click', () => {
        launchEditForm(editBtn);
      });
      // add edit icon to the button
      let editIcon = document.createElement('i');
      editIcon.classList.add('fas', 'fa-fw', 'fa-edit');
      
      // insert icon as child node to button node 
      editBtn.appendChild(editIcon);
      // insert button text after the icon node 
      editIcon.insertAdjacentHTML('afterend', '&nbsp;Edit')

      // insert button as a child node to button div
      buttonDiv.appendChild(editBtn);

      // insert card--actions div as child node to edit button table cell
      return editButtonCell.appendChild(buttonDiv);
    };
    // populate table cells with the party detail data
    partyName.innerHTML = `${party.party_name}`;
    partyAddress.innerHTML = `${party.hq_address}`;
    editButtonCell = createEditButton(`${party.party_id}`);
  });
};

const launchEditForm = (btn) => {
  let editTableCard = document.querySelector('.edit__table');
  let editForm = document.querySelector('.edit__form');
  
  // take party id, add it to the rename party button 
  const id = btn.dataset.partyId;
  const renamePartyBtn = document.querySelector('#rename-party-btn');
  renamePartyBtn.setAttribute('data-party-id', id);
  // hide the edit table
  editTableCard.classList.toggle("hide");
  // show the edit form
  editForm.classList.toggle("hide");
}
