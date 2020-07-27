import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tech_china.items import *
from tech_china.loaders import *
from tech_china.settings import COLLECTION
from bs4 import BeautifulSoup
from tech_china.configs.rule_component import process_value


class ChinaTechSpider(CrawlSpider):
    name = 'china_tech'
    allowed_domains = ['tech.china.com']
    start_urls = ['https://tech.china.com/'+COLLECTION+'/index.html']

    # 分别提取详情页url和列表页url
    rules = (
        Rule(LinkExtractor(allow='.*?/article/.*/.*\.html', restrict_xpaths='//*[@id="rank-defList"]/div/div/div/h3'),
             callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pages"]//a[contains(., "下一页")]',
                           process_value=lambda x: process_value(x)), follow=True, callback='parse_next_url')
    )

    def parse_item(self, response):
        """解析根据rule过滤的下一页链接对应的列表页，提取详情页url加入调度器
        一定要加dont_filter=True，否则所有详情页url会被当做重复域名过滤掉"""
        loader = ChinaTechLoader(item=NewsItem(), response=response)
        loader.add_xpath('title', '//div[@id="chan_mainBlk"]/h1/text()')
        loader.add_value('url', response.url)
        loader.add_xpath('text', '//div[@id="chan_newsDetail"]/p//text()')
        loader.add_xpath('datetime', '//div[@class="chan_newsInfo_source"]/span[@class="time"]/text()')
        loader.add_xpath('source', '//div[@class="chan_newsInfo_source"]/span[@class="source"]/text()')
        loader.add_value('website', '中华网科技')
        yield loader.load_item()

    def parse_next_url(self, response):
        """解析列表页"""
        print('下一页列表页的链接:', response.url)
        link = LinkExtractor(allow='.*?/article/.*/.*\.html', restrict_xpaths='//*[@id="rank-defList"]/div/div/div/h3')
        links = link.extract_links(response)
        for detail_url in links:
            print('这是要加入的url', detail_url.url)
            yield Request(url=detail_url.url, callback=self.parse_item, dont_filter=True)

