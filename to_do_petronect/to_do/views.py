from django.shortcuts import render
from .models import Task_list

def index(request):
    task_list = Task_list.objects.order_by("-pub_date")
    context = {"task_list": task_list}
    return render(request,"to_do/index.html", context)