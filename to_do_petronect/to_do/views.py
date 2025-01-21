
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import Task_Form

def creat_task_view(request):
    if request.method == "POST":
        form = Task_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Task_Form()
    context = {"form": form}
    return render(request, "to_do/task_form.html", context)

def edit_task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'GET':
        form = Task_Form(instance=task)
        context = {"form": form}
        return render(request, "to_do/task_form.html", context)
    elif request.method == 'POST':
        form = Task_Form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, "to_do/error_page1.html")
    
def index(request):
    task_list = Task.objects.order_by("-pub_date")
    context = {"task_list": task_list}
    return render(request,"to_do/index.html", context)