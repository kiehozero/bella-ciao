/* Logic and Code taken from a cominbation of the Stripe
documentation in the README and the Boutique Ado tutorial */

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
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
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var errorPrompt = `
            <span role="alert">
                <i class="far fa-times-circle"></i>
            </span>
            <span>${event.error.message}</span>`;
        $(errorDiv).html(errorPrompt);
    } else {
        errorDiv.textContent = '';
    }
});

// Form Submission

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true);

    /* variables that can only be added as metadata payment intent and sends it to cache_checkout_data */
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
        /* add loyalty_stamps here, will be similar to saveInfo */
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                /* submits user information to Stripe, below items are fields that can
                be sent inside a payment intent, then populated with user's information */
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.city.value),
                    }
                }
            },
            shipping:    {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.city.value),
                    postal_code: $.trim(form.eircode.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var errorPrompt = `
                    <span role="alert">
                        <i class="fas fa-times-circle"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(errorPrompt);
                card.update({'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        /* posts error to Django messages and displays on reload */
        location.reload();
    })
});