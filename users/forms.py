from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User
from .base_forms import BaseFormUsers


class CustomUserLibrarianRegisterForm(UserCreationForm, BaseFormUsers):
    role = forms.ChoiceField(
        choices=User.ROLE_USER,
        initial='librarian',
        widget=forms.HiddenInput(),
        label=" ",
    )

    employee_id = forms.CharField(
        required=False,
        label="Табельный номер"
    )

    class Meta:
        model = User
        fields = [
            "username",
            "employee_id",
            "password1",
            "password2",
        ]


class CustomUserReaderRegisterForm(UserCreationForm, BaseFormUsers):
    role = forms.ChoiceField(
        choices=User.ROLE_USER,
        initial='reader',
        widget=forms.HiddenInput(),
        label=" ",
    )
    address = forms.CharField(
        required=False,
        label="Адрес проживания"
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "address",
            "password1",
            "password2",
        ]

