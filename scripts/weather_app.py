import streamlit as st
from datetime import datetime, timedelta
from scripts.weather_api import get_weather_data
import plotly.express as px

st.title("🌤️ Weather Dashboard")

# -----------------------
# City Dropdown
cities = {
    "Kolkata": (22.5744, 88.3629),
    "Delhi": (28.7041, 77.1025),
    "Mumbai": (19.0760, 72.8777),
    "Bangalore": (12.9716, 77.5946),
}

city = st.selectbox("Select City", list(cities.keys()))
lat, lon = cities[city]

# -----------------------
# Date Picker
start_date = st.date_input("Start Date", datetime.now() - timedelta(days=7))
end_date = st.date_input("End Date", datetime.now())

# -----------------------
# Button
if st.button("Get Data"):
    df = get_weather_data(
        lat,
        lon,
        start_date.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d"),
    )

    # -----------------------
    # Show Data
    st.subheader("📊 Data")
    st.dataframe(df)

    # -----------------------
    # Summary
    st.subheader("📈 Summary")

    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Max Temp", round(df["max_temp"].mean(), 2))
    col2.metric("Avg Min Temp", round(df["min_temp"].mean(), 2))
    col3.metric("Max Temp", round(df["max_temp"].max(), 2))

    # -----------------------
    # Chart
    fig = px.line(df, x="date", y=["max_temp", "min_temp"], markers=True)
    st.plotly_chart(fig)

    # -----------------------
    # Download CSV
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download CSV",
        data=csv,
        file_name=f"{city}_weather.csv",
        mime="text/csv",
    )
