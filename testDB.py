from pymongo import MongoClient
from run import scrapData
import json
import datetime
import uuid
from bson.codec_options import CodecOptions, DEFAULT_CODEC_OPTIONS
from bson.binary import Binary, UuidRepresentation


client = MongoClient(
    "mongodb+srv://sanjith-s:ssanjith@cluster0.h4wpmya.mongodb.net/?retryWrites=true&w=majority")
db = client.test

db = client["scrappedData"]
collection = db["events"]


def pushData():
    print("Scrapping Data...")
    resList = scrapData()
    explicit_binary = Binary.from_uuid(uuid.uuid4(), UuidRepresentation.STANDARD)
    collection.insert_one({"_id": explicit_binary, "data": json.dumps(resList), "ts": datetime.datetime.utcnow()})


pushData()
print("Inserted into db")