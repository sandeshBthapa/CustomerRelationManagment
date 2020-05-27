from django.shortcuts import redirect
from django.http import HttpResponse


def orginal_function(view_fun):
    def wrapper_fun(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homePage')
        else:
            return view_fun(request, *args, **kwargs)

    return wrapper_fun


def allowed_user(allowed_roles=()):
    def decorator(view_fun):
        def wrapper_fun(request, *args, **kwargs):
            group = ''
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_fun(request, *args, **kwargs)
            else:
                return redirect('user_page')

        return wrapper_fun

    return decorator


