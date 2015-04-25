from django.shortcuts import redirect

from django.contrib.auth import logout as logout_user


def logout(request):
    logout_user(request)
    return redirect("home")
