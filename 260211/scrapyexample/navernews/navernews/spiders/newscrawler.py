import scrapy


class NewscrawlerSpider(scrapy.Spider):
    name = "newscrawler"
    allowed_domains = ["search.naver.com"]
    start_urls = ["https://search.naver.com"]

    def parse(self, response):
        pass
