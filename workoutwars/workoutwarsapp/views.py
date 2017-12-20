# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# workoutwarsapp/views.py
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

from workoutwarsapp.forms import SignUpForm, AddWorkoutForm
from workoutwarsapp.models import Profile, Class, Team, Exercise, Workout

# Page views
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

def scoreboard(request):
    classes = Class.objects.all()
    class_scores = []
    class_chart_data = []
    teams = Team.objects.all()
    team_scores = []
    team_chart_data = []

    for c in classes:
        c_workouts = Workout.objects.filter(user__profile__class_name=c)
        c_score = sum([workout.score for workout in c_workouts])
        c_count = len(Profile.objects.filter(class_name=c))
        if c_count == 0:
            c_normalized = 0
        else:
            c_normalized = c_score / c_count
        class_scores.append([c.plural, round(c_score), round(c_normalized)])
        class_chart_data.append([str(c.plural), round(c_normalized)])

    for t in teams:
        t_workouts = Workout.objects.filter(user__profile__team=t)
        t_score = sum([workout.score for workout in t_workouts])
        t_count = len(Profile.objects.filter(team=t))
        if t_count == 0:
            t_normalized = 0
        else:
            t_normalized = t_score / t_count
        team_scores.append([t.name, round(t_score), round(t_normalized)])
        team_chart_data.append([str(t.name), round(t_normalized)])

    try:
        recent_workouts = Workout.objects.all().order_by('workout_date')
    except ObjectDoesNotExist:
        recent_workouts = []

    return render(request,
        'scoreboard.html',
        {
            'class_scores': class_scores,
            'class_chart_data': class_chart_data,
            'team_scores': team_scores,
            'team_chart_data': team_chart_data,
        }
    )

@login_required
def indiv(request):
    workouts = Workout.objects.filter(user=request.user)
    try:
        workouts = Workout.objects.filter(user=request.user).order_by('-workout_date')
        scores = [w.score for w in workouts]
    except ObjectDoesNotExist:
        user_workouts = []
        scores = []
    num_workouts = len(workouts)
    total_points = round(sum(scores))

    return render(request,
        'indiv.html',
        {
            'workouts': workouts,
            'num_workouts': num_workouts,
            'total_points': total_points
        }
    )

@login_required
def feed(request):
    workouts = Workout.objects.all().order_by('-workout_date')
    try:
        workouts = Workout.objects.all().order_by('-workout_date')
    except ObjectDoesNotExist:
        workouts = []

    return render(request,
        'feed.html',
        {
            'workouts': workouts,
        }
    )


# Form views
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
            return redirect('scoreboard')
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
            return redirect('scoreboard')
    else:
        form = AddWorkoutForm()
    return render(request, 'add.html', {'form': form})
