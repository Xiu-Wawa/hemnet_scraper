import scrapy


class HemnetSpider(scrapy.Spider):
	name = 'hemnet'
	start_urls = ['https://www.hemnet.se/bostader?location_ids%5B%5D=474361&item_types%5B%5D=bostadsratt']
	page_number = 2


	def parse(self, response):
		ads = response.xpath('//li[@class="normal-results__hit js-normal-list-item"]')

		for ad in ads:
			link = ad.xpath('./a/@href').get()

			yield {
				"link": link
			}

		next_page = f'https://www.hemnet.se/bostader?location_ids%5B%5D=474361&item_types%5B%5D=bostadsratt&page={self.page_number}'

		if self.page_number > 2:
			return

		yield response.follow(next_page, callback=self.parse)

		self.page_number += 1

		yield scrapy.Request(url=ad.get(), callback=self.parseInnerPage)


	def parseInnerPage(self, response):
		address = response.xpath('//h1[@class="qa-property-heading hcl-heading hcl-heading--size2"]')
		print(address)

