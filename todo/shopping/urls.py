from django.urls import path
from . import views

urlpatterns = [
    path("update/<int:pk>/", views.update_shop, name="update_shop"),
    path("delete/<int:pk>/", views.delete_shop, name="delete_shop"),
]