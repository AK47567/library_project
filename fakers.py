import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_project.settings')

import django
django.setup()

from faker import Faker
from books.models import Book

fake = Faker()

def generate_books(num_books):
    for _ in range(num_books):
        title = fake.sentence(nb_words=3)
        author = fake.name()
        genre = fake.word()
        Book.objects.create(title=title, author=author, genre=genre)

if __name__ == '__main__':
    num_books = 50  # Change this number to generate more or fewer books
    generate_books(num_books)
    print(f"{num_books} books created successfully.")
