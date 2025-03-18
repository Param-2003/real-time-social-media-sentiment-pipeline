from kafka import KafkaConsumer
import json
from pymongo import MongoClient 

#connecting to mongodb
mongo_client = MongoClient("mongodb://root:example@localhost:27017/")
db = mongo_client ["twitterDB"]
collection = db["tweets"]

#kafka consumer
consumer = KafkaConsumer(
    'raw-data',
    bootstrap_servers= "localhost:9092",
    auto_offset_reset = "earliest",
    enable_auto_commit=True, 
    group_id="twitter-group",
    #value_deserializer=lambda x: json.loads(x.decode("utf-8"))if x else None 
)

print("waiting for tweets")

#store consumed data to Mongo
for message in consumer:
    raw_data = message.value  # This is the data from Kafka
    print(f"Raw data from Kafka: {raw_data}")  # Debugging

    if not raw_data:  
        print("⚠️ Received empty message. Skipping...")
        continue  # Skip processing empty messages

    try:
        tweet = json.loads(raw_data.decode("utf-8"))  
        print(f"Decoded tweet: {tweet}")  
        collection.insert_one(tweet)  # Store in MongoDB
    except json.JSONDecodeError as e:
        print(f"❌ JSON Decode Error: {e} - Raw Data: {raw_data}")


