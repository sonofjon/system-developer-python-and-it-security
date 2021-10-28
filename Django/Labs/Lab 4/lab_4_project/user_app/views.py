from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    return render(request, "user_app/index.html")

def users(request):
    context = {"users": User.objects.all()}
    return render(request, "user_app/users.html", context)