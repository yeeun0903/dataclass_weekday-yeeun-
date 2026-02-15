import scrapy

class AladinItem(scrapy.Item):
    rank = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    publisher = scrapy.Field()
    price = scrapy.Field()
    point = scrapy.Field()
    url = scrapy.Field()
