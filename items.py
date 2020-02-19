# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class PropertyItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    address = Field()
    baths = Field()
    beds = Field()
    boardName = Field()
    city = Field()
    detailUrl = Field()
    #imageUrls = Field()
    isLuxury = Field()
    isCommercial = Field()
    isRemaxListing = Field()
    lat = Field()
    listingDate = Field()
    listingId = Field()
    listPrice = Field()
    listPriceMove = Field()
    listingTypeId = Field()
    lng = Field()
    lotSizeRaw = Field()
    lotSizeSearch = Field()
    mlsNum = Field()
    postalCode = Field()
    province = Field()
    remaxAgentName = Field()
    remaxOfficeName = Field()
    lastUpdated = Field()
    hasOpenHouse = Field()
