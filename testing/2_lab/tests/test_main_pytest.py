from lab.main import MainLab
import pytest 

def test_globas_in_object_as_function():
    """Цей тест використовує бібіліотеку PyTest"""
    obj = MainLab()
    assert obj.GLOBALS == [1, 2, 3, 4, 5]

class TestMainLab:
    """Тести для демонстрації сумісності тестів у PyTest."""
    def test_globals_in_object_in_class(self):
        obj = MainLab()
        assert obj.GLOBALS == [1, 2, 3, 4, 5]

    def test_get_exceptions_with_negative_index(self):
        """Тест чекає на винекнення помилки ValueError при передачі негативного індексу."""
        obj = MainLab()
        with pytest.raises(ValueError):
            # є навмисно помилка якщо передами -1
            obj.get_exeptions(-1)

    def test_get_exceptions_with_positive_index(self):
        """Тест чекає на винекнення помилки ValueError при передачі додатного індексу."""
        obj = MainLab()
        with pytest.raises(ValueError):
           # якщо ми передомо додатній індекс, то помилки не буде
           # цей тест буде проваленим!
           obj.get_exeptions(1)

    def test_get_exceptions_with_wrong_exception(self):
        """Тест чекає на винекнення помилки ValueError при передачі негативного індексу."""
        obj = MainLab()
        with pytest.raises(ZeroDivisionError):
            # якщо ми неправильно визначимо очікувану помилку, 
            # то тест також буде проваленим
            obj.get_exeptions(-1)