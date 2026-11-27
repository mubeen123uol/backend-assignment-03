from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Question 1: Blog URL routing
    path('blog/', include('blog.urls')),

    # Question 2: Bookstore URL routing
    path('', include('bookstore.urls')),
]
