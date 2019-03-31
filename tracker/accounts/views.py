from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.



def loginview(request):
    if request.method == 'POST':
        user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return render(request, 'accounts/home.html')
        else:
            return render(request, 'accounts/login.html', {'error':'Please check the creds'})
    else:
        return render(request, 'accounts/login.html')


def signupview(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:

         try:
             user = User.objects.get(username=request.POST['username'])
             return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})

         except User.DoesNotExist:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return render(request, 'accounts/usercreated.html')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords did not match'})
    else: # here the request method is get
        return render(request, 'accounts/signup.html')




def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('accounts:login')



@login_required
def homeview(request):
    if request.method == 'POST':
        return render(request, 'accounts/home.html')
    else:
        return render(request, 'accounts/home.html')



def forgotview(request):
    return render(request, 'accounts/forgot.html')


def usercreatedview(request):
    return render(request, 'accounts/usercreated.html')
