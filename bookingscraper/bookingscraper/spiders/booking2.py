import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.crawler import CrawlerProcess


class BookingScraper(scrapy.Spider):
    name = "booking2"
    allowed_domains = ["booking.com"]
    url = 'https://www.booking.com/searchresults.html?aid=304142&ss=United+Kingdom&nflt=ht_id%3D220'
    page_num = 0

    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}


    def start_requests(self):
        yield scrapy.Request(url=self.url, headers=self.headers, callback=self.parse)


    def parse(self, response):
        for hotelurl in response.xpath('//h3[@class="a4225678b2"]/a'):
            urls = hotelurl.xpath('./@href').get()
            yield scrapy.Request(url=urls, callback=self.parseInnerPage)

        next_page = f'https://www.booking.com/searchresults.html?aid=304142&ss=United+Kingdom&nflt=ht_id%3D220&offset={self.page_num}'
        if self.page_num <= 975:
            self.page_num += 25
            yield response.follow(next_page, callback=self.parse)


    def parseInnerPage(self, response):
        title = response.xpath('normalize-space(//div[@class="hp__hotel-title"]/following-sibling::a/text())').get()
        t_type = response.xpath('normalize-space(//div[@class="hp__hotel-title"]/descendant::span[@class="hp__hotel-type-badge"]/text())').get()
        address = response.xpath('normalize-space(//p[@class="address address_clean"]/child::span/text())').get().split(', ', 4)
        rating = response.xpath('normalize-space(//div[@data-testid="review-score-component"]/child::div[@aria-label="Scored 9.1 "]/text())').get()
        reviews = response.xpath('normalize-space(//div[@class="b1e6dd8416 b48795b3df"]/child::div[2])').get()

        

        print(address)
        

        # yield {
        #     "Title": title,
        #     "Address": address,
        #     "Type": t_type,
        #     "Rating": rating,
        #     "Reviews": reviews
        # }
        



if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(BookingScraper)
    process.start()
