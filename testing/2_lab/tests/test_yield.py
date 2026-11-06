import pytest
from lab.main import MainLab
import random

# Це створилось один раз бо ми задали scope="module", 
# тому цей об'єкт буде використовуватись у всіх тестах цього модуля 
@pytest.fixture(scope="module")
def main_lab_object_with_return():
    """Фікстура для створення об'єкта MainLab."""
    rs = random.randint(1, 100)
    obj = MainLab("Return Lab Fixture", 123, f"Число з Фікстури return: {rs}")
    return obj

# Це створюється для кожного тесту окремо бо ми задали scope="function", 
# тому цей об'єкт буде створюватись для кожного тесту окремо
# але з yield обєкт після кожного тесту буде видалятись і створюватись новий для наступного тесту
@pytest.fixture(scope="function")
def main_lab_object_with_yield():
    """Фікстура для створення об'єкта MainLab з використанням yield."""
    s = random.randint(1, 100)
    obj = MainLab("Yield Lab Fixture", 123, f"Число з Фікстури yield: {s}")
    yield obj
    # після завершення тесту можна додати код для очищення ресурсів, якщо це необхідно
    del obj

def test_example_with_fixture_return(main_lab_object_with_return):
    """Тест, який використовує фікстуру для отримання об'єкта MainLab."""
    obj = main_lab_object_with_return
    assert obj.name == "Return Lab Fixture"
    assert obj.test_var == 123
    assert obj.output_name == "Return Lab Fixture - Output: 123"

@pytest.mark.parametrize("number", [
    (1, 122),
    (2, 121),
    (3, 120),
    (4, 119),
    (5, 118)
])
def test_example_with_yield_fixture(main_lab_object_with_yield, 
                                    main_lab_object_with_return,
                                    number):
    """Тест, який використовує фікстуру з yield для отримання об'єкта MainLab."""
    obj_yield = main_lab_object_with_yield
    assert obj_yield.name == "Yield Lab Fixture"
    assert obj_yield.test_var - number[0] == number[1]
    
    obj_return = main_lab_object_with_return
    assert obj_return.name == "Return Lab Fixture"
    assert obj_return.test_var - number[0] == number[1]
    # Цей ассерт спеціально падає що ми побачили як працює yield фікстура, бо вона створює новий об'єкт для кожного тесту, а return фікстура повертає один і той же об'єкт для всіх тестів
    assert obj_yield.random_field == obj_return.random_field, "Yield і Return фікстури створюють різні об'єкти, тому їх random_field не повинні бути однаковими."
    