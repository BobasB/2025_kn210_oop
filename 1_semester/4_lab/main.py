"""
Головна програма імітації роботи бібліотеки
"""

from book import Book
from student import Student
from library import Library


def main():
    """
    Головна функція програми - демонстрація роботи бібліотеки
    """
    
    # Створення бібліотеки
    print("=" * 60)
    print("СИСТЕМА УПРАВЛІННЯ БІБЛІОТЕКОЮ")
    print("=" * 60)
    
    library = Library("Бібліотека IT коледжу")

    library.display_all_books()
    
    # Створення книг
    print("\n--- Додавання книг до бібліотеки ---")
    for book in [Book("Кобзар", "Тарас Шевченко", 1840),
                 Book("Лісова пісня", "Леся Українка", 1911),
                 Book("Енеїда", "Іван Котляревський", 1798),
                 Book("Python для початківців", "Марк Лутц", 2019),
                 Book("Чисті функції", "Роберт Мартін", 2018),
                 Book("Тіні забутих предків", "Михайло Коцюбинський", 1911),
                 Book("Захар Беркут", "Іван Франко", 1883),
                 Book("Футбол у житті людини", "Василь Гроссман", 1952)]:
        library.add_book(book)
    
    # Відображення всіх книг
    library.display_all_books()
    
    # Створення студентів
    print("\n--- Створення студентів ---")
    for student in [Student("Іван", "Петренко", "КН-210, 2 курс"),
                    Student("Марія", "Коваленко", "КН-210, 2 курс"),
                    Student("Олексій", "Сидоренко", "КН-210, 2 курс"),
                    Student("Анна", "Ткаченко", "КН-210, 2 курс"),
                    Student("Дмитро", "Бондаренко", "КН-210, 2 курс")]:
        print(f"Створено студента: {student}")
        library.students.append(student)
 
    library.display_all_students()
    
    ##### +++ НА НАСТУПНІЙ ПАРІ ДОРОБИМОТЬ ЦЮ ЧАСТИНУ +++ #####
    # Видача книг студентам
    print("\n--- Видача книг студентам ---")
    library.lend_book(book1, student1)
    library.lend_book(book4, student1)
    library.lend_book(book2, student2)
    library.lend_book(book5, student3)
    
    # Спроба взяти вже видану книгу
    print("\n--- Спроба взяти вже видану книгу ---")
    library.lend_book(book1, student2)
    
    # Відображення стану бібліотеки
    print(f"\n{library}")
    
    # Відображення доступних книг
    library.display_available_books()
    
    # Відображення інформації про студентів
    print("\n--- Інформація про студентів ---")
    print(f"{student1}")
    print(f"  Книги студента {student1.get_full_name()}:")
    for i, book in enumerate(student1.borrowed_books, 1):
        print(f"    {i}. {book.title} - {book.author}")
    
    print(f"\n{student2}")
    print(f"  Книги студента {student2.get_full_name()}:")
    for i, book in enumerate(student2.borrowed_books, 1):
        print(f"    {i}. {book.title} - {book.author}")
    
    print(f"\n{student3}")
    print(f"  Книги студента {student3.get_full_name()}:")
    for i, book in enumerate(student3.borrowed_books, 1):
        print(f"    {i}. {book.title} - {book.author}")
    
    # Повернення книг
    print("\n--- Повернення книг ---")
    library.return_book(book1, student1)
    library.return_book(book2, student2)
    
    # Відображення оновленого стану
    print(f"\n{library}")
    library.display_available_books()
    
    # Пошук книг
    print("\n--- Пошук книг ---")
    print("\nПошук за автором 'Франко':")
    found_books = library.search_by_author("Франко")
    for book in found_books:
        print(f"  {book}")
    
    print("\nПошук за назвою 'Python':")
    found_books = library.search_by_title("Python")
    for book in found_books:
        print(f"  {book}")
    
    # Відображення всіх книг на кінець
    library.display_all_books()
    
    # Фінальна інформація про студентів
    print("\n--- Фінальна інформація про студентів ---")
    print(f"{student1}")
    print(f"{student2}")
    print(f"{student3}")
    
    print("\n" + "=" * 60)
    print("РОБОТА ПРОГРАМИ ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    main()
