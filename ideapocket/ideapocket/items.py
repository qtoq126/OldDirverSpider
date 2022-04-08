# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class WorkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field()
    producer = scrapy.Field()
    actress = scrapy.Field()
    year = scrapy.Field()
    date = scrapy.Field()
    cover = scrapy.Field()
    pre_pics = scrapy.Field()
    pre_video = scrapy.Field()

class ActressItem(scrapy.Item):
    name = scrapy.Field()
    birthday = scrapy.Field()
    height = scrapy.Field()
    bwh = scrapy.Field()
    birthplace = scrapy.Field()
    hobby = scrapy.Field()
    specialty = scrapy.Field()
