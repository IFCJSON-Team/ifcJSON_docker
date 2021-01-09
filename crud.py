#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 04:41:54 2020

@author: nirviksaha
"""

from pymongo import MongoClient
import random

class Database(object):
    def __init__(self):
        print('connecting to db...')
        mongo_uri="mongodb+srv://ns:Root@cluster0.wwegb.mongodb.net"
        client=MongoClient(mongo_uri)
        self.db=client.business # db=client['business']

    def create_records(self, num, suppress=True):
        print("CREATE")
        names=['a','b','c','d','e']
        restaurant_type=['kitchen','restaurant','deli','diner']
        restaurant_cuisine=['pizza','korean','indian']
        for i in range(num):
            restaurant={
                'name':random.choice(names),
                'type':random.choice(restaurant_type),
                'cuisine':random.choice(restaurant_cuisine),
                'rating':random.randint(0,5)
                }
            
            result=self.db.data.insert_one(restaurant)
            if suppress==True:
                print('Created {0} with record id {1}'.format(i, result.inserted_id))
        print('process complete')


    def read_records(self, find_name="", find_type=""):
        print("READ --> FILTER")
        r=self.db.data.find({"name": find_name, "cuisine": find_type})
        for i in r:
            print(i)

    def update_records(self, initial_name, final_name):
        print("UPDATE")
        r=self.db.data.update_many({"name":initial_name}, {"$set":{"name":"changed"}})
        r=self.db.data.find()
        for i in r:
            print(i)

    def delete_records(self):
        print("DELTE")
        r=self.db.data.find({"name":"changed"})
        self.db.data.delete(r)
        self.print_all_records()

    def print_all_records(self):
        print("READ & PRINT ALL")
        r=self.db.find()
        for i in r:
            print(i)
    


num_records=10
DB=Database()
DB.create_records(num_records, False)

find_name="d"
find_type="indian"
print('find all records with name {0}, type {1} and print...'.format(find_name, find_type))
DB.read_records(find_name)


update_ini_name="a"
update_final_name="x"
print('update a records...')
DB.update_records(update_ini_name, update_final_name)


