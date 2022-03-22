# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from lxml import etree


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }

    proxies = {'http': 'http://127.0.0.1:8001'}

    # Press the green button in the gutter to run the script.
    if __name__ == '__main__':
        url = 'https://ideapocket.com/works/list/date/2022-04-12'
        page = requests.get(url=url, headers=headers, proxies=proxies).text
        tree = etree.HTML(page)
        li_list = tree.xpath('.//div[@class="swiper-slide c-low--6"]/div')
        for li in li_list :
            cover = li.xpath('.//img[@class="c-main-bg lazyload"]/@data-src')
            video_url = li.xpath('.//a[@class="img hover"]/@href')
            print(cover)
            print(video_url)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
