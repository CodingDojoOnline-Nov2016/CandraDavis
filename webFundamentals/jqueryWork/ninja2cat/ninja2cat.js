$(document).ready(function(){
  $('img').click(function() {
    $(this).fadeOut('slow', function() {
      $($(this).attr('replace-piece-src')).fadeIn('slow');
    });
  });
});