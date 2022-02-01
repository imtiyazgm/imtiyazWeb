from django.shortcuts import redirect, render
from . models import Profile, WorkExpirnce
# import for loging / logout 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Profile
from django.contrib import messages


# Create your views here.

def profile(request):
    profile_details = Profile.objects.all()
    workExp_details =reversed(WorkExpirnce.objects.all())
    context = {'profile_details':profile_details, 'workExp_details':workExp_details }
    return render(request, 'users/profile.html', context)


    

def login_user(request):
    if request.user.is_authenticated:
        return redirect('user-profile')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')
            

        user =authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('user-profile')
        else:
            messages.error(request, 'Username or Password are incorrect')
            

    return render(request, "users/login_register.html" )


def logoutUser(request):
    logout(request)
    return redirect('loginPage')
