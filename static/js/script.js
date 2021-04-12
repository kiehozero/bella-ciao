/* jQuery for interactive design */

/* jshint esversion: 6 */
/* globals $:false */
/* Comments above tells JSHint what version of JS is being used, and secondly overrides JSHint's assumption that the 
$ symbol is an undefined variable */

 $('.nav-option').mouseenter(function() {
     $(this).children().css("color", "#008763");
 });

 $('.nav-option').mouseleave(function() {
    $(this).children().css("color", "#f0eee9");
});


/* Tablet and Mobile Only */

if ($(window).width() < 1280) {
    $("#searchButton").html("<i class='fas fa-search' aria-label='Search Products'></i>");
    $("#searchReset").html("<i class='fas fa-power-off' aria-label='Reset Search Criteria'></i>");
    /* does cart-total change only need to happen on mobile screens? */
    $(".cart-total").attr("colspan","3");
};