import scrapy
from puma_scraper.items import PumaScraperItem

class PumaSpider(scrapy.Spider):
    name = "puma"
    allowed_domains = ["in.puma.com"]
    start_urls = ["https://in.puma.com/in/en/mens/mens-shoes/mens-shoes-sneakers"] # ?offset=648

    def parse(self, response):
        response_data = response.css("#product-list-items .text-base.font-bold::text").extract()
        for i in range(0, len(response_data), 2):
            print(response_data[i], response_data[i+1])

            item = PumaScraperItem()
            item['name'] = response_data[i]
            item['price'] = response_data[i+1]

            yield item
            
