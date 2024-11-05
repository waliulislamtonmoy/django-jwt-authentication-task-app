from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from App_Task.models import Task

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['username','email']

class TaskSerializer(ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=Task
        fields='__all__'
        depth=1
    
    