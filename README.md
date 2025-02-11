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
###  **Clone the Repository**
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
### Run the Producer (Generates Sentiment Data)

python -m producers.producer_case

## Run the Custom Consumer (Processes & Stores Data)

python -m consumers.consumer_monsuru

## Visualization of Sentiment Trends

python visualize_sentiment.py


## Save Space

To save disk space, you can delete the .venv folder when not actively working on this project. You can always recreate it, activate it, and reinstall the necessary packages later. Managing Python virtual environments is a valuable skill.

## License

This project is licensed under the MIT License as an example project. You are encouraged to fork, copy, explore, and modify the code as you like. See the LICENSE file for more.