# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# workoutwarsapp/views.py
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import TemplateView

from workoutwarsapp.forms import SignUpForm, AddWorkoutForm

# Home page view
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Can also use the following format (a get request will
# automatically use this template):
# class HomePageView(TemplateView):
#     template_name = "about.html"

# Authentication views
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() # load the profile instance created by the signals
            user.profile.nick_name = form.cleaned_data.get('nick_name')
            user.profile.class_name = form.cleaned_data.get('class_name')
            user.profile.team = form.cleaned_data.get('team')
            if not user.profile.nick_name:
                user.profile.nick_name = user.first_name + " " + user.last_name
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def addworkout(request):
    if request.method == 'POST':
        form = AddWorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('/')
    else:
        form = AddWorkoutForm()
    return render(request, 'add.html', {'form': form})
