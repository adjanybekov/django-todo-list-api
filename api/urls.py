from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path(r'', views.index,name='index'),
    path(r'task-list/', views.taskList,name='task-list'),
    path(r'task-detail/<str:pk>/', views.taskDetail,name='task-detail'),
    path(r'task-create/', views.taskCreate,name='task-create'),
    path(r'task-update/<str:pk>/', views.taskUpdate,name='task-update'),
    path(r'task-delete/<str:pk>/', views.taskDelete,name='task-delete'),
]
