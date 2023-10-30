import asyncio
import os
import time

from colorama import Fore
from pyrogram import Client
from datetime import datetime, date

from b1_helpers.main import get_random_elem_name_from_folder, get_file_from_folder_by_name, get_json_field, \
    make_caption, make_morality, make_image, remove_folder

# https://docs.pyrogram.org/start/
# https://t.me/m0nte_cristo  @m0nte_cristo
# +7 950 764 7534
api_id = 29906022
api_hash = "a1c7f78ea0a19a662fe531f00a4e5ff2"
bot_token = "6659447899:AAEe8JjANEGzeZ2TKsRkteM8Bx-TI2vhLlA"
app = Client("my_account")
tg_url = 'https://t.me/nfxjdnfxlhxfithjpij'


time_arr = []
for el in range(26, 27):
    t_1 = datetime(2023, 10, el, 8, 10)
    time_arr.append(t_1)
    t_2 = datetime(2023, 10, el, 12, 10)
    time_arr.append(t_2)
    t_3 = datetime(2023, 10, el, 16, 10)
    time_arr.append(t_3)
    t_4 = datetime(2023, 10, el, 20, 10)
    time_arr.append(t_4)

for el in time_arr:
    realpath = os.path.dirname(os.path.realpath(__file__))
    variants_folder_path = os.path.join(realpath, 'variants')
    random_elem_name = get_random_elem_name_from_folder(folder_path=variants_folder_path)
    variants_folder_path_img = os.path.join(variants_folder_path, random_elem_name)

    if random_elem_name is None:
        print(Fore.LIGHTRED_EX + f'закончились данные' + Fore.BLUE)
        break
    else:
        print(el)
        random_folder_path = os.path.join(variants_folder_path, random_elem_name)
        random_elem_file_json_title = get_file_from_folder_by_name(folder_path=random_folder_path,
                                                                   file_name='text.json')
        random_elem_file_json_description = get_file_from_folder_by_name(folder_path=random_folder_path,
                                                                         file_name='text.json')
        random_elem_file_morality = get_file_from_folder_by_name(folder_path=random_folder_path, file_name='text.json')

        title_from_file = get_json_field(json_data=random_elem_file_json_title, field_name='title')
        description_from_file = get_json_field(json_data=random_elem_file_json_description, field_name='description')
        morality_from_file = get_json_field(json_data=random_elem_file_morality, field_name='morality')

        description = make_caption(data=description_from_file)
        morality = make_morality(data=morality_from_file)

        caption = f'<b>{title_from_file}</b> \n\n {description} \n\n {morality} \n\n <a href="{tg_url}">👉 Я есть Фрейд! Подписаться</a>'

        random_elem_file_json_title.close()
        random_elem_file_json_description.close()
        random_elem_file_morality.close()

        image = make_image(variants_folder_path_img)

        if len(caption) > 1024:
            caption = f'<b>{title_from_file}</b> \n\n {description}  \n\n <a href="{tg_url}">👉 Я есть Фрейд! Подписаться</a>'

            if len(caption) > 1024:
                caption = f'{description}  \n\n <a href="{tg_url}">👉 Я есть Фрейд! Подписаться</a>'

                if len(caption) > 1024:
                    print(f'у номера {random_elem_name} более 1024')
                    continue


        if caption and image:
            print('ok')
            # with app:
            #     app.send_photo(chat_id="@nfxjdnfxlhxfithjpij", photo=image, caption=caption, schedule_date=el)

            image.close()
            # remove_folder(folder_path=variants_folder_path_img)

    time.sleep(1)
# for el in time_arr:
#
#     with app:
#         # app.send_message("@nfxjdnfxlhxfithjpij", text="Hi77555555555!", schedule_date=el)
#         app.send_photo(chat_id="@nfxjdnfxlhxfithjpij", photo="", text="Hi77555555555!", schedule_date=el)
#
#     print(el)
#     time.sleep(1)






