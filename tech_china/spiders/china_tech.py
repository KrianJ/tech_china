import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tech_china.items import *
from tech_china.loaders import *
from tech_china.settings import COLLECTION
from bs4 import BeautifulSoup


class ChinaTechSpider(CrawlSpider):
    name = 'china_tech'
    allowed_domains = ['tech.china.com']
    base_url = 'https://tech.china.com/'
    start_urls = ['https://tech.china.com/'+COLLECTION+'/index.html']

    # 分别提取详情页url和列表页url
    rules = (
        Rule(LinkExtractor(allow='.*?/article/.*/.*\.html', restrict_xpaths='//div[@class="wntjItem item_defaultView clearfix"]//h3[@class="tit"]'),
             callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pages"]//a[contains(., "下一页")]'))
    )

    def parse_item(self, response):
        """对详情页做提取"""
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
        print('下一页的链接:', response.url)
        # soup = BeautifulSoup(response.text, 'lxml')
        # titles = soup.find_all('h3', attrs={'class': 'tit'})
        # links = [title.find('a')['href'] for title in titles]
        # print(links)
        # for link in links:
        #     yield Request(url=link, callback=self.parse_item)
