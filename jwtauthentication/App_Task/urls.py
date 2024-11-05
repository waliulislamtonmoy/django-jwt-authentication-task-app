
from django.urls import path,include

from App_Task.views import TaskView,TaskDetailView,TaskAddView,TaskUpdateView,TaskDeleteView

urlpatterns = [
    path('',TaskView.as_view(),name="taskview"),
    path('<int:id>/',TaskDetailView.as_view(),name="taskdetailview"),
    path('add/',TaskAddView.as_view(),name="taskaddview"),
    path('update/<int:id>/',TaskUpdateView.as_view(),name="taskupdateview"),
    path('delete/<int:id>/',TaskDeleteView.as_view(),name="taskdeleteview"),
]
