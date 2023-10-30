import os
import time
from datetime import datetime

import schedule

from b1_helpers.main import check_folders_main

from a0_proba.main import start as a0_proba_start
from a1_doctor_psyh.main import start as a1_doctor_psyh_start

is_develop = True


def main():
    realpath = os.path.dirname(os.path.realpath(__file__))

    if is_develop:
        projects = ['a0_proba']
    else:
        folder_list = os.listdir(realpath)
        projects = list(filter(check_folders_main, folder_list))

    if len(projects) == 0:
        print(f'🔴 нет проектов')
        return

    else:
        for project in projects:
            if project == 'a0_proba':
                a0_proba_start()
            if project == 'a1_doctor_psyh':
                a1_doctor_psyh_start()



print('start')
main()
# post_timer(main)
# schedule.every().day.at("8:05").do(main)
# schedule.every().day.at("9:05").do(main)
# schedule.every().day.at("12:05").do(main)
# schedule.every().day.at("15:05").do(main)
# schedule.every().day.at("19:05").do(main)
# schedule.every().day.at("20:05").do(main)

# schedule.every().minute.at(":37").do(a0_proba_message_text_bez_title_i_img)
#
# while True:
#     schedule.run_pending()
#     print(datetime.now())
#     time.sleep(1)
