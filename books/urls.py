from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView, BookListAPIView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books-list/', BookListAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-retrieve-update-destroy'),
]
