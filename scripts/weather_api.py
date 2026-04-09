import pandas as pd
import requests


def get_weather_data(lat, lon, start_date, end_date):
    # lat=52.52
    # lon=13.405
    # start_date="2026-04-05"
    # end_date="2026-04-07"#*/
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
    response = requests.get(url)
    data = response.json()

    # print(data)
    daily_data = data["daily"]

    # Create a DataFrame
    df = pd.DataFrame(
        {
            "date": daily_data["time"],
            "max_temp": daily_data["temperature_2m_max"],
            "min_temp": daily_data["temperature_2m_min"],
            "rainfall": daily_data["precipitation_sum"],
        }
    )
    df["date"] = pd.to_datetime(df["date"])
    return df
