"""
User DAO for MongoDB
"""
import os
from dotenv import load_dotenv
from models.user import User
from pymongo import MongoClient
from bson.objectid import ObjectId


class UserDAOMongo:
    def __init__(self):
        try:
            env_path = "./.env"
            print(os.path.abspath(env_path))
            load_dotenv(dotenv_path=env_path)

            mongo_host = os.getenv("MONGODB_HOST", "localhost")
            mongo_port = 27017
            mongo_db_name = os.getenv("MYSQL_DB_NAME", "mydb")
            mongo_username = os.getenv("DB_USERNAME")
            mongo_password = os.getenv("DB_PASSWORD")
            
            connection_string = f"mongodb://{mongo_username}:{mongo_password}@{mongo_host}:{mongo_port}/{mongo_db_name}?authSource=admin"
            self.client = MongoClient(connection_string)
            
            self.db = self.client[mongo_db_name]
            self.collection = self.db.users
            
        except FileNotFoundError as e:
            print("Attention : Veuillez créer un fichier .env")
        except Exception as e:
            print("Erreur : " + str(e))

    def select_all(self):
        """ Select all users from MongoDB """
        documents = self.collection.find()
        users = []
        for doc in documents:
            user_id = str(doc.get('_id'))
            name = doc.get('name')
            email = doc.get('email')
            users.append(User(user_id, name, email))
        return users

    def insert(self, user):
        """ Insert given user into MongoDB """
        document = {
            'name': user.name,
            'email': user.email
        }
        result = self.collection.insert_one(document)
        return str(result.inserted_id)

    def update(self, user):
        """ Update given user in MongoDB """
        object_id = ObjectId(user.id)
        filter_criteria = {'_id': object_id}
        update_data = {
            '$set': {
                'name': user.name,
                'email': user.email
            }
        }
        result = self.collection.update_one(filter_criteria, update_data)
        return result.modified_count

    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        object_id = ObjectId(user_id)
        filter_criteria = {'_id': object_id}
        
        result = self.collection.delete_one(filter_criteria)
        return result.deleted_count

    def delete_all(self):
        """ Empty users collection in MongoDB """
        result = self.collection.delete_many({})
        return result.deleted_count

    def close(self):
        """ Close MongoDB connection """
        self.client.close()
