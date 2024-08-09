from django.urls import path

from . import views

urlpatterns = [
    path("", views.catalog_page, name="catalog"),
    path("my-books", views.my_books, name="my_books"),

    path("book-add/read/<int:book_id>/", views.add_book_for_read, name="add_book"),
    path("book-del/read/<int:book_id>/", views.return_book_catalog, name="del_book"),

]
