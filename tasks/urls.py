from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.board, name='board'),
    path('all/', views.all_tasks, name='all_tasks'),
    path('<int:pk>/edit/', views.edit_task, name='edit_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('<int:pk>/update-category/', views.update_category, name='update_category'),
]
