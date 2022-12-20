
import motor.motor_asyncio
from pymongo import MongoClient
import os
#from bson.objectid import ObjectId

client_asincrono = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://carlos:Micro2020@cluster0.rxxyl.mongodb.net/?retryWrites=true&w=majority")
client_sincrono = MongoClient("mongodb+srv://carlos:Micro2020@cluster0.rxxyl.mongodb.net/?retryWrites=true&w=majority")
#client_asincrono = motor.motor_asyncio.AsyncIOMotorClient(os.environ["DB_URL"])
#client_sincrono = MongoClient(os.environ["DB_URL"])


# database = client.socies

# socie_collection = database.get_collection("socies_collections")