import scrapy


class GumtreeScraper(scrapy.Spider):
	name = "gumtree"
	allowed_domains = ["web"]
	start_urls = ['https://www.gumtree.com/flats-houses/london']


	def parse(self, response):
		ads = response.xpath('//article[@class="listing-maxi"]/parent::li')
		for ad in ads:
			link = ad.xpath('/descendant::a/@href').get()
			title = ad.xpath('normalize-space(descendant::h2/text())').get()
			# location = ad.xpath('normalize-space(span[@class="truncate-line"]/text())').get()

			yield {
				"link": link,
				"title": title
			}
			