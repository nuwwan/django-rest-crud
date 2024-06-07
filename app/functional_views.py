from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def get_hello(request):
    data = {"message": "Hello from Nuwan"}
    return Response(data=data, status=status.HTTP_200_OK)
