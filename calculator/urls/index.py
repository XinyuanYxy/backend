from django.urls import path, re_path
from calculator.views.login import signIn
from calculator.views.get_status import get_status
from calculator.views.logout import signOut
from calculator.views.register import register
from calculator.views.index import index

urlpatterns = [
    path("login/", signIn, name="calculator_login"),
    path("logout/", signOut, name="calculator_logout"),
    path("register/", register, name="calculator_register"),
    path("get_status/", get_status, name="calculator_get_status"),
    re_path(r".*", index, name="calculator_index")
]
