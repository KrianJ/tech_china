import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tech_china.utils import get_config
from tech_china.rules import rules
from tech_china.items import *
from tech_china.loaders import *
from tech_china import urls


class UniversalSpider(CrawlSpider):
    name = 'universal'

    def __init__(self, name, *args, **kwargs):
        config = get_config(name)
        self.config = config
        self.rules = rules.get(config.get('rules'))
        start_urls = config.get('start_urls')
        if start_urls:
            if start_urls.get('type') == 'static':
                self.start_urls = start_urls.get('value')
            elif start_urls.get('type') == 'dynamic':
                self.start_urls = list(eval('urls.' + start_urls.get('method'))())
        self.allowed_domains = config.get('allowed_domains')
        super(UniversalSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        item = self.config.get('item')
        if item:
            cls = eval(item.get('class'))()
            loader = eval(item.get('loader'))(cls, response=response)
            # 动态获取属性配置
            for key, value in item.get('attrs').items():
                for extractor in value:
                    if extractor.get('method') == 'xpath':
                        loader.add_xpath(key, *extractor.get('args'))
                    if extractor.get('method') == 'css':
                        loader.add_css(key, *extractor.get('args'))
                    if extractor.get('method') == 'value':
                        loader.add_value(key, *extractor.get('args'))
                    if extractor.get('method') == 'attr':
                        loader.add_value(key, getattr(response, *extractor.get('args')))
            yield loader.load_item()

    def parse_next_url(self, response):
        """解析根据rule过滤的下一页链接对应的列表页，提取详情页url加入调度器
        一定要加dont_filter=True，否则所有详情页url会被当做重复域名过滤掉"""
        link = LinkExtractor(allow='.*?/article/.*/.*\.html', restrict_xpaths='//*[@id="rank-defList"]/div/div/div/h3')
        links = link.extract_links(response)
        for detail_url in links:
            yield Request(url=detail_url.url, callback=self.parse_item, dont_filter=True)
