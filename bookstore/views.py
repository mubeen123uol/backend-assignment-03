from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book

# 1. Display list of all books available in bookstore
def book_list(request):
    books = Book.objects.all()
    if not books.exists():
        return HttpResponse("No books available in the bookstore.")
    
    response_text = "Books Available in Bookstore:\n"
    for book in books:
        response_text += f"- ID: {book.id}, Title: {book.title}, Author: {book.author}, Price: ${book.price}\n"
    return HttpResponse(response_text, content_type="text/plain")

# 2. Display details of a specific book by ID
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    response_text = f"Book Details:\nID: {book.id}\nTitle: {book.title}\nAuthor: {book.author}\nPrice: ${book.price}\nStock: {book.stock}\n"
    return HttpResponse(response_text, content_type="text/plain")

# 3. Allow users to update details of a book
def book_update(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        new_title = request.POST.get("title")
        new_author = request.POST.get("author")
        new_price = request.POST.get("price")
        
        if new_title:
            book.title = new_title
        if new_author:
            book.author = new_author
        if new_price:
            book.price = new_price
            
        book.save()
        return HttpResponse(f"Book with ID {book_id} updated successfully!\nNew Title: {book.title}\nNew Price: ${book.price}", content_type="text/plain")
        
    return HttpResponse(f"Update view for Book ID {book_id}: Ready to receive updates.", content_type="text/plain")

# 4. Allow users to delete a book from database
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    title = book.title
    book.delete()
    return HttpResponse(f"Book '{title}' with ID {book_id} has been deleted successfully from database.", content_type="text/plain")
