"""
Created on Wed Nov  4 04:41:54 2020

@author: nirviksaha
"""

from pymongo import MongoClient


class Database(object):
    def __init__(self):
        self.filename = "temp"
        self.mongo_uri = "mongodb+srv://ns:Root@cluster0.wwegb.mongodb.net"
        self.client = MongoClient(self.mongo_uri)
        try:
            self.db = self.client['ifcproj']  # db=client['ifcproj']
            print('connected to db...')
        except:
            print('ERROR connecting to db...')

    def create_records(self, filename):
        print("create")
        self.filename = filename
        try:
            k = 0
            data = ""
            with open("tmpIfcFile.ifc", "r") as reader:
                for line in reader.readlines():
                    data += line + "\n"
                    k += 1
            key = "data"
            num_lines= "num_lines"
            entry = {key: data, num_lines: k}
            self.db.temp.insert_one(entry)
            self.db.temp.rename(self.filename)
            print('write to db process complete')
        except:
            print('ERROR writing to db...')

    def get_collections(self):
        db_names = self.client.list_databases()
        # for i in db_names:
        # print(i)
        # we want : self.db = ifcproject
        db_collections = self.db.list_collections()
        li_db_coll_names = []
        for i in db_collections:
            li_db_coll_names.append(i)
        return li_db_coll_names

    def read_records(self, filename):
        print("READ --> FILTER")
        cursor = self.db[filename].find({})
        data=""
        for document in cursor:
            data=document['data']
        return data

    def update_records(self, initial_name, final_name):
        print("UPDATE")
        r = self.db.data.update_many({"name": initial_name}, {"$set": {"name": "changed"}})
        r = self.db.data.find()
        for i in r:
            print(i)

    def delete_records(self):
        print("DELTE")
        r = self.db.data.find({"name": "changed"})
        self.db.data.delete(r)
        self.print_all_records()

    def print_all_records(self):
        print("READ & PRINT ALL")
        r = self.db.find()
        for i in r:
            print(i)

