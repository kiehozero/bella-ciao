from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_name',
        'default_phone_number',
        'default_street_address1',
        'default_street_address2',
        'default_city',
        'default_eircode',
    )

    ordering = ('user',)


admin.site.register(UserProfile, UserProfileAdmin)
