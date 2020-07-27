# -*- coding:utf-8 -*-
__Author__ = "KrianJ wj_19"
__Time__ = "2020/7/26 18:49"
__doc__ = """ """

from tech_china.settings import COLLECTION


def china_tech():
    """获取china_tech.json中的start_urls"""
    start_url = 'https://tech.china.com/' + COLLECTION + '/index.html'
    yield start_url