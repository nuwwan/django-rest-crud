from django.db import models

"""
Author and Book has one to many relationship.
@relationship : Book --> one-to-many
"""
class Author(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

"""
Book and Author has many to one relationship.
@relationship: Book --> one-to-many
"""    
class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
