from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="user_app_index"),
    path('users/', views.users, name="user_app_users"),
]
