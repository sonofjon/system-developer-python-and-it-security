from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="app_two_index"),
    path('help/', views.help, name="app_two_help"),
]