from django.shortcuts import render,redirect
from .forms import UserRegistrationForm, UserLoginForm
from .models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username=data['username'], email=data['email'], phone=data['phone']
                                     , password=data['password'])

    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = authenticate(username=data['username'], password=data['password'])

            except:
                user = authenticate(email=data['email'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('home:home')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request,'accounts/login.html', context)


def user_logout(request):
    logout(request)

