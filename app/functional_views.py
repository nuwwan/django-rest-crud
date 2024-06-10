import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Author, Book

# Register Logger
logger = logging.getLogger(__name__)


@api_view(["GET"])
def get_hello(request):
    data = {"message": "Hello from Nuwan"}
    return Response(data=data, status=status.HTTP_200_OK)


"""
This endpoint creates author on database
@param name : string
@method POST
"""
@api_view(["POST"])
def create_author(request):
    body = request.data
    name = body.get("name")
    if name:
        try:
            author = Author(name=name)
            author.save()
            logger.info(f"Author for name={name} is saved successfully!")
            return Response({"message": "Success"}, status=status.HTTP_201_CREATED)
        except Exception as ex:
            logger.error("Error occured when saving the author!")
            logger.error(ex)
            return Response(
                {"message": "Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    else:
        logger.debug("Invalid input data!")
        return Response(
            {"message": "Wrong input data!"}, status=status.HTTP_400_BAD_REQUEST
        )


"""
This API endpoint adds book objects to a Author object that already on db.
@method POST
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
            logger.info(f"Books were added for the user={author_id} successfully!")
            return Response(data=data, status=status.HTTP_201_CREATED)

    except Author.DoesNotExist as ex:
        data = {"message": "Author does not exist"}
        logger.error("Author does not exist")
        logger.error(ex)
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        # return internal error
        data = {"message": "Internal server Error"}
        logger.error("Internal Server Error!")
        return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""
This API endpoint returns an author specefied by an id
@method POST
@params id : author id
@return author and books associated with the author id
"""
@api_view(["GET"])
def get_author(request, id):
    author_id = id

    # fetch the Author object
    try:
        author = Author.objects.get(pk=author_id)
        return_data = {
            "id": author.pk,
            "name": author.name,
            "books": [{"title": b.title, "id": b.pk} for b in author.books.all()],
        }
        data = {"message": "Author data fetched Successfully", "data": return_data}
        logger.info(f"AUthor for id={author_id} is fetched successfully.")
        return Response(data=data, status=status.HTTP_200_OK)
    except Author.DoesNotExist as ex:
        logger.error(f"Author for id={author_id} does not exist!")
        logger.error(ex)
        data = {"message": "Author does not exist!"}
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        data = {"message": "Internal Server Error"}
        logger.error("internal server error!")
        logger.error(ex)
        Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
