# -*- coding:utf-8 -*-
__Author__ = "KrianJ wj_19"
__Time__ = "2020/7/26 12:58"
__doc__ = """ ItemLoader类"""

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, Compose


class NewsLoader(ItemLoader):
    # 相当于extract_fisrt()
    default_output_processor = TakeFirst()


class ChinaTechLoader(NewsLoader):
    """继承NewsLoader"""
    # Join()将列表拼接成字符串，lambda xxxx: 去掉前后空白字符
    text_out = Compose(Join(), lambda s: s.strip())
    source_out = Compose(Join(), lambda s: s.strip())
