# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random,time
from xspider.spiders.getposition import GetpositionSpider
from xspider.spiders.geturl import GeturlSpider
import json,urllib2,re

import ippool

class RotateHeadersMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    def __init__(self):

        self.user_agent_list = [
        r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:54.0) Gecko/20100101 Firefox/54.0",
        r"Opera/9.27 (Windows NT 5.2; U; zh-cn)",  
        r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",  
        r"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",  
        r"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",  
        r"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",  
        r"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",  
        r"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",  
        r"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",  
        r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", 
        r"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",  
        r"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", 
        r"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",  
        r"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",  
        r"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",  
        r"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",  
        r"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",  
        r"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"  
        ] 

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

    
    def process_request(self,request,spider):

    # 把传过来的request处理掉，{'User-Agent': 'Opera/9.27 (Windows NT 5.2; U; zh-cn)'}
        pass
        print "----------头部信息----------"
        print request.headers

        # 替换掉：
        # request.headers.setdefault('User-Agent', random.choice(self.agents))
        # request.headers.setdefault('User-Agent',self.user_agent_list[random.randint(0,len(self.user_agent_list))-1])
        request.headers["User-Agent"] = random.choice(self.user_agent_list)

        print "---------替换后----------"
        print request.headers

    def process_response(self,request,response,spider):
        pass
        return response


class DelayDownloadMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    def __init__(self):

        self.sleeptime = random.randint(0,5)


    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

    
    def process_request(self,request,spider):

        # 延迟
        if isinstance(spider,GetpositionSpider):
            time.sleep(self.sleeptime)
      
        return None


    def process_response(self,request,response,spider):
        pass
        return response

# IP代理
class ProxyMiddleware(object):

    # 类变量
    ip_list = []
    make_ip_list_is_run = False # 保证只访问一次API获取IP


    def __init__(self):
        pass
        
    def make_ip_list_for_apis(self):

        # 通过网上api，提取到何时的ip地址和端口，保证只运行一次。
        if self.make_ip_list_is_run == False:

            print("------正在访问API----------")
            ip_response = urllib2.urlopen(r"http://dev.kuaidaili.com/api/getproxy/?orderid=960107510336959&num=100&b_pcchrome=1&b_pcie=1&b_pcff=1&b_android=1&b_iphone=1&protocol=1&method=2&an_an=1&an_ha=1&sp1=1&sp2=1&quality=1&sort=1&format=json&sep=1")
            api_str = ip_response.read()
            ip_addr_list = re.findall(r'"(\d+.\d+.\d+.\d+:\d+)"', api_str)
            for one_ip in ip_addr_list:
                url = r"http://%s" % (one_ip)
                self.ip_list.append(url)
            
            self.make_ip_list_is_run = True

            return self.ip_list
        else:
            print("已经访问过API了")
            return self.ip_list
    def make_ip_list_for_ippool(self):
        # 调用自己写的库
        if self.make_ip_list_is_run == False:
            # 通过自己库获取IP
            x = ippool.IpSpiders()
            ip_addr_list = x.get_ip()
            for one_ip in ip_addr_list:
                url = "http://%s:%s" % (one_ip['ip'],one_ip['port'])
                self.ip_list.append(url)
            self.make_ip_list_is_run = True
        else:
            print("已经访问过API了")
            return self.ip_list

    def process_request(self,request,spider):
        # 设置代理

        if isinstance(spider, GeturlSpider):
            return None

        flag = random.choice([1,10])
        if flag == 0:
            print("------不用代理---------")
            print("-----------request.meta 和 headers------------")
            print request.meta
            print request.headers
            print("-----------request.meta 和 headers------------")
            return None
        else:
            print("------使用代理---------")
            x = self.make_ip_list_for_ippool()
            print("-----------------IP池-----------")
            print x 
            print("-----------------IP池-----------")

            request.meta["proxy"] = random.choice(self.ip_list)
            print("-----------request.meta 和 headers------------")
            print request.meta
            print request.headers
            print("-----------request.meta 和 headers------------")

        # pass
        return None


    def process_response(self,request,response,spider):
    
        return response



# 遇到非200的的response，再次换IP发起请求，提高成功率
class ReDownloadMiddleware(object):

    def __init__(self):
        pass
    def process_request(self,request,spider):

        return None

    def process_response(self,request,response,spider):
        # 检查头部 - > 没问题就通过，有问题重新request
  
        print("-------中间件状态判断-----")
        status =  response.status
        print response.status
        print response.headers
        # print response.meta
        # print response.request.headers
        # print response.request.meta
        print(type(status))
        flag = (status == 200)
        print flag
        print("-------中间件状态判断-----")

        if response.status == 302:

            print "状态码为302"
            return request

        return request

        
        # if response.status:
        #     return response
        # else:
        #     print("状态为%s,重新发送请求" % str(status))
        #     # return request

        # # no_pass = [301,302,404,400,500,502,301]
        # # print("-------状态判断-----")
        # # print(status)
        # # print(response.headers)
        # # print("-------状态判断-----")

        # if status == 200:
        #     print("-----通过检查-------")
        #     return response
        # else:
        #     print("状态为%s,重新发送请求" % str(status))
        #     # time.sleep(3)
        #     return request
        





