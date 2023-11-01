$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const newItem = $('<li></li>').text('Item');
    $('UL.my_list').append(newItem);
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last').remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list li').remove();
  });
});
