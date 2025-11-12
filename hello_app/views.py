from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def print_hello(request):
    movie_data =  {
        'movies':[
            {
        'title' : 'Godfather',
        'year': 1990,
        'summury' : 'sdfghjkxcvbnmcv',
        'success' : False,
            },
            {
        'title' : 'Godfather',
        'year': 1990,
        'summury' : 'sdfghjkxcvbnmcv',
        'success' : False,
            },
            {
        'title' : 'Godfather',
        'year': 1990,
        'summury' : 'sdfghjkxcvbnmcv',
        'success' : False,
            },
            ]
    }
    return render(request,'hello.html',movie_data)