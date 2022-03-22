import scrapy
import json
from ..items import NetmedsScrapeDataItem



class NetmedsSpider(scrapy.Spider):
    name = 'netmeds'
    allowed_domains = ['netmeds.com']
    start_urls = ['https://netmeds.com/']
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}

    def start_requests(self):
        urls = ['https://www.netmeds.com/non-prescriptions/skin-care',
                'https://www.netmeds.com/non-prescriptions/skin-care/page/2']
        for url in urls: yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        items = NetmedsScrapeDataItem()
        title = response.css('.clsgetname::text').extract()

        price = response.css('#final_price::text').extract()

        title_list = list()

        for prod in title:
            if len(prod) > 19:
                title_list.append(prod)
        # creating a list of dict with extracted values
        result_list = list()
        for title_out, price_out in zip(title_list, price):
            result_list.append({"title": title_out, "price": price_out})

        items['fin_result'] = result_list
        yield items

