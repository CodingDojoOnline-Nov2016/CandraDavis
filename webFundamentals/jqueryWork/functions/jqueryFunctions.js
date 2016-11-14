$(document).ready(function(){
  console.log('jquery is ready!');
  $('#aC').click(function() {
    var addTop = $('p#add-class').css('background', 'coral').addClass('selected');
      return addTop;
  });

  $('#after').click(function() {
    var addAfter = $('p#add-after').after('<h2>I am getting the hang of this!</h2>').css('color', 'red');
      return addAfter;
  });

  $('#insert').click(function() {
    var addAfter = $('p#insert-content').append('<p><strong>What are <i>you<i> doing?!</strong></p>').css('color', 'darkviolet');
      return addAfter;
  });
// not working for me right now
  $('#attribute').click(function() {
    var anAttribute = $('#check1').attr('checked');
      return anAttribute;
  });
// image is not loading, just the text
  $('#b4').click(function() {
    var aImg = $('#aboveThis').before('url(peer_through.jpeg)');
      return aImg;
  });

  $('#onClick').click(function() {
    var colorMe = $('#colorMeBad').css('background-color', 'hotpink');
      return colorMe;
  });
// not sure how to use this at all!
  $('#addData').click(function() {
    var dataAdd = $( "body" ).data( { "my-name": "aValue" } ).data();
      return dataAdd;
  });

  $('#fade-in').click(function() {
     var fadeInImg = $('#peerThrough').fadeIn('slow');
      return fadeInImg;
  });

  $('#fade-out').click(function() {
    var fadeOutImg = $('#peerThrough').fadeOut('slow');
      return fadeOutImg;
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
     var changeText = $('#textMe').text('You know, I am always changing my mind. Does this p look good on me?').css('color', 'teal');
      return changeText;
  });
// not showing first toggle alert message
  $('#toggled').click(function() {
     alert('My mind is Toggled!');
   }, function() {
   alert('I did not think it was possible to be toggled');
});
$('#valBtn').click(function() {
  var nameChange = $('#valBtn').val('Whose your momma?!');
    return nameChange;
});

});
