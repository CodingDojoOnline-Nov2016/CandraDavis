$(document).ready(function(){
  console.log('jquery is ready!');
  $('#aC').click(function() {
    $('p#add-class').css('background', 'coral').addClass('selected');
  });

  $('#after').click(function() {
    $('p#add-after').after('<h2>I am getting the hang of this!</h2>').css('color', 'red');
  });

  $('#insert').click(function() {
    $('p#insert-content').append('<p><strong>What are <i>you<i> doing?!</strong></p>').css('color', 'darkviolet');
  });

  $('#attribute').click(function() {
     $('#check1').attr('checked','checked');
  });
  $('#b4').click(function() {
    var aImg = $('#aboveThis').before('<img src="peer_through.jpeg" width="100px"/>');
      return aImg;
  });

  $('#onClick').click(function() {
    $('#colorMeBad').css('background-color', 'hotpink');
  });
  
  $('#addData').click(function() {
    $('.dataAdd').data('Davis', 35 );
    $('.dataAdd').after($('.dataAdd').data('Davis'));
  });

  $('#fade-in').click(function() {
     $('#peerThrough').fadeIn('slow');
  });

  $('#fade-out').click(function() {
    $('#peerThrough').fadeOut('slow');
  });

  $('#radial1').focus(function() {
    $('.s1').css("display", "inline").fadeOut(2000);
  });

  $('#radial2').focus(function() {
    $('.s2').css("display", "inline").fadeOut(2000);
  });

  $('#radial3').focus(function() {
    $('.s3').css("display", "inline").fadeOut(2000);
  });

  $('#hidden').click(function() {
    $('#hideMe').hide();
  });

  $('#reveal').click(function() {
    $('#hideMe').show();
  });

  $('#alterHtml').click(function() {
     $('#pChange').html('Look Ma, No Hands!!').css('background-color', 'lavenderblush');
  });

  $('#down').click(function() {
     $('#puppers').slideDown('slow');
  });

  $('#sToggle').click(function() {
    $('#puppers').slideToggle('slow');
  });

  $('#up').click(function() {
   $('#puppers').slideUp('slow');
  });

  $('#textChange').click(function() {
     $('#textMe').text('You know, I am always changing my mind. Does this p look good on me?').css('color', 'teal');
  });
// not showing first toggle alert message
  $('#toggled').click(function() {
    $('p').toggle();
});
$('#valBtn').click(function() {
  $('#valBtn').val('Whose your momma?!');
});

});
