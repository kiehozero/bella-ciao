from django import forms

from .models import UserProfile


# based on checkout form from Boutique Ado
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = (
            'user',)

    def __init__(self, *args, **kwargs):
        """ Adds some user-friendly placeholders and form styling,
        this is taken from the Boutique Ado project """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_city': 'City',
            'default_eircode': 'Eircode',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'text-red mx-5 profile-form-input'
            self.fields[field].label = False
