from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Author, Book


@api_view(["GET"])
def get_hello(request):
    data = {"message": "Hello from Nuwan"}
    return Response(data=data, status=status.HTTP_200_OK)


"""
This endpoint creates author on database
@param name : string
"""
@api_view(["POST"])
def create_author(request):
    body = request.data
    name = body.get("name")
    if name:
        try:
            author = Author(name=name)
            author.save()
            return Response({"message": "Success"}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response(
                {"message": "Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    else:
        return Response(
            {"message": "Wrong input data!"}, status=status.HTTP_400_BAD_REQUEST
        )


"""
This API endpoint adds book objects to a Author object that already on db.
@param author_id : author id of the author object that is going to be base object of the books.
@param books[] : books object 
sample request body = 
{
    'author_id':xxxx, 
    'books':[
        {'title':'book1'},
        {'title':'book1'},
        {'title':'book1'}
    ]
}
"""
@api_view(["POST"])
def add_books_to_author(request):
    body = request.data
    try:
        author_id = body.get("author_id")
        books = body.get("books", [])
        # get author object for the author id
        author = Author.objects.get(pk=author_id)

        # if author is presented, proceed
        if author and books:
            book_objs = [Book(title=b.get("title"), author=author) for b in books]
            Book.objects.bulk_create(book_objs)
            data = {"message": "Books saved successfully"}
            return Response(data=data, status=status.HTTP_201_CREATED)
        
    except Author.DoesNotExist:
        data = {"message": "Author does not exist"}
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        # return internal error
        data = {"message": "Internal server Error"}
        return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

