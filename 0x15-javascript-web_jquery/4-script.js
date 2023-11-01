$(document).ready(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red', true);
    $('header').toggleClass('green');
  });
});
