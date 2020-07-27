# -*- coding:utf-8 -*-
__Author__ = "KrianJ wj_19"
__Time__ = "2020/7/26 18:49"
__doc__ = """ 为爬虫的配置文件（.json）提供start_urls的value，即爬取规则"""

from tech_china.settings import COLLECTION, DIGI_COLLECTION


def china_tech():
    """获取china_tech.json中的start_urls"""
    start_url = 'https://tech.china.com/' + COLLECTION + '/index.html'
    yield start_url

def china_digi():
    """获取china_digi.json中的start_urls"""
    start_url = 'https://digi.china.com/' + DIGI_COLLECTION + '/index.html'
    yield start_url