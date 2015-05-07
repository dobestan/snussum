from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from users.decorators import anonymous_required

from django.contrib import messages


@anonymous_required
def signup(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password2']
            user_form.save()

            user = authenticate(username=username, password=password)
            login(request, user)

            messages.add_message(request, messages.INFO,
                                 '입력하신 정보를 바탕으로 성공적으로 회원가입 되었습니다.',
                                 extra_tags="success")
            return redirect("users:verify-snu")

        messages.add_message(request, messages.INFO,
                             '입력하신 정보가 올바르지 않습니다. 다시 한번 확인 부탁드립니다. 감사합니다.',
                             extra_tags="danger")
        return render(request, "users/signup.html", {
            'form': user_form
        })

    return render(request, "users/signup.html", {
        'form': UserCreationForm
    })
