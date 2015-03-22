import scrapy
from tutorial.items import MuseumItem
from scrapy.contrib.spiders import SitemapSpider
import re

class MuseumSpider(SitemapSpider):
    """docstring for MuseumSpider"""
    name="museum"
    sitemap_urls = ['http://www.nga.gov/sitemap.xml']
    sitemap_rules = [
        ('/content/ngaweb/Collection/art-object-page', 'parse'),
    ]

    def parse_helper(self,response,item,xpath):
        for sel in response.xpath(xpath):
            if sel.xpath('a'):
                key=sel.xpath('@class').extract()[0].strip()
                value=sel.xpath('a/text()').extract()[0].strip()
                url=sel.xpath('a/@href').extract()[0].strip()
                if key in item:
                    item[key]=[item[key]]+[url,value]
                else:
                    item[key]=[url,value]
            else:
                text=sel.xpath('text()').extract()
                if text:
                    key=sel.xpath('@class').extract()[0].strip()
                    value=text[0].strip()
                    #item[key]=value
                    if key in item:
                        item[key]=[item[key]]+[value]
                    else:
                        item[key]=value
        return item

    def parse(self,response):
        item=MuseumItem()
        self.parse_helper(response,item,'//dl[contains(@class,"artwork-details")]/dd')
        self.parse_helper(response,item,'//dl[contains(@class,"artwork-details")]/dt')
        self.parse_helper(response,item,'//dl[contains(@class,"artist-details")]/dd')
        self.parse_helper(response,item,'//dl[contains(@class,"artist-details")]/dt')
        item[u'src']=response.xpath('//img[contains(@class,"mainImg")]/@src').extract()[0].strip()
        item[u'id']=response.url
        if item:
            # if table has key created
            if item.has_key('created'):
                # find digits
                year=re.search(r'\d+',item['created']).group()
                self.log(year)
                # later than 1700, add to list
                if (len(year)==4 and int(year[:2]) >= 17) or (len(year)==2 and int(year) >=18) :
                    yield item
