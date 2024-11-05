from django.contrib import admin
from App_Task.models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display=['title','user','date']
    ordering=['-id']

admin.site.register(Task,TaskAdmin)