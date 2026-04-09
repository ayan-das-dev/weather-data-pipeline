# 🌤️ Weather Data Pipeline & Dashboard

## 📌 Project Overview
This project fetches weather data for multiple cities using an API, processes it, stores it, and visualizes it using a Streamlit dashboard.

---

## ⚙️ Tech Stack
- Python
- Pandas
- Matplotlib
- Plotly
- Streamlit
- REST API (Open-Meteo)

---

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
(Will be added after deployment)

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