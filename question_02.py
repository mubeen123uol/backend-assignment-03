import os
import django

# Configure Django settings environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.test import Client
from bookstore.models import Book

def main():
    print("=" * 65)
    print("           ASSIGNMENT 03 - QUESTION # 02 SOLUTION           ")
    print("=" * 65)
    print("Task: Bookstore Management URL Patterns and Views\n")

    client = Client()

    # Pre-populate sample books if table is empty
    if Book.objects.count() == 0:
        b1 = Book.objects.create(title="Django 5 for Beginners", author="William S. Vincent", price=29.99, stock=10)
        b2 = Book.objects.create(title="Two Scoops of Django", author="Daniel Roy Greenfeld", price=39.99, stock=5)
        b3 = Book.objects.create(title="Fluent Python", author="Luciano Ramalho", price=45.00, stock=8)
        print("Pre-populated sample books into database.\n")

    first_book = Book.objects.first()

    # 1. Test /books/
    print("--> 1. Testing URL: /books/ (Display all books)")
    response = client.get('/books/')
    print(f"    Status Code: {response.status_code}")
    print(f"    Response Content:\n{response.content.decode()}")
    print("-" * 65)

    # 2. Test /book/<int:book_id>/
    print(f"--> 2. Testing URL: /book/{first_book.id}/ (Display book details)")
    response = client.get(f'/book/{first_book.id}/')
    print(f"    Status Code: {response.status_code}")
    print(f"    Response Content:\n{response.content.decode()}")
    print("-" * 65)

    # 3. Test /book/<int:book_id>/update/
    print(f"--> 3. Testing URL: /book/{first_book.id}/update/ (Update book details)")
    update_data = {
        'title': 'Django 5 for Beginners (Updated 2nd Edition)',
        'author': 'William S. Vincent',
        'price': 34.99
    }
    response = client.post(f'/book/{first_book.id}/update/', data=update_data)
    print(f"    Status Code: {response.status_code}")
    print(f"    Response Content: {response.content.decode()}")
    print("-" * 65)

    # 4. Test /book/<int:book_id>/delete/
    # Create a temporary book to demonstrate delete safely
    temp_book = Book.objects.create(title="Temporary Test Book", author="Test Author", price=9.99, stock=1)
    print(f"--> 4. Testing URL: /book/{temp_book.id}/delete/ (Delete book from database)")
    response = client.get(f'/book/{temp_book.id}/delete/')
    print(f"    Status Code: {response.status_code}")
    print(f"    Response Content: {response.content.decode()}")
    print("=" * 65 + "\n")

if __name__ == '__main__':
    main()
