from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile

# Create your views here.

def register(request):
    '''View used to validate the form and save the user in database'''
    form = UserRegisterForm(request.POST or None)
    if form.is_valid(): # Form Validation
        user = form.save()
        pfp = Profile(user= user)
        pfp.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f"Account {username} created. You can login now.")
        return redirect('user-login')
    
    return render(request, 'user/register.html', {'form': form, 'title': 'Register'})

@login_required
def profile(request):
    userForm = UserUpdateForm(request.POST or None, instance= request.user)
    profileForm = ProfileUpdateForm(request.POST or None, request.FILES, instance= request.user.profile)

    if userForm.is_valid() and profileForm.is_valid():
        userForm.save()
        profileForm.save()
        username = userForm.cleaned_data.get('username')
        messages.success(request, f"Account {username} successfully updated!")
        return redirect('user-profile')

    context = {
        'u_form': userForm,
        'p_form': profileForm,
        'title': 'Profile'
    }
    return render(request, 'user/profile.html', context)