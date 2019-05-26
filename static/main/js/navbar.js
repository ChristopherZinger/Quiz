
$(document).ready(function() {
  $('#nav-button-dropdown').click(function(){
    $('.my-dropdown').toggleClass('drop-active');
      $(".dropdown-nav-link").fadeToggle('1',function(){
        if($('.dropdown-nav-link').css('opacity') == 1){
            $('.dropdown-nav-link').animate({opacity:0}, 200);
        }else{
            $('.dropdown-nav-link').animate({opacity:1}, 200);
        }
      }).css('display', 'block');
  });
});
