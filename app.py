import streamlit as st
from datetime import datetime, timedelta
import plotly.express as px
import pandas as pd
from scripts.weather_api import get_weather_data

# -----------------------
# Page Config
st.set_page_config(page_title="Weather Dashboard", layout="wide")


# -----------------------
# Caching
@st.cache_data
def fetch_data(lat, lon, start_date, end_date):
    return get_weather_data(lat, lon, start_date, end_date)


# -----------------------
# Title
st.title("🌤️ Weather Dashboard")

# -----------------------
# Sidebar
st.sidebar.header("Filters")

cities = {
    "Kolkata": (22.5744, 88.3629),
    "Delhi": (28.7041, 77.1025),
    "Mumbai": (19.0760, 72.8777),
    "Bangalore": (12.9716, 77.5946),
}

today = datetime.now().date()
week_ago = today - timedelta(days=7)

start_date = st.sidebar.date_input("Start Date", week_ago)
end_date = st.sidebar.date_input("End Date", today)

if start_date > end_date:
    st.error("Start date must be before end date")
    st.stop()

# -----------------------
# Tabs
tab1, tab2 = st.tabs(["📊 Single City", "🌍 Multi-City Comparison"])

# =========================================================
# 📊 TAB 1: SINGLE CITY
# =========================================================
with tab1:
    city = st.selectbox("Select City", list(cities.keys()))
    lat, lon = cities[city]

    df = fetch_data(
        lat,
        lon,
        start_date.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d"),
    )

    st.subheader(f"{city} Weather Data")

    # Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Avg Max Temp", round(df["max_temp"].mean(), 2))
    col2.metric("Avg Min Temp", round(df["min_temp"].mean(), 2))
    col3.metric("Max Temp", round(df["max_temp"].max(), 2))

    # Chart
    fig = px.line(
        df,
        x="date",
        y=["max_temp", "min_temp"],
        markers=True,
        title=f"{city} Temperature Trend",
    )

    st.plotly_chart(fig, width="stretch")

    # Data
    st.dataframe(df, width="stretch")

# =========================================================
# 🌍 TAB 2: MULTI-CITY
# =========================================================
with tab2:
    selected_cities = st.multiselect(
        "Select Cities", list(cities.keys()), default=["Kolkata", "Delhi"]
    )

    if selected_cities:
        all_data = []

        for city in selected_cities:
            lat, lon = cities[city]

            df = fetch_data(
                lat,
                lon,
                start_date.strftime("%Y-%m-%d"),
                end_date.strftime("%Y-%m-%d"),
            )

            df["city"] = city
            all_data.append(df)

        final_df = pd.concat(all_data)

        st.subheader("📈 Temperature Comparison")

        # Chart
        fig = px.line(
            final_df,
            x="date",
            y="max_temp",
            color="city",
            markers=True,
            title="Max Temperature Comparison",
        )

        st.plotly_chart(fig, width="stretch")

        # Summary Table
        st.subheader("📊 Summary")

        summary = (
            final_df.groupby("city")
            .agg({"max_temp": "mean", "min_temp": "mean"})
            .reset_index()
        )

        summary.columns = ["City", "Avg Max Temp", "Avg Min Temp"]

        st.dataframe(summary, width="stretch")

    else:
        st.warning("Please select at least one city")
