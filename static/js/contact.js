/* Scripts for contact form interactivity */

/* jshint esversion: 6 */
/* globals $:false */
/* Comments above tells JSHint what version of JS is being used, and secondly overrides JSHint's assumption that the 
$ symbol is an undefined variable */

/* EmailJS requests */

/* Copied from the Code Institute resume tutorial */

function sendMail(contactForm) {
    emailjs.send("gmail", "template_vn6mied", {
        "name": contactForm.name.value, 
        "email_address": contactForm.email.value, 
        "feedback": contactForm.feedback.value,
    })
    .then(
        function(response) {
            $("#full_name").val("");
            $("#email_address").val("");
            $("#feedback").val("");
            $("#sendButton").html("<i class='far fa-check-square'></i>Message sent!");
            $("#sendButton").prop('disabled', true);
        },

        function(error) {
            alert("Please complete all fields.");
        }
    );
    return false;
}