from django.shortcuts import render,HttpResponse
import random
from django.http import JsonResponse
def home(request):
    return render(request,'index.html')

def passgen(request):
    char=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('digits'):
        char.extend(list('0123456789'))
    if request.GET.get('symbol'):
        char.extend(list('!@#$%^&*'))
    length=(int(request.GET.get('length')))
    password=""
    for x in range(length):
        password+=random.choice(char)
    pas={'password':password}
    # return JsonResponse(pas)
    return render(request,'password.html',{'password':password,'name':"Alok"})

# Create your views here.
