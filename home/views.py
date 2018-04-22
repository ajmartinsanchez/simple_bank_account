from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from home.models import Profile
from home.forms import UserForm,ProfileForm
from django.views import View


class Home(View):
    def get(self, request):
        return render(request, 'home/home.html')

class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

    def post(self, request):
        logout(request)
        return HttpResponseRedirect('/')
"""
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            raise Exception(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'home/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
"""

