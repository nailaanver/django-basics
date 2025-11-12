from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def print_hello(request):
    movie_details = {
        'title' : 'Godfather',
        'year': 1990,
        'summury' : 'sdfghjkxcvbnmcv'
    }
    return render(request,'hello.html',movie_details)