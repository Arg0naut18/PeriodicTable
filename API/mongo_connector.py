import os
from pymongo.mongo_client import MongoClient


class Connector:
    def __init__(self):
        self._mongo_username = os.getenv("MONGO_USERNAME", "admin")
        self._mongo_password = os.getenv("MONGO_PASSWORD")
        self._uri = f"mongodb+srv://{self._mongo_username}:{self._mongo_password}@cluster0.7tdrigg.mongodb.net/?retryWrites=true&w=majority"
        self._client = MongoClient(self._uri)
        assert self.ping()
        self._db = self._client["PeriodicTable"]
        self._data = self._db["Elements"]

    def ping(self):
        try:
            self._client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
            return True
        except Exception as e:
            print(e)
            return False

    def get_data(self):
        return self._data.find(projection={"_id": 0})
