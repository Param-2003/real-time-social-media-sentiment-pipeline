from kafka import KafkaConsumer
from pymongo import MongoClient
import json

# MongoDB Config
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "twitterDB"
COLLECTION_NAME = "tweets"

# Kafka Config
KAFKA_TOPIC = "tweets"
KAFKA_BROKER = "localhost:9092"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Kafka Consumer
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset="earliest",
    #value_deserializer=lambda v: json.loads(v.decode("utf-8")),
)

print("🛠️ Waiting for tweets...")
for message in consumer:
    tweet = message.value
    print("✅ Storing tweet:", tweet)
    collection.insert_one(tweet)
