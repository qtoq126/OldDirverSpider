# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IdeapocketItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    year = scrapy.Field()
    date = scrapy.Field()
    cover = scrapy.Field()
    code = scrapy.Field()
    previews_pics = scrapy.Field()
    previews_video = scrapy.Field()
    actress = scrapy.Field()