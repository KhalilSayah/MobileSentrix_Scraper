# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MobilesentrixItem(scrapy.Item):
    # define the fields for your item here like:
     NAME = scrapy.Field()
     SKU = scrapy.Field()
     PRICE = scrapy.Field()
     TAGS = scrapy.Field()
     DESCRIPTION = scrapy.Field()
     IMAGE = scrapy.Field()
     OTHER_IMAGES = scrapy.Field()

    
