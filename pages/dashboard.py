import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
from streamlit_autorefresh import st_autorefresh
st.set_page_config(
    page_title="CivicPulse Dashboard",
    page_icon="📍",
    layout="wide",
    initial_sidebar_state="expanded"
)

dark_mode = st.sidebar.toggle("🌙 Dark Mode")
st.markdown("""
<div style="
background: linear-gradient(135deg,#111827,#1E293B);
padding:35px;
border-radius:22px;
margin-bottom:25px;
border:1px solid #374151;
">

<h1 style="
color:white;
font-size:42px;
margin-bottom:10px;
">
📊 Civic Analytics Dashboard
</h1>

<p style="
color:#CBD5E1;
font-size:18px;
">
Monitor complaint trends, civic hotspots, AI insights,
and urban issue analytics in real time.
</p>

</div>
""", unsafe_allow_html=True)
if dark_mode:

    st.markdown("""
        <style>

            .main .block-container{
            background:#111827;
             padding:2rem;
            border-radius:20px;
            border:1px solid #30363d;}

        </style>
    """, unsafe_allow_html=True)
    st.markdown("""
    <style>

    .stApp {
        background-color: #0f1117;
        color: white;
    }

    section[data-testid="stSidebar"] {
        background-color: #161b22;
    }

    div[data-testid="metric-container"] {
        background-color: #1c2128;
        border-radius: 12px;
        padding: 15px;
    }

    div[data-testid="metric-container"] * {
        color: white !important;
    }

    h1,h2,h3,h4,h5,h6,p,label,span {
        color: white !important;
    }
    
    
    </style>
    """, unsafe_allow_html=True)

# Auto Refresh Every 5 Seconds
st_autorefresh(
    interval=5000,
    key="dashboard_refresh"
)

st.title("📊 Civic Pulse Dashboard")
st.markdown("Monitor and analyze civic complaints in real-time.")

# Database
conn = sqlite3.connect("data/complaints.db")

df = pd.read_sql_query(
    "SELECT * FROM complaints",
    conn
)
m = folium.Map(
    location=[17.3850, 78.4867],
    zoom_start=11,
    tiles="CartoDB dark_matter"
)
# ======================
# METRICS
# ======================

total_complaints = len(df)

water_count = len(df[df["category"] == "Water"])
road_count = len(df[df["category"] == "Road"])
electricity_count = len(df[df["category"] == "Electricity"])
garbage_count = len(df[df["category"] == "Garbage"])

c1, c2, c3, c4, c5 = st.columns(5)

col1, col2, col3, col4, col5 = st.columns(5)

cards = [
    ("📋 Total", total_complaints),
    ("💧 Water", water_count),
    ("🛣️ Road", road_count),
    ("⚡ Electricity", electricity_count),
    ("🗑️ Garbage", garbage_count)
]

for col, (title, value) in zip([col1,col2,col3,col4,col5], cards):
    with col:
        st.markdown(f"""
        <div style="
            background:#1c2128;
            padding:20px;
            border-radius:15px;
            border:1px solid #30363d;
            text-align:center;">
            <h4>{title}</h4>
            <h1>{value}</h1>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ======================
# CHARTS
# ======================

if not df.empty:

    st.subheader("📈 Complaints by Category")

    category_counts = df["category"].value_counts()

    # Bar Chart
    bar_fig = px.bar(
        x=category_counts.index,
        y=category_counts.values,
        title="Complaints by Category"
    )

    if dark_mode:
        bar_fig.update_layout(
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            font_color="white"
        )

    st.plotly_chart(bar_fig, use_container_width=True)

    # Pie Chart
    fig = px.pie(
        values=category_counts.values,
        names=category_counts.index,
        title="Complaint Distribution"
    )

    if dark_mode:
        fig.update_layout(
            paper_bgcolor="#0f1117",
            plot_bgcolor="#0f1117",
            font_color="white"
        )

    st.plotly_chart(fig, use_container_width=True)


st.divider()

# ======================
# INSIGHTS
# ======================

if not df.empty:

    top_category = df["category"].value_counts().idxmax()

    st.success(
        f"Most Reported Issue: {top_category}"
    )

st.divider()

# ======================
# MAP
# ======================

st.markdown("""
<div class="glass-card">

<h2 style="color:white;">
🗺 Complaint Hotspots
</h2>

<p style="color:#CBD5E1;">
Track complaint density and monitor civic issue hotspots
across different regions in real time.
</p>

</div>
""", unsafe_allow_html=True)

location_coords = {
    "Hyderabad": [17.3850, 78.4867],
    "Miyapur": [17.4966, 78.3562],
    "Gachibowli": [17.4401, 78.3489],
    "Uppal": [17.4058, 78.5591],
    "Kukatpally": [17.4948, 78.3996],
    "Ameerpet": [17.4375, 78.4482],
    "Hitech City": [17.4435, 78.3772]
}

m = folium.Map(
    location=[17.3850, 78.4867],
    zoom_start=10
)

heat_data = []

for _, row in df.iterrows():

    location = row["location"]

    if location in location_coords:

        lat, lon = location_coords[location]

        heat_data.append([lat, lon])

        folium.Marker(
            [lat, lon],
            popup=f"{row['category']} - {row['description']}"
        ).add_to(m)

if heat_data:
    HeatMap(heat_data).add_to(m)

st_folium(
    m,
    width=1000,
    height=500
)

st.write(df["category"].unique())

st.divider()

# ======================
# TABLE
# ======================

st.subheader("📋 Complaint Records")

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

# ======================
# RECENT COMPLAINTS
# ======================

st.subheader("🚨 Recent Complaints")

for _, row in df.tail(5).iterrows():

    st.info(
        f"""
Category: {row['category']}

Location: {row['location']}

Issue: {row['description']}
"""
    )

conn.close()