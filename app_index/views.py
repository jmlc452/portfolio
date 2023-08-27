from django.shortcuts import render,redirect
import smtplib

# Create your views here.

def index(request):
    return render(request,'indexEn.html')

def alter_index(request):
    return render(request,'index.html')
