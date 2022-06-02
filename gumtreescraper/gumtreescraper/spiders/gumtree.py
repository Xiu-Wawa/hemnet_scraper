import scrapy
from gumtreescraper.items import GumtreescraperItem
from scrapy.loader import ItemLoader


class GumtreeScraper(scrapy.Spider):
	name = "gumtree"
	allowed_domains = ["web"]
	start_urls = ['https://www.gumtree.com/flats-houses/london']


	def start_request(self):
		url = 'https://www.gumtree.com/flats-houses/london'
		yield scrapy.Request(url=url, callback=self.parse)

	def add_base_url(self, selector, response, xpath: str) -> str:
		return response.urljoin(selector.xpath(xpath).get())

	def parse(self, response):
		for ad in response.xpath('//article[@class="listing-maxi"]'):
			url = self.add_base_url(ad, response, './a/@href')

			l = ItemLoader(item = GumtreescraperItem(), selector=ad)
			l.add_value('link', url)
			l.add_xpath('title', './/h2[@class="listing-title"]')
			l.add_xpath('location', './/span[@class="truncate-line"]')
			l.add_xpath('price', './/strong[@class="h3-responsive"]')

			# item["link"] = response.urljoin(ad.xpath('./a/@href').get())
			# item["title"] = ad.xpath('normalize-space(.//h2[@class="listing-title"]/text())').get()
			# item["location"] = ad.xpath('normalize-space(.//span[@class="truncate-line"]/text())').get()
			# item["price"] = ad.xpath('.//strong[@class="h3-responsive"]/text()').re('[.0-9]+')

			yield l.load_item()