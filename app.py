from flask import Flask, request, jsonify
from telethon import TelegramClient, events
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# API ID и API HASH
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# Создание клиента
client = TelegramClient('session', api_id, api_hash)

# Функция для авторизации по QR-коду
@client.on(events.NewMessage)
async def handle_new_message(event):
    if event.text == '/start':
        await client.send_message(event.chat_id, 'Welcome to the Telegram client!')

# Функция для отправки текстовых сообщений
@client.on(events.NewMessage)
async def handle_new_message(event):
    if event.text.startswith('/send'):
        text = event.text[6:]
        chat_id = event.chat_id
        await client.send_message(chat_id, text)

# Функция для получения новых текстовых сообщений
@client.on(events.NewMessage)
async def handle_new_message(event):
    if event.text.startswith('/get'):
        chat_id = event.chat_id
        messages = await client.get_messages(chat_id)
        await client.send_message(chat_id, str(messages))

# Запуск клиента
client.start()

# API для авторизации
@app.route('/auth', methods=['POST'])
def auth():
    code = request.json['code']
    client.start()
    client.connect()
    client.send_code_request(code)
    return jsonify({'status': 'success'})

# API для отправки текстовых сообщений
@app.route('/send', methods=['POST'])
def send_message():
    text = request.json['text']
    chat_id = request.json['chat_id']
    client.send_message(chat_id, text)
    return jsonify({'status': 'success'})

# API для получения новых текстовых сообщений
@app.route('/get', methods=['GET'])
def get_messages():
    chat_id = request.json['chat_id']
    messages = client.get_messages(chat_id)
    return jsonify({'messages': messages})

# API для запуска парсинга Wildberries
@app.route('/wild', methods=['POST'])
def wild():
    city = 'Москва'
    query = 'любой товар'
    # Запустите парсинг Wildberries
    # ...
    return jsonify({'status': 'success'})

# Запуск веб-интерфейса
if __name__ == '__main__':
    app.run(debug=True)
