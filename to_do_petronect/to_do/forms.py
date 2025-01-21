from django.forms import ModelForm
from .models import Task

class Task_Form(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date"]

