import streamlit as st
import asyncio
import websockets
import json
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# Auto-refresh the page every 2 seconds
st_autorefresh(interval=2000, key="auto_refresh")

st.title("📊 Real-time KPI Dashboard")

# Placeholder containers
active_placeholder = st.empty()
pending_placeholder = st.empty()
rejected_placeholder = st.empty()

# Chart container
chart_placeholder = st.line_chart(pd.DataFrame(columns=["Active", "Pending", "Rejected"]))

# Session state to store KPI history
if "data" not in st.session_state:
    st.session_state["data"] = []

async def fetch_kpi_data():
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            msg = await websocket.recv()
            return json.loads(msg)
    except Exception as e:
        st.error(f"WebSocket connection failed: {e}")
        return None

def update_dashboard():
    kpi_data = asyncio.run(fetch_kpi_data())
    if kpi_data:
        active_placeholder.metric("Active Sessions", kpi_data["active_sessions"])
        pending_placeholder.metric("Pending Sessions", kpi_data["pending_sessions"])
        rejected_placeholder.metric("Rejected Requests", kpi_data["rejected_requests"])

        # Store data
        st.session_state["data"].append([
            kpi_data["active_sessions"],
            kpi_data["pending_sessions"],
            kpi_data["rejected_requests"]
        ])

        df = pd.DataFrame(
            st.session_state["data"],
            columns=["Active", "Pending", "Rejected"]
        )
        chart_placeholder.line_chart(df)

update_dashboard()

