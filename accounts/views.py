from random import randint

from django.shortcuts import render,redirect
from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm, ProfileUpdateForm, PhoneLoginForm, VerifyForm
from .models import User,Profile
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
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


@login_required
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!', 'success')
            return redirect('accounts:user_profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'user_form': user_form, 'profile_form': profile_form}

    return render(request,'accounts/update.html',context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password has been updated!', 'success')
            return redirect('accounts:user_profile')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'accounts/change.html', context)


def login_phone(request):
    if request.method == 'POST':
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            global random_code,phone_number
            phone_number = form.cleaned_data['phone']
            if User.objects.filter(phone=phone_number).exists():
                random_code = randint(100000,999999)
                print(random_code)
                # sms=ghasedak.Ghasedak('APIKEY')
                # sms.send({'message': random_code,'receptor':phone,'linenumber':"10008566"})
                return redirect('accounts:verify')
            else:
                messages.error(request, 'Invalid phone number', 'danger')




    else:
        form = PhoneLoginForm()
    context = {'form': form}
    return render(request,'accounts/phoneLogin.html', context)


def verify(request):
    if request.method == 'POST':
        form = VerifyForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['code'] == random_code:
                user = User.objects.get(phone=phone_number)
                login(request, user)
                return redirect('home:home')
            else:
                messages.error(request, 'Invalid code', 'danger')
    else:
        form = VerifyForm()
    context = {'form': form}
    return render(request,'accounts/verify.html',context)

