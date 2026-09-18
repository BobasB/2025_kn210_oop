import unittest
from lab_main.main import check_passed_parameter, count_passed_parameters, MainLab

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

###
class TestMainLabConstructor(unittest.TestCase):
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
    
    def test_main_lab_constructor(self):
        """
        Тест може падати через незалежні умови.
        """
        self.assertEqual(self.main_lab.name, "Main Lab", "Очікується, що атрибут 'name' буде 'Main Lab' після створення об'єкта MainLab")
        self.assertTrue(False, "Навмисно провалений тест для перевірки механізму тестування")

    def test_object_attributes(self):
        self.assertTrue(hasattr(self.main_lab, "name"), "Об'єкт повинен мати атрибут 'name'")


if __name__ == "__main__":
    unittest.main(verbosity=2)
