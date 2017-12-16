#!/usr/bin/env python
#-*-coding:utf-8-*-
import pymongo

class DbMan():

    def __init__(self):

        self.client = pymongo.MongoClient('localhost',27017)
        self.db = self.client['lagou']
        pass

    def get_position_info(self):

        position_collection = self.db['position']
        
        print('到这里')
        for i in self.db.position.find({}):
            print i
            print type(i)

        pass



if "__name__" =="__main__":

    x = DbMan()
    x.get_position_info()
