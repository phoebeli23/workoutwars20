# workoutwarsapp/urls.py
from django.conf.urls import url
from workoutwarsapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # home page
    url(r'^$', views.HomePageView.as_view()),

    # authentication pages
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup',),

    # workout pages
    url(r'^add/$', views.addworkout, name='add',),
    url(r'^scoreboard/$', views.scoreboard, name='scoreboard',),
    url(r'indiv/$', views.indiv, name='indiv'),
]
