from django.contrib.auth.views import login as default_login_view
from users.decorators import anonymous_required
from django.contrib import messages


@anonymous_required
def login(request):
    messages.add_message(request, messages.INFO,\
            '안전하게 로그인 되었습니다. 서비스를 이용해주셔서 감사합니다.',\
            extra_tags="success")
    return default_login_view(
        request, template_name="users/login.html"
    )
