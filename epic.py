import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import urllib
import json

class EpicGames(scrapy.Spider):
    name = 'epic'

    base_url = 'https://www.epicgames.com/store/pt-BR/browse?sortBy=releaseDate&sortDir=DESC&count=40&'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'epics.csv'
    }


    def start_requests(self):

        for page in range(0,600,40):
            next_page = self.base_url + urllib.parse.urlencode({'start': str(page)})
            print(next_page)

            # https://www.epicgames.com/store/pt-BR/browse?sortBy=releaseDate&sortDir=DESC&count=40&start=120
            # https://www.epicgames.com/store/pt-BR/browse?sortBy=releaseDate&sortDir=DESC&count=40&start=120
            #yield scrapy.Request(url=next_page, headers=self.headers, callback=self.parse)
            #break

    #def parse(self,res):
        #print('\n\nRES:', res)

        #with open ('res.html', 'w') as f:
            #f.white(res.text)





if __name__ == '__main__':
    # run scraper
    process = CrawlerProcess()
    process.crawl(EpicGames)
    process.start()
