from django.db import models

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=150,unique=True)
    author_name=models.CharField(max_length=120)
    book_price=models.IntegerField()
    book_pages=models.IntegerField()
    category=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.book_name


# python manage.py makemigrations
# book>python manage.py migrate
# book>python manage.py shell

# from books.models import Book

# ORM QURIEs
#to add book detais
# book=Book(book_name="My journey",author_name="APJ Abdul Kalam",book_price=250,book_pages=250)

# to save the details
#book.save

#to print all book name
#books=Book.objects.all()
#books
# to print 1st book details
#book=Book.objects.get(id=1)
#print(book.book_name)
#print(book.book_price)
# books=Book.objects.all()

#for taking all books
#for book in books:
    # print(book.book_name)
    # print(book.book_price)

#to update the values
# book.book_price=170
# book.save()
# book.book_price

