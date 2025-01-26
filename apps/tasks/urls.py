from django.urls import path

from apps.tasks import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list'),
    path('<int:id>/', views.TaskDetailView.as_view(), name='task-detail'),
]