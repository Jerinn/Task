#!/usr/bin/env python
# -*- coding: utf-8 -*-
import BeautifulSoup
import re
import csv
import dropbox
import  datetime
from lxml import html

from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
import scrapy
from scrapy.http.request import Request

from ..items import CtripItem

class CtripSpider(scrapy.Spider):
    name = "ctrip"
    start_urls = [
        'http://hotels.ctrip.com/hotel/taipei617?lipi=urn%3Ali%3Apage%3Ad_flagship3_messaging%3B8f06BRCeScWPrOiQam6onw%3D%3D#ctm_ref=hod_hp_sb_lst',
    ]
    def __init__(self):
        with open('result.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['HOTEL NAME','RATING', 'PRICE','IMAGE SOURCE'])
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.access_token = '89TbeZTHE-AAAAAAAAAAClndQ3_tYt9cVuU3jBYT1bgfri1v5YBrQHg8ItSGAxze'

    def parse(self, response):
        if response.status == 200:
            item = CtripItem()
            soup = BeautifulSoup.BeautifulSoup(response.body)
            hotel_list = soup.findAll('div', attrs={'class':"searchresult_list searchresult_list2"})
            if len(hotel_list) == 0:
                hotel_list = soup.findAll('div', attrs={'class':"hotel_new_list"})

            for hotel in hotel_list:
                temp_hotel_name = hotel.find('a')['title']
                item["hotel_name"] = re.findall(r'\(([^\)]+)\)',temp_hotel_name,re.I|re.M)[0]
                item["image_src"] = hotel.find('img')['src'][2:]
                item["price"] = hotel.find('span', attrs={'class': "J_price_lowList"}).text
                item["rate"] = hotel.find('span',attrs={'class':'hotel_value'}).text
                if item:
                    yield item

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        # clt = dropbox.client.DropboxClient(self.access_token)
        # print 'linked account: ', clt.account_info()


    def spider_closed(self, spider):
        """
        Write data to the file after closing the spider
        :param spider:
        :return:
        """

        if spider is not self:
            return

        utc_datetime = datetime.datetime.utcnow()
        formated_string = utc_datetime.strftime("%Y-%m-%d-%H%MZ")
        file_from = 'result.csv'
        # filename = str(formated_string)+'_ctrip_result.csv'
        file_to = 'result.csv'
        # self.upload_file(file_from, file_to)




