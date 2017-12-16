# -*- coding: utf-8 -*-

# Scrapy settings for xspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xspider'
LOG_LEVEL = 'INFO'

SPIDER_MODULES = ['xspider.spiders']
NEWSPIDER_MODULE = 'xspider.spiders'

# 并发数量
CONCURRENT_REQUESTS = 200

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xspider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)

COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xspider.middlewares.LagouSpiderV1SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,

    # 'scrapy.downloadermiddlewares.retry.RetryMiddleware': 500, 
    'xspider.middlewares.RotateHeadersMiddleware': 543, # 轮转头部
    # 'xspider.middlewares.DelayDownloadMiddleware': 600,
    'xspider.middlewares.ProxyMiddleware': 700, # 设置代理IP信息
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 710, # 启用代理访问
    # 'xspider.middlewares.ReDownloadMiddleware': 1000, # 下载重试


}

# scrapy默认会过滤掉200-300之外的response，这个允许这些response返回到prase方法中
HTTPERROR_ALLOWED_CODES = [403,404,302,500,505,501,502]


# 禁用重定向
REDIRECT_ENABLED = True

#开启重试下载中间件
RETRY_ENABLED = True
RETRY_TIMES = 5
RETRY_HTTP_CODES =[500, 502, 503, 504, 400, 408,404]


#下载延迟
# DOWNLOAD_DELAY = 0.25 

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'xspider.pipelines.PositionPipeline': 1,
   # 'xspider.pipelines.DbPipeline': 2
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 15 # 延迟下载
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
