import scrapy
from ..items import Withscrapy1Item

class ThirdSpider(scrapy.Spider):
    name = 'third'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        items = Withscrapy1Item()

        for quote in response.css('div.quote'):
            items['text'] = quote.css('.text::text').get()
            items['author'] = quote.css('.author::text').get()
            items['tags'] = quote.css('.tag::text').getall()

            yield items
