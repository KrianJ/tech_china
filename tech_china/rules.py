# -*- coding:utf-8 -*-
__Author__ = "KrianJ wj_19"
__Time__ = "2020/7/26 13:26"
__doc__ = """ """
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from tech_china.configs.rule_component import process_value

"""定制爬取规则"""
rules = {
    # china_tech的爬取规则
    'china_tech': (
        Rule(LinkExtractor(allow='.*?/article/.*/.*\.html', restrict_xpaths='//*[@id="rank-defList"]/div/div/div/h3'),
             callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pages"]//a[contains(., "下一页")]',
                           process_value=lambda x: process_value(x)), follow=True, callback='parse_next_url')
    )
}
