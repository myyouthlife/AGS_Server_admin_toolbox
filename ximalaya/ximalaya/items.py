# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XimalayaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    mp3_url = scrapy.Field()
    title=scrapy.Field()

    # mp3_ids = scrapy.Field()
    pass

class FileDownloadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    audio_urls=scrapy.Field()
    audios=scrapy.Field()