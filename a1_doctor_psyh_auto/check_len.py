import os

from a1_doctor_psyh.main import tg_url
from b1_helpers.main import get_file_from_folder_by_name, get_json_field, make_caption, make_morality

folder_list = os.listdir('variants')

realpath = os.path.dirname(os.path.realpath(__file__))
variants_folder_path = os.path.join(realpath, 'variants')


for el in folder_list:
    el_folder_path = os.path.join(variants_folder_path, el)
    random_elem_file_json_title = get_file_from_folder_by_name(folder_path=el_folder_path,
                                                               file_name='text.json')
    random_elem_file_json_description = get_file_from_folder_by_name(folder_path=el_folder_path,
                                                                     file_name='text.json')
    random_elem_file_morality = get_file_from_folder_by_name(folder_path=el_folder_path, file_name='text.json')

    title_from_file = get_json_field(json_data=random_elem_file_json_title, field_name='title')
    description_from_file = get_json_field(json_data=random_elem_file_json_description, field_name='description')
    morality_from_file = get_json_field(json_data=random_elem_file_morality, field_name='morality')

    description = make_caption(data=description_from_file)
    morality = make_morality(data=morality_from_file)

    caption = f'<b>{title_from_file}</b> \n\n {description} \n\n {morality} \n\n <a href="{tg_url}">👉 Я есть Фрейд! Подписаться</a>'

    random_elem_file_json_title.close()
    random_elem_file_json_description.close()
    random_elem_file_morality.close()

    if len(caption) > 1020:
        print(el, len(caption))
        print('----')