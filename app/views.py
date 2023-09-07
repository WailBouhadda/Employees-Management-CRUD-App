from django.shortcuts import render
from .models import Employee
# Create your views here.

def index(request):
    return render(request, "app/index.html")

def adduser(request):
    return render(request, "app/adduser.html")

def insertuser(request):

    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    phone = request.POST['phone']

    emp = Employee(firstname=firstname, lastname=lastname, phone=phone);

    emp.save()

    return render(request, 'app/index.html')
