from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import contact
# Create your views here.

# def index(request):
#     return HttpResponse("This is my home page")
def index(request):
 return render(request,'index.html')
def about(request):
   return render(request,'about.html')
    # return HttpResponse("This is my about  page")
def services(request):
    return render(request,'services.html')
    # return HttpResponse("This is my services  page")

def contact(request):
    if request.method == "POST":
       name=request.POST.get('name')
       email=request.POST.get('email')
       password=request.POST.get('password')
       country=request.POST.get('country')
       gender=request.POST.get('gender')
       message=request.POST.get('message')
       contact=contact(name=name,email=email,password=password,country=country,gender=gender,message=message)
       contact.save()
    return render(request,'contact.html')


def mountains(request):
    return render(request, 'mountains.html')

def forests(request):
    return render(request, 'forests.html')

def beaches(request):
    return render(request, 'beaches.html')

def sunsets(request):
    return render(request, 'sunsets.html')