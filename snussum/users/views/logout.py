from django.shortcuts import redirect
from django.contrib.auth import logout as logout_user
from django.contrib import messages


def logout(request):
    logout_user(request)
    messages.add_message(request, messages.INFO,\
            '안전하게 로그아웃 되었습니다. 많은 서비스 이용 부탁드립니다. 감사합니다.',\
            extra_tags="success")
    return redirect("home")
