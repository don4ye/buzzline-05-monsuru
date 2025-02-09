#  Real-Time Sentiment Analysis with Kafka & SQLite

##  Project Overview
This project processes real-time sentiment data using **Kafka** for message streaming and **SQLite** for structured storage. The goal is to analyze sentiment trends across different categories and visualize insights using **Matplotlib**.

##  Custom Kafka Consumer
The custom consumer **reads messages from a Kafka topic**, extracts relevant data (timestamp, category, sentiment), and stores it in an **SQLite database** for further analysis. This allows tracking sentiment trends over time to detect shifts in public opinion.

##  Insights Stored
The consumer processes each message and stores:
- **timestamp** → Tracks when the message was received.
- **category** → Groups sentiment by topic.
- **sentiment** → Helps analyze trends and mood shifts.

##  Setup & Installation
### 1️⃣ **Clone the Repository**
```bash
git clone <https://github.com/don4ye/buzzline-05-monsuru>

## Create & Activate Virtual Environment

python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate  # Windows

## Install Dependencies

pip install -r requirements.txt

## Start Kafka & Zookeeper

zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties

## How to Run the Producer & Consumer
  # Run the Producer (Generates Sentiment Data)

python -m producers.producer_case

## Run the Custom Consumer (Processes & Stores Data)

python -m consumers.consumer_monsuru

## Visualization of Sentiment Trends

python visualize_sentiment.py

