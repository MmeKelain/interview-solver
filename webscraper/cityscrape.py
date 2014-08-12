import scrapy

class CitySpider(scrapy.Spider):
    name = "city"
    allowed_domains = ["census.gov", "wikipedia.org"]
    start_urls = []
    
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
