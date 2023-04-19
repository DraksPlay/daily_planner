from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    tasks = []
    if request.user:
        tasks = Task.objects.filter(user_id=request.user.id)
    return render(request, "tasks/index.html", context={"tasks": tasks})


def create(request):
    if request.user.id is not None:
        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                task = Task(title=form.cleaned_data["title"], content=form.cleaned_data["content"], user_id=request.user.id)
                task.save()
                return HttpResponseRedirect('..')
        else:
            form = TaskForm
        return render(request, "tasks/create.html", context={"form": form})
    else:
        return HttpResponse(status=404)


def delete_tasks(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        tasks_id = data.get('tasks_id')
        for task_id in tasks_id:
            task = Task.objects.get(id=task_id)
            task.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)


def edit_task(request):
    if request.user.id is not None:
        if request.method == "POST" and request.session.get("task_id") is not None:
            form = TaskForm(request.POST)
            if form.is_valid():
                task = Task.objects.filter(id=request.session.get("task_id"))
                task.update(title=form.cleaned_data["title"], content=form.cleaned_data["content"])
                return HttpResponseRedirect('..')
        else:
            request.session["task_id"] = request.GET.get("task_id")
            task = Task.objects.get(id=request.session.get("task_id"))
            form = TaskForm(initial={'title': task.title, "content": task.content})
        return render(request, "tasks/edit.html", context={"form": form})
    else:
        return HttpResponse(status=404)


def set_session(request):
    if request.method == 'POST':
        request.session['key'] = request.POST.get('value')
        return redirect('success-page')
    return render(request, 'index.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

