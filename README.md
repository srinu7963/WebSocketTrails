
# 📈 Real-Time KPI Dashboard (WebSocket + Streamlit)

This project simulates 3 KPIs — **Active Sessions**, **Pending Sessions**, and **Rejected Requests** — and serves them via WebSocket APIs. A live dashboard built with **Streamlit** consumes this data and visualizes it in real-time.

---

## 🛠️ Setup Instructions

Follow these steps to get started with the project:

### 1️⃣ Clone the repository or create the project directory

```shell
mkdir kpi-dashboard
cd kpi-dashboard
```

### 2️⃣ 📦 Create a Virtual Environment

```shell
python3 -m venv WSenv
```

### 3️⃣ 🚀 Activate the Virtual Environment

```shell
source WSenv/bin/activate    # Linux/macOS
```

> 🪟 For Windows:
```shell
WSenv\Scripts\activate
```

---

## 📥 Install Dependencies

```shell
pip install -r requirements.txt
```

Ensure your `requirements.txt` includes:

```txt
websockets==12.0
streamlit==1.35.0
streamlit-autorefresh==1.0.1
pandas>=1.0
```

---

## ▶️ Start the Application

### 🔁 Start WebSocket Backend

```shell
python kpi_websocket_server.py
```

> This will start a WebSocket server at `ws://localhost:8765`.

### 📊 Start Streamlit Dashboard (in a new terminal)

```shell
streamlit run kpi_dashboard.py
```

> This opens the dashboard in your default browser at:  
👉 **http://localhost:8501**

---

## 🛑 Stopping the App

### ⛔ Stop Backend Server

In the terminal where the backend is running, press:

```
Ctrl + C
```

### ⛔ Stop Streamlit Dashboard

In the dashboard terminal, press:

```
Ctrl + C
```

---

## 🔚 Deactivate the Virtual Environment

```shell
deactivate
```

---

## 📸 Preview

> _Add screenshots or a demo gif here if desired._

---

## 💡 Notes

- The KPIs are randomly generated every 2 seconds.
- You can customize the simulation logic and dashboard layout easily.
- Perfect for POCs or real-time monitoring demos.

---

🧑‍💻 Developed by Srinivas Anjoori using Python, WebSockets & Streamlit.
