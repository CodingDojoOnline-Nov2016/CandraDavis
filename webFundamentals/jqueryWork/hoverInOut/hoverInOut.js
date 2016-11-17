$(document).ready(function() {
  $('img').hover(function() {
    var originalImg = $(this).attr('src');
    var replacementImg = $(this).attr('alternateImg');
    $(this).attr('src', replacementImg);
    $(this).attr('alternateImg', originalImg);
  });
});
