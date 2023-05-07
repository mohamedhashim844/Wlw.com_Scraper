import scrapy
from scrapy_playwright.page import PageMethod
from scrapy.loader import ItemLoader
import json
from scrapy.spiders import CrawlSpider , Rule
from scrapy.linkextractors import LinkExtractor

#https://www.wlw.de/de/suche?q=automation
#https://www.wlw.de/de/firma/boschen-oetting-automatisierungs-bau-gmbh-346407 (componies)
#https://www.wlw.de/de/firma/boschen-oetting-automatisierungs-bau-gmbh-346407/produkte (product list)

class WlwgSpider(scrapy.Spider):
    name = 'wlwg'
    allowed_domains = ['wlw.de']
    #start_urls = ['https://www.wlw.de/de/suche?q=automation']
    url = 'https://www.wlw.de/de/suche/page/{}?q=automation'
    def start_requests(self):
        for i in range(1,300):
            yield scrapy.Request(self.url.format(i),callback=self.pars_request)

    def pars_request(self, response):
        for links in response.css('a.company-title-link::attr(href)').extract():
            urls = response.urljoin(links)
            yield scrapy.Request(urls,callback=self.parse_item)

    def parse_item(self, response):
        
        yield{
            'name':response.css('div.flex.flex-col.flex-1.p-0 strong::text').get(),
            'address':response.css('div.business-card__address.mb-2.text-base::text').get().strip(),
            'description':response.css('p.company-summary__text::text').get().strip(),
            'year_of_foundation':response.css('div.text-navy-100.font-semi-bold.mr-2::text')[1].get(),
            'number_of_employees':response.css('div.text-navy-100.font-semi-bold.mr-2::text')[2].get(),
            'manager': response.css('div.direct-contact__person.font-semi-bold.ml-2  div::text').get(),
            'website':response.css('a#location-and-contact__website::text').get().strip(),
        }

        