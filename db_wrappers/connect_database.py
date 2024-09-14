import pymongo
from pymongo import MongoClient
from config import CLUTER_NAME, CLUTER_PASSWORD


db = cluster["UserData"]
collection = db["Flask_mongo"]

class ConnectDatabase:


    def __init__(self):
        """configure database"""
        self.cluster = MongoClient("mongodb+srv://"+CLUTER_NAME+":"+CLUTER_PASSWORD+"@cluster0.rqeps.mongodb.net/")
    
    def get_db(self,dbname):
        """Retrieve a database"""
        return self.cluster[dbname]

    def get_collection(self, dbname, collection_name):
        """Retrieve a collection from the database"""
        db = self.get_db(dbname)
        return db[collection_name]

    def close_connection(self):
        self.cluster.close()
        