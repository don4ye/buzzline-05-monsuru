import json
import sqlite3
import os
from kafka import KafkaConsumer

# Get absolute path to the database file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the directory of this script
DB_PATH = os.path.join(BASE_DIR, "..", "data", "buzz.sqlite")  # Construct full path

# Connect to SQLite database
conn = sqlite3.connect(DB_PATH)  
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS sentiment_analysis (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    category TEXT,
                    sentiment REAL
                )''')
conn.commit()

# Kafka settings
KAFKA_TOPIC = "buzzline_db"  # Your Kafka topic name
KAFKA_SERVER = "localhost:9092"  # Adjust if using a different address

# Create Kafka consumer
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def process_message(msg):
    """Process and store a single Kafka message."""
    timestamp = msg.get("timestamp", "")
    category = msg.get("category", "unknown")
    sentiment = msg.get("sentiment", 0.0)

    cursor.execute('''INSERT INTO sentiment_analysis (timestamp, category, sentiment)
                      VALUES (?, ?, ?)''', (timestamp, category, sentiment))
    conn.commit()

    print(f"Stored: {timestamp} | {category} | Sentiment: {sentiment}")

# Consume messages from Kafka
for message in consumer:
    process_message(message.value)
