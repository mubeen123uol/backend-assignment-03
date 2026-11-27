import os
import django

# Configure Django settings environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.test import Client

def main():
    print("=" * 65)
    print("           ASSIGNMENT 03 - QUESTION # 01 SOLUTION           ")
    print("=" * 65)
    print("Task: Blog Routing with Advanced URL Patterns and Views\n")

    client = Client()

    # 1. Test /blog/
    print("--> Testing URL: /blog/")
    response = client.get('/blog/')
    print(f"    Status Code: {response.status_code}")
    print(f"    Response Content: {response.content.decode()}")
    print("-" * 65)

    # 2. Test /blog/<int:year>/
    year = 2026
    print(f"--> Testing URL: /blog/{year}/")
    response = client.get(f'/blog/{year}/')
    print(f"    Status Code: {response.status_code}")
    print(f"    Response Content: {response.content.decode()}")
    print("-" * 65)

    # 3. Test /blog/<int:year>/<int:month>/
    month = 11
    print(f"--> Testing URL: /blog/{year}/{month}/")
    response = client.get(f'/blog/{year}/{month}/')
    print(f"    Status Code: {response.status_code}")
    print(f"    Response Content: {response.content.decode()}")
    print("-" * 65)

    # 4. Test /blog/<slug:slug>/
    slug = "getting-started-with-django"
    print(f"--> Testing URL: /blog/{slug}/")
    response = client.get(f'/blog/{slug}/')
    print(f"    Status Code: {response.status_code}")
    print(f"    Response Content: {response.content.decode()}")
    print("=" * 65 + "\n")

if __name__ == '__main__':
    main()
