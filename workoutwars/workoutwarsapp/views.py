# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# workoutwarsapp/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Can also use the following format (a get request will
# automatically use this template):
# class HomePageView(TemplateView):
#     template_name = "about.html"
