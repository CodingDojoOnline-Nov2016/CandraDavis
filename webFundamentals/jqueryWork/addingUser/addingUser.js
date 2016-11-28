$(document).ready(function() {
  console.log('I am ready');

  $('.query-form').on('click', '#addUser' , function() {
    var newTableRow = '<tr><td>'+ $('input.first-name').val() +'</td><td>'+ $('input.last-name').val() +'</td><td>'+ $('input.email').val() +'</td><td>'+ $('input.phone').val() +'</td></tr>';
      $('tbody').append(newTableRow);
  })
})






{/* this code did not work because I did not have the concatonated jquery command to search for the val entered by the user <td>$('input.first-name')</td><td>input.last-name</td><td>input.email</td><td>input.phone</td> */}
