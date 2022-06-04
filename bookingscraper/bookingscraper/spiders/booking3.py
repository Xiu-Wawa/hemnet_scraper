from selenium.webdriver import Chrome, ChromeOptions
import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.crawler import CrawlerProcess
from bookingscraper.items import BookingscraperItem
from scrapy.loader import ItemLoader
import os


class BookingScraper(scrapy.Spider):
	name = "booking3"
	page_num = 25


	def start_requests(self):
		# options = ChromeOptions()
		# options.headless = True
		driver = Chrome()
		driver.get('https://www.booking.com/searchresults.html?aid=304142&ss=United+Kingdom&nflt=ht_id%3D220&offset=0')
		link_elements = driver.find_elements_by_xpath('//h3[@class="a4225678b2"]/a')

		for link_elem in link_elements:
			href = link_elem.get_attribute('href')
			yield scrapy.Request(href)


		# driver.quit()

		next_page = f'https://www.booking.com/searchresults.html?aid=304142&ss=United+Kingdom&nflt=ht_id%3D220&offset={self.page_num}'
		if self.page_num <= 25:
			self.page_num += 25
			yield response.follow(next_page, callback=self.parse)


		driver.quit()


	def parse(self, response):
		l = ItemLoader(item=BookingscraperItem(), selector=response)

		l.add_xpath("Title", 'normalize-space(//div[@class="hp__hotel-title"]/following-sibling::a)')
		l.add_xpath("Type", 'normalize-space(//div[@class="hp__hotel-title"]/descendant::span[@class="hp__hotel-type-badge"])')
		l.add_xpath("Address", 'normalize-space(//p[@class="address address_clean"]/child::span[1])')
		l.add_xpath("Rating", 'normalize-space(//div[@data-testid="review-score-component"]/child::div[@aria-label="Scored 9.1 "])')
		l.add_xpath("Reviews", 'normalize-space(//div[@class="b1e6dd8416 b48795b3df"]/child::div[2])')

		# next_page = f'https://www.booking.com/searchresults.html?aid=304142&ss=United+Kingdom&nflt=ht_id%3D220&offset={self.page_num}'
		# if self.page_num <= 25:
		# 	self.page_num += 25
		# 	yield response.follow(next_page, callback=self.parse)


		yield l.load_item()

    