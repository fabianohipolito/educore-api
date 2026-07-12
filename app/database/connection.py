import pymongo
from pymongo import MongoClient



class Connection:
    def __init__(self):
        self.client = MongoClient("mongodb://172.20.0.10:27017/educore")
        self.db = self.client["educore"]
        self.collection = self.db["students"]

    def connect_mongo(self):
        self.client.admin.command("ping")

        print("Conectado ao MongoDB com sucesso!")

if __name__ == "__main__":
    app = Connection()
    app.connect_mongo()