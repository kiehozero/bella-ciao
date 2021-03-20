from django.shortcuts import render


def index(request):
    """ Homepage """
    return render(request, 'home/index.html')
