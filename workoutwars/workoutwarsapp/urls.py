# workoutwarsapp/urls.py
from django.conf.urls import url
from workoutwarsapp import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
