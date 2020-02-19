# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors

class Demo1Pipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # host
            port=3306,  # port
            db='remax_housing',  # database name
            user='root',  # username
            passwd='12345',  # password
            charset='utf8',
            use_unicode=True)

        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        sql = """insert into calgary_housing(address, 
                                            baths, 
                                            beds, 
                                            boardName,
                                            city,
                                            detailUrl,
                                            isLuxury,
                                            isCommercial,
                                            isRemaxListing,
                                            lat,
                                            listingDate,
                                            listingId,
                                            listPrice,
                                            listPriceMove,
                                            listingTypeId,
                                            lng,
                                            lotSizeRaw,
                                            lotSizeSearch,
                                            mlsNum,
                                            postalCode,
                                            province,
                                            remaxAgentName,
                                            remaxOfficeName,
                                            lastUpdated,
                                            hasOpenHouse)
            values (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"""

        data = (item['address'],
                 item['baths'],
                 item['beds'],
                 item['boardName'],
                 item['city'],
                 item['detailUrl'],
                 item['isLuxury'],
                 item['isCommercial'],
                 item['isRemaxListing'],
                 item['lat'],
                 item['listingDate'],
                 item['listingId'],
                 item['listPrice'],
                 item['listPriceMove'],
                 item['listingTypeId'],
                 item['lng'],
                 item['lotSizeRaw'],
                 item['lotSizeSearch'],
                 item['mlsNum'],
                 item['postalCode'],
                 item['province'],
                 item['remaxAgentName'],
                 item['remaxOfficeName'],
                 item['lastUpdated'],
                 item['hasOpenHouse'])
        try:
            self.cursor.execute(sql, data)
            self.connect.commit()

        except pymysql.err.IntegrityError:
            pass

        return item
