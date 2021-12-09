from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random
def home(request):
    return render(request,'generator/home.html')
def about(request):
    return render(request,'generator/about.html')
    
def password(request):
    thepassword=''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length =int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    if request.GET.get('specialcharacters'):
        characters.extend('!@#$%^&*()')    
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})

