$(function () {
    $(document).one('click', '.like-review', function (e) {
        $(this).html('<i class="fa fa-thumbs-up" aria-hidden="true"></i>Liked');
        $(this).children('.fa-thumbs-up').addClass('animate-like');
    });
});

