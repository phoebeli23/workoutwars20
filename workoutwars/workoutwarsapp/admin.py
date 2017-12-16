# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from workoutwarsapp.models import Profile, Workout, Exercise, Team, Class

# Register your models here.
admin.site.register(Profile)
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Team)
admin.site.register(Class)
