import os
import time

import schedule

from b2_variant_message.message_text_bez_title_i_img.main import message_text_bez_title_i_img
from b2_variant_message.message_img_s_title_i_text.main import message_img_s_title_i_text

project = 'a1_doctor_psyh'
tg_url = 'https://t.me/doctor_psyh'
api_token = '6324718682:AAGPn4xYfKuVo33W1V2Jl93YWnUSUpev_Sk'
api_chat_id = '-1001698544953'
api_url = f"https://api.telegram.org/bot{api_token}"
sign = f'<a href="{tg_url}">👉 Я есть Фрейд! Подписаться</a>'
is_remove = True

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
    # schedule.every().day.at("8:05").do(main)
    # schedule.every().day.at("9:05").do(main)
    # schedule.every().day.at("12:05").do(main)
    # schedule.every().day.at("15:05").do(main)
    # schedule.every().day.at("19:05").do(main)
    # schedule.every().day.at("20:05").do(main)
    schedule.every().day.at("12:05").do(send_message_img_s_title_i_text)
    # schedule.every().day.at("15:05").do(send_message_text_bez_title_i_img)
    schedule.every().day.at("15:05").do(send_message_img_s_title_i_text)
    schedule.every().day.at("19:05").do(send_message_img_s_title_i_text)
    schedule.every().day.at("20:05").do(send_message_img_s_title_i_text)

    while True:
        schedule.run_pending()
        # print(datetime.now())
        time.sleep(1)