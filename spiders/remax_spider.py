# -*- coding: utf-8 -*-
import json

import logging
from scrapy import Spider, Request
import io
import sys
from random import randint
from time import sleep

from demo1.items import PropertyItem

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


class RemaxSpiderSpider(Spider):
    name = 'remax_spider'
    allowed_domains = ['remax.ca']
    # URL Parameters
    province = 'ab'
    city = 'calgary'
    page = 1
    Requested_pages = 300
    start_urls = 'https://www.remax.ca/{province}/{city}-real-estate?page={page}'
    property_url = 'https://www.remax.ca/api/v1/listings/previews/{property_ids}?includeOffice=true'

    logger = logging.getLogger()
    def start_requests(self):
        self.logger.info('################Starting Request First Page##################')
        yield Request(self.start_urls.format(province=self.province, city=self.city, page=self.page),
                      callback=self.parse_page, meta = {'index': self.page})
    #
    def parse_page(self, response):
        # Obtain the IDs of each property in current page
        self.logger.info('################Scraping Page {page} Information##################'.format(page = self.page))
        property_id_list = response.css('div.has-flex-wrap app-listing-card a::attr(href)').re('wp_id(.*?)-lst')
        property_ids = ','.join(property_id_list)
        sleep(randint(1, 10))
        yield Request(self.property_url.format(property_ids = property_ids), dont_filter= True, callback = self.parse_property, meta = {'index': self.page})

    def parse_property(self, response):
        # Load the results into item pipeline
        self.logger.info('################Scraping Property Details##################')
        result = json.loads(response.text)
        item = PropertyItem()

        if 'result' in result.keys():
            for data in result['result']['results']:
                for field in item.fields:
                    if field in data.keys():
                        item[field] = data.get(field)
                    else:
                        item[field] = 'NULL'
                self.logger.info('################Scraping {id} Details##################'.format(id = item['listingId']))
                yield item
        #Parse to next pages
        # index = response.meta.get('index', self.page)
        self.page += 1
        sleep(randint(1, 15))
        yield Request(self.start_urls.format(province=self.province, city=self.city, page=self.page), dont_filter= True,
                      callback=self.parse_page, meta = {'index': self.page})
