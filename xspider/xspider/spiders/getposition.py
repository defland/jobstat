# -*- coding: utf-8 -*-
import scrapy
import random
from scrapy.selector import Selector
from xspider.items import Position_Info
from cprint import cprint 
import re
import time

class GetpositionSpider(scrapy.Spider):
    name = 'getposition'
    allowed_domains = ['lagou.com']
    start_urls = ['http://lagou.com/']

    handle_httpstatus_list = [302] 
    meta = {'dont_redirect':True,'handle_httpstatus_list':[302,404,301,502,403]}

    # 轮转headers头部
    def rotate_headers(self):
        headers = {}
        a = r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:54.0) Gecko/20100101 Firefox/54.0"
        b = r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        c = r"Opera/9.27 (Windows NT 5.2; U; zh-cn)"
        d = r"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)"
        e = r"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
        f = r"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
        g = r"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"
        h = r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
        user_agent_list= [a,b,c,d,e,f,g,h]
        print("正在构建请求报头")
        headers["User-Agent"] =  user_agent_list[random.randint(0,7)]
        return headers
    def read_position_url_for_file(self):
        try:
            with open("position_url.txt","r") as f:

                url_list = []
                url = f.readline().replace("\n",'') # 没行读取URL,并且去掉\n
                while url:
                    # 不停地额返回网址
                    url_list.append(url)
                    url = f.readline().replace("\n",'')

                return url_list

        except Exception as e:
           print "---------没有找到这个文件--------"
           return False

    # 重新start_request方法，构建请求
    def start_requests(self):
       
        # # 正式用 
        # # 从文件读取url列表：
        url_list = self.read_position_url_for_file()
        
        for url in url_list:
            headers = self.rotate_headers()
            yield scrapy.Request(url=url,callback=self.parse,meta=self.meta)
        
        # 调试，只访问单个网页
        # headers = self.rotate_headers()
        # yield scrapy.Request(url="http://m.lagou.com/jobs/3318392.html",headers=headers)
    
    def retry_request(self,response):
        # 这里处理，如果状态码失败，则重新请求。
        print("=======response.url========")
        print("状态码为：%s：" % response.status)
        print response.url
        print("=======response.url========")
        if response.status == 302:
            return False
        elif response.status in [403,500,501,502]:
            print("遇到错误:%s" % response.status)
            return False
        elif response.status == 200:
            return True



    def get_position_date(self,items,response):

        # 收到符合条件的数据才解析
        # print("====================response包体打印======================")
        # print response.body
        # print("====================response包体打印======================")  

        is_blank_page = re.findall(r'.*(页面加载).*', response.body) # 如果下载到空白页就是页面加载中
        if is_blank_page != [] :
            # 说明反爬虫机制，这一次下载的是空页面。
            print("本次下载为空白页")
            return items
        else:
            # 拿到完整的网页数据
            # 使用Seletors的xpath选择器，返回时符合条件的列表[]。
            # 标题

            items["position_name"] = Selector(response).xpath(r"//*[@id='content']/div[1]/h2/text()").extract()[0]

            # 公司
            items["position_company"] = Selector(response).xpath(r"//div[@class='dleft']/h2/text()").extract()[0].strip()

            # 薪资
            items["position_pay"] = Selector(response).xpath(r"//span[@class='item salary']/span/text()").extract()[0]

            # 地区：
            items["position_location"] = Selector(response).xpath(r"//span[@class='item workaddress']/span/text()").extract()[0]

            # 职位详情,需要list里面的关键字来拼接成str
            xpstr = r'//*[@id="content"]/div[4]/div/text()|//*[@id="content"]/div[4]/div/*/text()|//*[@id="content"]/div[4]/div/*/*/text()'
            detail_list = Selector(response).xpath(xpstr).extract()
            # 有2中情况，一种是<p>内容,另外是<p><span>内容，大部分是第一种
            # if detail_list == []:
            #     detail_list = Selector(response).xpath(r'//*[@id="content"]/div[4]/div/*/*/text()').extract()   
            detail_str = ''
            for keyword in detail_list: # 返回来是列表的字段，需要拼接成str
                detail_str = detail_str  + keyword 
            items["position_detail"] = detail_str.strip()

            # 把url也保存起来
            items['position_url'] = response.url

            return items
    

    def parse(self, response):
        
        # 遇到302错误就重新放入request队列
        if self.retry_request(response) == False:
            # time.sleep()
            return scrapy.Request(url=response.url,callback=self.parse,meta=self.meta)
        else:            
            # print response.body
            # 定义数据字典
            items = Position_Info()
            # 分析出来放到items
            itmes = self.get_position_date(items, response)
      
            # 打印
            for i in items.items():
                cprint(i)
            return items




        
