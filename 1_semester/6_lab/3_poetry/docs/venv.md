# Робота з venv

## Огляд

`venv` - це модуль стандартної бібліотеки Python (починаючи з версії 3.3), який дозволяє створювати віртуальні середовища.

## Встановлення

venv входить у стандартну поставку Python, тому додаткове встановлення не потрібне.

Перевірка наявності:
```bash
python -m venv --help
```

## Створення віртуального середовища

### Базовий синтаксис

```bash
python -m venv <назва_середовища>
```

### Приклади

```bash
# Створення середовища з назвою my_env
python -m venv my_env

# Створення середовища з назвою venv
python -m venv venv

# Створення з конкретною версією Python
python3.13 -m venv my_env
```

### Структура створеного середовища

```
my_env/
├── bin/              # Виконувані файли (Linux/macOS)
│   ├── activate      # Скрипт активації
│   ├── python        # Символічне посилання на Python
│   └── pip           # pip для цього середовища
├── Scripts/          # Виконувані файли (Windows)
│   ├── activate.bat
│   └── python.exe
├── include/          # C заголовки
├── lib/              # Встановлені пакети
│   └── python3.13/
│       └── site-packages/
└── pyvenv.cfg        # Конфігураційний файл
```

## Активація середовища

### Linux / macOS

```bash
source my_env/bin/activate
```

### Windows (Command Prompt)

```cmd
my_env\Scripts\activate.bat
```

### Windows (PowerShell)

```powershell
my_env\Scripts\Activate.ps1
```

!!! note "Примітка"
    Після активації у командному рядку з'явиться префікс `(my_env)`, який вказує на активне середовище.

## Робота з пакетами

### Встановлення пакетів

```bash
# Активуйте середовище
source my_env/bin/activate

# Встановіть пакет
pip install requests

# Встановіть кілька пакетів
pip install Flask jikanpy-v4 requests

# Встановіть конкретну версію
pip install Flask==3.1.3
```

### Перегляд встановлених пакетів

```bash
# Список усіх пакетів
pip list

# Детальна інформація про пакет
pip show Flask

# Дерево залежностей (потрібен pipdeptree)
pip install pipdeptree
pipdeptree
```

### Видалення пакетів

```bash
pip uninstall requests

# Видалення без підтвердження
pip uninstall -y requests
```

## Управління залежностями

### Створення requirements.txt

```bash
# Експорт усіх встановлених пакетів
pip freeze > requirements.txt

# Вміст файлу буде виглядати так:
# Flask==3.1.3
# jikanpy-v4==1.0.2
# requests==2.32.5
# ...
```

### Встановлення з requirements.txt

```bash
# Встановлення всіх залежностей
pip install -r requirements.txt

# Встановлення з оновленням
pip install -r requirements.txt --upgrade
```

### Розділення залежностей

Часто створюють окремі файли для різних оточень:

**requirements.txt** (продакшн залежності):
```txt
Flask==3.1.3
jikanpy-v4==1.0.2
requests==2.32.5
```

**requirements-dev.txt** (залежності для розробки):
```txt
-r requirements.txt
flake8==7.3.0
mypy==1.19.1
pytest==8.0.0
```

Встановлення:
```bash
# Тільки продакшн
pip install -r requirements.txt

# З dev-залежностями
pip install -r requirements-dev.txt
```

## Деактивація середовища

```bash
deactivate
```

Після деактивації префікс `(my_env)` зникне з командного рядка.

## Видалення віртуального середовища

Віртуальне середовище - це просто директорія, тому:

```bash
# Linux/macOS
rm -rf my_env

# Windows
rmdir /s my_env
```

## Практичний приклад: Проект Anime API

### Крок 1: Створення середовища

```bash
cd 6_lab/1_venv
python -m venv my_env
```

### Крок 2: Активація

```bash
source my_env/bin/activate  # Linux/macOS
```

### Крок 3: Встановлення залежностей

```bash
# Встановлення продакшн залежностей
pip install -r requirements.txt

# Встановлення dev-залежностей
pip install -r requirements-dev.txt
```

### Крок 4: Перевірка

```bash
pip list
```

Вивід:
```
Package              Version
-------------------- -------
Flask                3.1.3
jikanpy-v4           1.0.2
requests             2.32.5
flake8               7.3.0
mypy                 1.19.1
...
```

### Крок 5: Запуск проекту

```bash
python anime.py
```

### Крок 6: Перевірка коду

```bash
# Перевірка стилю коду
flake8 anime.py

# Перевірка типів
mypy anime.py
```

### Крок 7: Деактивація

```bash
deactivate
```

## Швидке відтворення середовища

Коли потрібно створити середовище заново:

```bash
# Одна команда для створення, активації та встановлення
python -m venv my_env && \
source my_env/bin/activate && \
pip install -r requirements.txt
```

## Поширені проблеми

### Проблема 1: venv не встановлено

**Симптом:**
```bash
The virtual environment was not created successfully because ensurepip is not available.
```

**Рішення (Ubuntu/Debian):**
```bash
sudo apt install python3-venv
```

### Проблема 2: PowerShell блокує виконання скриптів

**Симптом:**
```
Activate.ps1 cannot be loaded because running scripts is disabled
```

**Рішення:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Проблема 3: Старий pip

**Симптом:**
```
WARNING: You are using pip version X.X.X; however, version Y.Y.Y is available.
```

**Рішення:**
```bash
pip install --upgrade pip
```

## Корисні команди

```bash
# Перевірка версії Python у середовищі
python --version

# Шлях до Python інтерпретатора
which python  # Linux/macOS
where python  # Windows

# Перевірка, чи активовано середовище
echo $VIRTUAL_ENV  # Linux/macOS
echo %VIRTUAL_ENV%  # Windows

# Очищення кешу pip
pip cache purge
```

## Переваги та недоліки

### ✅ Переваги

- Входить у стандартну поставку Python
- Простий у використанні
- Швидке створення середовища
- Підтримується усіма інструментами

### ❌ Недоліки

- Немає автоматичного керування залежностями
- Відсутність lock-файлів
- Ручне керування requirements.txt
- Не підходить для складних проектів

## Наступні кроки

- Спробуйте більш сучасні інструменти: [Pipenv →](pipenv.md)
- Або перейдіть до [Poetry →](poetry.md)
- Дізнайтеся більше про [проект Anime API →](anime_project.md)
