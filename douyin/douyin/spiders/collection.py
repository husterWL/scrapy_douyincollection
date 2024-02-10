import scrapy


class CollectionSpider(scrapy.Spider):
    name = "collection"
    allowed_domains = ["douyin.com"]
    start_urls = ["https://douyin.com"]

    def parse(self, response):
        pass
