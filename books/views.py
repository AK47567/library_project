from rest_framework import generics
from rest_framework import mixins
from .models import Book
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import BookSerializer
from .pagination import StandardResultsSetPagination

class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    List all books or create a new one.
    """
    queryset = Book.objects.all().order_by('book_no')
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination
    # The pagination class controls the pagination style of the view

    

    """
    Retrieve, update or delete a book instance.

    
    """
class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    
class BookListAPIView(APIView):
    pagination_class = StandardResultsSetPagination
    template_name = 'book_list.html'

    def get(self, request, format=None):
        queryset = Book.objects.all().order_by('book_no')
        serializer = BookSerializer(queryset, many=True)
        return render(request, self.template_name, {'books': serializer.data})