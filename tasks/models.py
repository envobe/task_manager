from django.db import models
# from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User


# class User(models.Model):
#     projects = []
#     tasks = []
#
#     def add_project(self, project):
#         self.projects.append(project)
#         project.add_user(self)
#
#     def add_task(self, task):
#         self.tasks.append(task)
#         return self.tasks

class Project(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    project_title = models.FileField()
    users = []
    tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return self.tasks

    def add_user(self, user):
        self.users.append(user)
        user.add_project(self)
    #
    # def get_absolute_url(self):
    #     return reverse('tasks:detail', kwargs={'pk': self.pk})

    def __str__(self):
       return self.project_title

class Task(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, default=1, on_delete=models.CASCADE)

    task_title = models.FileField()
    task_description = models.FileField()
    task_due_date = models.FileField()


    def get_absolute_url(self):
        return reverse('tasks:detail', kwargs={'pk': self.pk})

    def __str__(self):
        #return self.template_logo + '-' + self.template_title
        return self.task_title + '-' + self.task_description + '-' + self.task_due_date




