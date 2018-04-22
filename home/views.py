from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db import transaction
from home.models import ClientBank
from home.forms import ClientForm
from django.views import View


class Home(View):
    def get(self, request):
        context = {}
        email = request.user.email
        user = User.objects.filter(email=email).first()

        if not user or not user.is_staff:
            logout(request)
            return HttpResponseRedirect('/')

        context['clients'] = ClientBank.objects.filter(creator=user)
        return render(request, 'home/home.html', context)

class AddClient(View):
    def get(self, request):
        context = {}
        form = ClientForm()

        context['form'] = form

        return render(request, 'home/client.html', context)

    def post(self, request):
        context = {}
        form = ClientForm(request.POST)

        if form.is_valid():
            form.save(creator=request.user)
            return HttpResponseRedirect('/')

        context['form'] = form

        return render(request, 'home/client.html', context)

class UpdateClient(View):
    def get(self, request, *args, **kwargs):
        context = {}
        client = ClientBank.objects.filter(id=kwargs.get('user_id'), creator=request.user).first()
        if not client:
            return HttpResponseRedirect('/')

        form = ClientForm(instance=client)
        context['form'] = form

        return render(request, 'home/client.html', context)

    def post(self, request, *args, **kwargs):
        context = {}

        client = ClientBank.objects.filter(id=kwargs.get('user_id'), creator=request.user).first()
        if not client:
            return HttpResponseRedirect('/')

        form = ClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        context['form'] = form

        return render(request, 'home/client.html', context)


class RemoveClient(View):
    def get(self, request, *args, **kwargs):
        client = ClientBank.objects.filter(id=kwargs.get('user_id'), creator=request.user).first()
        if not client:
            return HttpResponseRedirect('/')

        client.delete()
        return HttpResponseRedirect('/')


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

    def post(self, request):
        logout(request)
        return HttpResponseRedirect('/')

