# import necessary library
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'practice1'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        # 'http://quotes.toscrape.com/page/2/',
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

        '''
        anchors = response.css('li.next a')
        yield from response.follow_all(anchors, callback = self.parse)
        '''
        '''
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback = self.parse)
        '''
        '''
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback = self.parse)
            
            # yield response.follow(next_page, callback = self.parse)
        '''



