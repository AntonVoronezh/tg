from datetime import datetime

import schedule
import time

def fff():
    print(5555)

def fff2():
    print(4444)


def job():
    print("Работаю")
    # schedule.every(10).minutes.do(fff)
    # schedule.every().hour.do(job)
    # schedule.every().day.at("10:30").do(job)
    # schedule.every(5).to(10).minutes.do(job)
    # schedule.every().monday.do(job)
    # schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)
# schedule.every().minute.at(":37").do(fff2)
    # нужно иметь свой цикл для запуска планировщика с периодом в 1 секунду:
while True:
    schedule.run_pending()
    print( datetime.now())

    time.sleep(1)



