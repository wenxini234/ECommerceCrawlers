#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'AJay'
__mtime__ = '2019/4/15 0015'

"""


from pymongo import MongoClient, ASCENDING
from settings import MONGO_PORT, MONGO_IP


class Mongo():
    def __init__(self, ip=MONGO_IP, port=MONGO_PORT):
        conn = MongoClient(ip, port)
        self.db = conn.taobao
        self.collection = self.db.userinfo
        self.collection.create_index([('nid', ASCENDING)])

    def insert(self, item_dict):
        self.collection.insert_one(item_dict)

    def select(self,dict):
        return  self.collection.find(dict)
    def select_one(self,dict):
        return  self.collection.find_one(dict)

    def delete(self, query_dict):
        self.collection.delete_one(query_dict)
    def delete_all(self,dict):
        self.collection.delete_many(dict)
    def count(self):
        self.collection.count_documents({})

# db =Mongo()
#
# db.insert({"user":"15993248973","password":"Bu19951218."})