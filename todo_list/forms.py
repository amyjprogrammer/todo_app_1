"""Forms page for my todo list app"""

from django import forms

from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['context', 'completed']
        labels = {'context': '', 'completed': 'completed'}
