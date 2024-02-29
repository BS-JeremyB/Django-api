
from django.urls import path
from books import views

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:id>/', views.book_detail),
]