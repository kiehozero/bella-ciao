/* Enter and leave settings for icon and anchor container buttons */

$("#backShopBtn").mouseenter(function() {
    $("#backShopBtn a").css("color", "#f0eee9");
});

$("#backShopBtn").mouseleave(function() {
    $("#backShopBtn a").css("color", "#008763");
});

$("#checkoutBtn").mouseenter(function() {
    $("#checkoutBtn a").css("color", "#f0eee9");
});

$("#checkoutBtn").mouseleave(function() {
    $("#checkoutBtn a").css("color", "#008763");
});

/* items below need to only hover for each item rather than all of them */

$(".update-item").mouseenter(function() {
    $(".update-item i").css("color", "#f0eee9");
});

$(".update-item").mouseleave(function() {
    $(".update-item i").css("color", "#008763");
});

$(".remove-item").mouseenter(function() {
    $(".remove-item i").css("color", "#f0eee9");
});

$(".remove-item").mouseleave(function() {
    $(".remove-item i").css("color", "e64757");
});

if ($(window).width() < 1280) {
    /* does cart-total change only need to happen on mobile screens? */
    $(".cart-total").attr("colspan","6");
};
