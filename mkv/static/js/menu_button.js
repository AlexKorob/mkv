$(function () {
  // menu button
  $(document).on("click", ".menu-circle", function() {
    $(".pop-up").toggleClass("pop-up-hide");
  });
  // end menu button

  $(document).on("click", ".main", function() {
    if (!$(".pop-up").hasClass("pop-up-hide")) {
      $(".pop-up").addClass("pop-up-hide")
    }
  });
});
