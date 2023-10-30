from datetime import datetime, timedelta
from b0_in_tg.main import send_message2
from pyrogram import Client, types, raw

# app = Client(name=name_uset_admin, api_id=api_id, api_hash=api_hash)
# app.send_message()

project = 'a0_proba'
tg_url = 'https://t.me/nfxjdnfxlhxfithjpij'
api_token = '6659447899:AAEe8JjANEGzeZ2TKsRkteM8Bx-TI2vhLlA'
api_chat_id = '-1001802264924'
api_url = f"https://api.telegram.org/bot{api_token}"

next_time = datetime.now() + timedelta(hours=3, minutes=40)
print(next_time)
date = datetime(year=2023, month=10, day=18, hour=00, minute=9)
print(date)
response = send_message2(api_url=api_url, chat_id=api_chat_id, message='@@@222message', next_time=date)
print(response)