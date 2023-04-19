from django import forms
from .models import Task


class TaskForm(forms.Form):
    title = forms.CharField(max_length=255)
    content = forms.CharField(max_length=4096, widget=forms.Textarea)

