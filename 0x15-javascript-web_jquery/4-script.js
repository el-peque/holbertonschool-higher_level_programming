$(document).ready(function() {
  $("DIV#toggle_header").on('click', function() {
    if ($("body header").is(".red")) {
      $("body header").toggleClass("green");
      } else {
      $("body header").toggleClass("red");
    }
  });
});
