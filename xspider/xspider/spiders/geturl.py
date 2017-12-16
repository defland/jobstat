# -*- coding: utf-8 -*-
import scrapy
import urllib2,re
from cprint import cprint 
from xspider.items import Position_Url_List 
from scrapy.selector import Selector

class GeturlSpider(scrapy.Spider):
    name = 'geturl'
    allowed_domains = ['lagou.com']

    start_urls = ['http://lagou.com/']

    # 定义要爬的岗位地区和关键字
    city = urllib2.quote("广州")
    position_keyword = urllib2.quote("python")

    # 获取分页链接的方法只能执行一次，这里做个标志
    get_paging_url_is_run = False

    # 重写start_requests():
    def start_requests(self):

        # 第一个url
        url =r"http://m.lagou.com/search.json?city=" + self.city + "&positionName=" + self.position_keyword + "&pageNo=1&pageSize=15"
        yield self.make_requests_from_url(url)

    def get_paging_url(self,response):

        # 把分页的url组建起来。
        paging_url_list = []
        all_position_count = re.findall(r".totalCount.:.(\d+).", response.body)[0] #岗位数量,正则从json里面提取 "totalCount":."231"提取出来数量
        paging_number = int(all_position_count)/15 + 1 # 分页数量
        print "岗位数量为：" + all_position_count[0]
        print "分页数量：" + str(paging_number)

        # 组件url
        for i in range(1,paging_number + 1):
            url =r"http://m.lagou.com/search.json?city=" + self.city + "&positionName=" + self.position_keyword + "&pageNo="+ str(i) +"&pageSize=15"
            paging_url_list.append(url) # 添加到列表中

        print paging_url_list
        print "已经运行了！！！！！！！！！"
        return {"url":paging_url_list,"position_count":all_position_count}

    def get_position_url(self,response):
        # 这个方法把response里面的positionid正则拿出来，构造url
        
        print "----------此分页职位ID正在获取中---------------"
        url = []
        # 因为是json字符串，就不用scrapy的选择器了，用re
        # http://m.lagou.com/jobs/3119907.html 
        url_list = re.findall(r".positionId.:(\d+),", response.body)
        
        for i in url_list:
            position_url = r"http://m.lagou.com/jobs/"+ i + ".html" 
            url.append(position_url)
        
        return url


    def get_url_sub_parse(self,response):

        # 这个专门用来处理所有分页的url构建
        items = Position_Url_List()
        items["position_url"] = self.get_position_url(response) 
        print(items) 
        return items

    def parse(self, response):
        # 回调，处理response对象
        # 思路：拿到第一个response,获取分页链接。 -> 例如拿8分页链接，加入下载队列中。
        print("--------打印内容---------")
        print(response.body)

        # 一、获取剩余分页url和再次请求request 
        # 获取分页的其他url，
        url_dict = {"url":False}
        if self.get_paging_url_is_run == False:
            url_dict = self.get_paging_url(response) # 让这个函数只执行一次
            print(url_dict["position_count"])
            # 把分页的url构造成request，丢给scrapy继续爬,下载到的respose继续给这个parse函数处理

            paging_url_list = url_dict["url"]
            if paging_url_list != []: # 这样做防止分页在还在用这个方法
                cprint(paging_url_list)
                for url in paging_url_list:
                    yield scrapy.Request(url=url,callback=self.get_url_sub_parse)
            # 保证只执行一次。
            self.get_paging_url_is_run = True

        # # 二、提取数据
        # # 把里面的职位id数据拿出来，构造成职位详情页的url
        # # 每个items保存了多个职位的url
        # items = Position_Url_List()
        # items["position_url"] = self.get_position_url(response) 
        # print(items) 

        # # 这段也不是很理解，但是不能直接return，需要用yield 返回，再加return 
        # yield items
        # return









