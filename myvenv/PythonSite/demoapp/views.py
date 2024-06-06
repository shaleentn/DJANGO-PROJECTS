from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homepage(request):
    content="<html><body><h1>My first Python Site</h1></body></html>"
    return HttpResponse(content)