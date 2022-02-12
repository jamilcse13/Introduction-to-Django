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

def myFristPage(request):
    return render(request, 'index.html')

def mySecondPage(request):
    return render(request, 'second.html')

def myThirdPage(request):
    var = "assalamu alaikum"
    greeting = "hey how are you?"
    fruits = ['apple', 'mango', 'banana']
    num1, num2 = 8, 5
    ans = num1>num2
    mydictionary = {
        "var" : var,
        "msg" : greeting,
        "myFruits" : fruits,
        "num1" : num1,
        "num2" : num2,
        "ans" : ans,
    }
    return render((request), 'third.html', context=mydictionary)

def myImagePage(request):
    return render(request, 'imagepage.html')

def myImagePage2(request):
    return render(request, 'imagepage2.html')

def myImagePage3(request):
    return render(request, 'imagepage3.html')

def myImagePage4(request):
    return render(request, 'imagepage4.html')

def myImagePage5(request, imagename):
    myImageName = str(imagename)
    myImageName = myImageName.lower()
    if myImageName == 'django':
        var = True
    elif myImageName == 'python':
        var = False
    mydictionary = {
        "var" : var
    }
    return render(request, 'imagepage5.html', context=mydictionary)

def myForm(request):
    return render(request, 'myform.html')

def submitMyFrom(request):
    mydictionary = {
        "text" : request.POST['myText'],
        "textarea" : request.POST['myTextarea'],
        "method" : request.method
    }
    return JsonResponse(mydictionary)