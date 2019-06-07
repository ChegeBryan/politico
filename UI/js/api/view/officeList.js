/**
 * @fileoverview renders offices to the DOM
 * @exports renderOffices
 */

/**
 * @description populates office table with office data
 * @param {json} offices list with the office details
 */
export const renderOffices = offices => {
  // display a message when there is no office registered
  if (offices.data.length === 0) {
    const cardHeader = document.querySelector('.card--title');
    cardHeader.innerHTML = `Oops! No Office has been registered yet.`;
    return;
  }
  const table = document.querySelector('#offices-table-list');
  const tableHeader = table.createTHead();
  const tableHeaderRow = tableHeader.insertRow(0);
  let officeNameHeader = tableHeaderRow.insertCell(0);
  let officeTypeHeader = tableHeaderRow.insertCell(1);
  officeNameHeader.innerHTML = 'Office name';
  officeTypeHeader.innerHTML = 'Office Type';

  // office list
  const tableBody = document.createElement('tbody');
  table.appendChild(tableBody);

  // loop through the parties detail & render the data to edit table
  offices.data.forEach(office => {
    let tableRow = tableBody.insertRow(0);
    let officeName = tableRow.insertCell(0);
    let officeType = tableRow.insertCell(1);

    // populate table cells with the office detail data
    officeName.innerHTML = `${office.office_name}`;
    officeType.innerHTML = `${office.office_type}`;
  });
  return;
};
