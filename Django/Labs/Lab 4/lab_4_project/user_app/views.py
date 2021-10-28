from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "user_app/index.html")

def users(request):
    context = {???}
    return render(request, "user_app/users.html", context)