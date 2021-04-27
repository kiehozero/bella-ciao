/* jshint esversion: 6 */
/* globals $:false */
/* Comments above tells JSHint what version of JS is being used, and secondly overrides JSHint's assumption that the 
$ symbol is an undefined variable */

/* jQuery for interactive design */

$(".nav-option").mouseenter(function() {
    $(this).children().css("color", "#008763");
});

$(".nav-option").mouseleave(function() {
    $(this).children().css("color", "#f0eee9");
});

$(".nav-option#cart-container").mouseenter(function() {
    $(".nav-option a#cart-full").css("color", "#008763");
});

$(".nav-option#cart-container").mouseleave(function() {
    $(".nav-option a#cart-full").css("color", "#ceca03");
});

$(".close-message").click(function () {
    $(".message-row").css("display", "none")
})

/* Confirmation Modal */

$("#delEventButton").click(function() {
    $("#delEventModal").modal("show");
});

$("#delItemButton").click(function() {
    $("#delItemModal").modal("show");
});

$("#modalEventClose").click(function() {
    $("#delEventModal").modal("hide");
});

$("#modalItemClose").click(function() {
    $("#delItemModal").modal("hide");
});


/* Auto-Scroll Button - taken from Boutique Ado */

$('#backToTop').click(function () {
    window.scrollTo(0, 0);
});


/* Mobile Navbar */

$(".navbar-toggler").click(function() {
    $("#navbarNav").toggle();
});

$("#navbarDropdownMenuLink").click(function() {
    $(".dropdown-menu").toggle();
});


/* Tablet and Mobile Rendering */

if ($(window).width() < 1280) {
    $("#searchButton").html("<i class='fas fa-search' aria-label='Search Products'></i>");
    $("#searchReset").html("<i class='fas fa-power-off' aria-label='Reset Search Criteria'></i>");
    $(".cart-total").attr("colspan","3");
};