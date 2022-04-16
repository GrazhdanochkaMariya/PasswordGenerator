from django.shortcuts import render
from django.http import HttpResponse
import random
import string


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):

    characters = string.ascii_lowercase
    length = 10
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})
