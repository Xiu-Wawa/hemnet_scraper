import scrapy
from ..items import QuotescraperItem


class QuoteSpider(scrapy.Spider):
	name = "quotes"
	start_urls = {"https://quotes.toscrape.com/"}


	def parse(self, response):
		items = QuotescraperItem()
		all_quotes = response.css('div.quote')

		for quote in all_quotes:
			quotes = quote.css('span.text::text').extract()
			authors = quote.css('.author::text').extract()
			tags = quote.css('.tag::text').extract()

			items['quotes'] = quotes
			items['authors'] = authors
			items['tags'] = tags

			yield items