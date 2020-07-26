# -*- coding:utf-8 -*-
__Author__ = "KrianJ wj_19"
__Time__ = "2020/7/26 18:49"
__doc__ = """ """

from tech_china.settings import COLLECTION


def china_tech(start, end):
    for page in range(start, end+1):
        yield 'https://tech.china.com/' + COLLECTION + '/index_' + str(page) + '.html'