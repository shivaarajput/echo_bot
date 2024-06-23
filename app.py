from flask import Flask, request, render_template
import requests

TOKEN = '5815143397:AAFLbtbPRKGqVngTbDmw-4ZfXqqeOBPIUM8'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TOKEN}/'

app = Flask(__name__)

def send_message(chat_id, text):
    url = TELEGRAM_API_URL + 'sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url, json=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.json

    if 'message' in update:
        chat_id = update['message']['chat']['id']
        text = update['message']['text']
        send_message(chat_id, text)

    return 'OK'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000)
