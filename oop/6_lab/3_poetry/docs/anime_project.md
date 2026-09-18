# Проект Anime API

## Огляд проекту

**Anime API** - це веб-додаток на Flask, який інтегрується з MyAnimeList через Jikan API для отримання інформації про аніме та персонажів, зберігає дані у локальній SQLite базі даних та надає веб-інтерфейс для перегляду.

## Технології

### Backend
- **Flask 3.1.3** - веб-фреймворк для Python
- **SQLite3** - вбудована реляційна база даних
- **Jikanpy-v4 1.0.2** - Python обгортка для Jikan API

### API
- **Jikan API** - неофіційний RESTful API для MyAnimeList
- **MyAnimeList** - найбільша база даних аніме та манги

### Dev Tools
- **Flake8 7.3.0** - перевірка стилю коду (PEP 8)
- **Mypy 1.19.1** - статична перевірка типів

## Архітектура проекту

```
anime.py
├── Database Layer (SQLite)
│   ├── init_db() - створення таблиць
│   ├── save_anime_to_db() - збереження аніме
│   ├── save_character_to_db() - збереження персонажів
│   ├── get_anime_from_db() - отримання аніме
│   ├── get_all_anime_from_db() - список аніме
│   └── get_character_from_db() - отримання персонажа
│
├── API Layer (Jikan)
│   └── jikan = Jikan() - клієнт API
│
└── Web Layer (Flask)
    ├── / - головна сторінка
    ├── /about - інформація про персонажа
    ├── /anime/list - список аніме
    ├── /anime/add/<id> - додавання аніме
    └── /character/add/<id> - додавання персонажа
```

## Структура бази даних

### Таблиця `anime`

```sql
CREATE TABLE anime (
    id INTEGER PRIMARY KEY,              -- MAL ID аніме
    title TEXT NOT NULL,                 -- Назва
    type TEXT,                           -- Тип (TV, Movie, OVA)
    episodes INTEGER,                    -- Кількість епізодів
    score REAL,                          -- Рейтинг (0-10)
    status TEXT,                         -- Статус (Airing, Finished)
    added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Таблиця `episodes`

```sql
CREATE TABLE episodes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    anime_id INTEGER,                    -- Зовнішній ключ
    mal_id INTEGER,                      -- MAL ID епізоду
    title TEXT,                          -- Назва епізоду
    score REAL,                          -- Рейтинг епізоду
    aired DATE,                          -- Дата виходу
    FOREIGN KEY (anime_id) REFERENCES anime(id)
);
```

### Таблиця `characters`

```sql
CREATE TABLE characters (
    id INTEGER PRIMARY KEY,              -- MAL ID персонажа
    name TEXT NOT NULL,                  -- Ім'я латиницею
    name_kanji TEXT,                     -- Ім'я японською
    about TEXT,                          -- Опис персонажа
    favorites INTEGER,                   -- Кількість улюблених
    added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Основні функції

### 1. Ініціалізація бази даних

```python
def init_db():
    """Створює таблиці при першому запуску"""
```

- Створює файл `anime.db` якщо його немає
- Створює три таблиці: anime, episodes, characters
- Викликається автоматично при запуску програми

### 2. Збереження аніме

```python
def save_anime_to_db(anime_id):
    """Завантажує дані з API та зберігає в БД"""
```

**Процес:**
1. Робить запит до Jikan API: `/anime/{id}`
2. Отримує основну інформацію про аніме
3. Робить запит до `/anime/{id}/episodes`
4. Отримує всі епізоди
5. Зберігає у відповідні таблиці

**Приклад:**
```python
save_anime_to_db(57658)  # Death Note
save_anime_to_db(16498)  # Attack on Titan
```

### 3. Збереження персонажа

```python
def save_character_to_db(character_id):
    """Завантажує інформацію про персонажа та зберігає в БД"""
```

**Процес:**
1. Робить запит до `/characters/{id}`
2. Отримує інформацію про персонажа
3. Зберігає в таблицю characters

**Приклад:**
```python
save_character_to_db(164470)  # L Lawliet (Death Note)
```

### 4. Отримання даних з БД

```python
def get_anime_from_db(anime_id):
    """Повертає аніме та його епізоди з БД"""

def get_all_anime_from_db():
    """Повертає список усіх аніме в БД"""

def get_character_from_db(character_id):
    """Повертає персонажа з БД"""
```

## Flask маршрути

### 1. Головна сторінка `/`

**Функціонал:**
- Показує епізоди аніме з ID 57658 (Death Note)
- Якщо даних немає в БД, завантажує з API
- Виводить список епізодів з назвами та оцінками

**Приклад виводу:**
```
Епізоди з бази даних
Епізод 1 з назвою: Rebirth має оцінку 4.5
Епізод 2 з назвою: Confrontation має оцінку 4.6
...
```

### 2. Сторінка про персонажа `/about`

**Функціонал:**
- Показує інформацію про персонажа з ID 164470 (L Lawliet)
- Завантажує з API якщо немає в БД
- Виводить ім'я, японське ім'я, статистику улюблених, опис

**Приклад виводу:**
```
L Lawliet
Японське ім'я: エル・ローライト
Улюблене: 50000 разів
Про персонажа: [перші 500 символів опису]...
```

### 3. Список аніме `/anime/list`

**Функціонал:**
- Показує всі аніме в базі даних
- Сортує за датою додавання (новіші спершу)
- Для кожного аніме виводить: назву, тип, кількість епізодів, оцінку, статус

### 4. Додавання аніме `/anime/add/<id>`

**Параметри:**
- `id` - MAL ID аніме

**Приклади:**
- `/anime/add/1` - Cowboy Bebop
- `/anime/add/5114` - Fullmetal Alchemist: Brotherhood
- `/anime/add/11061` - Hunter x Hunter

**Процес:**
1. Завантажує дані з Jikan API
2. Зберігає в базу даних
3. Перенаправляє на список аніме

### 5. Додавання персонажа `/character/add/<id>`

**Параметри:**
- `id` - MAL ID персонажа

**Приклади:**
- `/character/add/40` - Spike Spiegel
- `/character/add/11` - Edward Elric
- `/character/add/17` - Light Yagami

## Jikan API

### Що таке Jikan?

**Jikan** - це неофіційний безкоштовний RESTful API для MyAnimeList. Він надає доступ до величезної бази даних аніме, манги, персонажів без необхідності офіційного API ключа.

### Основні ендпоінти

```python
# Інформація про аніме
jikan.anime(57658)

# Епізоди аніме
jikan.anime(57658, extension='episodes')

# Персонажі аніме
jikan.anime(57658, extension='characters')

# Інформація про персонажа
jikan.characters(164470)
```

### Структура відповіді

**Anime:**
```json
{
    "data": {
        "mal_id": 57658,
        "title": "Death Note",
        "type": "TV",
        "episodes": 37,
        "score": 8.62,
        "status": "Finished Airing",
        "synopsis": "...",
        "genres": [...]
    }
}
```

**Episodes:**
```json
{
    "data": [
        {
            "mal_id": 1,
            "title": "Rebirth",
            "score": 4.5,
            "aired": "2006-10-04",
            "filler": false
        }
    ]
}
```

### Rate Limiting

⚠️ **Важливо:** Jikan API має обмеження:
- **3 запити в секунду**
- **60 запитів в хвилину**

Тому в продакшні варто додати кешування та rate limiting.

## Запуск проекту

### 1. З venv

```bash
cd 6_lab/1_venv
python -m venv my_env
source my_env/bin/activate
pip install -r requirements.txt
python anime.py
```

### 2. З Pipenv

```bash
cd 6_lab/2_pipenv
pipenv install
pipenv run python anime.py
```

### 3. З Poetry

```bash
cd 6_lab/3_poetry
poetry install
poetry run python anime.py
```

### Доступ до додатку

```
http://localhost:5000/          - головна сторінка
http://localhost:5000/about     - про персонажа
http://localhost:5000/anime/list - список аніме
```

## Можливості розширення

### 1. Додати веб-інтерфейс

Замість HTML рядків використати шаблони:

```python
from flask import render_template

@app.route('/')
def home():
    data = get_anime_from_db(57658)
    return render_template('home.html', data=data)
```

### 2. Додати пошук

```python
@app.route('/anime/search')
def search_anime():
    query = request.args.get('q')
    results = jikan.search('anime', query)
    return render_template('search.html', results=results)
```

### 3. Додати API ендпоінти

```python
@app.route('/api/anime/<int:anime_id>')
def api_anime(anime_id):
    data = get_anime_from_db(anime_id)
    return jsonify(data)
```

### 4. Додати автентифікацію

```python
from flask_login import LoginManager, login_required

@app.route('/anime/add/<int:anime_id>')
@login_required
def add_anime(anime_id):
    # ...
```

### 5. Додати кешування

```python
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'simple'})

@app.route('/')
@cache.cached(timeout=300)
def home():
    # ...
```

### 6. Додати фоновї завдання

```python
from celery import Celery

@celery.task
def fetch_anime_data(anime_id):
    save_anime_to_db(anime_id)
```

## Перевірка коду

### Flake8 (стиль коду)

```bash
# Перевірка
flake8 anime.py

# З конфігурацією
flake8 anime.py --max-line-length=100

# Ігнорування правил
flake8 anime.py --ignore=E501,W503
```

### Mypy (типи)

```bash
# Перевірка типів
mypy anime.py

# З суворим режимом
mypy anime.py --strict

# З ігноруванням відсутніх типів
mypy anime.py --ignore-missing-imports
```

## Структура файлів проекту

```
6_lab/
├── 1_venv/
│   ├── anime.py              # Основний код
│   ├── requirements.txt      # Продакшн залежності
│   ├── requirements-dev.txt  # Dev залежності
│   ├── anime.db              # База даних (створюється автоматично)
│   └── my_env/               # Віртуальне середовище
│
├── 2_pipenv/
│   ├── anime.py              # Той самий код
│   ├── Pipfile               # Конфігурація Pipenv
│   └── Pipfile.lock          # Lock файл
│
└── 3_poetry/
    ├── anime.py              # Той самий код
    ├── pyproject.toml        # Конфігурація Poetry
    ├── poetry.lock           # Lock файл
    └── docs/                 # Документація MkDocs
```

## Популярні аніме ID для тестування

| ID | Назва | Тип | Епізодів |
|----|-------|-----|---------|
| 1 | Cowboy Bebop | TV | 26 |
| 5114 | Fullmetal Alchemist: Brotherhood | TV | 64 |
| 16498 | Attack on Titan | TV | 25 |
| 11061 | Hunter x Hunter (2011) | TV | 148 |
| 1535 | Death Note | TV | 37 |
| 9253 | Steins;Gate | TV | 24 |
| 28977 | Gintama° | TV | 51 |

**Приклади:**
```bash
# В браузері
http://localhost:5000/anime/add/5114  # FMA: Brotherhood
http://localhost:5000/anime/add/16498 # Attack on Titan
```

## Популярні персонажі ID

| ID | Ім'я | Аніме |
|----|------|-------|
| 40 | Spike Spiegel | Cowboy Bebop |
| 11 | Edward Elric | FMA |
| 17 | Light Yagami | Death Note |
| 164470 | L Lawliet | Death Note |
| 40 | Spike Spiegel | Cowboy Bebop |

## Troubleshooting

### Помилка: Rate limit exceeded

**Проблема:** Занадто багато запитів до API

**Рішення:**
```python
import time

def save_anime_to_db(anime_id):
    time.sleep(1)  # Затримка між запитами
    # ...
```

### Помилка: Database is locked

**Проблема:** Одночасний доступ до SQLite

**Рішення:**
```python
conn = sqlite3.connect(DB_NAME, timeout=10)
```

### Помилка: Anime not found

**Проблема:** Неіснуючий MAL ID

**Рішення:** Перевіряйте ID на [myanimelist.net](https://myanimelist.net)

## Ресурси

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jikan API Documentation](https://docs.api.jikan.moe/)
- [Jikanpy GitHub](https://github.com/abhinavk99/jikanpy)
- [MyAnimeList](https://myanimelist.net/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

## Наступні кроки

- Вивчіть [інструкції по встановленню →](instructions.md)
- Порівняйте [різні віртуальні середовища →](introduction.md)
- Експериментуйте з різними аніме та персонажами!
