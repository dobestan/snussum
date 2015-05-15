from django.contrib.auth.views import login as default_login_view
from django.views.generic.base import TemplateView

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user

from django.shortcuts import render, redirect

from django.contrib import messages

from django.utils.decorators import method_decorator
from users.decorators import anonymous_required


@anonymous_required
def login(request):
    return default_login_view(
        request, template_name="users/login.html"
    )


def logout(request):
    logout_user(request)
    messages.add_message(request, messages.INFO,
                         '안전하게 로그아웃 되었습니다. 많은 서비스 이용 부탁드립니다. 감사합니다.',
                         extra_tags="success")
    return redirect("home")


@anonymous_required
def signup(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password2']
            user_form.save()

            user = authenticate(username=username, password=password)
            login_user(request, user)

            messages.add_message(request, messages.INFO,
                                 '입력하신 정보를 바탕으로 성공적으로 회원가입 되었습니다.',
                                 extra_tags="success")
            return redirect("users:verify-snu")

        return render(request, "users/signup.html", {
            'form': user_form
        })

    return render(request, "users/signup.html", {
        'form': UserCreationForm
    })


class PasswordReset(TemplateView):
    template_name = "users/password_reset.html"

    @method_decorator(anonymous_required)
    def dispatch(self, *args, **kwargs):
        return super(PasswordReset, self).dispatch(*args, **kwargs)
