# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
import functions
from scrapy.loader.processors import Join, MapCompose
from w3lib.html import remove_tags

class AntamItem(scrapy.Item):
    # define the fields for your item here like:
    city = scrapy.Field(
        input_processor=MapCompose(
            functions.replace,
        ),
        output_processor=Join(),
    )

    buy_back = scrapy.Field(
        input_processor=MapCompose(
            functions.remove_html,
            functions.parse_money,
        ),
        output_processor=Join(),
    )

    gold_data = scrapy.Field(
        input_processor=MapCompose(
            functions.parse_gold_data,
        ),
    )

    info_date = scrapy.Field(
        input_processor=MapCompose(
        ),
        output_processor=Join(),
    )

    info_time = scrapy.Field(
        input_processor=MapCompose(
        ),
        output_processor=Join(),
    )

    butik_id = scrapy.Field(
        output_processor=Join(),
    )
