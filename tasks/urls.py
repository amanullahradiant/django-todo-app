from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="list"),
    path("createPost", views.createPost, name="create_task"),
    path("update_task/<str:pk>/", views.updateTask, name="update_task"),
    path("delete_task/<str:pk>/", views.deleteTask, name="delete_task"),
]
