import scrapy


class PbSpider(scrapy.Spider):
    name = 'pb'
    allowed_domains = ['pb.com']
    start_urls = ['http://pb.com/']

    def parse(self, response):
        pass
