# Coverage demo

Невеликий приклад тестування Python-коду. Модуль `cov.score` містить
функції для обчислення середнього бала та визначення результату.

## Встановлення

У каталозі цього проєкту (`testing/3_lab/cov`) виконайте:

```bash
poetry install
```

## `unittest` + `coverage`

Запустити тести:

```bash
PYTHONPATH=src poetry run coverage run -m unittest discover -s tests -p "test_unittest.py" -v
```

Показати звіт у терміналі:

```bash
poetry run coverage report -m
```

Створити HTML-звіт:

```bash
poetry run coverage html
```

Звіт буде збережено в каталозі `htmlcov`. Відкрити його можна у файлі
`htmlcov/index.html`.

## `pytest` + `pytest-cov`

Запустити тести та побачити покриття в терміналі:

```bash
poetry run pytest tests/test_pytest.py --cov=cov --cov-report=term-missing
```

Створити HTML-звіт:

```bash
poetry run pytest tests/test_pytest.py --cov=cov --cov-report=html:htmlcov-pytest
```

Звіт буде збережено у `htmlcov-pytest/index.html`.