$(document).ready(function() {
  //pass
  new WOW().init();

  $(".sidenav").sidenav();
  $(".carousel").carousel({
    fullWidth: true,
    indicators: true
  });
  $(".tabs").tabs();
  $(".scrollspy").scrollSpy();

  function resetCarouselHeight() {
    setTimeout(() => {
      image_height = $(".carousel img").height();
      $(".carousel").css("min-height", image_height + "px");
      $(".carousel").css("height", image_height + "px");
      $(".carousel").css("max-height", image_height + "px");
      resetCarouselHeight();
    }, 1000);
  }
  resetCarouselHeight();

  setTimeout(function() {
    $(".preloader").fadeOut();
  }, 5000);
});
