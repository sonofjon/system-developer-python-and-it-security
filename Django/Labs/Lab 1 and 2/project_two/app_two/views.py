from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "app_two/index.html")

def help(request):
    context = {"body": "Help Page"}
    return render(request, "app_two/help.html", context)