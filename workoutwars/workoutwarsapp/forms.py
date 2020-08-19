from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone

from workoutwarsapp.models import Team, Class, Exercise, Workout

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,
        label='First Name')
    last_name = forms.CharField(max_length=30, required=True,
        label='Last Name')
    nick_name = forms.CharField(max_length=30, required=False,
        label='Nickname',
        help_text='(or what you go by if you don&#39;t have one)'
        )
    email = forms.EmailField(max_length=254, required=True)
    # team = forms.ModelChoiceField(
    #     queryset=Team.objects.all(),
    #     required=False,
    #     help_text='Check PQ Captains\' email for your assigned team'
    #     )
    class_name = forms.ModelChoiceField(
        queryset=Class.objects.all(),
        label='Pods',
        required=True
         )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'nick_name', 'email', 'class_name', 'password1', 'password2', )

class AddWorkoutForm(forms.ModelForm):
    workout_date = forms.DateField(
        initial=timezone.now,
        widget=forms.SelectDateWidget(years=(range(2020, 2021)),
            months={5: ('May'), 4:('April'), 3:('March')}),
        label="Workout Date",
        required=True,
        help_text="When did you do the workout?"
        )
    exercise = forms.ModelChoiceField(
        queryset=Exercise.objects.all().order_by('description'),
        required=True
        )
    duration = forms.DecimalField(
        min_value=0, max_digits=5, decimal_places=2,
        required=True,
        label="Duration (in mins)",
        help_text="unless pushups or burpees (quantity)")
    # with_other_class = forms.BooleanField(required=False)

    class Meta:
        model = Workout
        fields = ('workout_date', 'exercise', 'duration')
