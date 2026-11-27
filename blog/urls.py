from django.urls import path
from . import views

urlpatterns = [
    # /blog/
    path('', views.post_list, name='post_list'),

    # /blog/<int:year>/
    path('<int:year>/', views.post_archive_year, name='post_archive_year'),

    # /blog/<int:year>/<int:month>/
    path('<int:year>/<int:month>/', views.post_archive_month, name='post_archive_month'),

    # /blog/<slug:slug>/
    path('<slug:slug>/', views.post_detail_slug, name='post_detail_slug'),
]
