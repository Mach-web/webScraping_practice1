'''
scrapy crawl tagScraping -O quotes-humor.csv -a tag=love
'''
import scrapy

class tagSpider(scrapy.Spider):
    name = 'tagScraping'
    '''start_requests works the same way as start_urls but now enables tweaking of the url to accomodate tag defined'''
    def start_requests(self):
        url = 'http://quotes.toscrape.com/tag/'
        tag = getattr(self, 'tag', None)
        '''Concat url with tag attribute'''
        if tag is not None:
            url = url + tag
        yield scrapy.Request(url, self.parse)
    '''Create a dictionary of quotes in the given tag'''
    def parse(self, response):
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            author = quote.css('small.author::text').get()
            tags = quote.css('a.tag::text').getall()
            tag_quotes = {
                'Quotes': text,
                'Author': author,
                'Tags':tags,
            }
            yield tag_quotes
        '''Move to next page if it not empty'''
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
            