# My Django REST API Project

This project is a Django-based RESTful API for managing books.

## Requirements

- Python 3.9.x
- Django 3.2.x
- Django REST Framework 3.12.x

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AK47567/library_project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd library_project
    ```

3. Create virtual environment:

    '''bash
   python -m venv .venv

   .venv\scripts\activate
    '''

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Set up your database in `settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

2. Migrate the database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Usage

1. Run the development server:

    ```bash
    python manage.py runserver
    ```

2. Access the API at `http://localhost:8000/books/`

## API Endpoints

- `GET /books/`: Retrieve a list of all books.
- `POST /books/`: Create a new book.
- `GET /books/<id>/`: Retrieve details of a specific book.
- `PUT /books/<id>/`: Update details of a specific book.
- `DELETE /books/<id>/`: Delete a specific book.

### Data Entry

    ''' 
    In order to enter data into the database for checking the API, run the fakers.py script to enter Random fake datasets. Make sure to manage the number of fake data based on your requirement.
    '''

