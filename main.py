import os
from src.commands import open_application, process_command
from src.api_integration import chat_with_ai
from src.db import create_db, save_applications, get_applications


def find_installed_applications():
    """Находит установленные приложения в системе."""
    applications = []
    program_files = [os.environ['ProgramFiles'], os.environ['ProgramFiles(x86)']]

    for path in program_files:
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith('.exe'):  # Ищем исполняемые файлы
                        applications.append({
                            'name': file,
                            'path': os.path.join(root, file)
                        })
    return applications

# После сохранения приложений
saved_apps = get_applications()
print("Сохранённые приложения:")
for app in saved_apps:
    print(app)
def main():
    create_db()  # Создаем базу данных и таблицу
    apps = find_installed_applications()  # Находим установленные приложения
    save_applications(apps)  # Сохраняем их в базу данных

    while True:
        user_input = input("Введите сообщение (или 'выход' для выхода): ")
        if user_input.lower() == "выход":
            break

        # Получаем ответ от AI через g4f
        ai_response = chat_with_ai(user_input)


if __name__ == "__main__":
    main()