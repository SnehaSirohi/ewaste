from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from myapp.models import Form_edonator
from datetime import datetime

# Create your views here.
def index(request):
   
    return render(request,'index.html')

def about(request):
    return HttpResponse("this is aboutpage")

def services(request):
    return HttpResponse("this is servicespage")

def login(request):
    return HttpResponse("this is loginpage")

def loginall(request):
    return render(request,'loginall.html')

def form_edonator(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Contact_no = request.POST.get('Contact_no')
        email = request.POST.get('email')
        address = request.POST.get('address')
        e_img = request.POST.get('e_img')
        form_edonator = Form_edonator(Name=Name,Contact_no=Contact_no, email=email, address=address, e_img=e_img, date=datetime.today())  
        form_edonator.save()
    return render(request,'form_edonator.html')