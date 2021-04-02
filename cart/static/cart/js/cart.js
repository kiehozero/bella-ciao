if ($(window).width() < 1280) {
    /* does cart-total change only need to happen on mobile screens? */
    $(".cart-total").attr("colspan","3");
};


/* Update and Remove Items - Modified parts of Boutique Ado cart update process */
$('.update-item').click(function(e){
    var form = $(this).parent().siblings('.form-container').children('.update-form');
    form.submit();
})

$('.remove-item').click(function(e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var size = $(this).data('size');
    var url = `/cart/remove/${itemId}`;
    var data = {'csrfmiddlewaretoken': csrfToken, 'size': size};

    $.post(url, data)
     .done(function() {
         location.reload();
     });
})