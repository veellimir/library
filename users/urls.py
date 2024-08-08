from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path('register-librarian/', views.user_register, {'role': 'librarian'}, name='register_librarian'),
    path('register-reader/', views.user_register, {'role': 'reader'}, name='register_reader'),
    path("logout/", views.user_logout, name="logout"),

]
