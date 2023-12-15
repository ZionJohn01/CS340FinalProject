from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    def __init__(self, username, password, host, port, db_name, collection_name):
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}/{db_name}')
        self.database = self.client[db_name]
        self.collection = self.database[collection_name]
    
    def create(self, data):
        if data:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"Failed to insert document: {e}")
                return False
        else:
            raise Exception("Nothing to save. Data parameter is empty")
    
    def read(self, query):
        try:
            result = list(self.collection.find(query))
            return result
        except Exception as e:
            print(f"Failed to read document: {e}")
            return []
    
    def update(self, query, update_data):
        try:
            result = self.collection.update_many(query, {'$set': update_data})
            return result.modified_count
        except Exception as e:
            print(f"Failed to update document: {e}")
            return 0
    
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Failed to delete document: {e}")
            return 0
    
    def filter_by_rescue_type(self, rescue_type):
        try:
            print(f"Filtering by rescue type: {rescue_type}")
            
            if rescue_type == 'water_rescue':
                query = {'rescue_type': 'water_rescue'}
            elif rescue_type == 'mountain_wilderness':
                query = {'rescue_type': 'mountain_wilderness'}
            elif rescue_type == 'disaster_tracking':
                query = {'rescue_type': 'disaster_tracking'}
            else:
                query = {}  # Default: no filtering
            
            print(f"Constructed query: {query}")
            
            result = list(self.collection.find(query))
            return result
        except Exception as e:
            print(f"Failed to filter data by rescue type: {e}")
            return []