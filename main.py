# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from lxml import etree
import pymysql


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
        url = 'https://ideapocket.com/actress/detail/72858'
        page = requests.get(url=url, headers=headers, proxies=proxies).text
        tree = etree.HTML(page)
        li_list = tree.xpath('.//div[@class="table"]/div')
        for info in li_list:
            cate = info.xpath('.//p[@class="th"]/text()')[0]
            res = info.xpath('.//p[@class="td"]/text()')[0].split()[0]
            if cate == '誕生日':
                print(res)
            elif cate == '身長':
                print(res)
            else:
                break


        # div_list = tree.xpath('.//div[@class="swiper-wrapper"]/div')
        # previews = set()
        # for li in div_list:
        #     previews.add(li.xpath('./img/@data-src')[0])
        #
        # p_str = ','.join(previews)
        #
        # print(p_str)
        # for li in li_list :
        #     cover = li.xpath('.//img[@class="c-main-bg lazyload"]/@data-src')[0]
        #     video_url = li.xpath('.//a[@class="img hover"]/@href')[0]
        #     number = video_url.split('/')[-1]
        #     print(video_url)
        #     print(number)

        # connect = None
        # connect = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='5201314yes', db='old_driver')
        # print(connect)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
