# import necessary library
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'practice1'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            # author = quote.xpath('//span/small/text()').get()
            author = quote.css('small.author::text').get()
            tags = quote.css('div.tags a.tag::text').getall()
            # info = dict(text = text, author = author, tags = tags)
            info = {
                "text": text, "author": author, "tags": tags
            }
            yield(info)