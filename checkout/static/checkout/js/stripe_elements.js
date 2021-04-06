/* Logic and Code taken from a cominbation of the Stripe
documentation in the README and the Boutique Ado tutorial */

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
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

// Error validation in the main card element
card.addEventListener('change', function(event) {
    var cardErrorDiv = document.getElementById('card-errors');
    if (event.error) {
        var errorPrompt = `
            <span role="alert">
                <i class="far fa-times-circle"></i>
            </span>
            <span>${event.error.message}</span>`
        $(cardErrorDiv).html(errorPrompt);
    } else {
        cardErrorDiv.textContent = '';
    }
})

// Form Submission

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span role="alert">
                    <i class="fas fa-times-circle"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});