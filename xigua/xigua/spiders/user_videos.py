import scrapy
import logging

class UserVideos(scrapy.Spider):
    name = "user-videos"

    def start_requests(self):
        urls = [
            'https://www.ixigua.com/c/user/article/?user_id=67198009423&max_behot_time=0&max_repin_time=0&count=20&page_type=0'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        logging.info(response.body)