/* Incremental quantity buttons, taken from Boutique Ado project */

$('.decrease-qty').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.qty-panel').find('.qty-select')[0];
    var currentQty = parseInt($(closestInput).val());
    $(closestInput).val(currentQty - 1);
});

$('.increase-qty').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.qty-panel').find('.qty-select')[0];
    var currentQty = parseInt($(closestInput).val());
    $(closestInput).val(currentQty + 1);
});