from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login, authenticate
from y_analizeapp.forms import LoginForm
from . import function
from .forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required

@login_required
def test(request):
    return render(request,'y_analizeapp/template.html')

@login_required
def page1(request):
    inputbox1 = request.POST.get('inputbox1')
    inputbox2 = request.POST.get('inputbox2')
    print(inputbox1,inputbox2)
    page1_dict = function.send_page1(inputbox1,inputbox2)
    
    return render(request,'y_analizeapp/page1.html', {'page1_dict':page1_dict})

@login_required
def page2(request):
    return render(request,'y_analizeapp/page2.html')

@login_required
def page3(request): 
    inputbox1 = request.POST.get('inputbox1')
    if inputbox1 == '1':
        page3_dict = page3_dict=function.send_page3()
    else:
        page3_dict = page3_dict=function.send_page3()

    page3_dict = page3_dict=function.send_page3()
    
    
    return render(request,'y_analizeapp/page3.html',{'page3_dict':page3_dict})

@login_required
def page4(request):
    return render(request, 'y_analizeapp/page4.html')


class Login(LoginView):
    form_class = LoginForm
    template_name='y_analizeapp/login.html'

class Logout(LogoutView):
    template_name='y_analizeapp/logout.html'


def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            # 読み取った情報をログインに使用する情報として new_user に格納
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                # new_user の情報からログイン処理を行う
                login(request, new_user)
                # ログイン後のリダイレクト処理
                return redirect('home')
            # POST で送信がなかった場合の処理
            
    else:
        form = SignUpForm()
        
    return render(request, 'boatnavi5app/signup.html', {'form':form})