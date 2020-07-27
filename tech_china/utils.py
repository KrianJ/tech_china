# -*- coding:utf-8 -*-
__Author__ = "KrianJ wj_19"
__Time__ = "2020/7/26 13:32"
__doc__ = """ 获取通用爬虫的基本配置,即config.py"""

from os.path import realpath, dirname
import json


def get_config(name):
    """获取配置文件"""
    path = dirname(realpath(__file__)) + '/configs/' + name + '.json'
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
