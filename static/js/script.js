/* jQuery for interactive design */

/* jshint esversion: 6 */
/* globals $:false */
/* Comments above tells JSHint what version of JS is being used, and secondly overrides JSHint's assumption that the 
$ symbol is an undefined variable */

$(document).ready(function(){
    /* initialises... */
    /* ... mobile side navigation bar */
    $('.sidenav').sidenav();
    /* ... floating button to open side nav bar */
    $('.fixed-action-btn').floatingActionButton();
    /* ... dropdown elements */
    $('.dropdown-trigger').dropdown();
    /* ... back-to-top button */
    $('.fixed-action-btn').floatingActionButton();
    /* ... customisation drop-downs */
    $('select').formSelect();
});

/* Navbar - need to add mouseenter and mouseleaves on li.nav-option
    and li.nav-option a to highlight whole box when insider */

/* Tablet and Mobile Only */

if ($(window).width() < 1280) {
    $("#searchButton").html("<i class='fas fa-search' aria-label='Search Products'></i>");
    $("#searchReset").html("<i class='fas fa-power-off' aria-label='Reset Search Criteria'></i>");
    /* does cart-total change only need to happen on mobile screens? */
    $(".cart-total").attr("colspan","4");
};