from django.contrib import messages
from django.shortcuts import render


def index(request):
    """ Homepage """
    return render(request, 'home/index.html')


def faq(request):
    """ Frequently Asked Questions """
    return render(request, 'home/faq.html')


def contact(request):
    """ Contact Form"""

    return render(request, 'home/contact.html')
