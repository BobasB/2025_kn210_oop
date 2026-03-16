from flask import Flask, render_template, jsonify
from jikanpy import Jikan
import sqlite3
from datetime import datetime

jikan = Jikan()
app = Flask(__name__)
DB_NAME = 'anime.db'


# Функції для роботи з базою даних
def init_db():
    """Ініціалізація бази даних та створення таблиць"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Таблиця для аніме
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS anime (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            type TEXT,
            episodes INTEGER,
            score REAL,
            status TEXT,
            added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Таблиця для епізодів
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS episodes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            anime_id INTEGER,
            mal_id INTEGER,
            title TEXT,
            score REAL,
            aired DATE,
            FOREIGN KEY (anime_id) REFERENCES anime(id)
        )
    ''')
    
    # Таблиця для персонажів
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            name_kanji TEXT,
            about TEXT,
            favorites INTEGER,
            added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("База даних ініціалізована")


def save_anime_to_db(anime_id):
    """Збереження інформації про аніме в базу даних"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        # Отримуємо дані з API
        anime_data = jikan.anime(anime_id)['data']
        
        # Зберігаємо основну інформацію про аніме
        cursor.execute('''
            INSERT OR REPLACE INTO anime 
            (id, title, type, episodes, score, status)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            anime_data['mal_id'],
            anime_data['title'],
            anime_data.get('type'),
            anime_data.get('episodes'),
            anime_data.get('score'),
            anime_data.get('status')
        ))
        
        # Отримуємо епізоди
        episodes_data = jikan.anime(anime_id, extension='episodes')
        
        # Видаляємо старі епізоди для цього аніме
        cursor.execute('DELETE FROM episodes WHERE anime_id = ?', (anime_id,))
        
        # Зберігаємо епізоди
        for episode in episodes_data["data"]:
            cursor.execute('''
                INSERT INTO episodes 
                (anime_id, mal_id, title, score, aired)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                anime_id,
                episode.get('mal_id'),
                episode.get('title'),
                episode.get('score'),
                episode.get('aired')
            ))
        
        conn.commit()
        print(f"Аніме {anime_data['title']} збережено в базу даних")
        return True
    except Exception as e:
        print(f"Помилка збереження в БД: {e}")
        return False
    finally:
        conn.close()


def save_character_to_db(character_id):
    """Збереження інформації про персонажа в базу даних"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        char_data = jikan.characters(character_id)['data']
        
        cursor.execute('''
            INSERT OR REPLACE INTO characters 
            (id, name, name_kanji, about, favorites)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            char_data['mal_id'],
            char_data['name'],
            char_data.get('name_kanji'),
            char_data.get('about'),
            char_data.get('favorites')
        ))
        
        conn.commit()
        print(f"Персонаж {char_data['name']} збережено в базу даних")
        return True
    except Exception as e:
        print(f"Помилка збереження персонажа: {e}")
        return False
    finally:
        conn.close()


def get_anime_from_db(anime_id):
    """Отримання інформації про аніме з бази даних"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM anime WHERE id = ?', (anime_id,))
    anime = cursor.fetchone()
    
    if anime:
        cursor.execute('SELECT * FROM episodes WHERE anime_id = ?', (anime_id,))
        episodes = cursor.fetchall()
        conn.close()
        return {'anime': anime, 'episodes': episodes}
    
    conn.close()
    return None


def get_all_anime_from_db():
    """Отримання списку всіх аніме з бази даних"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM anime ORDER BY added_date DESC')
    anime_list = cursor.fetchall()
    
    conn.close()
    return anime_list


def get_character_from_db(character_id):
    """Отримання інформації про персонажа з бази даних"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM characters WHERE id = ?', (character_id,))
    character = cursor.fetchone()
    
    conn.close()
    return character


# Маршрути Flask
@app.route('/')
def home():
    """Головна сторінка - показує епізоди з бази даних"""
    anime_id = 57658
    data = get_anime_from_db(anime_id)
    
    if not data:
        # Якщо даних немає в БД, завантажуємо з API
        save_anime_to_db(anime_id)
        data = get_anime_from_db(anime_id)
    
    html = "<h1>Епізоди з бази даних</h1>"
    if data and data['episodes']:
        for episode in data['episodes']:
            html += f"<p>Епізод {episode[2]} з назвою: {episode[3]} має оцінку {episode[4]}</p>"
    else:
        html += "<p>Немає даних</p>"
    
    return html


@app.route('/about')
def about():
    """Сторінка про персонажа"""
    character_id = 164470
    character = get_character_from_db(character_id)
    
    if not character:
        # Якщо даних немає в БД, завантажуємо з API
        save_character_to_db(character_id)
        character = get_character_from_db(character_id)
    
    if character:
        return f"""
        <h1>{character[1]}</h1>
        <p><strong>Японське ім'я:</strong> {character[2]}</p>
        <p><strong>Улюблене:</strong> {character[4]} разів</p>
        <p><strong>Про персонажа:</strong> {character[3][:500] if character[3] else 'Немає опису'}...</p>
        """
    return "<p>Персонаж не знайдено</p>"


@app.route('/anime/list')
def anime_list():
    """Список всіх аніме в базі даних"""
    anime_list = get_all_anime_from_db()
    
    html = "<h1>Список аніме в базі даних</h1>"
    for anime in anime_list:
        html += f"""
        <div style='border:1px solid #ccc; margin:10px; padding:10px;'>
            <h3>{anime[1]}</h3>
            <p>Тип: {anime[2]} | Епізоди: {anime[3]} | Оцінка: {anime[4]} | Статус: {anime[5]}</p>
            <p>Додано: {anime[6]}</p>
        </div>
        """
    
    return html if anime_list else "<p>База даних порожня</p>"


@app.route('/anime/add/<int:anime_id>')
def add_anime(anime_id):
    """Додавання нового аніме в базу даних"""
    if save_anime_to_db(anime_id):
        return f"<p>Аніме {anime_id} успішно додано в базу даних! <a href='/anime/list'>Переглянути список</a></p>"
    return "<p>Помилка додавання аніме</p>"


@app.route('/character/add/<int:character_id>')
def add_character(character_id):
    """Додавання нового персонажа в базу даних"""
    if save_character_to_db(character_id):
        return f"<p>Персонаж {character_id} успішно додано в базу даних!</p>"
    return "<p>Помилка додавання персонажа</p>"


if __name__ == '__main__':
    # Ініціалізуємо базу даних при запуску
    init_db()
    app.run(debug=True)
