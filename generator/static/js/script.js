// Animate Smooth Scroll
$('#view-work').on('click', function() {
    const images = $('#images').position().top;
  
    $('html, body').animate(
      {
        scrollTop: images
      },
      900
    );
  });
$(document).ready(function(){
  //Chosen
  $(".multipleChosen").chosen({
      placeholder_text_multiple: "Ваши противопоказания" //placeholder
  });
  //Select2
 
})
jQuery(document).ready(function($)
{
    $( window ).resize(function() {
        resize_info();
    });
});

function resize_info()
{
    (function($) {
      $('.chosen-container').css('width', '100%');
    })(jQuery);
}
$('.chosen-container').css('width', '100%');
