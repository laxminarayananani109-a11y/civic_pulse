import streamlit as st
import plotly.express as px
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.database import get_all_complaints

complaints = get_all_complaints()
st.set_page_config(page_title="Civic Pulse Dashboard")

st.markdown("""
<h1 style='text-align: center; color: #4CAF50;'>
🚨 Civic Pulse Dashboard
</h1>

<h4 style='text-align: center; color: gray;'>
Real-Time Civic Issue Monitoring System
</h4>
""", unsafe_allow_html=True)


# ---------------- METRICS ----------------

col1, col2, col3 = st.columns(3)

st.header("Dashboard Overview")

with col1:
    st.metric("📢 Total Complaints", len(complaints))

with col2:
    st.metric("✅ Resolved", int(len(complaints) * 0.6))

with col3:
    st.metric("⏳ Pending", int(len(complaints) * 0.4))
# ---------------- PIE CHART ----------------

df = pd.DataFrame(
    complaints,
    columns=["ID", "Description", "Category", "Location", "Date"]
)

category_data = df["Category"].value_counts().reset_index()

category_data.columns = ["Category", "Complaints"]



fig = px.pie(
    category_data,
    names="Category",
    values="Complaints",
    title="Complaints by Category"
)

st.plotly_chart(fig)

# ---------------- BAR CHART ----------------

location_df = df["Location"].value_counts().reset_index()

location_df.columns = ["Location", "Complaints"]

bar_fig = px.bar(
    location_df,
    x="Location",
    y="Complaints",
    title="Complaints by Location"
)

st.plotly_chart(bar_fig)

# ---------------- LINE CHART ----------------

trend_data = {
    "Date": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Complaints": [10, 25, 18, 30, 22]
}

trend_df = pd.DataFrame(trend_data)

line_fig = px.line(
    trend_df,
    x="Date",
    y="Complaints",
    title="Complaint Trends"
)

st.plotly_chart(line_fig)
# ---------------- HEATMAP ----------------
# ---------------- HEATMAP ----------------

st.header("🗺️ Geographical Insights")

st.subheader("📍 Civic Complaints Heatmap")

map_data = pd.DataFrame({
    "lat": [17.3850, 17.4474, 17.4948, 17.3616],
    "lon": [78.4867, 78.3762, 78.3995, 78.4747]
})

st.map(map_data)
