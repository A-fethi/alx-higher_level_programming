$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const newItem = $('<li></li>').text('Item');
    $('UL.my_list').append(newItem);
  });
});
