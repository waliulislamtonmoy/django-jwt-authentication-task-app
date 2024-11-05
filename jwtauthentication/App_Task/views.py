from django.shortcuts import render

# Create your views here.
from App_Task.models import Task
from App_Task.serializer import TaskSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class TaskView(APIView):
    def get(self,request):
        try:
            data=Task.objects.all().order_by('-id') 
            serializer=TaskSerializer(data,many=True)
            return Response({'task':serializer.data})
        except:
            return Response({'message':'no task found'})

    
            
            
            
        
        
        
        
