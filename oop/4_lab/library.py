"""
Клас Library - представляє бібліотеку
"""
from book import Book
from student import Student


class Library:
    """
    Клас для представлення бібліотеки
    
    Атрибути:
        name (str): Назва бібліотеки
        books (list): Список всіх книг у бібліотеці
    """
    
    def __init__(self, name):
        """
        Ініціалізація об'єкту Library
        
        Args:
            name (str): Назва бібліотеки
        """
        self.name = name
        self.books: list[Book] = []
        self.students: list[Student] = [] # Список студентів бібліотеки
    
    def add_book(self, book: Book):
        """
        Додає книгу до бібліотеки
        
        Args:
            book (Book): Об'єкт книги
        """
        self.books.append(book)
        print(f"Книга '{book.title}' додана до бібліотеки.")
    
    def search_by_title(self, title: str):
        """
        Пошук книг за назвою
        
        Args:
            title (str): Назва книги або частина назви
            
        Returns:
            list: Список знайдених книг
        """
        found_books = []
        for book in self.books:
            if title.lower() in book.title.lower():
                found_books.append(book)
        return found_books
    
    def search_by_author(self, author: str):
        """
        Пошук книг за автором
        
        Args:
            author (str): Автор або частина імені автора
            
        Returns:
            list: Список знайдених книг
        """
        found_books = []
        for book in self.books:
            if author.lower() in book.author.lower():
                found_books.append(book)
        return found_books
    
    def lend_book(self, book: Book, student: Student):
        """
        Видає книгу студенту
        
        Args:
            book (Book): Об'єкт книги
            student (Student): Об'єкт студента
            
        Returns:
            bool: True якщо книга успішно видана, False якщо книга вже видана
        """
        if book not in self.books:
            print(f"Книга '{book.title}' не знайдена в бібліотеці.")
            return False
        
        if book.borrow():
            student.add_book(book)
            print(f"Книга '{book.title}' видана студенту {student.get_full_name()}.")
            return True
        else:
            print(f"Книга '{book.title}' вже видана.")
            return False
    
    def return_book(self, book: Book, student: Student):
        """
        Приймає повернену книгу від студента
        
        Args:
            book (Book): Об'єкт книги
            student (Student): Об'єкт студента
            
        Returns:
            bool: True якщо книга успішно повернена, False якщо книга не була видана
        """
        if book not in self.books:
            print(f"Книга '{book.title}' не належить цій бібліотеці.")
            return False
        
        if book.return_book():
            student.remove_book(book)
            print(f"Книга '{book.title}' повернена студентом {student.get_full_name()}.")
            return True
        else:
            print(f"Книга '{book.title}' не була видана.")
            return False
    
    def display_all_books(self):
        """
        Відображає всі книги в бібліотеці
        """
        if not self.books:
            print("Бібліотека порожня.")
            return
        
        print(f"\n=== Книги в бібліотеці '{self.name}' ===")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
    
    def display_available_books(self):
        """
        Відображає доступні книги в бібліотеці
        """
        available_books = [book for book in self.books if book.is_available]
        
        if not available_books:
            print("Немає доступних книг.")
            return
        
        print(f"\n=== Доступні книги в бібліотеці '{self.name}' ===")
        for i, book in enumerate(available_books, 1):
            print(f"{i}. {book}")
    
    def display_all_students(self):
        """
        Відображає всіх студентів бібліотеки
        """
        if not self.students:
            print("У бібліотеці немає зареєстрованих студентів.")
            return
        
        print(f"\n=== Студенти бібліотеки '{self.name}' ===")
        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student.get_full_name()} - {student.description}")
    
    def __str__(self):
        """
        Строкове представлення бібліотеки
        
        Returns:
            str: Інформація про бібліотеку
        """
        total_books = len(self.books)
        available_books = len([book for book in self.books if book.is_available])
        return f"Бібліотека '{self.name}' - всього книг: {total_books}, доступно: {available_books}"
    
    def __repr__(self):
        """
        Представлення об'єкту для розробників
        
        Returns:
            str: Технічне представлення об'єкту
        """
        return f"Library('{self.name}')"
