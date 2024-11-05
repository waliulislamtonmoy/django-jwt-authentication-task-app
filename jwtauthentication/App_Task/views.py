from django.shortcuts import render

# Create your views here.
from App_Task.models import Task
from App_Task.serializer import TaskSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status

class TaskView(APIView):
    permission_classes=[IsAuthenticated,]
    parser_classes=[JWTAuthentication,]
    def get(self,request):
        try:
            data=Task.objects.all().order_by('-id').filter(user=request.user)
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
            return Response({'message':'no task found for this user'})
        
class TaskAddView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        try:
            data = request.data.copy()
            serializer = TaskSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response({'status': True, 'message': 'New task added successfully', 'Task': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status': False, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:  
            return Response({'status': False, 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
class TaskDeleteView(APIView):
    def delete(self,request,id):
        try:
            data=Task.objects.get(id=id).delete()
            return Response({'status':True,'message':'task delete successfully'})
        except:
            return Response({'status':False,'message':'Task Not Delete Successfully'})
        
        
    
        
        
        
        
        

    
            
            
            
        
        
        
        
