from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def myFunction(request):
    return HttpResponse(('Hello World'))

def myFunctionAbout(request):
    return HttpResponse('About Response')

def add(request, a, b):
    return HttpResponse(a+b)

def intro(request, name, age):
    myDictionary = {
        "name" : name,
        "age" : age
    }
    return JsonResponse(myDictionary)
