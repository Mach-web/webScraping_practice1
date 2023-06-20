'''scrapy crawl author_info -O author.csv'''
import scrapy

class authorScrapy(scrapy.Spider):
    name = 'author_info'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # loop through every quote
        for quote in response.css('div.quote'):
            about = quote.css('small.author + a::attr(href)').get()
            '''
            Follow link to authors page the call the method which scrapes authors page
            '''
            yield response.follow(about, self.authorScraping)
        '''Follow link to next page then call the method again if page is not empty'''
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)

    def authorScraping(self, response):
        '''Capture details in authors page'''
        title = response.css('h3.author-title::text').get().strip()
        birth = response.css('span.author-born-date::text').get()
        desc = response.css('div.author-description::text').get().strip()
        author = {
            'title': title,
            'BirthDate': birth,
            'Description': desc,
        }
        yield author
