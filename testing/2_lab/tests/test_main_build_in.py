import unittest
from lab.main import MainLab

class TestMainLab(unittest.TestCase):
    """Тести для демонстрації сумісності тестів у PyTest."""
    def test_globals_in_object_unittest(self):
        obj = MainLab()
        self.assertListEqual(obj.GLOBALS, [1, 2, 3, 4, 5])

    def test_globals_in_object_with_assert(self):
        obj = MainLab()
        assert obj.GLOBALS == [1, 2, 3, 4, 5]
