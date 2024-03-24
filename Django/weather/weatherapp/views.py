from django.shortcuts import render, HttpResponse
import json
import requests
# Create your views here.
def weatherapp(request):
    if request.method=="POST":
        city=request.POST["city"]
        source=""
    return HttpResponse("<h1>Alok</h1>")