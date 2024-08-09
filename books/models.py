from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from .mixins import StrMixin
from users.models import User


class Book(StrMixin, models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name="Название книги")
    author = models.CharField(max_length=50, blank=False, null=False, verbose_name="Автор книги")
    picture = models.ImageField(blank=False, null=False, verbose_name="Обложка книги")
    file_book = models.FileField(upload_to="books/", blank=False, null=False, verbose_name="Файл книги")
    date_of_receipt = models.DateTimeField(verbose_name="Дата получения книги")

    genre = models.ForeignKey(
        "GenreBook",
        on_delete=models.CASCADE,
        related_name="books",
        verbose_name="Жанр"
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["-date_of_receipt"]

    def clean_pdf(self):
        super().clean()
        if self.file_book and not self.file_book.name.lower().endswith('.pdf'):
            raise ValidationError(_("Только PDF-файлы разрешены."))


class GenreBook(StrMixin, models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Жанр")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class ReadBookForUser(StrMixin, models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name="Книга"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Книгу для чтения"
        verbose_name_plural = "Книги которые читают"

