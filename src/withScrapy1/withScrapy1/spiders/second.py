import scrapy


class SecondSpider(scrapy.Spider):
    name = 'second'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        print('==' * 100)
        for quote in response.css('div.quote'):
            yield {
                'url': response.url,
                'title': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
