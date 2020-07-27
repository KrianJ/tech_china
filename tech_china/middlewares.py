# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import requests


class ProxyMiddleware:
    __doc__ = """为整个爬虫项目获取随机代理"""

    @classmethod
    def get_proxy(self):
        """从代理池获取随机代理"""
        proxypool_url = 'http://127.0.0.1:5555/random'
        return requests.get(proxypool_url).text.strip()

    def process_request(self, request, spider):
        request.meta['http_proxy'] = self.get_proxy()
        print("正在使用代理：", request.meta['http_proxy'])
