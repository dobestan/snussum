from django.contrib.auth.views import login as default_login_view


def login(request):
    return default_login_view(
        request, template_name="users/login.html"
    )
