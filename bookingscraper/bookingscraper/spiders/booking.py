import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.crawler import CrawlerProcess
from bookingscraper.items import BookingscraperItem
from scrapy.loader import ItemLoader


class BookingScraper(scrapy.Spider):
    name = "booking"
    allowed_domains = ["booking.com"]
    url = 'https://www.booking.com/searchresults.html?label=gen173nr-1DCAEoggI46AdIM1gEaLQBiAEBmAExuAEZyAEP2AED6AEB-AECiAIBqAIDuAL2vuOUBsACAdICJDhjMjM3NDE4LWE3ZTMtNDcwMS1iZGM4LWUzYTA2NzQyZDYyMtgCBOACAQ&sid=7f95d6b3149a5de0d1a0a40b85b06fde&aid=304142&sb_lp=1&src=index&error_url=https%3A%2F%2Fwww.booking.com%2Findex.html%3Flabel%3Dgen173nr-1DCAEoggI46AdIM1gEaLQBiAEBmAExuAEZyAEP2AED6AEB-AECiAIBqAIDuAL2vuOUBsACAdICJDhjMjM3NDE4LWE3ZTMtNDcwMS1iZGM4LWUzYTA2NzQyZDYyMtgCBOACAQ%26sid%3D7f95d6b3149a5de0d1a0a40b85b06fde%26sb_price_type%3Dtotal%26%26&ss=United+Kingdom&is_ski_area=&checkin_year=&checkin_month=&checkout_year=&checkout_month=&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ss_raw=uni&ac_position=2&ac_langcode=en&ac_click_type=b&dest_id=222&dest_type=country&place_id_lat=54.4983&place_id_lon=-3.07394&search_pageview_id=067370fbe77c0317&search_selected=true&search_pageview_id=067370fbe77c0317&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0&nflt=ht_id%3D220'
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}


    def start_requests(self):
        yield scrapy.Request(url=self.url, headers=self.headers, callback=self.parse)


    def parse(self, response):
        for hotelurl in response.xpath('//h3[@class="a4225678b2"]/a'):
            link = hotelurl.xpath('./@href').get()
            yield scrapy.Request(url=link, callback=self.parseInnerPage)
            


    def parseInnerPage(self, response):
        l = ItemLoader(item = BookingscraperItem(), response=response)

        l.add_xpath("Title", 'normalize-space(//div[@class="hp__hotel-title"]/following-sibling::a)')
        l.add_xpath("Type", 'normalize-space(//div[@class="hp__hotel-title"]/descendant::span[@class="hp__hotel-type-badge"])') 
        l.add_xpath("Address", 'normalize-space(//p[@class="address address_clean"]/child::span[1])')
        l.add_xpath("Rating", 'normalize-space(//div[@data-testid="review-score-component"]/child::div[@aria-label="Scored 9.1 "])')
        l.add_xpath("Reviews", 'normalize-space(//div[@class="b1e6dd8416 b48795b3df"]/child::div[2])')

        
        yield l.load_item()
        


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(BookingScraper)
    process.start()
