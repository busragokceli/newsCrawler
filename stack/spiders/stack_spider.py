from scrapy import Spider
from scrapy.selector import Selector
from stack.pagedetails import PageDetails
import scrapy
import logging

class StackSpider(Spider):
    name = "stack_name"
    allowed_domains = ["www.sondakika.com"]
    start_urls = [
        "http://www.sondakika.com/kripto/",
    ]
    BASE_URL = 'https://www.sondakika.com'

    def parse(self, response):
        news = Selector(response).xpath('//div[@class="content-container category-page mt20"]/main/ul[@class="news-list"]/li')
        for new in news:
            absolute_url = self.BASE_URL + new.xpath(
                'a[@class="content"]/@href').extract()[0]
            yield scrapy.Request(absolute_url,callback=self.parse_attr)

    def parse_attr(self, response):
        pageDetail = PageDetails()
        pageDetail['title'] = response.xpath(
            '//h1[@class="haber_baslik"]/text()').extract()[0]
        pageDetail['summary'] = response.xpath(
            '//h2[@class="mt10 haber_ozet"]/text()').extract()[0]
        pageDetail['fullText'] = response.xpath(
            '//div[@class = "wrapper detay-v3_3 haber_metni"]').extract()[0]
        #logging.debug(pageDetail['title'])
        #logging.debug(pageDetail['summary'])
        logging.debug(pageDetail['fullText'])

























