from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Task


# Create your views here.
def index(request):
    tasks = []
    if request.user:
        tasks = Task.objects.filter(user_id=request.user.id)
    return render(request, "tasks/index.html", context={"tasks": tasks})


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class LogOut(CreateView):
    success_url = reverse_lazy("logout")
    template_name = "registration/logout.html"
