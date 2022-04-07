# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import threading

from itemadapter import ItemAdapter
import pymysql

from ideapocket.settings import MYSQL_HOST, MYSQL_USER, MYSQL_PWD


class IdeapocketPipeline:
    def process_item(self, item, spider):
        print(item)
        return item

class MySqlPipeLine(object):
    def __init__(self):
        self.connect = pymysql.Connect(host=MYSQL_HOST, port=3306, user=MYSQL_USER, password=MYSQL_PWD, db='old_driver', charset='utf8')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        sql = 'INSERT INTO old_driver.works VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (0, item['code'], item['producer'], item['actress'], item['year'], item['date'], item['pre_pics'], item['pre_video'], item['cover'])
        try:
            self.cursor.execute(sql, data)
            self.connect.commit()
        except Exception as e:
            print('插入数据失败', e)
            self.connect.rollback()

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()

