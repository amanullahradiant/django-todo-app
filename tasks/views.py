from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
import json


# Create your views here.
def index(request):
    # return HttpResponse("hello world!")
    createTaskForm = TaskForm()

    tasks = Task.objects.all()

    context = {"tasks": tasks, "createTaskForm": createTaskForm}
    return render(request, "tasks/list.html", context)


def createPost(request):
    if request.method == "POST":
        # data = {"method": request.method, "POST": request.POST.dict()}
        # return JsonResponse(data)

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "tasks/update_task.html", context)
