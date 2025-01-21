from django import forms
from django.forms import ModelForm
from .models import Task

class Task_Form(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date"]
        widgets = {
            'due_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

