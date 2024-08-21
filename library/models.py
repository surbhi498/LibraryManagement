from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    date_of_birth = models.DateField()

# just instead of printing address of an object print useful information here    
    def __str__(self) -> str:
        return f"{self.first_name}{self.last_name}"
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publication_date = models.DateField()
    description = models.TextField()
    isbn = models.CharField(max_length=100, unique=True)
    

    def __str__(self):
        return self.title