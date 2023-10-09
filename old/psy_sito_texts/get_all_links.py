from bs4 import BeautifulSoup
import fake_useragent
import requests
import time

url = 'https://neurosciencenews.com/neuroscience-topics/psychology/page/'
arr = []
arr_img = []
# for i in range(1, 5):
for i in range(1, 575):
    next_url = f'{url}{i}/'
    ua = fake_useragent.UserAgent()
    fake_ua = {'user-agent': ua.random}
    response = requests.get(url=next_url, headers=fake_ua)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    div = soup.find('div', class_='tipi-row content-bg block-300 clearfix')
    div2 = div.find_all('div', class_='mask')
    # print(div2)

    for txt in div2:
        link = txt.find("a")
        img = txt.find("img")
        # print(img.get("srcset"))
        if link:
            # print(link.get("href"))
            arr.append(link.get("href"))
            arr_img.append(f'{img.get("src")}***{link.get("href")}')

    arr_set = list(set(arr))
    arr_img_set = list(set(arr_img))



for i in arr_img_set:
    print(i)

# for i in arr_set:
#     print(i)
#
# print(len(arr))
# print(len(arr_set))