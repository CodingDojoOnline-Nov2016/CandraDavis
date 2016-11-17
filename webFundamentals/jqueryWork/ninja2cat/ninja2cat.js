$(document).ready(function(){
  $('img').click(function() {
    // $(this).fadeOut('slow', function() {
    //   $($(this).attr('replace-piece-src')).fadeIn('slow');
    // }); this is code doesn't work because I don't need to remove the pic and then replace it
    // with the new picture, I need to swap the photos.
    var original = $(this).attr('src');
    var replace = $(this).attr('replace-piece-src');
    $(this).attr('src', replace);
    $(this).attr('replace-piece-src', original);
    // by storing the image, selected by it's attribute in a local variable, and storing the second photo
    // by the it's created attribute id, in a different local variable, I can swap the phots by setting the
    // attr function.
  });
});
