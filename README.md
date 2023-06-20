### Website scraped: http://quotes.toscrape.com
This folder was first created through 'scrapy startproject' command and therefore has many dependent files that I did not necessarily create.
The file I worked with are found in 'tutorial/spiders' folder.

### Practice1.py
Run the following command in virtual environment: scrapy crawl practice1 -O practice1.csv
This command crawls the website defined in the file and stores the results in a csv file.
Scrapy is able to move to the next page when it reaches the end of current page.

### Practice2a.py
In this file, I implement how scrapy would follow the link found in an attribute and extract author data from it.
Run the following command in virtual environment: scrapy crawl author_info -O author.csv
The command works like the previous command in practice1

### Practice3a.py
In this file, I implement how scrapy would follow the link of a tag and extract various quotes for the given tag.
Run the following command in virtual environment: scrapy crawl tagScraping -O quotes-love.json -a tag=love
In this command, we define a tag which we want to scrape quotes from.
