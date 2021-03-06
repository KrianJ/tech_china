# -*- coding:utf-8 -*-
__Author__ = "KrianJ wj_19"
__Time__ = "2020/7/26 13:36"
__doc__ = """ 爬虫入口文件"""
import sys
from scrapy.utils.project import get_project_settings
from tech_china.spiders.universal import UniversalSpider
from tech_china.utils import get_config
from scrapy.crawler import CrawlerProcess


def run():
    name = sys.argv[1]
    custom_settings = get_config(name)
    # 爬取使用的spider名称
    spider = custom_settings.get('spider', 'universal')
    project_settings = get_project_settings()
    settings = dict(project_settings.copy())
    # 合并配置
    settings.update(custom_settings.get('settings'))
    process = CrawlerProcess(settings)
    # 启动爬虫
    process.crawl(spider, **{'name': name})
    process.start()


if __name__ == '__main__':
    run()
