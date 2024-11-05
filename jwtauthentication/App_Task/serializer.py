from rest_framework.serializers import ModelSerializer
from App_Task.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'
    
    