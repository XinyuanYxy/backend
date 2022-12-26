from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def signIn(request):
    data = request.GET
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({
            "result": "Wrong password or username may not exist"
        })
    login(request, user)
    return JsonResponse({
        "result": "success"
    })

    
    


