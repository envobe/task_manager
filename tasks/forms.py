from django import forms
from django.contrib.auth.models import User

from .models import Project,Task

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['project_title']

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['task_title', 'task_description', 'task_due_date']