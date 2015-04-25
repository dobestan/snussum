from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


def signup(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            username = user_form.clean_username()
            password = user_form.clean_password2()
            user_form.save()

            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect("home")

        return render(request, "users/signup.html", {
            'form': user_form
        })

    return render(request, "users/signup.html", {
        'form': UserCreationForm
    })
