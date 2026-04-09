import streamlit as st
from datetime import datetime, timedelta

# import pandas as pd
import plotly.express as px

# Import your API function
from scripts.weather_api import get_weather_data

st.set_page_config(page_title="Weather Dashboard", layout="wide")

# -------------------------------
# Title
st.title("🌤️ Weather Data Dashboard")

# -------------------------------
# Sidebar Inputs

st.sidebar.header("User Input")

# City selection
cities = {
    "Kolkata": (22.5744, 88.3629),
    "Delhi": (28.7041, 77.1025),
    "Mumbai": (19.0760, 72.8777),
    "Bangalore": (12.9716, 77.5946),
}

city = st.sidebar.selectbox("Select City", list(cities.keys()))
lat, lon = cities[city]

# Date selection
start_date = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=7))
end_date = st.sidebar.date_input("End Date", datetime.now())

# -------------------------------
# Fetch Data

if start_date > end_date:
    st.error("Start date must be before end date")
else:
    with st.spinner("Fetching weather data..."):
        df = get_weather_data(
            lat,
            lon,
            start_date.strftime("%Y-%m-%d"),
            end_date.strftime("%Y-%m-%d"),
        )

    # -------------------------------
    # Show Data
    st.subheader(f"Weather Data for {city}")
    st.dataframe(df)

    # -------------------------------
    # Metrics

    st.subheader("📊 Summary Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Avg Max Temp (°C)", round(df["max_temp"].mean(), 2))
    col2.metric("Avg Min Temp (°C)", round(df["min_temp"].mean(), 2))

    if "rainfall" in df.columns:
        col3.metric("Total Rainfall (mm)", round(df["rainfall"].sum(), 2))
    else:
        col3.metric("Total Rainfall (mm)", "N/A")

    # -------------------------------
    # Temperature Chart

    st.subheader("📈 Temperature Trend")

    fig = px.line(
        df,
        x="date",
        y=["max_temp", "min_temp"],
        title=f"{city} Temperature Trend",
        markers=True,
    )

    st.plotly_chart(fig, width="stretch")

    # -------------------------------
    # Rainfall Chart (if available)

    if "rainfall" in df.columns:
        st.subheader("🌧️ Rainfall")

        fig2 = px.bar(
            df,
            x="date",
            y="rainfall",
            title=f"{city} Daily Rainfall",
        )

        st.plotly_chart(fig2, width="stretch")

    # -------------------------------
    # Download CSV

    st.subheader("⬇️ Download Data")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name=f"{city}_weather.csv",
        mime="text/csv",
    )
