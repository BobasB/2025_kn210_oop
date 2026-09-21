import unittest
from lab_main.main import check_passed_parameter, count_passed_parameters, \
    MainLab, \
    get_input_from_user, \
    doing_api_call_to_external_system

###
class TestCountPassedParameters(unittest.TestCase):
    def test_count_passed_parameters(self):
        """
        Тестуємо передану функцію count_passed_parameters з різними кількостями параметрів."""
        self.assertEqual(
            count_passed_parameters(1, 2, 3),
            3,
            "Очікується, що функція поверне 3, коли передано три параметри",
        )
        self.assertEqual(count_passed_parameters("a", "b"), 2)
        self.assertEqual(count_passed_parameters(), 0)

### Якщо треба зщоб кожен тест був незалежним, то можна використовувати setUp та tearDown для підготовки та очищення перед кожним тестом.
### бо тести можуть впливати один на одного, якщо вони змінюють стан об'єкта або глобальні змінні.
class TestMainLab(unittest.TestCase):
    """Перший клас використовує методи setUp та tearDown для підготовки та очищення перед кожним тестом."""
    def setUp(self):
        """
        Метод setUp виконується перед кожним тестом.
        """
        print("*** Виконується setUp ***")
        self.main_lab = MainLab()

    def tearDown(self):
        """
        Метод tearDown виконується після кожного тесту.
        """
        print("*** Виконується tearDown ***")
        del self.main_lab
    
    def test_return_numbers(self):
        """
        Тестуємо метод return_numbers класу MainLab.
        """
        numbers = list(self.main_lab.return_numbers())
        self.assertEqual(numbers, [1, 2, 3, 4, 5], "Очікується, що метод return_numbers поверне список [1, 2, 3, 4, 5]")

    def test_check_return_nambers_in_globals(self):
        """
        Тестуємо, що метод return_numbers повертає числа, які знаходяться в атрибуті GLOBALS.
        """
        numbers = list(self.main_lab.return_numbers())
        for number in numbers:
            self.assertIn(number, self.main_lab.GLOBALS, f"Очікується, що число {number} буде в атрибуті GLOBALS")

## Якщо обєкт є idempotent і його обєкт не змінює стан, то можна перевіряти його атрибути безпосередньо після створення обєкта.
class TestMainLabConstructor(unittest.TestCase):
    """Другий клас використовує методи setUpClass та tearDownClass для підготовки та очищення перед усіма тестами в класі."""
    @classmethod
    def setUpClass(cls):
        """
        Метод setUpClass виконується один раз перед усіма тестами в класі.
        """
        print("+++ Виконується setUpClass +++")
        cls.main_lab = MainLab()

    @classmethod
    def tearDownClass(cls):
        """
        Метод tearDownClass виконується один раз після усіх тестів в класі.
        """
        print("+++ Виконується tearDownClass +++")
        del cls.main_lab
    
    def test_main_lab_constructor(self):
        """
        Тест може падати через незалежні умови.
        """
        self.assertEqual(self.main_lab.name, "Main Lab", "Очікується, що атрибут 'name' буде 'Main Lab' після створення об'єкта MainLab")
        #self.assertTrue(False, "Навмисно провалений тест для перевірки механізму тестування")

    def test_object_attributes(self):
        self.assertTrue(hasattr(self.main_lab, "name"), "Об'єкт повинен мати атрибут 'name'")


class TestCheckInputFromUserFunction(unittest.TestCase):
    """Тестуємо функцію get_input_from_user."""
    def test_get_input_from_user(self):
        """
        Тестуємо, з використанням mock функції input всередині get_input_from_user.
        """
        from unittest.mock import patch

        with patch('builtins.input', return_value='тестовий ввід'):
            user_input = get_input_from_user()
            self.assertEqual(user_input, 'тестовий ввід', "Очікується, що функція поверне 'тестовий ввід' при введенні користувачем 'тестовий ввід'")

    def test_doing_api_call_to_external_system(self):
        """
        Тестуємо функцію з використанням mock для імітації виклику до зовнішньої системи.
        """
        from unittest.mock import patch

        with patch('lab_main.main.doing_api_call_to_external_system', return_value={"status": "success", "data": "Результат від зовнішньої системи"}):
            result = doing_api_call_to_external_system()
            self.assertEqual(result, {"status": "success", "data": "Результат від зовнішньої системи"}, "Очікується, що функція поверне фіктивний результат від зовнішньої системи")


if __name__ == "__main__":
    unittest.main(verbosity=2)
