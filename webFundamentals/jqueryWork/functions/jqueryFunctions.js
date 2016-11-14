$(document).ready(function(){
  console.log('jquery is ready!');
//I'm noticing that you're creating a variable and returning each function. This will work for many of them but
//it's unnecessary and may lead to confusion about how things are actually working.

//Try removing the variable declaration and the return statement from your .after function for example.
//Under the hood, the .after function in the library already returns the value to js, so you're just doing extra work.

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

//This function only returns a value for the FIRST element in the set you're looking to access.
//This means that it will only ever output "yes"
  $('#attribute').click(function() {
    var anAttribute = $('input').attr('value');
      $("#attrP").before(anAttribute);
      return anAttribute;
  });
// image is not loading, just the text

//Here you're just passing a string, and it will input anything you pass through exactly how it's written.
//Refer to your .after and .insert functions.
  $('#b4').click(function() {
    var aImg = $('#aboveThis').before('<img src="peer_through.jpeg"/>');
      return aImg;
  });

  $('#onClick').click(function() {
    var colorMe = $('#colorMeBad').css('background-color', 'hotpink');
      return colorMe;
  });
// not sure how to use this at all!

//This is a strange one. It's meant to be used for things that we haven't learned about in class yet.
//The idea is that you can assign useless data to any element and call that data back later.
//First, you need to set the element's data to something, then you need to get it and display it.
//When you want to get the data, you need to access it by its key. Which is the left side of the : in an object.
    //example... {"key" : "value"}
//However, the API documentation for setting reads like this .data(key, value). So $("body").data("my-name", "aValue")
//is the proper way to set a key value pair. ({"my-name": "aValue"}) is setting {"my-name": "aValue"} as a valueless key
  $('#addData').click(function() {
    $( "body" ).data("my-name", "aValue");
    $("#dataP").before($( "body" ).data("my-name"));
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
