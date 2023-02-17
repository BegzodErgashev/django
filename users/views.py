from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate


# Create your views here.
def login(request):
    return render(request=request, template_name='login.html')
