from scrapy.spiders import Spider
from scrapy.utils.spider import iterate_spider_output


class InitSpider(Spider):
   

    def start_requests(self):
        self._postinit_reqs = super().start_requests()
        return iterate_spider_output(self.init_request())

    def initialized(self, response=None):
     
        return self.__dict__.pop("_postinit_reqs")

    def init_request(self):
      
        return self.initialized()