# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from datetime import timedelta, date
from antam.items import AntamItem
from antam.functions import get_id_butik, daterange

class LogammuliaSpider(scrapy.Spider):
    name = "logammulia"
    allowed_domains = ["logammulia.com"]

    def start_requests(self):
        start_date = date(2016, 7, 25)
        # start_date = date(2017, 1, 1)
        end_date = date(2017, 1, 7)
        for single_date in daterange(start_date, end_date):
            today = single_date.strftime("%Y-%m-%d")
            yield scrapy.Request('http://www.logammulia.com/price_list.php?idbutik=1&idkat=2&tanggal='+today+'&iddesc=0001', self.parse)
            yield scrapy.Request('http://www.logammulia.com/price_list.php?idbutik=5&idkat=2&tanggal='+today+'&iddesc=0001', self.parse)
            yield scrapy.Request('http://www.logammulia.com/price_list.php?idbutik=7&idkat=2&tanggal='+today+'&iddesc=0001', self.parse)
            yield scrapy.Request('http://www.logammulia.com/price_list.php?idbutik=8&idkat=2&tanggal='+today+'&iddesc=0001', self.parse)
            yield scrapy.Request('http://www.logammulia.com/price_list.php?idbutik=9&idkat=13&tanggal='+today+'&iddesc=0001', self.parse)
            yield scrapy.Request('http://www.logammulia.com/price_list.php?idbutik=10&idkat=2&tanggal='+today+'&iddesc=0001', self.parse)
            yield scrapy.Request('http://www.logammulia.com/price_list.php?idbutik=11&idkat=2&tanggal='+today+'&iddesc=0001', self.parse)
            yield scrapy.Request('http://www.logammulia.com/price_list.php?idbutik=12&idkat=2&tanggal='+today+'&iddesc=0001', self.parse)
            yield scrapy.Request('http://www.logammulia.com/price_list.php?idbutik=13&idkat=2&tanggal='+today+'&iddesc=0001', self.parse)
            yield scrapy.Request('http://www.logammulia.com/price_list.php?idbutik=14&idkat=2&tanggal='+today+'&iddesc=0001', self.parse)
            yield scrapy.Request('http://www.logammulia.com/price_list.php?idbutik=15&idkat=2&tanggal='+today+'&iddesc=0001', self.parse)
            yield scrapy.Request('http://www.logammulia.com/price_list.php?idbutik=16&idkat=2&tanggal='+today+'&iddesc=0001', self.parse)
            yield scrapy.Request('http://www.logammulia.com/price_list.php?idbutik=17&idkat=2&tanggal='+today+'&iddesc=0001', self.parse)

    def parse(self, response):
        # Check for empty response, like : antam didn't open on sunday
        xpath = {}
        xpath['city'] = '//*[@id="title_breadcrumbs_bar"]/div/div[1]/h1/text()'
        xpath['buy_back'] = '/html/body/section[2]/div/div/div/div[1]/font/text()'
        xpath['info_date'] = '//*[@id="tab-2"]/section/div/div/div/div/table[1]/tr[1]/td[3]/text()'
        xpath['info_time'] = '//*[@id="tab-2"]/section/div/div/div/div/table[1]/tr[2]/td[3]/text()'
        xpath['gold_data'] = '//*[@id="tab-2"]/section/div/div/div/div/table[2]'
        result = response.xpath(xpath['buy_back'])

        if result <> []:
            l = ItemLoader(item=AntamItem(), response=response)
            l.add_xpath('city', xpath['city'])
            l.add_xpath('buy_back', xpath['buy_back'])
            l.add_xpath('info_date', xpath['info_date'])
            l.add_xpath('info_time', xpath['info_time'])
            l.add_xpath('gold_data', xpath['gold_data'])
            l.add_value('butik_id', get_id_butik(response))
            yield l.load_item()

