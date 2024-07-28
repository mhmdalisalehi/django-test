from django.shortcuts import render
from .forms import UserRegistrationForm


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)



