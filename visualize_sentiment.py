import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect("data/buzz.sqlite")

# Load sentiment data
query = "SELECT timestamp, category, sentiment FROM sentiment_analysis"
df = pd.read_sql(query, conn)

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Improved Plot
plt.figure(figsize=(12, 6))

# Loop through categories and smooth the lines
for category in df["category"].unique():
    subset = df[df["category"] == category]
    plt.plot(
        subset["timestamp"], 
        subset["sentiment"], 
        label=category, 
        marker='o',  # Add markers for clarity
        linestyle='-',  # Use a clean line style
        alpha=0.8  # Add slight transparency for overlapping lines
    )

# Add grid, labels, and title
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlabel("Timestamp")
plt.ylabel("Sentiment Score")
plt.title("Sentiment Trends Over Time")
plt.legend(title="Categories", loc="upper left")
plt.xticks(rotation=45)

# Add tighter spacing for the plot
plt.tight_layout()

# Show the plot
plt.show()
