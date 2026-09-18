"""
Клас Book - представляє книгу в бібліотеці
"""


class Book:
    """
    Клас для представлення книги
    
    Атрибути:
        title (str): Назва книги
        author (str): Автор книги
        year (int): Рік видання
        is_available (bool): Статус доступності книги (True - доступна, False - видана)
    """
    
    def __init__(self, title, author, year):
        """
        Ініціалізація об'єкту Book
        
        Args:
            title (str): Назва книги
            author (str): Автор книги
            year (int): Рік видання
        """
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.is_available: bool = True  # Початково всі книги доступні
    
    def borrow(self):
        """
        Позначає книгу як видану
        
        Returns:
            bool: True якщо книга була доступна і успішно видана, False якщо книга вже видана
        """
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def return_book(self):
        """
        Позначає книгу як повернену (доступну)
        
        Returns:
            bool: True якщо книга була видана і успішно повернена, False якщо книга вже доступна
        """
        if not self.is_available:
            self.is_available = True
            return True
        return False
    
    def __str__(self):
        """
        Строкове представлення книги
        
        Returns:
            str: Інформація про книгу
        """
        status = "доступна" if self.is_available else "видана"
        return f'>>>|Книга: "{self.title}";\nАвтор: {self.author};\nРік: {self.year};\nСтатус: [{status}]\n'
    
    def __repr__(self):
        """
        Представлення об'єкту для розробників
        
        Returns:
            str: Технічне представлення об'єкту
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
