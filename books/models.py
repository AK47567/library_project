from django.db import models

class Book(models.Model):
    book_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
'''
Model for Book to store the data in table Book
'''