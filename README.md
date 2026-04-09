# 🌤️ Weather Data Pipeline & Dashboard

## 📌 Project Overview

This project is an end-to-end Weather Data Pipeline and Interactive Dashboard that fetches real-time weather data using an API, processes it, and visualizes insights through an interactive Streamlit application.

It supports multi-city analysis, date filtering, caching for performance optimization, and provides both graphical and tabular insights.

This project demonstrates core data engineering concepts such as data ingestion, transformation, storage, logging, and visualization.
---

## ⚙️ Tech Stack

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/API-Open--Meteo-green?style=for-the-badge"/>
</p>

## 🚀 Features

### 🔹 Data Pipeline
- Fetches weather data using API
- Processes multiple cities (Kolkata, Delhi, Mumbai, Bangalore)
- Stores data as CSV
- Generates plots
- Logs execution details

### 🔹 Dashboard
- City selection dropdown
- Date range selection
- Interactive charts
- Summary statistics
- CSV download option

---

## 📂 Project Structure
weather-app/
│
├── data/ # CSV outputs
├── plots/ # Charts
├── logs/ # Log files
│
├── scripts/
│ ├── weather_api.py
│ └── weather_app.py
│
├── app.py # Streamlit app
├── requirements.txt
├── README.md


---

## ▶️ How to Run

### 1. Clone repo

git clone https://github.com/ayan-das-dev/weather-data-pipeline.git

cd weather-data-pipeline


### 2. Install dependencies

pip install -r requirements.txt


### 3. Run pipeline

python scripts/weather_app.py


### 4. Run dashboard

streamlit run app.py


---

## 🌐 Live App
👉 [Click here to view the app](https://weather-data-pipeline-n9hm7xhmx9kyuueusxlp7q.streamlit.app/)

---

## 📊 Sample Output
- Weather charts
- CSV data files
- Summary statistics

---

## 💡 Future Improvements
- Add more weather parameters
- Multi-city comparison
- Database integration
- Airflow scheduling

---

## 🙌 Author
Ayan Das