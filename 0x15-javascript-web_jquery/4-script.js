$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    $('header').toggleClass('red', true);
    $('header').toggleClass('green');
  });
});
