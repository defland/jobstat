#!/usr/bin/python
#-*-coding:utf-8-*-

import jieba
from jieba import analyse
from cprint import cprint
import re
from read_for_db import DbMan


def print_txt(txt_list):

    cprint(txt_list)



def keyword(txt):
    keyword_list = []


    keyword_list = jieba.analyse.extract_tags(txt)

    pass
    return keyword_list
def seg(txt):

    seg_list = jieba.cut(txt,cut_all=False)
    print(type(seg_list))

    return seg_list


def read_txt():

    pass
    return True


if __name__ == "__main__":

    txt = "职位描述： \n1、负责机器学习算法的线上布置和生产环境安全；\n2、负责数据计算平台的设计与研发；  \n3、负责数据计算平台的运营维护，推进标准化运维，提升运维质量。\n\n任职要求： \n1、本科以上学历计算机相关专业，有Python相关开发工作经验； \n2、熟悉MySQL数据库的使用与性能优化，熟悉NoSQL（Redis与MongoDB）者优先； \n3、熟悉MVC架构，精通Tornado、Django或Flask等web框架； \n4、熟悉Javascript / HTML / JSON / HTML5 / JQuery /CSS相关技术； \n5、有爬虫开发经验者优先； \n6、有机器学习算法开发经验者优先；\n7、有大数据系统（Hadoop、Hbase）经验者优先。"
        
    # print txt

    p = re.compile("\s")
    txt = p.sub('', txt)

    # print txt


    x = re.compile('\d')
    txt = x.sub('', txt)

    print txt

    print("关键词提取如下：")
    print_txt(keyword(txt))

    print("分词算法")
    x = seg(txt)
    cprint([i for i in x])


    pass