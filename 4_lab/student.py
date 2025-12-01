"""
Клас Student - представляє студента бібліотеки
"""
from book import Book


class Student:
    """
    Клас для представлення студента
    
    Атрибути:
        first_name (str): Ім'я студента
        last_name (str): Прізвище студента
        description (str): Опис студента (факультет, курс тощо)
        borrowed_books (list): Список книг, які взяв студент
    """
    
    def __init__(self, first_name, last_name, description=""):
        """
        Ініціалізація об'єкту Student
        
        Args:
            first_name (str): Ім'я студента
            last_name (str): Прізвище студента
            description (str): Опис студента (необов'язковий параметр)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.description = description
        self.borrowed_books: list[Book] = []  # Список взятих книг
    
    def get_full_name(self):
        """
        Повертає повне ім'я студента
        
        Returns:
            str: Повне ім'я (ім'я + прізвище)
        """
        return f"{self.first_name} {self.last_name}"
    
    def add_book(self, book: Book):
        """
        Додає книгу до списку взятих студентом книг
        
        Args:
            book (Book): Об'єкт книги
        """
        self.borrowed_books.append(book)
    
    def remove_book(self, book: Book):
        """
        Видаляє книгу зі списку взятих студентом книг
        
        Args:
            book (Book): Об'єкт книги
            
        Returns:
            bool: True якщо книга була знайдена та видалена, False якщо книги немає у списку
        """
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return True
        return False
    
    def get_borrowed_books_count(self):
        """
        Повертає кількість взятих книг
        
        Returns:
            int: Кількість взятих книг
        """
        return len(self.borrowed_books)
    
    def __str__(self):
        """
        Строкове представлення студента
        
        Returns:
            str: Інформація про студента
        """
        books_count = len(self.borrowed_books)
        info = f"{self.get_full_name()}"
        if self.description:
            info += f" ({self.description})"
        info += f" - взято книг: {books_count}"
        return info
    
    def __repr__(self):
        """
        Представлення об'єкту для розробників
        
        Returns:
            str: Технічне представлення об'єкту
        """
        return f"Student('{self.first_name}', '{self.last_name}', '{self.description}')"
