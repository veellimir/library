from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_USER = [
        ('librarian', 'Библиотекарь'),
        ('reader', 'Читатель'),
    ]

    role = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        choices=ROLE_USER,
    )

    employee_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Табельный номер"
    )

    first_name = models.CharField(max_length=150, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=150, blank=True, verbose_name="Фамилия")
    address = models.TextField(blank=True, verbose_name="Адрес проживания")

    def __str__(self):
        return self.username
