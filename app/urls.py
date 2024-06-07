from rest_framework.urls import path

from .functional_views import get_hello

urlpatterns = [path("hello/", get_hello, name="get_hello")]
