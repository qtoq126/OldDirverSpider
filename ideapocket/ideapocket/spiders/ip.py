import time
from copy import deepcopy

import scrapy
from ideapocket.items import IdeapocketItem

class IpSpider(scrapy.Spider):
    name = 'ip'
    # allowed_domains = ['ip.com']
    start_urls = ['https://ideapocket.com/works/date']

    def parse(self, response):
        t1 = time.time()

        li_list = response.xpath('//ul[@class="p-accordion"]/li')
        for li in li_list:
            item = IdeapocketItem()
            item['year'] = li.xpath('.//h2[@class="year c-main-font"]/text()').extract_first()
            url_list = li.xpath('.//div[@class="genre -s"]/a')
            for each_url in url_list:
                item['date'] = each_url.xpath('.//p[@class="title"]/text()').extract_first()
                date_detail_url = each_url.xpath('./@href').extract_first()
                if date_detail_url is not None:
                    yield scrapy.Request(
                        url=date_detail_url,
                        callback=self.date_url_parse,
                        meta={'item':deepcopy(item)}
                    )

        t2 = time.time()
        print(t2 - t1)

    def date_url_parse(self, response):
        item = response.meta['item']
        video_list = response.xpath('.//div[@class="swiper-slide c-low--6"]/div')
        for video in video_list:
            item['cover'] = video.xpath('.//img[@class="c-main-bg lazyload"]/@data-src').extract_first()
            video_url = video.xpath('.//a[@class="img hover"]/@href').extract_first()
            item['code'] = video_url.split('/')[-1]
            item['actress'] = video.xpath('.//a[@class="name c-main-font-hover"]/text()').extract_first()

            if video_url is not None:
                yield scrapy.Request(
                    url=video_url,
                    callback=self.video_detail_parse,
                    meta={'item': deepcopy(item)}
                )

    def video_detail_parse(self, response):
        item = response.meta['item']
        div_list = response.xpath('.//div[@class="swiper-wrapper"]/div')
        previews = set()
        for li in div_list:
            previews.add(li.xpath('./img/@data-src').extract_first())
        item['previews_pics'] = previews # 字符串url集合，预览图
        item['previews_video'] = response.xpath('.//div[@class="video"]/video/@src').extract_first()
        yield item











