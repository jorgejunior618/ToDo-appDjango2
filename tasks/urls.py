from django.urls import path

from . import views

urlpatterns = [
    path('', views.taskList, name='tasks-list'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('newtask/', views.newTask, name='new-task'),
    path('edittask/<int:id>', views.editTask, name='edit-task'),
    path('deletetask/<str:id>', views.deleteTask, name='delete-task'),
]
