/* Logic and Code taken from a cominbation of the Stripe
documentation in the README and the Boutique Ado tutorial */

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
    base: {
        color: '#303238',
        fontSize: '14px',
        fontFamily: '"Montserrat", sans-serif',
        fontSmoothing: 'antialiased',
        '::placeholder': {
            color: '#CFD7DF',
        },
    },
    invalid: {
        color: '#e5424d',
        ':focus': {
            color: '#303238',
        },
    },
};

var card = elements.create('card', {style: style});
card.mount('#card-element');