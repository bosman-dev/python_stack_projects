from django.urls import path
from . import views

app_name = 'todo_app1'

urlpatterns = [
	path('', views.index, name="task_list"),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete_task/<str:pk>/', views.deleteTask, name="delete_task"),
]