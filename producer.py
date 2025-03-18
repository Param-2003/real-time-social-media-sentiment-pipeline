import tweepy
from kafka import KafkaProducer
import json

# Twitter API Credentials
BEARER_TOKEN = "YOUR_TWITTER_BEARER_TOKEN"

# Kafka Config
KAFKA_TOPIC = "tweets"
KAFKA_BROKER = "localhost:9092"

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

# Twitter Streaming Class
class TwitterStream(tweepy.StreamingClient):
    def on_data(self, raw_data):
        tweet = json.loads(raw_data)
        if "data" in tweet:
            tweet_data = {
                "user": tweet["data"].get("author_id", "Unknown"),
                "text": tweet["data"].get("text", ""),
                "timestamp": tweet["data"].get("created_at", ""),
            }
            print("Tweet Received:", tweet_data)
            producer.send(KAFKA_TOPIC, tweet_data)
        return True

    def on_error(self, status_code):
        print("Error:", status_code)
        return False

if __name__ == "__main__":
    stream = TwitterStream(BEARER_TOKEN)
    stream.add_rules(tweepy.StreamRule("python"))  # Fetch tweets related to Python
    print("🔥 Streaming tweets...")
    stream.filter()
