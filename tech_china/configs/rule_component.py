# -*- coding:utf-8 -*-
__Author__ = "KrianJ wj_19"
__Time__ = "2020/7/27 11:35"
__doc__ = """ Rule对象的参数设置"""


def process_value(url):
    """process_value参数，解决重定向"""
    try:
        url = url.replace('http', 'https')
        return url
    finally:
        return url