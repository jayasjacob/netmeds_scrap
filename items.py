# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NetmedsScrapeDataItem(scrapy.Item):
   
    fin_result = scrapy.Field()
