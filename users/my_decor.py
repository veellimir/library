from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def auth_and_role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            try:
                user_role = request.user.role
            except AttributeError:
                return redirect('login')

            if user_role == role:
                return view_func(request, *args, **kwargs)
            elif user_role == "librarian":
                return redirect('users_read_books')
            elif user_role == "reader":
                return redirect('catalog')

        return _wrapped_view
    return decorator
