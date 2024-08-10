from django.contrib import admin
from django.contrib.auth.models import Group

from books.models import Book, GenreBook, ReadBookForUser
from mainapp.utils import html_image
from users.models import User


class ReaderForUserAdmin(admin.ModelAdmin):
    # TODO : параметры читателей для админа

    list_display = ("book", "html_img", "user", "created_at", )
    list_filter = ("user", "created_at", )
    ordering = ('-created_at', )

    def html_img(self, obj):
        return html_image(obj.book.picture)

    html_img.short_description = "Миниатюра"


class BooksAdmin(admin.ModelAdmin):
    # TODO : параметры книг для админа

    list_display = ("title", "author", "html_img", )

    def html_img(self, obj):
        return html_image(obj.picture)

    html_img.short_description = "Миниатюра"


admin.site.register(User)
admin.site.register(GenreBook)
admin.site.register(Book, BooksAdmin)
admin.site.register(ReadBookForUser, ReaderForUserAdmin)

admin.site.unregister(Group)

admin.site.site_header = "Администрирование Онлайн Библиотеки"
