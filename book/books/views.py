from django.shortcuts import render
from .forms import BookForm
from .models import Book

# Create your views here.
def get_book(request):
    context={}
    form=BookForm()
    context['form']=form
    if request.method=="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            Book_Name = form.cleaned_data.get('Book_Name')
            Author_Name = form.cleaned_data.get('Author_Name')
            Book_Price = form.cleaned_data.get('Book_Price')
            Pages = form.cleaned_data.get('Pages')
            Category = form.cleaned_data.get('Category')
            # print(Book_Name,Author_Name,Book_Price,Number_of_Pages,Category)
            books=Book(book_name=Book_Name,author_name=Author_Name,book_price=Book_Price,book_pages=Pages,category=Category)
            books.save()
            print('saved')
            return render(request, 'books/book.html',context)


        else:
            form = BookForm(request.POST)
            context['form'] = form
            return render(request, 'books/book.html', context)

    return render(request,'books/book.html',context)