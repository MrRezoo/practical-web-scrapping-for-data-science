import scrapy

from ..items import DownloadscrapyItem


class FirstSpider(scrapy.Spider):
    name = 'first'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    """ Atention for downloa you should have pillow package"""
    def parse(self, response):
        items = DownloadscrapyItem()
        images_urls = list()

        for img in response.css('.product_pod'):
            img_relative_url = img.css('a img::attr(src)').get()
            img_full_url = response.urljoin(img_relative_url)
            images_urls.append(img_full_url)

        items['image_urls'] = images_urls

        yield items
