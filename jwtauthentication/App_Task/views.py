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
        
class TaskDetailView(APIView):
    def get(self,request,id):
        try:
            data=Task.objects.get(id=id)
            serializer=TaskSerializer(data)
            return Response({'task':serializer.data})
        except:
            return Response({'message':'no task found'})
        
class TaskAddView(APIView):
    def post(self, request):
       try: 
            data=request.data
            print(data)
            serializer = TaskSerializer(data,context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'message': 'New task added successfully', 'Task': serializer.data})
       except:    
           return Response({'status': False, 'error': serializer.error_messages})
       
class TaskDeleteView(APIView):
    def delete(self,request,id):
        try:
            data=Task.objects.get(id=id).delete()
            return Response({'status':True,'message':'task delete successfully'})
        except:
            return Response({'status':False,'message':'Task Not Delete Successfully'})
        
        
    
        
        
        
        
        

    
            
            
            
        
        
        
        
