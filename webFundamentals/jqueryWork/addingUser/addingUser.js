var newTableRow = $('<tr><td></td></tr>');

$(document)ready(function() {
  $('.query-form').on('click', '#addUser', function() {
    $('table').html(newTableRow);
  })
})
// {/* <td>input.first-name</td><td>input.last-name</td><td>input.email</td><td>input.phone</td> */}
