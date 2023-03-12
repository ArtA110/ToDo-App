from django.shortcuts import render
from accounts.forms import UserForm, ProfileForm, LoginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from .models import User


def signup_view(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, user)

            return HttpResponseRedirect('/accounts/complete-profile/')
        else:
            return render(
                request, "accounts/signup.html", {"form": form}
            )
    user_form = UserForm()
    return render(request, 'accounts/signup.html', context={'user_form': user_form})


def complete_profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/todo/tasks/')
    profile_form = ProfileForm()
    return render(request, 'accounts/complete_profile.html', context={'profile_form': profile_form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():

            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/todo/tasks/')
            return HttpResponse('something went wrong')
        else:
            return render(request, 'accounts/login.html', context={'form': form})


    return render(request,'accounts/login.html', context={'form': LoginForm})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse('logged out')
    return redirect('/accounts/login/')


