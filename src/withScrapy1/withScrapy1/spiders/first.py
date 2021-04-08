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

        print('==' * 100)
        #  ---------------------------------------------------------------------
        """ use xpath"""
        print(response.xpath('/html/head/title').getall())
        print('==' * 100)
        """ use xpath => text """
        print(response.xpath('//title/text()').getall())
        print('==' * 100)
        """ use xpath => attributes"""
        print(response.xpath('//meta/@charset').getall())
        print('==' * 100)
        """ use xpath => get with inspect on browser"""
        print(response.xpath(
            '/html/body/div/div[2]/div[1]/div[1]/span[2]/small').getall())
        print('==' * 100)
        """ user xpath => get it with selectorGadget"""
        print(response.xpath(
            '//*[contains(concat( " ", @class, " " ), concat( " ", "author", '
            '" " ))]').getall())
        print('==' * 100)
