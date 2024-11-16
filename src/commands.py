import subprocess
from src.db import get_applications


def open_application(app_name):
    """Открывает приложение по его имени."""
    applications = get_applications()

    for app in applications:
        # Приводим к нижнему регистру для сравнения
        if app_name.lower() in app[1].lower():  # app[1] - это имя приложения
            subprocess.Popen(app[2])  # app[2] - это путь приложения
            print(f"Открываю приложение: {app[1]}")  # Отладочное сообщение
            return True

    print(f"Приложение '{app_name}' не найдено.")  # Отладочное сообщение
    return False


def process_command(ai_response):
    print(f"AI Response: {ai_response}")  # Отладочное сообщение

    # Проверяем наличие команды на открытие приложения
    if "открой" in ai_response.lower():
        # Извлекаем имя приложения из ответа
        app_name = ai_response.lower().replace("открой", "").strip()
        print(f"Попытка открыть приложение: {app_name}")  # Отладочное сообщение

        if open_application(app_name):
            print(f"AI: Открываю {app_name}.")
        else:
            print(f"AI: Извините, но я не могу открыть {app_name}.")
    else:
        print(f"AI: {ai_response}")  # Вывод обычного ответа
