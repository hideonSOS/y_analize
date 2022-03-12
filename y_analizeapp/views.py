from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return render(request,'y_analizeapp/template.html')

def page1(request):
    return render(request,'y_analizeapp/page1.html')

def page2(request):
    return render(request,'y_analizeapp/page2.html')