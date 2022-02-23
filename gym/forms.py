from django import forms
from .models import Practice, Exercises


class AddPracticeForm(forms.ModelForm):
    class Meta:
        model = Practice
        fields = ['title', 'date_plan']


class AddExercisesForm(forms.ModelForm):
    class Meta:
        model = Exercises
        fields = ['title', 'podhod', 'povtor', 'weight_work', 'es','md','hd']