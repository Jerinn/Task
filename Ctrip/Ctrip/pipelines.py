#!/usr/bin/env python
# -*- coding: utf-8 -*


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class CtripPipeline(object):
    def process_item(self, item, spider):
        with open('result.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([item['hotel_name'],item['rate'], item['price'],item['image_src']])
        return item
