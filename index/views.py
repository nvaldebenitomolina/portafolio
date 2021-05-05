from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def project1(request):
    return render(request,'project1.html',{})
def project2(request):
    return render(request,'project2.html',{})
def project3(request):
    return render(request,'project3.html',{})
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