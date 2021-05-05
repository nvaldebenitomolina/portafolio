from django.shortcuts import render


import portafolio.project1 as pr1
import portafolio.project2 as pr2
import portafolio.project3 as pr3
# Create your views here.
def index(request):
    return render(request,'index.html',{})

def project1(request):

    return render(request, "project1.html", context={'plot_div': pr1.plot1})

  
def project2(request):
    return render(request, "project2.html", context={'plot_div': pr2.plot1})
def project3(request):
    return render(request, "project3.html", context={'plot_div': pr3.plot1})
def project4(request):
    return render(request,'project4.html',{})
def project5(request):
    return render(request,'project5.html',{})
def project6(request):
    return render(request,'project6.html',{})

def challenge1(request):
    return render(request,'challenge1.html',{})

def challenge2(request):
    return render(request,'challenge2.html',{})

def challenge3(request):
    return render(request,'challenge3.html',{})

def challenge4(request):
    return render(request,'challenge4.html',{})

def challenge5(request):
    return render(request,'challenge5.html',{})