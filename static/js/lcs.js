$(function(){
	$(document).one('click', '.like-review', function(e) {
		$(this).html('<i class="fa fa-thumbs-o-up" aria-hidden="true"></i>liked');
		$(this).children('.fa-thumbs-o-up').addClass('animate-like');
	});
});