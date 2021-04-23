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


/* Responsiveness */

if ($(window).width() < 768) {
    $(".cart-total").attr("colspan","5");
};

if ($(window).width() < 350) {
    $("a.update-item").addClass("btn-sm").removeClass("btn");
    $("a.remove-item").addClass("btn-sm").removeClass("btn");
};
