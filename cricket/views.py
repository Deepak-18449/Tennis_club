from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound

# Create your views here.
def index(request):
    return HttpResponse("welcome cricket home page")

def index2(request):
    return HttpResponse("welcome cricket page")