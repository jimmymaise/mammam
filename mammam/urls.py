from django.urls import path
from mammam import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
]