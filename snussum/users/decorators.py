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
                return view_func(request, *arg, **kwargs)
            else:
                messages.add_message(request, messages.SUCCESS,\
                        '이미 대학교 인증이 완료되었습니다.')
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
                return redirect('users:verify-profile')

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)
