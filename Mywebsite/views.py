from django.http import HttpResponse
from django.shortcuts import render
import datetime
def aboutUS(request):
    return HttpResponse("Welcome to my website")
def homepage(request):
    date=datetime.datetime.now()
    print("homepage function is called from views")
    return render(request,"home.html",{})
def aboutpage(request):
    date=datetime.datetime.now()
    print("aboutpage function is called from views")  
    name="LearnCodeWithANNU"
    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle'
    ]
    student={
        'student_name':"Rahul",
        'student_college':"ZYZ",
        'student_city':'LUCKNOW'
    }
    # return HttpResponse("<h1>Hello this is index page  </h1> "+str(date))
    data={
        'date':date,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    return render(request,"about.html",data)
def servicespage(request):
    date=datetime.datetime.now()
    print("servicespage function is called from views")
    return render(request,"services.html",{})
    
