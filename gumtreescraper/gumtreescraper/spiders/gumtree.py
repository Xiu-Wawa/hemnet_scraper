import scrapy

from ..items import GumtreeItem


class GumtreeScraper(scrapy.Spider):
	name = "gumtree"
	start_urls = ['https://www.gumtree.com/flats-houses/london']

	def parse(self, response):
		items = GumtreeItem()

		ads = response.xpath('//article[@class="listing-maxi"]')

		for ad in ads:
			items['url'] = response.urljoin(ad.xpath('./a/@href').extract_first())
			items['title'] = ad.xpath('.//h2[@class="listing-title"]/text()').extract_first()

			yield items

			



			