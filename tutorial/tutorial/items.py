# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MuseumItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    medium=scrapy.Field()
    dimensions=scrapy.Field()
    credit=scrapy.Field()
    accession=scrapy.Field()
    onview=scrapy.Field()
    nationality=scrapy.Field()
    title=scrapy.Field()
    artist=scrapy.Field()
    created=scrapy.Field()
    src=scrapy.Field()
    id=scrapy.Field()
    