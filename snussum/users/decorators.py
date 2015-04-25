from django.core.urlresolvers import reverse
from django.shortcuts import redirect


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
