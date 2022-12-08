
import motor.motor_asyncio
from pymongo import MongoClient

client_asincrono = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://carlos:Micro2020@cluster0.rxxyl.mongodb.net/?retryWrites=true&w=majority/test")
client_sincrono = MongoClient("mongodb+srv://carlos:Micro2020@cluster0.rxxyl.mongodb.net/?retryWrites=true&w=majority/test")