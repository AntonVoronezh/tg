import os
import time
from datetime import datetime

import schedule

from b2_variant_message.message_text_bez_title_i_img.main import message_text_bez_title_i_img
from b2_variant_message.message_img_s_title_i_text.main import message_img_s_title_i_text

project = 'a0_proba'
tg_url = 'https://t.me/nfxjdnfxlhxfithjpij'
api_token = '6659447899:AAEe8JjANEGzeZ2TKsRkteM8Bx-TI2vhLlA'
api_chat_id = '-1001802264924'
api_url = f"https://api.telegram.org/bot{api_token}"
sign = f'<a href="{tg_url}">👉 Я есть Фрейд! Подписаться</a>'
is_remove = False

realpath = os.path.dirname(os.path.realpath(__file__))
realpath_replaced = realpath.replace(project, '')


def send_message_text_bez_title_i_img():
    print(f'🔴 {project}')
    message_text_bez_title_i_img(
        api_url=api_url,
        api_chat_id=api_chat_id,
        real_path=realpath_replaced,
        folder_name=project,
        sign=sign,
        is_remove=is_remove,
        emoji={'start': '💬', 'end': '👆'},
    )


def send_message_img_s_title_i_text():
    print(f'🔴 {project}')
    message_img_s_title_i_text(
        api_url=api_url,
        api_chat_id=api_chat_id,
        real_path=realpath_replaced,
        folder_name=project,
        sign=sign,
        is_remove=is_remove,
    )


def start():
    # schedule.every().minute.at(":07").do(send_message_text_bez_title_i_img)
    # schedule.every().minute.at(":37").do(send_message_img_s_title_i_text)

    schedule.every().second.do(send_message_text_bez_title_i_img)



    while True:
        schedule.run_pending()
        # print(datetime.now())
        time.sleep(1)
