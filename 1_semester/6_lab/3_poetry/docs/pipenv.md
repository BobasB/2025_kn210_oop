# Робота з Pipenv

## Огляд

**Pipenv** - це інструмент, який об'єднує управління пакетами (pip) та віртуальними середовищами (venv) в один зручний workflow. Створений Кеннетом Рейтцом (автором бібліотеки requests).

## Особливості

- 🔄 Автоматичне створення та управління віртуальними середовищами
- 📋 Використання Pipfile замість requirements.txt
- 🔒 Pipfile.lock для детермінованих встановлень
- 🎯 Розділення залежностей на prod і dev
- 🛡️ Перевірка безпеки залежностей
- 📊 Візуалізація дерева залежностей

## Встановлення Pipenv

### macOS (Homebrew)

```bash
brew install pipenv
```

### Linux/Windows (pip)

```bash
pip install --user pipenv
```

### Перевірка встановлення

```bash
pipenv --version
```

## Базові команди

### Створення середовища

```bash
# Створення з Python за замовчуванням
pipenv --python 3.13

# Або коротко
pipenv --python 3.13
```

Pipenv автоматично:
- Створює віртуальне середовище
- Створює файл Pipfile
- Визначає розташування середовища

### Розташування середовища

```bash
# Показати шлях до віртуального середовища
pipenv --venv

# Показати шлях до Python
pipenv --py

# Показати інформацію про проект
pipenv --where
```

## Встановлення пакетів

### Продакшн залежності

```bash
# Встановити пакет
pipenv install requests

# Встановити кілька пакетів
pipenv install Flask jikanpy-v4

# Встановити конкретну версію
pipenv install Flask==3.1.3
```

### Dev залежності

```bash
# Встановити dev-пакет
pipenv install --dev flake8

# Або використати коротку форму
pipenv install -d mypy

# Встановити кілька dev-пакетів
pipenv install --dev flake8 mypy pytest
```

### Встановлення з Pipfile

```bash
# Встановити всі залежності
pipenv install

# Встановити тільки prod (без dev)
pipenv install --deploy

# Встановити з Pipfile.lock
pipenv sync
```

## Файл Pipfile

### Структура

```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
flask = "*"
jikanpy-v4 = "*"
requests = ">=2.32.5"

[dev-packages]
flake8 = "*"
mypy = "*"
pytest = "*"

[requires]
python_version = "3.13"
python_full_version = "3.13.7"
```

### Пояснення секцій

- **[[source]]** - джерела пакетів (PyPI)
- **[packages]** - продакшн залежності
- **[dev-packages]** - залежності для розробки
- **[requires]** - вимоги до версії Python

### Специфікація версій

```toml
[packages]
flask = "*"              # Будь-яка версія
requests = ">=2.32.0"    # >= 2.32.0
django = "~=4.2.0"       # >= 4.2.0, < 4.3.0
numpy = "==1.24.0"       # Точно 1.24.0
```

## Pipfile.lock

Автоматично генерований файл, який містить:
- Точні версії всіх пакетів
- Хеші для верифікації
- Повне дерево залежностей

```json
{
    "_meta": {
        "hash": {
            "sha256": "..."
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "3.13"
        }
    },
    "default": {
        "flask": {
            "hashes": ["sha256:..."],
            "version": "==3.1.3"
        }
    },
    "develop": {
        "flake8": {
            "hashes": ["sha256:..."],
            "version": "==7.3.0"
        }
    }
}
```

## Запуск команд

### Запуск у середовищі

```bash
# Запустити Python скрипт
pipenv run python anime.py

# Запустити команду
pipenv run flask run

# Запустити перевірку коду
pipenv run flake8 anime.py
pipenv run mypy anime.py
```

### Відкриття shell

```bash
# Активувати середовище
pipenv shell

# Тепер можна використовувати команди напряму
python anime.py
flask run
flake8 anime.py

# Вийти з shell
exit
```

## Управління пакетами

### Видалення пакетів

```bash
# Видалити пакет
pipenv uninstall requests

# Видалити dev-пакет
pipenv uninstall --dev pytest

# Видалити всі пакети
pipenv uninstall --all

# Видалити всі dev-пакети
pipenv uninstall --all-dev
```

### Оновлення пакетів

```bash
# Оновити всі пакети
pipenv update

# Оновити конкретний пакет
pipenv update Flask

# Оновити тільки Pipfile.lock
pipenv lock
```

### Перегляд залежностей

```bash
# Показати дерево залежностей
pipenv graph

# Вивід:
# Flask==3.1.3
#   - blinker [required: >=1.6.2, installed: 1.9.0]
#   - click [required: >=8.1.3, installed: 8.3.1]
#   - itsdangerous [required: >=2.1.2, installed: 2.2.0]
#   - Jinja2 [required: >=3.1.2, installed: 3.1.6]
#     - MarkupSafe [required: >=2.0, installed: 3.0.3]
```

### Перевірка безпеки

```bash
# Перевірити на відомі вразливості
pipenv check
```

## Практичний приклад: Проект Anime API

### Крок 1: Ініціалізація проекту

```bash
cd 6_lab/2_pipenv
pipenv --python 3.13
```

### Крок 2: Встановлення залежностей

```bash
# Продакшн залежності
pipenv install jikanpy-v4 Flask

# Dev залежності
pipenv install flake8 mypy --dev
```

### Крок 3: Перегляд Pipfile

```bash
cat Pipfile
```

### Крок 4: Перегляд дерева залежностей

```bash
pipenv graph
```

### Крок 5: Запуск проекту

```bash
# Варіант 1: Через pipenv run
pipenv run python anime.py

# Варіант 2: Через shell
pipenv shell
python anime.py
```

### Крок 6: Перевірка коду

```bash
pipenv run flake8 anime.py
pipenv run mypy anime.py
```

### Крок 7: Експорт залежностей

```bash
# Для сумісності з pip
pipenv requirements > requirements.txt
pipenv requirements --dev > requirements-dev.txt
```

## Змінні оточення

### Файл .env

Pipenv автоматично завантажує змінні з `.env`:

```env
FLASK_APP=anime.py
FLASK_ENV=development
DATABASE_URL=sqlite:///anime.db
API_KEY=your-api-key-here
```

Використання в коді:

```python
import os

app_name = os.getenv('FLASK_APP')
db_url = os.getenv('DATABASE_URL')
```

### Завантаження .env

```bash
# .env завантажується автоматично при
pipenv shell
pipenv run python app.py
```

## Корисні команди

```bash
# Очистити середовище
pipenv --rm

# Показати змінні оточення
pipenv --envs

# Відкрити Pipfile в редакторі
pipenv open Flask

# Перевірити права доступу
pipenv verify

# Показати розташування site-packages
pipenv --venv
```

## Інтеграція з IDE

### VS Code

VS Code автоматично знаходить Pipenv середовища. Або вручну:

1. `Cmd/Ctrl + Shift + P`
2. "Python: Select Interpreter"
3. Виберіть інтерпретатор з Pipenv

### PyCharm

1. File → Settings → Project → Python Interpreter
2. Add Interpreter → Pipenv Environment
3. PyCharm автоматично знайде Pipfile

## Міграція з requirements.txt

```bash
# З існуючого requirements.txt
pipenv install -r requirements.txt

# Конвертувати requirements.txt в Pipfile
pipenv install

# Видалити requirements.txt після міграції
rm requirements.txt
```

## Поширені проблеми

### Проблема 1: Повільне встановлення

**Рішення:**
```bash
# Вимкнути lock
pipenv install --skip-lock

# Або використати pypi-mirror
export PIPENV_PYPI_MIRROR=https://pypi.tuna.tsinghua.edu.cn/simple
```

### Проблема 2: Конфлікти залежностей

**Рішення:**
```bash
# Перествор lock файл
pipenv lock --clear

# Або передстановити
pipenv uninstall --all
pipenv install
```

### Проблема 3: Середовище не знайдено

**Рішення:**
```bash
# Показати шлях
pipenv --venv

# Пересоздать середовище
pipenv --rm
pipenv install
```

## Переваги та недоліки

### ✅ Переваги

- Автоматичне управління venv
- Pipfile зручніший за requirements.txt
- Pipfile.lock гарантує відтворюваність
- Вбудована перевірка безпеки
- Візуалізація залежностей
- Підтримка .env файлів

### ❌ Недоліки

- Повільніший за pip
- Іноді складні конфлікти залежностей
- Потребує окремого встановлення
- Не підходить для публікації пакетів

## Порівняння з venv

| Характеристика | venv + pip | Pipenv |
|----------------|-----------|--------|
| Створення середовища | Ручне | Автоматичне |
| Файл залежностей | requirements.txt | Pipfile |
| Lock файл | ❌ | ✅ Pipfile.lock |
| Dev залежності | Окремий файл | В Pipfile |
| Дерево залежностей | ❌ | ✅ pipenv graph |
| Перевірка безпеки | ❌ | ✅ pipenv check |

## Наступні кроки

- Спробуйте ще більш сучасний інструмент: [Poetry →](poetry.md)
- Дізнайтеся більше про [проект Anime API →](anime_project.md)
- Перегляньте [покрокові інструкції →](instructions.md)
