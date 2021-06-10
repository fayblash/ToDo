from django.urls import path
from . import views

urlpatterns = [
    path("update/<int:pk>/", views.update_goal, name="update_goal"),
    path("delete/<int:pk>/", views.delete_goal, name="delete_goal"),
]