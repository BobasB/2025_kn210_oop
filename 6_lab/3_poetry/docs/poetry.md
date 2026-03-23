# Робота з Poetry

## Огляд

**Poetry** - це сучасний інструмент для управління залежностями та пакетами Python. Він використовує стандарт PEP 518 (pyproject.toml) та надає повний цикл розробки: від створення проекту до публікації.

## Особливості

- 📦 Повне управління життєвим циклом проекту
- 🎯 Єдиний файл конфігурації (pyproject.toml)
- 🔒 Детальний lock файл (poetry.lock)
- 🚀 Швидкий розв'язувач залежностей
- 📚 Групи залежностей (dev, docs, test, etc.)
- 🌟 Публікація пакетів на PyPI
- 🔄 Управління версіями проекту

## Встановлення Poetry

### Офіційний інсталятор (рекомендовано)

```bash
# Linux, macOS, Windows (WSL)
curl -sSL https://install.python-poetry.org | python3 -

# Додати до PATH (якщо потрібно)
export PATH="$HOME/.local/bin:$PATH"
```

### Homebrew (macOS)

```bash
brew install poetry
```

### Перевірка встановлення

```bash
poetry --version
# Poetry (version 1.8.0)
```

## Базові команди

### Створення нового проекту

```bash
# Створити новий проект
poetry new my-project

# Структура:
# my-project/
# ├── pyproject.toml
# ├── README.md
# ├── my_project/
# │   └── __init__.py
# └── tests/
#     └── __init__.py
```

### Ініціалізація у існуючій директорії

```bash
# Створити pyproject.toml в поточній директорії
poetry init

# Інтерактивний режим з питаннями
```

## Файл pyproject.toml

### Структура для нашого проекту

```toml
[project]
name = "3-poetry"
version = "0.1.0"
description = "Вчимось працювати з віртуальними середовищами"
authors = [
    {name = "BobasB", email = "bugil.bogdan@gmail.com"}
]
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "requests>=2.32.5,<3.0.0",
    "jikanpy-v4>=1.0.2,<2.0.0",
    "flask>=3.1.3,<4.0.0"
]

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"

[dependency-groups]
dev = [
    "flake8>=7.3.0,<8.0.0",
    "mypy>=1.19.1,<2.0.0"
]
docs = [
    "mkdocs>=1.6.1,<2.0.0"
]
```

### Пояснення секцій

#### [project] - Метадані проекту
- **name** - назва пакету
- **version** - версія проекту
- **description** - короткий опис
- **authors** - автори проекту
- **dependencies** - основні залежності

#### [dependency-groups] - Групи залежностей
- **dev** - для розробки (linters, formatters)
- **docs** - для документації
- **test** - для тестування
- _можна створювати власні групи_

#### [build-system] - Система збірки
- Визначає, як Poetry збирає пакет

### Специфікація версій

```toml
dependencies = [
    "requests>=2.32.5,<3.0.0",   # >= 2.32.5 і < 3.0.0
    "flask^3.1.3",                # >= 3.1.3, < 4.0.0
    "django~=4.2.0",              # >= 4.2.0, < 4.3.0
    "numpy==1.24.0",              # Точно 1.24.0
    "pandas*"                     # Будь-яка версія
]
```

## Управління віртуальними середовищами

### Створення середовища

```bash
# Poetry автоматично створює venv при
poetry install
```

### Інформація про середовище

```bash
# Показати шлях до venv
poetry env info

# Показати тільки шлях
poetry env info --path

# Список всіх venv для проекту
poetry env list
```

### Управління середовищами

```bash
# Використати конкретну версію Python
poetry env use python3.13
poetry env use 3.13

# Видалити віртуальне середовище
poetry env remove python3.13

# Видалити всі середовища проекту
poetry env remove --all
```

## Встановлення залежностей

### Додавання  пакетів

```bash
# Додати продакшн залежність
poetry add requests

# Додати кілька пакетів
poetry add flask jikanpy-v4

# Додати конкретну версію
poetry add "Flask==3.1.3"

# Додати з обмеженням версії
poetry add "requests>=2.32,<3.0"
```

### Додавання в групи

```bash
# Додати в dev групу
poetry add --group dev flake8

# Додати в docs групу
poetry add --group docs mkdocs

# Додати в test групу
poetry add --group test pytest
```

### Встановлення залежностей

```bash
# Встановити всі залежності (включно з групами)
poetry install

# Встановити без dev залежностей
poetry install --without dev

# Встановити тільки prod залежності
poetry install --only main

# Встановити тільки конкретну групу
poetry install --only docs

# Встановити з конкретними групами
poetry install --with docs,test
```

## Видалення пакетів

```bash
# Видалити пакет
poetry remove requests

# Видалити з групи
poetry remove --group dev flake8
```

## Оновлення залежностей

```bash
# Оновити всі залежності
poetry update

# Оновити конкретний пакет
poetry update flask

# Оновити тільки dev залежності
poetry update --only dev

# Показати застарілі пакети
poetry show --outdated
```

## Запуск команд

### Виконання в середовищі

```bash
# Запустити Python скрипт
poetry run python anime.py

# Запустити команду
poetry run flask run

# Запустити linters
poetry run flake8 anime.py
poetry run mypy anime.py
```

### Відкриття shell

```bash
# Активувати віртуальне середовище
poetry shell

# Тепер можна використовувати команди напряму
python anime.py
flask run
flake8 anime.py

# Вийти з shell
exit
```

## Перегляд залежностей

```bash
# Список всіх пакетів
poetry show

# Дерево залежностей
poetry show --tree

# Інформація про конкретний пакет
poetry show flask

# Тільки dev залежності
poetry show --only dev

# Тільки застарілі пакети
poetry show --outdated
```

## Блокування залежностей

```bash
# Оновити poetry.lock без встановлення
poetry lock

# Оновити з перевіркою
poetry lock --check

# Оновити з останніми версіями
poetry lock --no-update
```

## Практичний приклад: Проект Anime API

### Крок 1: Ініціалізація проекту

```bash
cd 6_lab/3_poetry
poetry init
```

Відповідаємо на питання або пропускаємо.

### Крок 2: Додавання залежностей

```bash
# Продакшн залежності
poetry add requests jikanpy-v4 flask

# Dev залежності
poetry add --group dev flake8 mypy

# Документація
poetry add --group docs mkdocs
```

### Крок 3: Встановлення

```bash
poetry install
```

### Крок 4: Перегляд структури

```bash
# Дерево залежностей
poetry show --tree

# Інформація про середовище
poetry env info
```

### Крок 5: Запуск проекту

```bash
poetry run python anime.py
```

### Крок 6: Робота з документацією

```bash
# Запустити mkdocs сервер
poetry run mkdocs serve

# Збудувати документацію
poetry run mkdocs build
```

### Крок 7: Перевірка коду

```bash
poetry run flake8 anime.py
poetry run mypy anime.py
```

## Публікація пакету

### Підготовка

```bash
# Збудувати пакет
poetry build

# Створюється:
# dist/
# ├── my_package-0.1.0.tar.gz
# └── my_package-0.1.0-py3-none-any.whl
```

### Конфігурація PyPI

```bash
# Додати токен PyPI
poetry config pypi-token.pypi your-token-here
```

### Публікація

```bash
# Опублікувати на PyPI
poetry publish

# Або build + publish
poetry publish --build

# Опублікувати на test PyPI
poetry publish -r testpypi
```

## Управління версіями

```bash
# Patch: 0.1.0 -> 0.1.1
poetry version patch

# Minor: 0.1.0 -> 0.2.0
poetry version minor

# Major: 0.1.0 -> 1.0.0
poetry version major

# Конкретна версія
poetry version 1.2.3

# Pre-release
poetry version prepatch  # 0.1.0 -> 0.1.1-alpha.0
poetry version preminor  # 0.1.0 -> 0.2.0-alpha.0
poetry version premajor  # 0.1.0 -> 1.0.0-alpha.0
```

## Скрипти

Можна додати власні команди в pyproject.toml:

```toml
[tool.poetry.scripts]
start = "anime:main"
test = "pytest:main"
```

Використання:

```bash
poetry run start
poetry run test
```

## Конфігурація Poetry

```bash
# Показати конфігурацію
poetry config --list

# Створювати venv в директорії проекту
poetry config virtualenvs.in-project true

# Встановити шлях до venv
poetry config virtualenvs.path ~/my-venvs

# Увімкнути/вимкнути автоматичне створення venv
poetry config virtualenvs.create false
```

## Експорт залежностей

```bash
# Експорт в requirements.txt
poetry export -f requirements.txt -o requirements.txt

# З dev залежностями
poetry export -f requirements.txt --with dev -o requirements-dev.txt

# Без хешів (для PIP)
poetry export -f requirements.txt --without-hashes -o requirements.txt
```

## Корисні команди

```bash
# Перевірити pyproject.toml
poetry check

# Показати інформацію про проект
poetry about

# Очистити кеш
poetry cache clear pypi --all

# Самооновлення Poetry
poetry self update

# Встановити plugin
poetry self add poetry-plugin-export
```

## Інтеграція з IDE

### VS Code

1. Poetry автоматично визначається VS Code
2. Або виберіть інтерпретатор вручну:
   - `Cmd/Ctrl + Shift + P`
   - "Python: Select Interpreter"
   - Виберіть з `.venv` в проекті

### PyCharm

1. File → Settings → Project → Python Interpreter
2. Add Interpreter → Poetry Environment
3. PyCharm знайде pyproject.toml

## Міграція з інших інструментів

### З requirements.txt

```bash
# Додати всі пакети з requirements.txt
poetry add $(cat requirements.txt)

# Або
cat requirements.txt | xargs poetry add
```

### З Pipenv

```bash
# Прочитати Pipfile і створити pyproject.toml
poetry init

# Потім вручну перенести залежності
```

## Поширені проблеми

### Проблема 1: Конфлікти залежностей

**Рішення:**
```bash
# Оновити lock з останніми версіями
poetry lock --no-update

# Або повне оновлення
poetry update
```

### Проблема 2: Poetry не знаходить Python

**Рішення:**
```bash
# Вказати явно
poetry env use /usr/bin/python3.13

# Або через pyenv
poetry env use $(pyenv which python)
```

### Проблема 3: Повільна установка

**Рішення:**
```bash
# Встановити без dev залежностей
poetry install --no-dev

# Паралельна установка
poetry config installer.parallel true
```

## Переваги та недоліки

### ✅ Переваги

- Сучасний стандарт (PEP 518, pyproject.toml)
- Швидкий розв'язувач залежностей
- Групи залежностей
- Вбудована публікація на PyPI
- Управління версіями проекту
- Детальний lock файл
- Активна розробка

### ❌ Недоліки

- Потребує окремого встановлення
- Крива навчання вища за venv
- Іноді складні помилки залежностей
- Не завжди сумісний з усіма інструментами

## Порівняння з іншими інструментами

| Характеристика | venv+pip | Pipenv | Poetry |
|----------------|----------|--------|--------|
| Файл конфігурації | requirements.txt | Pipfile | pyproject.toml |
| Lock файл | ❌ | Pipfile.lock | poetry.lock |
| Групи залежностей | ❌ | ✅ (dev) | ✅ (будь-які) |
| Публікація пакетів | ❌ | ❌ | ✅ |
| Управління версіями | ❌ | ❌ | ✅ |
| Швидкість | ⭐⭐⭐ | ⭐ | ⭐⭐ |
| Стандарт PEP 518 | ❌ | ❌ | ✅ |

## Чому Poetry для цього проекту?

1. ✅ Підтримка груп залежностей (dev, docs)
2. ✅ Зручна робота з mkdocs через групу docs
3. ✅ Сучасний стандарт pyproject.toml
4. ✅ Швидкий та надійний
5. ✅ Гарна документація

## Наступні кроки

- Дізнайтеся більше про [проект Anime API →](anime_project.md)
- Перегляньте [покрокові інструкції →](instructions.md)
- Порівняйте з [venv →](venv.md) та [Pipenv →](pipenv.md)
