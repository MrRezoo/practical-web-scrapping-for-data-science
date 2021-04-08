import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    allowed_domains = ['https://quotes.toscrape.com/']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        print('==' * 100)
        """ Start Of => get VS get all """
        print(response.css('small.author').get())
        print('==' * 100)
        print(response.css('small.author').getall())
        """ End Of => get VS get all """

        #  ---------------------------------------------------------------------

        """ get inside text """
        print('==' * 100)
        print(response.css('small.author::text').getall())
        print('==' * 100)
        print(response.css('small.author').getall())

        #  ---------------------------------------------------------------------

        """extract, extract_first is old method"""
        print('==' * 100)
        for quote in response.css('div.quote'):
            yield {
                'title': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('a.tag::text').getall(),
            }
        print('==' * 100)
        """extract, extract_first is old method"""
        for quote in response.css('div.quote'):
            yield {
                'title': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('a.tag::text').extract(),
            }
        #  ---------------------------------------------------------------------
