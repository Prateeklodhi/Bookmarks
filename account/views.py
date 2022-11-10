from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,UserResgistrationForm, UserEditForm,ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.
@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'section':'deshboard'})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print("Yupiee")
            cd = form.cleaned_data
            user = authenticate(request,username = cd["username"],password = cd["password"])
            if user is not None:
                print("Yess")
                if user.is_active:
                    print("Yes")
                    login(request,user)
                    return HttpResponse('Authenticated Suceessfully')
                else:
                    print("No")
                    return HttpResponse('Disabled Account')
        else:
            print("Noo")
            return HttpResponse('Invalid login')
          
    else:
        print("Ohh noo")
        form = LoginForm()
    return render(request,'account/login.html',{'form':form})
    

def register(request):
    if request.method =='POST':
        user_form = UserResgistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            #set the chosen password
            new_user.set_password(user_form.cleaned_data['password']
            )
            #save the user object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,'account/register_done.html',{'new_user':new_user})
    user_form = UserResgistrationForm()
    return render(request,'account/register.html',{'user_form':user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form =ProfileEditForm(instance=request.user.profile,data = request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Profile updated successfully')
        else:
            messages.error(request,'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'account/edit.html',{'user_form':user_form,'profile_form':profile_form
    })