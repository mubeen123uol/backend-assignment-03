from django.shortcuts import render
from django.http import HttpResponse

# View for displaying all blog posts
def post_list(request):
    print("Action: Displaying list of all blog posts")
    return HttpResponse("Displaying all blog posts")

# View for displaying blog posts of a specific year
def post_archive_year(request, year):
    print(f"Year retrieved: {year}")
    return HttpResponse(f"Displaying blog posts for year: {year}")

# View for displaying blog posts of a specific year and month
def post_archive_month(request, year, month):
    print(f"Year retrieved: {year}, Month retrieved: {month}")
    return HttpResponse(f"Displaying blog posts for year: {year}, month: {month}")

# View for displaying details of a specific blog post by slug
def post_detail_slug(request, slug):
    print(f"Slug retrieved: {slug}")
    return HttpResponse(f"Displaying details for blog post: {slug}")
