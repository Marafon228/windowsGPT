from g4f.client import Client
from src.commands import open_application, process_command  # Импортируем правильную функцию

def chat_with_ai(user_input):
    client = Client()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
    )

    ai_response = response.choices[0].message.content

    # Проверяем, является ли это ответом на команду
    if "открой" in user_input.lower():  # Проверяем введённое пользователем сообщение
        process_command(ai_response)  # Передаем ответ AI для обработки
    else:
        print(f"AI: {ai_response}")  # Просто выводим ответ AI
