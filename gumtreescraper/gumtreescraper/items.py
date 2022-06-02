import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags



def clean_price(value):
    return value.replace('£', '').replace('pm', '').replace('pw', '')


def remove_space(value):
    return value.replace('\n', '').replace('\t', '')

def path(value, response):
    return response.urljoin(value)


class GumtreescraperItem(scrapy.Item):
    link = scrapy.Field(input_processor=MapCompose(remove_tags, remove_space, path), output_processor=TakeFirst())
    title = scrapy.Field(input_processor=MapCompose(remove_tags, remove_space), output_processor=TakeFirst())
    location = scrapy.Field(input_processor=MapCompose(remove_tags, remove_space), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags, clean_price), output_processor=TakeFirst())