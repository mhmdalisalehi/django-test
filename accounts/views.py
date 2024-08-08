from django.shortcuts import render,redirect
from .forms import UserRegistrationForm, UserLoginForm
from .models import User,Profile
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.signals import post_save


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['username'], email=data['email'], phone=data['phone']
                                     , password=data['password2'])
            user.save()
            login(request, user)
            messages.success(request, 'Thank you for registering', 'primary')
            return redirect('home:home')
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
                user = authenticate(request,username=User.objects.get(email=data['user']).username, password=data['password'])
            except:
                user = authenticate(request,username=data['user'], password=data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in',extra_tags='primary')
                return redirect('home:home')
            else:
                messages.error(request, 'Invalid username or password', 'danger')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request,'accounts/login.html', context)


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.',extra_tags='primary')
    return redirect('home:home')


@login_required
def user_profile(request):
    profile = Profile.objects.get(user_id=request.user.id)
    return render(request,'accounts/profile.html', {'profile':profile})


def save_user_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = Profile(user=kwargs['instance'])
        user_profile.save()


post_save.connect(save_user_profile, sender=User)


def user_update(request):
    return render(request,'accounts/update.html')