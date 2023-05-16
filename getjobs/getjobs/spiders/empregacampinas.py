import scrapy


class EmpregacampinasSpider(scrapy.Spider):
    name = "empregacampinas"
    allowed_domains = ["empregacampinas.com.br"]
    start_urls = ["https://empregacampinas.com.br"]

    def parse(self, response):
        pass
