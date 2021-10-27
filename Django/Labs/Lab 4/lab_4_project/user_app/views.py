from django.shortcuts import render

# Create your views here.
def users(request):
    context = {???}
    return render(request, "user_app/users.html", context)