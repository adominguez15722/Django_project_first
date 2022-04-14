from django.shortcuts import render
from datetime import datetime
# Create your views here.

from django.http import HttpResponse

def welcome(request):
    return HttpResponse('Welcome to the Meeting Planner Application')

def date(request):
    return HttpResponse(f'This page was served at {str(datetime.now())}')

def about(request):
    return HttpResponse('My name is Anthony Dominguez')