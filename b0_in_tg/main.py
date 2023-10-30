import requests
import json


def parsed_response(url_message, files={}):
    try:
        response = requests.post(url_message, files=files)
        return json.loads(response.text)
    except Exception as e:
        print(e)


def send_message(api_url, chat_id, message):
    url_message = f"{api_url}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=html"
    return parsed_response(url_message)


def send_photo_from_file(api_url, chat_id, image, caption):
    url_message = f"{api_url}/sendPhoto?chat_id={chat_id}&caption={caption}&parse_mode=html"
    files = {'photo': image}
    return parsed_response(url_message, files)





def parsed_response2(url_message):
    try:
        response = requests.post(url_message)
        return json.loads(response.text)
    except Exception as e:
        print(e)

def send_message2(api_url, chat_id, message, next_time):
    url_message = f"{api_url}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=html&schedule_date={next_time}"
    return parsed_response2(url_message=url_message)