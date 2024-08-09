from django.contrib import admin

from books.models import Book, GenreBook, ReadBookForUser


admin.site.register(Book)
admin.site.register(GenreBook)
admin.site.register(ReadBookForUser)