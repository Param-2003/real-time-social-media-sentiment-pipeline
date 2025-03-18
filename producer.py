import json
import time
from faker import Faker
from kafka import KafkaProducer

# Kafka Configuration
KAFKA_BROKER = "localhost:9092"
TOPIC = "raw-data"

# Initialize Faker for generating fake tweets
fake = Faker()

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

# Function to generate fake tweets
def generate_fake_tweet():
    return {
        "user": fake.name(),
        "text": fake.sentence(),
        "timestamp": str(fake.date_time_this_year()),
    }

# Send Fake Tweets
if __name__ == "__main__":
    while True:
        tweet = generate_fake_tweet()
        producer.send(TOPIC, tweet)
        print("Sent:", tweet)
        time.sleep(2)  # Send a tweet every 2 seconds
