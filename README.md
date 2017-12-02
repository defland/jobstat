# YJobsCrawler

基Scrapy + MongoDB + 代理IP池 求职岗位定向爬虫。


# 实现需求

- 定向爬取lagou.com的职位信息，任意关键字的所有岗位信息。如全国地区Python工程师。
- 爬取到的数据可以导出为excel/或者存入Mongodb中。
- 实现request header user-agent轮转。
- 利用FreeIPAgentPool.py，获取一个免费可用的IP代理池，100个request可以轮转xx个免费IP访问，避免单个IP频繁访问被和谐。
