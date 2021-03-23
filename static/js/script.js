/* jQuery for interactive design */

/* jshint esversion: 6 */
/* globals $:false */
/* Comments above tells JSHint what version of JS is being used, and secondly overrides JSHint's assumption that the 
$ symbol is an undefined variable */

$(document).ready(function(){
    /* initialises mobile side navigation bar */
    $('.sidenav').sidenav();
});

if ($(window).width() < 992) {
    $('.trigger-display a').click(function() {
        $('#mobile-snav').toggle();
    });
}