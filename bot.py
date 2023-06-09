#!/usr/bin/env python3

import requests
from dotenv import load_dotenv
import os

# Загрузить переменные из файла .env в текущее окружение
load_dotenv()

API_link = "https://api.telegram.org/bot" + os.getenv('token')

updates = requests.get(API_link + "/getUpdates?offset=-1").json()

print(updates)

message = updates["result"][0]["message"]

chat_id = message["from"]["id"]
text = message["text"]

print(chat_id)
print(text)
sent_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text=Привет,ты написал:  \" {text}\"")
