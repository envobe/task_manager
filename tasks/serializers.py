from rest_framework import serializers

from tasks.models import Task

from django.contrib.auth.models import User



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'id', 'task_title', 'task_description', 'task_due_date')



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')