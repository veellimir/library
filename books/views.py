from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Book, ReadBookForUser


@login_required
def catalog_page(request):
    catalog_books = Book.objects.all()
    all_read_books = ReadBookForUser.objects.filter(user=request.user).values_list("book_id", flat=True)

    context = {
        "title": "Каталог книг",
        "catalog_books": catalog_books,
        "all_read_books": all_read_books
    }
    return render(request, "books/catalog.html", context)


@login_required
def my_books(request):
    my_book_read = ReadBookForUser.objects.filter(user=request.user)

    context = {
        "title": "Мои книги",
        "my_book_read": my_book_read
    }
    return render(request, "books/my_books.html", context)


@login_required
def add_book_for_read(request, book_id):
    current_page = request.META.get("HTTP_REFERER")

    book = Book.objects.get(id=book_id)
    read_books = ReadBookForUser.objects.filter(user=request.user, book=book)

    if not read_books.exists():
        ReadBookForUser.objects.create(user=request.user, book=book)
        return redirect(current_page)


@login_required
def return_book_catalog(request, book_id):
    current_page = request.META.get("HTTP_REFERER")

    read_book = ReadBookForUser.objects.get(id=book_id)
    read_book.delete()
    return redirect(current_page)

