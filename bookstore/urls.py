from django.urls import path
from . import views

urlpatterns = [
    # /books/: Display a list of all books available in the bookstore.
    path('books/', views.book_list, name='book_list'),

    # /book/<int:book_id>/: Display details of a specific book identified by its ID.
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),

    # /book/<int:book_id>/update/: Allow users to update the details of a book.
    path('book/<int:book_id>/update/', views.book_update, name='book_update'),

    # /book/<int:book_id>/delete/: Allow users to delete a book from the database.
    path('book/<int:book_id>/delete/', views.book_delete, name='book_delete'),
]
