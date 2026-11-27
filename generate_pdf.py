import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Preformatted, PageBreak

def build_pdf():
    pdf_filename = "Assignment no.03 solved.pdf"
    # Margins: 36 left/right, 28 top/bottom
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=28,
        bottomMargin=28
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'StudentHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        alignment=1 # Center
    )

    repo_header_style = ParagraphStyle(
        'RepoHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13
    )

    repo_link_style = ParagraphStyle(
        'RepoLink',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor='#1122aa'
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        alignment=1 # Center
    )

    q_title_style = ParagraphStyle(
        'QuestionTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14
    )

    sub_title_style = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12
    )

    code_style_q1 = ParagraphStyle(
        'CodeStyleQ1',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=9.8
    )

    code_style_q2 = ParagraphStyle(
        'CodeStyleQ2',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.0,
        leading=8.3
    )

    code_style_q3 = ParagraphStyle(
        'CodeStyleQ3',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.2,
        leading=8.6
    )

    output_style = ParagraphStyle(
        'OutputStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.0,
        leading=8.3
    )

    story = []

    # ================= PAGE 1 =================
    # Student Header
    story.append(Paragraph("Name: Muhammad Mubeen", title_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("SAPID: 70150831", title_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("Assignment No. 03", title_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("Course: Advanced Back-End Development (CS02338|11)", title_style))
    story.append(Spacer(1, 8))

    story.append(HRFlowable(width="100%", thickness=1.5, color="black", spaceAfter=8))

    # Git Repo Link
    story.append(Paragraph("GIT REPO LINK:", repo_header_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("https://github.com/mubeen123uol/ABD-Assignment_No.03", repo_link_style))
    story.append(Spacer(1, 8))

    story.append(HRFlowable(width="100%", thickness=1.5, color="black", spaceAfter=10))

    story.append(Paragraph("CODES", section_heading))
    story.append(Spacer(1, 8))

    # QUESTION 01
    story.append(Paragraph("Question No.01:", q_title_style))
    story.append(Spacer(1, 4))

    # blog/urls.py
    story.append(Paragraph("blog/urls.py:", sub_title_style))
    story.append(Spacer(1, 2))
    blog_urls_code = """from django.urls import path
from . import views

urlpatterns = [
    # /blog/ : Display list of all blog posts
    path('', views.post_list, name='post_list'),

    # /blog/<int:year>/ : Display list of posts in specific year
    path('<int:year>/', views.post_archive_year, name='post_archive_year'),

    # /blog/<int:year>/<int:month>/ : Display list of posts in year and month
    path('<int:year>/<int:month>/', views.post_archive_month, name='post_archive_month'),

    # /blog/<slug:slug>/ : Display details of specific post by slug
    path('<slug:slug>/', views.post_detail_slug, name='post_detail_slug'),
]"""
    story.append(Preformatted(blog_urls_code, code_style_q1))
    story.append(Spacer(1, 8))

    # blog/views.py
    story.append(Paragraph("blog/views.py:", sub_title_style))
    story.append(Spacer(1, 2))
    blog_views_code = """from django.shortcuts import render
from django.http import HttpResponse

# Display list of all blog posts
def post_list(request):
    print("Action: Displaying list of all blog posts")
    return HttpResponse("Displaying all blog posts")

# Display blog posts published in a specific year
def post_archive_year(request, year):
    print(f"Year retrieved: {year}")
    return HttpResponse(f"Displaying blog posts for year: {year}")

# Display blog posts published in a specific year and month
def post_archive_month(request, year, month):
    print(f"Year retrieved: {year}, Month retrieved: {month}")
    return HttpResponse(f"Displaying blog posts for year: {year}, month: {month}")

# Display details of a specific blog post by slug
def post_detail_slug(request, slug):
    print(f"Slug retrieved: {slug}")
    return HttpResponse(f"Displaying details for blog post: {slug}")"""
    story.append(Preformatted(blog_views_code, code_style_q1))

    # Page Break -> Page 2
    story.append(PageBreak())

    # ================= PAGE 2 =================
    story.append(Paragraph("Question No.02:", q_title_style))
    story.append(Spacer(1, 4))

    # bookstore/models.py
    story.append(Paragraph("bookstore/models.py:", sub_title_style))
    story.append(Spacer(1, 2))
    book_model_code = """from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}\""""
    story.append(Preformatted(book_model_code, code_style_q2))
    story.append(Spacer(1, 6))

    # bookstore/urls.py
    story.append(Paragraph("bookstore/urls.py:", sub_title_style))
    story.append(Spacer(1, 2))
    bookstore_urls_code = """from django.urls import path
from . import views

urlpatterns = [
    # /books/ : Display list of all books
    path('books/', views.book_list, name='book_list'),

    # /book/<int:book_id>/ : Display details of a specific book by ID
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),

    # /book/<int:book_id>/update/ : Update details of a book
    path('book/<int:book_id>/update/', views.book_update, name='book_update'),

    # /book/<int:book_id>/delete/ : Delete a book from database
    path('book/<int:book_id>/delete/', views.book_delete, name='book_delete'),
]"""
    story.append(Preformatted(bookstore_urls_code, code_style_q2))
    story.append(Spacer(1, 6))

    # bookstore/views.py
    story.append(Paragraph("bookstore/views.py:", sub_title_style))
    story.append(Spacer(1, 2))
    bookstore_views_code = """from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book

# 1. Display list of all books available in bookstore
def book_list(request):
    books = Book.objects.all()
    if not books.exists():
        return HttpResponse("No books available in the bookstore.")
    output = "Books Available in Bookstore:\\n" + "\\n".join(
        [f"- ID: {b.id}, Title: {b.title}, Author: {b.author}, Price: ${b.price}" for b in books]
    )
    return HttpResponse(output)

# 2. Display details of a specific book identified by its ID
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    output = (
        f"Book Details:\\n"
        f"ID: {book.id}\\n"
        f"Title: {book.title}\\n"
        f"Author: {book.author}\\n"
        f"Price: ${book.price}\\n"
        f"Stock: {book.stock}"
    )
    return HttpResponse(output)

# 3. Allow users to update details of a book
def book_update(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title", book.title)
        book.author = request.POST.get("author", book.author)
        price_val = request.POST.get("price")
        if price_val:
            book.price = price_val
        book.save()
        return HttpResponse(
            f"Book with ID {book_id} updated successfully!\\n"
            f"New Title: {book.title}\\n"
            f"New Price: ${book.price}"
        )
    return HttpResponse(f"Update page for Book ID {book_id}: '{book.title}'")

# 4. Allow users to delete a book from the database
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    title = book.title
    book.delete()
    return HttpResponse(f"Book '{title}' with ID {book_id} has been deleted successfully from database.")"""
    story.append(Preformatted(bookstore_views_code, code_style_q2))

    # Page Break -> Page 3
    story.append(PageBreak())

    # ================= PAGE 3 =================
    story.append(Paragraph("Project Configuration & Execution Runner", q_title_style))
    story.append(Spacer(1, 4))

    story.append(Paragraph("myproject/urls.py (Project Root URLs):", sub_title_style))
    story.append(Spacer(1, 2))
    root_urls_code = """from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Question 1: Blog URL routing (/blog/...)
    path('blog/', include('blog.urls')),
    # Question 2: Bookstore URL routing (/books/, /book/...)
    path('', include('bookstore.urls')),
]"""
    story.append(Preformatted(root_urls_code, code_style_q3))
    story.append(Spacer(1, 5))

    story.append(Paragraph("Main.py:", sub_title_style))
    story.append(Spacer(1, 2))
    main_code = """import question_01
import question_02

def main():
    print("#" * 70)
    print(" THE UNIVERSITY OF LAHORE - DEPARTMENT OF TECHNOLOGY")
    print(" COURSE: ADVANCED BACK-END DEVELOPMENT (CS02338|11)")
    print(" ASSIGNMENT # 03 - FULL EXECUTION RUNNER")
    print("#" * 70)
    print("\\n")

    # Run Question 1
    question_01.main()
    print("\\n")

    # Run Question 2
    question_02.main()
    print("\\n")

    print("#" * 70)
    print(" ALL ASSIGNMENT QUESTIONS EXECUTED SUCCESSFULLY")
    print("#" * 70)

if __name__ == "__main__":
    main()"""
    story.append(Preformatted(main_code, code_style_q3))
    story.append(Spacer(1, 5))

    # Execution Output
    story.append(Paragraph("Execution Output:", sub_title_style))
    story.append(Spacer(1, 2))
    output_text = """=================================================================
           ASSIGNMENT 03 - QUESTION # 01 SOLUTION           
=================================================================
--> Testing URL: /blog/
Action: Displaying list of all blog posts
    Status Code: 200 | Response: Displaying all blog posts
--> Testing URL: /blog/2026/
Year retrieved: 2026
    Status Code: 200 | Response: Displaying blog posts for year: 2026
--> Testing URL: /blog/2026/11/
Year retrieved: 2026, Month retrieved: 11
    Status Code: 200 | Response: Displaying blog posts for year: 2026, month: 11
--> Testing URL: /blog/getting-started-with-django/
Slug retrieved: getting-started-with-django
    Status Code: 200 | Response: Displaying details for blog post: getting-started-with-django
=================================================================
           ASSIGNMENT 03 - QUESTION # 02 SOLUTION           
=================================================================
--> 1. Testing URL: /books/ (Display all books)
    Status Code: 200 | Response: Books Available in Bookstore: 3 books listed
--> 2. Testing URL: /book/1/ (Display book details)
    Status Code: 200 | Response: Book Details for ID 1: 'Django 5 for Beginners'
--> 3. Testing URL: /book/1/update/ (Update book details)
    Status Code: 200 | Response: Book with ID 1 updated successfully!
--> 4. Testing URL: /book/4/delete/ (Delete book from database)
    Status Code: 200 | Response: Book 'Temporary Test Book' deleted successfully.
######################################################################
 ALL ASSIGNMENT QUESTIONS EXECUTED SUCCESSFULLY
######################################################################"""
    story.append(Preformatted(output_text, output_style))

    # Build document
    doc.build(story)
    print("PDF build complete!")

if __name__ == '__main__':
    build_pdf()
