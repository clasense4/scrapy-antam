# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from models import db_connect
import functions

class AntamPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates news table.
        """
        self.db = db_connect()

    def process_item(self, item, spider):
        # Insert buy back info
        # self.db.table('buy_back_info').insert({
        #     'price': item['buy_back'],
        # });
        # Insert gold data
        for gold in item['gold_data']:
            # print gold
            self.db.table('gold').insert({
                'butik_id': item['butik_id'],
                'city': item['city'],
                'gram': gold[0],
                'price': gold[1],
                'price_per_gram': gold[2],
                'stock': gold[3],
                'stock_int': 1 if gold[3] == 'Available' else 0,
                'year': item['info_date'].split('-')[2],
                'month': item['info_date'].split('-')[1],
                'date': item['info_date'].split('-')[0],
                'origin_datetime': functions.parse_datetime(item['info_date'], item['info_time']),
            });

        return item
