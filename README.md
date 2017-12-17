# jobstat

之前学习scrapy写了一个lagou的爬虫，做到了可爬取任意岗位的全国所有岗位数据。最近在学习web开发，正好借机会实践一波，利用django+scrapy，把抓取到的数据进行可视化分析，做统计数据的WEB展示。


# 技术栈

数据源爬取：Scrapy + Mongodb 

二次数据分析：结巴分词

WEB后端展示：Django + RESTful API + Postgre

WEB前端:Flask + Jinja2渲染 + Redis

部署基于Centos7 + Gunicorn(gevent)。


# 实现需求


