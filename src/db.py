import sqlite3
import os


def create_db():
    """Создает базу данных и таблицу для приложений."""
    conn = sqlite3.connect('applications.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            path TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()


def save_applications(applications):
    """Сохраняет список приложений в базу данных."""
    conn = sqlite3.connect('applications.db')
    cursor = conn.cursor()

    for app in applications:
        cursor.execute('''
            INSERT OR IGNORE INTO applications (name, path) VALUES (?, ?)
        ''', (app['name'], app['path']))

    conn.commit()
    conn.close()


def get_applications():
    """Возвращает список приложений из базы данных."""
    conn = sqlite3.connect('applications.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM applications')
    apps = cursor.fetchall()
    conn.close()
    return apps
