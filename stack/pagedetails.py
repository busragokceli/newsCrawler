
from scrapy.item import Item, Field


class PageDetails(Item):
    title = Field()
    summary = Field()
    fullText = Field()
