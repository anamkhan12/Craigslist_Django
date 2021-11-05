import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

def home(request):
    return render(request,'base.html')

def new_search(request):
    data_searched = request.POST.get('search')
    data_for_frontend = {
       'search' : data_searched,
    }
    return render(request,'my_app/new_search.html',data_for_frontend)