from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from django.contrib import messages


def anonymous_required(function=None, redirect_field_name=None):
    def _dec(view_func):
        def _view(request, *arg, **kwargs):
            if request.user.is_authenticated():
                url = None
                if redirect_field_name \
                        and redirect_field_name in request.REQUEST:
                    url = request.REQUEST[redirect_field_name]
                if not url:
                    url = reverse("home")
                return redirect(url)
            else:
                return view_func(request, *arg, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)


def university_verified_required(function=None):
    def _dec(view_func):
        def _view(request, *arg, **kwargs):
            if request.user.userprofile.is_university_verified:
                return view_func(request, *arg, **kwargs)
            else:
                return redirect('users:verify-snu')

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)


def university_not_verified_required(function=None):
    def _dec(view_func):
        def _view(request, *arg, **kwargs):
            if not request.user.userprofile.is_university_verified:
                messages.add_message(request, messages.INFO,
                                     '서비스 이용을 위해서 서울대학교 인증이 필요합니다.\
                        현재 이메일 인증(마이스누), 로그인 인증(마이스누, 스누라이프)을 지원합니다.',
                                     extra_tags="danger")
                return view_func(request, *arg, **kwargs)
            else:
                messages.add_message(request, messages.INFO,
                                     '이미 대학교 인증이 완료되었습니다. ( %s )' % request.user.userprofile.university.full_name,
                                     extra_tags="success")
                return redirect('users:verify-profile')

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)


def profile_verifed_required(function=None):
    def _dec(view_func):
        def _view(request, *arg, **kwargs):
            if request.user.userprofile.is_profile_verified:
                return view_func(request, *arg, **kwargs)
            else:
                messages.add_message(request, messages.INFO,
                                     '서비스 이용을 위해서 기본정보 입력이 필요합니다.\
                        성실한 개인정보 입력은 상대방에 대한 예의입니다.',
                                     extra_tags="danger")
                return redirect('users:verify-profile')

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)
