import pytest
from lab.main import MainLab

# Пройти фікстури
def test_mainlab_simple():
    """Класичний тест де все задається всеридині цього тесту"""
    _override_name = "Test Lab"
    _override_test_var = 99
    obj = MainLab(_override_name, _override_test_var)
    
    assert obj.name == _override_name
    assert obj.test_var == _override_test_var
    assert obj.output_name == _override_name + " - Output: " + str(_override_test_var)

# будь-який повторюваний код завжди виноситься у функцію
def _setup_mainlab_object():
    """Допоміжна функція для створення об'єкта MainLab з певними параметрами."""
    _override_name = "Test Lab"
    _override_test_var = 99
    # на вихід повертаємо словник з параметрами та об'єктом який створений з цих параметрів
    return {
        "name": _override_name,
        "test_var": _override_test_var,
        "obj": MainLab(_override_name, _override_test_var)
    }

def test_mainlab_with_setup_function():
    """Тест який використовує функцію для налаштування об'єкта MainLab."""
    setup_data = _setup_mainlab_object()
    obj = setup_data["obj"]
    
    assert obj.name == setup_data["name"]
    assert obj.test_var == setup_data["test_var"]
    assert obj.output_name == setup_data["name"] + " - Output: " + str(setup_data["test_var"])

# А тепер робимо фікстуру яка буде створювати об'єкт MainLab для тестів
@pytest.fixture
def mainlab_setup():
    """Фікстура для створення об'єкта MainLab з певними параметрами."""
    _override_name = "Test Lab"
    _override_test_var = 99
    obj = MainLab(_override_name, _override_test_var)
    return {
        "name": _override_name,
        "test_var": _override_test_var,
        "obj": obj
    }

def test_mainlab_with_fixture(mainlab_setup):
    """Тест який використовує фікстуру для налаштування об'єкта MainLab."""
    obj = mainlab_setup["obj"]
    
    assert obj.name == mainlab_setup["name"]
    assert obj.test_var == mainlab_setup["test_var"]
    assert obj.output_name == mainlab_setup["name"] + " - Output: " + str(mainlab_setup["test_var"])

@pytest.fixture
def mainlab_init_parameter_name():
    """Фікстура для передачі параметрів у конструктор MainLab."""
    return "Parameterized Lab"

@pytest.fixture
def mainlab_init_parameter_test_var():
    """Фікстура для передачі параметрів у конструктор MainLab."""
    return 123

# можемо створювати фікстури для фікстур, тобто фікстура яка приймає інші фікстури
@pytest.fixture
def mainlab_with_parameters(mainlab_init_parameter_name, mainlab_init_parameter_test_var):
    """Фікстура яка створює об'єкт MainLab з параметрами з інших фікстур."""
    return MainLab(mainlab_init_parameter_name, mainlab_init_parameter_test_var)

def test_mainlab_with_parameterized_fixture(
        mainlab_with_parameters, 
        mainlab_init_parameter_name, 
        mainlab_init_parameter_test_var
):
    """Тест який використовує параметризовану фікстуру для створення об'єкта MainLab."""
    # Копіюємо фікстури у змінні щоб не змінювати їх безпосередньо у тесті
    obj = mainlab_with_parameters
    
    assert obj.name == mainlab_init_parameter_name
    assert obj.test_var == mainlab_init_parameter_test_var
    assert obj.output_name == mainlab_init_parameter_name + " - Output: " + str(mainlab_init_parameter_test_var)
