#scrapy crawl stack
from scrapy import Spider
from scrapy.selector import Selector
from stack.pagedetails import PageDetails
import scrapy
import logging

class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["bctr.org/"]
    start_urls = [
        "https://bctr.org/haberler/",
    ]

    def parse(self, response):
        news = Selector(response).xpath('//*[@id="td-outer-wrap"]/div[2]/div/div[2]/div[1]/div')
        logging.debug(news)
        logging.debug("NEWS********************")

        for new in news:
            absolute_url = new.xpath(
                'div[@clas="td_module_16 td_module_wrap td-animation-stack"]/div/a/@href').extract()[0]
            logging.debug(absolute_url)
            logging.debug("URL********************")
            yield scrapy.Request(absolute_url,callback=self.parse_attr)


    def parse_attr(self, response):
        logging.debug("IMHERE")
        pageDetail = PageDetails()
        pageDetail['title'] = response.xpath(
            '//h1[@class="entry_title"]/text()').extract()[0]
        logging.debug("ANDALSOIMHERE")
        """pageDetail['summary'] = response.xpath(
            '//h2[@class="mt10 haber_ozet"]/text()').extract()[0]
        pageDetail['fullText'] = response.xpath(
            '//div[@class = "wrapper detay-v3_3 haber_metni"]').extract()[0]"""
        logging.debug(pageDetail['title'])
        #logging.debug(pageDetail['summary'])
        #logging.debug(pageDetail['fullText'])
