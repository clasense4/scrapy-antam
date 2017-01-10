# -*- coding: utf-8 -*-
# encoding=utf8

# from models import db_connect, create_news_table
from scrapy.selector import Selector
import re
import settings
import redis
import time, datetime
from datetime import timedelta, date
import sys
import urlparse
reload(sys)
sys.setdefaultencoding('utf8')

def remove_html(text):
    '''
    INPUT  : Raw Text (contains html is ok)
    OUTPUT : Fresh Text (No HTML, MYSQL escaped and Stripped)
    '''
    text = re.sub('<[^>]*>',' ',text.encode('utf-8')).strip()
    text = re.sub('\t','',text)
    text = re.sub('\n','',text)
    text = re.sub('\r','',text)
    return text

def remove_whitespace(text):
    text = re.sub('^\s+|\s+$|\s+(?=\s)','', text)
    return text

def replace(text):
    # text = re.sub('twitter','fajri',text)
    text = re.sub('Harga ','',text)
    return text

def parse_money(text):
    token_re = re.compile(r'([0-9])\w*\.([0-9])\w*\.([0-9])\w*|([0-9])\w*\.([0-9])\w*', re.DOTALL)
    rr = token_re.search(text).group()
    text = "".join(rr.split('.'))
    return text

def parse_gold_data(text):
    gold = []
    sel = Selector(text=text).xpath('//tbody/tr').extract()
    for s in sel:
        s = remove_html(s)
        s = remove_whitespace(s)
        g = s.split(' ')
        g.pop(0)
        g[1] = parse_money(g[1])
        g[2] = parse_money(g[2])
        # print g
        gold.append(g)
    return gold
    # token_re = re.compile(r'([0-9])\w*\.([0-9])\w*\.([0-9])\w*|([0-9])\w*\.([0-9])\w*', re.DOTALL)
    # rr = token_re.search(text).group()
    # text = "".join(rr.split('.'))
    # return text

def today():
    today = datetime.date.today().strftime('%Y-%m-%d')
    return str(today)

def parse_info_data(text):
    info = []
    sel = Selector(text=text).xpath('//tr/td').extract()
    for s in sel:
        s = remove_html(s)
        s = remove_whitespace(s)
        # print (s)
        info.append(s)
    return info

def get_id_butik(response):
    return dict(urlparse.parse_qsl(urlparse.urlsplit(response.url).query))['idbutik']

def parse_datetime(info_date, info_time):
    dt = info_date + info_time
    ts = time.mktime(datetime.datetime.strptime(dt, "%d-%m-%Y %H:%M:%S").timetuple())
    # dt2 = dt.strftime("%d-%m-%Y %H:%M:%S")
    return ts

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)
