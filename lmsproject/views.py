from django.http import HttpResponse
from django.shortcuts import render, redirect

def  signin(request):
        return render(request,'signin.html')  