from django.shortcuts import render,HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")


def welcome(request):
    return render(request,'index.html')