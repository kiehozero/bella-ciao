/* Incremental quantity buttons, taken from Boutique Ado project */

/* Disables button at chosen thresholds */
function handleEnableDisable(itemId) {
    var currentQty = parseInt($(`#id_qty_${itemId}`).val());
    var minusDisabled = currentQty < 2;
    var plusDisabled = currentQty > 49;
    $(`#decrease-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`#increase-qty_${itemId}`).prop('disabled', plusDisabled);
}

var allQtyInputs = $('.qty-select');
for (var i = 0; i < allQtyInputs.length; i++) {
    var itemId = $(allQtyInputs[i]).data('item_id');
    handleEnableDisable(itemId);
}

/* Re-checks whether thresholds are met every time the input element changes */
$('.qty-select').change(function() {
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

/* Operating decrease button */
$('.decrease-qty').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.qty-panel').find('.qty-select')[0];
    var currentQty = parseInt($(closestInput).val());
    $(closestInput).val(currentQty - 1);
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

/* Operating decrease button */
$('.increase-qty').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.qty-panel').find('.qty-select')[0];
    var currentQty = parseInt($(closestInput).val());
    $(closestInput).val(currentQty + 1);
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});