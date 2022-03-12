from django.shortcuts import render
from django.http import HttpResponse
from . import function

def test(request):
    return render(request,'y_analizeapp/template.html')

def page1(request):
    page1_dict = function.send_page1()
    print(page1_dict)
    return render(request,'y_analizeapp/page1.html', {'page1_dict':page1_dict})

def page2(request):
    function.test()
    return render(request,'y_analizeapp/page2.html')