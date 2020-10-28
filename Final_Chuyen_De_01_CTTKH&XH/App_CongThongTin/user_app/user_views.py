from django.contrib.auth import logout,login,authenticate,update_session_auth_hash
from django.shortcuts import render,redirect
from django.contrib import messages
from ..forms import *


def home(request):
    return render(request,'base.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('news:home')
        else:
            messages.success(request, ('Error logging in - Please try again!'))
            return redirect('news:login')
    else:
        return render(request, 'Login_tempalte/Login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!'))
    return redirect('news:home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, ('You have been logged in!'))
                return redirect('news:home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'Login_tempalte/register.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have been Edited your profile!'))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'Login_tempalte/edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form = EditPasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # so that id doesnt log out after password change
            messages.success(request, ('You have Changed your Password!'))
            return redirect('news:home')
    else:
        form = EditPasswordForm(user=request.user)

    context = {'form': form}
    return render(request, 'Login_tempalte/change_password.html', context)
