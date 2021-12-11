from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Profile

# Create your views here.

def register(request):
    '''View used to validate the form and save the user in database'''
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        pfp = Profile(user= user)
        pfp.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f"Account {username} created. You can login now.")
        # return redirect('user-login')
    
    return render(request, 'user/register.html', {'form': form, 'title': 'Register'})

