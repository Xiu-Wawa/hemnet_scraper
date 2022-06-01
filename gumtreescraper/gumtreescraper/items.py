import scrapy


class GumtreeItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    location = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
