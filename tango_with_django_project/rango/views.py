from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse('<html><body><p>Rango says hello world!</p><br><a href="/rango/about">About page</a>')


def about(request):
	return HttpResponse('<html><body><p>Rango Says: Here is the about page</p> <br><a href="/rango/">Index</a>')


