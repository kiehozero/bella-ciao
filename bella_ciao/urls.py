"""bella_ciao URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('events/', include('events.urls')),
    path('products/', include('products.urls')),
    path('profiles/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
