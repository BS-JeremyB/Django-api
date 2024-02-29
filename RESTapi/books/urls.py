
from django.urls import path
from books import views

urlpatterns = [
    path('', views.BookList.as_view(), name='book-list'),
    path('books/create/', views.BookCreate.as_view(), name='book-create'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
]