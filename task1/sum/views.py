from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'sum/base.html')

def print(request):
    n1= int(request.POST["num1"])
    n2= int(request.POST["num2"])
    return render(request, 'sum/result.html', {"r":range(n1,n2+1), "first":n1, "sec":n2})

