from django.shortcuts import render
from django.http import HttpResponse
from . import function

def test(request):
    return render(request,'y_analizeapp/template.html')

def page1(request):
    inputbox1 = request.POST.get('inputbox1')
    inputbox2 = request.POST.get('inputbox2')
    page1_dict = function.send_page1(inputbox1,inputbox2)
    
    return render(request,'y_analizeapp/page1.html', {'page1_dict':page1_dict})

def page2(request):
    return render(request,'y_analizeapp/page2.html')

def page3(request): 
    
    page3_dict = function.send_page3()
    return render(request,'y_analizeapp/page3.html',{'page3_dict':page3_dict})