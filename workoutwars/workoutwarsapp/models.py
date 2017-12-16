# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=30)
    class_name = models.ForeignKey('Class', on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, blank=True)

    def __unicode__(self):
        return '{}'.format(self.nick_name)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Workout(models.Model):
    workout_date = models.DateField(default = timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE, null=True)
    duration = models.DecimalField(max_digits = 5, decimal_places = 2,default = 15)
    with_other_class = models.BooleanField(default=False)

    @property
    def score(self):
        d = self.duration
        i = self.exercise.increment
        m = self.exercise.multiplier
        s = d / i * m
        #Bonus point for working out with a teammate from another class
        if self.with_other_class:
            s += 1
        return s

    def __unicode__(self):
        return '{0} | {1:%b-%d} | Score={2}'.format(
            self.user,
            self.workout_date,
            self.score,
          )

class Exercise(models.Model):
    description = models.CharField(max_length=60)
    notes = models.CharField(max_length=60, blank=True)
    measurement = models.CharField(max_length=60, default="mins")
    increment = models.DecimalField(
        max_digits = 5,
        decimal_places = 2,
        default = 15.0)
    multiplier = models.DecimalField(
        max_digits = 5,
        decimal_places = 2,
        default = 1.0)

    def __unicode__(self):
        return '{}'.format(self.description)

class Team(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return '{}'.format(self.name)

class Class(models.Model):
    name = models.CharField(max_length=30)
    plural = models.CharField(max_length=30)

    def __unicode__(self):
        return '{}'.format(self.name)