from rest_framework.urls import path

from .functional_views import get_hello, create_author, add_books_to_author, get_author

urlpatterns = [
    path("hello/", get_hello, name="get_hello"),
    path("create_author/", create_author, name="create_author"),
    path("add_books_to_author", add_books_to_author, name="add_books_to_author"),
    path("get_author/<int:id>/", get_author, name="get_author"),
]
