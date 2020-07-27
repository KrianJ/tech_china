# -*- coding:utf-8 -*-
__Author__ = "KrianJ wj_19"
__Time__ = "2020/7/27 11:35"
__doc__ = """ """


def process_value(url):
    try:
        url = url.replace('http', 'https')
        return url
    finally:
        return url