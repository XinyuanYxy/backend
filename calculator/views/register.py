from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User

def register(request):
    data = request.GET
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()
    password_confirm = data.get("password_confirm", "").strip()
    if not username or not password:
        return JsonResponse({
            "reuslt": "username or password cannot be empty"
        })
    if password != password_confirm:
        return JsonResponse({
            "result": "two passwords are not the same"
        })
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            "result": "user already exists"
        })
    user = User(username=username)
    user.set_password(password)
    user.save()
    login(request, user)
    return JsonResponse({
        "result": "success"
    })