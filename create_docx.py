import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def add_horizontal_line(doc):
    p = doc.add_paragraph()
    p_border = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '12')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), '000000')
    p_border.append(bottom)
    p._p.get_or_add_pPr().append(p_border)

def generate_assignment_docx():
    doc = docx.Document()

    # Set margins
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Base style
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)

    # Title / Student Info (Centered, Bold)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Name: Muhammad Mubeen\nSAPID: 70150831\nAssignment No. 03\n")
    run.bold = True
    run.font.size = Pt(14)

    course_run = p.add_run("Course: Advanced Back-End Development (CS02338|11)\nInstructor: Tahir Ilyas")
    course_run.font.size = Pt(11)

    add_horizontal_line(doc)

    # Git Repo Link
    p_git = doc.add_paragraph()
    p_git.paragraph_format.space_before = Pt(6)
    p_git.paragraph_format.space_after = Pt(4)
    run_git_label = p_git.add_run("GIT REPO LINK:\n")
    run_git_label.bold = True
    run_git_url = p_git.add_run("https://github.com/mubeen123uol/backend-assignment-03")
    run_git_url.font.color.rgb = RGBColor(0, 51, 153)
    run_git_url.underline = True

    add_horizontal_line(doc)

    # Header: CODES
    p_codes = doc.add_paragraph()
    p_codes.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_codes.paragraph_format.space_before = Pt(12)
    p_codes.paragraph_format.space_after = Pt(12)
    run_codes = p_codes.add_run("CODES & OUTPUTS")
    run_codes.bold = True
    run_codes.font.size = Pt(13)

    # ================= QUESTION NO 01 =================
    p_q1 = doc.add_paragraph()
    p_q1.paragraph_format.space_before = Pt(10)
    p_q1.paragraph_format.space_after = Pt(4)
    r_q1 = p_q1.add_run("Question No.01:\n")
    r_q1.bold = True
    r_q1.font.size = Pt(12)

    p_q1_desc = doc.add_paragraph()
    p_q1_desc.paragraph_format.space_after = Pt(6)
    p_q1_desc.add_run("Blog routing using advanced URL patterns and views in Django.")

    # 1. blog/urls.py
    p_b_urls_title = doc.add_paragraph()
    p_b_urls_title.paragraph_format.space_before = Pt(6)
    p_b_urls_title.paragraph_format.space_after = Pt(2)
    r = p_b_urls_title.add_run("blog/urls.py:")
    r.bold = True

    p_b_urls_code = doc.add_paragraph()
    p_b_urls_code.paragraph_format.space_after = Pt(8)
    p_b_urls_code.paragraph_format.left_indent = Inches(0.2)
    r_code = p_b_urls_code.add_run(
"""from django.urls import path
from . import views

urlpatterns = [
    # /blog/: Display list of all blog posts
    path('', views.post_list, name='post_list'),

    # /blog/<int:year>/: Display list of blog posts in specific year
    path('<int:year>/', views.post_archive_year, name='post_archive_year'),

    # /blog/<int:year>/<int:month>/: Display list of blog posts in specific year and month
    path('<int:year>/<int:month>/', views.post_archive_month, name='post_archive_month'),

    # /blog/<slug:slug>/: Display details of specific blog post identified by its slug
    path('<slug:slug>/', views.post_detail_slug, name='post_detail_slug'),
]"""
    )
    r_code.font.name = 'Consolas'
    r_code.font.size = Pt(9.5)

    # 2. blog/views.py
    p_b_views_title = doc.add_paragraph()
    p_b_views_title.paragraph_format.space_before = Pt(6)
    p_b_views_title.paragraph_format.space_after = Pt(2)
    r = p_b_views_title.add_run("blog/views.py:")
    r.bold = True

    p_b_views_code = doc.add_paragraph()
    p_b_views_code.paragraph_format.space_after = Pt(8)
    p_b_views_code.paragraph_format.left_indent = Inches(0.2)
    r_code = p_b_views_code.add_run(
"""from django.shortcuts import render
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
    )
    r_code.font.name = 'Consolas'
    r_code.font.size = Pt(9.5)

    # Execution / Output for Question 1
    p_q1_out_title = doc.add_paragraph()
    p_q1_out_title.paragraph_format.space_before = Pt(6)
    p_q1_out_title.paragraph_format.space_after = Pt(2)
    r = p_q1_out_title.add_run("Question 01 Execution Output:")
    r.bold = True

    p_q1_out_code = doc.add_paragraph()
    p_q1_out_code.paragraph_format.space_after = Pt(14)
    p_q1_out_code.paragraph_format.left_indent = Inches(0.2)
    r_code = p_q1_out_code.add_run(
"""--> Testing URL: /blog/
Action: Displaying list of all blog posts
    Status Code: 200
    Response Content: Displaying all blog posts

--> Testing URL: /blog/2026/
Year retrieved: 2026
    Status Code: 200
    Response Content: Displaying blog posts for year: 2026

--> Testing URL: /blog/2026/11/
Year retrieved: 2026, Month retrieved: 11
    Status Code: 200
    Response Content: Displaying blog posts for year: 2026, month: 11

--> Testing URL: /blog/getting-started-with-django/
Slug retrieved: getting-started-with-django
    Status Code: 200
    Response Content: Displaying details for blog post: getting-started-with-django"""
    )
    r_code.font.name = 'Consolas'
    r_code.font.size = Pt(9)

    add_horizontal_line(doc)

    # ================= QUESTION NO 02 =================
    p_q2 = doc.add_paragraph()
    p_q2.paragraph_format.space_before = Pt(10)
    p_q2.paragraph_format.space_after = Pt(4)
    r_q2 = p_q2.add_run("Question No.02:\n")
    r_q2.bold = True
    r_q2.font.size = Pt(12)

    p_q2_desc = doc.add_paragraph()
    p_q2_desc.paragraph_format.space_after = Pt(6)
    p_q2_desc.add_run("Django web application for managing a bookstore (CRUD URL patterns and views).")

    # 1. bookstore/models.py
    p_bs_model_title = doc.add_paragraph()
    p_bs_model_title.paragraph_format.space_before = Pt(6)
    p_bs_model_title.paragraph_format.space_after = Pt(2)
    r = p_bs_model_title.add_run("bookstore/models.py:")
    r.bold = True

    p_bs_model_code = doc.add_paragraph()
    p_bs_model_code.paragraph_format.space_after = Pt(8)
    p_bs_model_code.paragraph_format.left_indent = Inches(0.2)
    r_code = p_bs_model_code.add_run(
"""from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}\""""
    )
    r_code.font.name = 'Consolas'
    r_code.font.size = Pt(9.5)

    # 2. bookstore/urls.py
    p_bs_urls_title = doc.add_paragraph()
    p_bs_urls_title.paragraph_format.space_before = Pt(6)
    p_bs_urls_title.paragraph_format.space_after = Pt(2)
    r = p_bs_urls_title.add_run("bookstore/urls.py:")
    r.bold = True

    p_bs_urls_code = doc.add_paragraph()
    p_bs_urls_code.paragraph_format.space_after = Pt(8)
    p_bs_urls_code.paragraph_format.left_indent = Inches(0.2)
    r_code = p_bs_urls_code.add_run(
"""from django.urls import path
from . import views

urlpatterns = [
    # /books/ : Display a list of all books
    path('books/', views.book_list, name='book_list'),

    # /book/<int:book_id>/ : Display details of a specific book by ID
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),

    # /book/<int:book_id>/update/ : Update details of a book
    path('book/<int:book_id>/update/', views.book_update, name='book_update'),

    # /book/<int:book_id>/delete/ : Delete a book from database
    path('book/<int:book_id>/delete/', views.book_delete, name='book_delete'),
]"""
    )
    r_code.font.name = 'Consolas'
    r_code.font.size = Pt(9.5)

    # 3. bookstore/views.py
    p_bs_views_title = doc.add_paragraph()
    p_bs_views_title.paragraph_format.space_before = Pt(6)
    p_bs_views_title.paragraph_format.space_after = Pt(2)
    r = p_bs_views_title.add_run("bookstore/views.py:")
    r.bold = True

    p_bs_views_code = doc.add_paragraph()
    p_bs_views_code.paragraph_format.space_after = Pt(8)
    p_bs_views_code.paragraph_format.left_indent = Inches(0.2)
    r_code = p_bs_views_code.add_run(
"""from django.shortcuts import render, get_object_or_404
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

# 3. Allow users to update the details of a book
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
    )
    r_code.font.name = 'Consolas'
    r_code.font.size = Pt(9.5)

    # Execution / Output for Question 2
    p_q2_out_title = doc.add_paragraph()
    p_q2_out_title.paragraph_format.space_before = Pt(6)
    p_q2_out_title.paragraph_format.space_after = Pt(2)
    r = p_q2_out_title.add_run("Question 02 Execution Output:")
    r.bold = True

    p_q2_out_code = doc.add_paragraph()
    p_q2_out_code.paragraph_format.space_after = Pt(14)
    p_q2_out_code.paragraph_format.left_indent = Inches(0.2)
    r_code = p_q2_out_code.add_run(
"""--> 1. Testing URL: /books/ (Display all books)
    Status Code: 200
    Response Content:
Books Available in Bookstore:
- ID: 1, Title: Django 5 for Beginners, Author: William S. Vincent, Price: $34.99
- ID: 2, Title: Two Scoops of Django, Author: Daniel Roy Greenfeld, Price: $39.99
- ID: 3, Title: Fluent Python, Author: Luciano Ramalho, Price: $45.00

--> 2. Testing URL: /book/1/ (Display book details)
    Status Code: 200
    Response Content:
Book Details:
ID: 1
Title: Django 5 for Beginners
Author: William S. Vincent
Price: $34.99
Stock: 10

--> 3. Testing URL: /book/1/update/ (Update book details)
    Status Code: 200
    Response Content: Book with ID 1 updated successfully!
New Title: Django 5 for Beginners (Updated 2nd Edition)
New Price: $34.99

--> 4. Testing URL: /book/6/delete/ (Delete book from database)
    Status Code: 200
    Response Content: Book 'Temporary Test Book' with ID 6 has been deleted successfully from database."""
    )
    r_code.font.name = 'Consolas'
    r_code.font.size = Pt(9)

    add_horizontal_line(doc)

    # Project Root URLs and Main Runner
    p_main_title = doc.add_paragraph()
    p_main_title.paragraph_format.space_before = Pt(10)
    p_main_title.paragraph_format.space_after = Pt(4)
    r_main = p_main_title.add_run("Main.py & Root URLs Configuration:\n")
    r_main.bold = True
    r_main.font.size = Pt(12)

    p_r_urls_title = doc.add_paragraph()
    p_r_urls_title.paragraph_format.space_before = Pt(6)
    p_r_urls_title.paragraph_format.space_after = Pt(2)
    r = p_r_urls_title.add_run("myproject/urls.py:")
    r.bold = True

    p_r_urls_code = doc.add_paragraph()
    p_r_urls_code.paragraph_format.space_after = Pt(8)
    p_r_urls_code.paragraph_format.left_indent = Inches(0.2)
    r_code = p_r_urls_code.add_run(
"""from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Question 1: Blog URL routing (/blog/...)
    path('blog/', include('blog.urls')),
    # Question 2: Bookstore URL routing (/books/, /book/...)
    path('', include('bookstore.urls')),
]"""
    )
    r_code.font.name = 'Consolas'
    r_code.font.size = Pt(9.5)

    p_m_code_title = doc.add_paragraph()
    p_m_code_title.paragraph_format.space_before = Pt(6)
    p_m_code_title.paragraph_format.space_after = Pt(2)
    r = p_m_code_title.add_run("main.py:")
    r.bold = True

    p_m_code = doc.add_paragraph()
    p_m_code.paragraph_format.space_after = Pt(14)
    p_m_code.paragraph_format.left_indent = Inches(0.2)
    r_code = p_m_code.add_run(
"""import question_01
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
    )
    r_code.font.name = 'Consolas'
    r_code.font.size = Pt(9.5)

    # Core properties
    core_properties = doc.core_properties
    core_properties.author = "SYCO GAMER"
    core_properties.title = "Assignment No. 03 - Advanced Back-End Development"

    output_path = "Assignment no.03 solved.docx"
    doc.save(output_path)
    print(f"Generated {output_path} successfully!")

if __name__ == "__main__":
    generate_assignment_docx()
