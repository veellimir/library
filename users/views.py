from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import User
from .forms import CustomUserReaderRegisterForm, CustomUserLibrarianRegisterForm


def user_login(request):
    page = "login"

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, f"Пользователь {username} не найден")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, f"Добро пожаловать {username} !")

            if user.role == "reader":
                return redirect("catalog")
            else:
                return redirect("users_read_books")

        messages.error(request, "Неверный пароль !")

    context = {
        "title": "Войти",
        "page": page,
    }
    return render(request, "users/auth_user.html", context)


def user_register(request, role):
    if role == "librarian":
        page = "register_librarian"

        form_class = CustomUserLibrarianRegisterForm
        success_message = "Аккаунт библиотекаря зарегистрирован!"
    elif role == "reader":
        page = "register_reader"

        form_class = CustomUserReaderRegisterForm
        success_message = "Аккаунт читателя зарегистрирован!"
    else:
        return redirect("catalog")

    form = form_class(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save()

            messages.success(request, success_message)
            login(request, user)
            if user.role == "reader":
                return redirect("catalog")
            else:
                return redirect("users_read_books")
        else:
            for error in form.errors.values():
                messages.error(request, error)

    context = {
        "title": "Регистрация",
        "page": page,
        "form": form,
    }
    return render(request, "users/auth_user.html", context)


def user_logout(request):
    logout(request)
    messages.info(request, "Вы вышли.")
    return redirect("login")