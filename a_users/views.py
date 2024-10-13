from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def profile(request):
    profile = request.user.profile
    return render(request,'profile.html',{'profile':profile})



@login_required
def profile_edit(request):
    form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    return render(request,'profile_edit.html',{'form':form})