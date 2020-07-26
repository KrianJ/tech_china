# -*- coding:utf-8 -*-
__Author__ = "KrianJ wj_19"
__Time__ = "2020/7/26 13:26"
__doc__ = """ """
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

rules = {
    'china_tech': (
        Rule(LinkExtractor(allow='.*?/article/.*/.*\.html', restrict_xpaths='//div[@class="wntjItem item_defaultView clearfix"]//h3[@class="tit"]'),
             callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pages"]//a[contains(., "下一页")]'), follow=True)
    )
}