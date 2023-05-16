import scrapy


class InstagramSpider(scrapy.Spider):
    name = "instagram"
    allowed_domains = ["instagram.com"]
    start_urls = ["https://instagram.com"]

    def parse(self, response):
        pass
