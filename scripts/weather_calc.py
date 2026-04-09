# import requests
from datetime import datetime, timedelta

# import sys
import pandas as pd
import matplotlib.pyplot as plt
import os
from weather_api import get_weather_data
import logging


# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

cities = {
    "Kolkata": (22.5744, 88.3629),
    "Delhi": (28.7041, 77.1025),
    "Mumbai": (19.0760, 72.8777),
    "Bangalore": (12.9716, 77.5946),
}

os.makedirs("../data", exist_ok=True)
os.makedirs("../plots", exist_ok=True)
os.makedirs("../logs", exist_ok=True)

# Logging config (RIGHT AFTER imports & folder creation)
logging.basicConfig(
    filename="../logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

all_summaries = []

for city, (lat, lon) in cities.items():
    logging.info(f"Processing {city}")

    try:
        df = get_weather_data(lat, lon, start_date, end_date)

        # Save CSV
        df.to_csv(f"../data/{city.lower()}_weather.csv", index=False)

        # -------------------
        # Summary (INSIDE TRY)
        summary = {
            "city": city,
            "avg_max_temp": df["max_temp"].mean(),
            "avg_min_temp": df["min_temp"].mean(),
            "max_temp": df["max_temp"].max(),
            "min_temp": df["min_temp"].min(),
        }

        all_summaries.append(summary)

        # Plot
        plt.figure(figsize=(10, 6))
        plt.plot(df["date"], df["max_temp"], marker="o", label="Max Temp")
        plt.plot(df["date"], df["min_temp"], marker="o", label="Min Temp")

        plt.title(f"{city} Weather - Past 7 Days")
        plt.legend()

        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.savefig(f"../plots/{city.lower()}_chart.png")
        plt.close()

        logging.info(f"Completed {city}")

    except Exception as e:
        logging.error(f"Error processing {city}: {e}")

summary_df = pd.DataFrame(all_summaries)
summary_df.to_csv("../data/summary.csv", index=False)
