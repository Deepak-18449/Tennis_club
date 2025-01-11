from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    # return HttpResponse("welcome home page")
    return HttpResponse(render_to_string('tennis/tennis.html'))

def index2(request):
    return HttpResponse("welcome tennnis page")