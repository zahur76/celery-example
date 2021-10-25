"""
    All imports
"""
from django.shortcuts import (
    render, reverse, redirect, get_object_or_404, HttpResponse)


def home(request):
    """ A view to return the home page with site request"""
    
    return render(request, 'home/index.html')


def calculate(request):
    """ A view to return the home page with site request"""
    new_list = []

    list_numbers = list(range(10000))
    for i in list_numbers:
        new_list.append(i+2)

    context = {
        "list": new_list,
    }
    
    return render(request, 'home/calculate.html', context)