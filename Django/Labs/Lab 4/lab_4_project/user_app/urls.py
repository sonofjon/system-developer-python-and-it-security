from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="user_app_index"),
    path('user/', views.user, name="user_app_user"),
]
