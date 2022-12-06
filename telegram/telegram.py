import requests
from constants import SEND_URL
from credentials import CHAT_ID
from constants import DEFAULT_MESSAGE

class Telegram():
    def __init__(self):
        print()
    
    def send_telegram_msg(self, message):
        print("Enviando mensaje de Telegram...")
        try:
            requests.post(SEND_URL, json={
                      'chat_id': CHAT_ID, 'text': f"{message}"})
            print("Mensaje enviado...")
        except:
            print("Hubo un error enviando el mensaje")
