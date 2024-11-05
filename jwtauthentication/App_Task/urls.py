
from django.urls import path,include

from App_Task.views import TaskView

urlpatterns = [
    path('',TaskView.as_view(),name="taskview")
]
