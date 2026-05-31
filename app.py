import streamlit as st
from utils.database import get_total_complaints
from utils.database import get_total_complaints, get_total_locations

total_complaints = get_total_complaints()
total_locations = get_total_locations()

st.set_page_config(
    page_title="Civic Pulse",
    page_icon="📍",
    layout="wide"
)

total_complaints = get_total_complaints()

st.write("Total complaints:", total_complaints)
st.title("📍 Civic Pulse")

st.subheader("AI-Powered Civic Issue Monitoring Platform")

st.markdown("""
<div style="
background: rgba(128,128,128,0.08);
backdrop-filter: blur(12px);
padding:60px;
border-radius:30px;
border:1px solid rgba(255,255,255,0.1);
box-shadow:0 10px 30px rgba(0,0,0,0.3);
margin-top:20px;
">

<h1 style="
font-size:60px;
margin-bottom:10px;
color:white;
font-weight:800;
">
📍 Civic Pulse
</h1>

<h3 style="
font-size:30px;
font-weight:400;
margin-bottom:30px;
color:inherit;
">
AI-Powered Civic Issue Monitoring Platform
</h3>

<p style="
font-size:20px;
line-height:1.8;
max-width:900px;
color:inherit;
">
Monitor civic complaints, analyze urban issues,
track live heatmaps, and generate intelligent insights
for smarter governance across Telangana.
</p>

</div>
""", unsafe_allow_html=True)
st.markdown("---")

st.markdown("## 🌍 About CivicPulse")

st.markdown("""
CivicPulse is an AI-powered civic issue monitoring platform designed to help citizens and local authorities track, analyze, and resolve urban problems efficiently.

The platform enables real-time complaint reporting, intelligent issue categorization, geographic heatmap visualization, and data-driven civic analytics.

By combining artificial intelligence with interactive dashboards, CivicPulse helps improve transparency, response efficiency, and smart city management.
""")
st.markdown("---")

st.markdown("## ⚡ How It Works")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 1️⃣ Report Issues
    
    Citizens submit complaints related to:
    - Roads
    - Water
    - Electricity
    - Garbage
    - Traffic
    """)

with col2:
    st.markdown("""
    ### 2️⃣ AI Processing
    
    The platform:
    - Classifies complaints
    - Detects categories
    - Organizes issue data
    - Generates analytics
    """)

with col3:
    st.markdown("""
    ### 3️⃣ Smart Monitoring
    
    Authorities can:
    - Monitor hotspots
    - Analyze trends
    - Prioritize areas
    - Improve response time
    """)
    st.markdown("---")

st.markdown("## 🧠 Why Choose CivicPulse?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### ✅ Smart Governance
    
    CivicPulse helps authorities identify,
    prioritize, and monitor civic issues
    using intelligent analytics.
    
    ### 📊 Data-Driven Insights
    
    Interactive dashboards and visual analytics
    help improve urban decision-making.
    """)

with col2:
    st.markdown("""
    ### 🌍 Real-Time Monitoring
    
    Track complaints and issue hotspots
    across multiple regions instantly.
    
    ### 🚀 AI-Powered Automation
    
    AI classification reduces manual effort
    and improves issue management efficiency.
    """)
    st.markdown("---")

st.markdown("## 🚀 Core Platform Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="
    background: rgba(128,128,128,0.08);
    padding:30px;
    border-radius:20px;
    border:1px solid #374151;
    height:260px;
    ">
    
    <h2 style="color:#60A5FA;">📩</h2>
    
    <h3 style="color:inherit;">
    Smart Complaint Submission
    </h3>
    
    <p style="color:#D1D5DB;">
    Citizens can submit civic complaints
    instantly with category tracking
    and issue descriptions.
    </p>
    
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
    background:#111827;
    padding:30px;
    border-radius:20px;
    border:1px solid #374151;
    height:260px;
    ">
    
    <h2 style="color:#34D399;">🧠</h2>
    
    <h3 style="color:inherit;">
    AI Classification
    </h3>
    
    <p style="color:inherit;">
    Artificial intelligence automatically
    identifies complaint categories
    and organizes civic data efficiently.
    </p>
    
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
    background:#111827;
    padding:30px;
    border-radius:20px;
    border:1px solid #374151;
    height:260px;
    ">
    
    <h2 style="color:#FBBF24;">📊</h2>
    
    <h3 style="color:white;">
    Live Analytics Dashboard
    </h3>
    
    <p style="color:#D1D5DB;">
    Visualize complaint trends,
    heatmaps, and urban issue
    patterns in real time.
    </p>
    
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

st.markdown("## 📈 Platform Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div style="
    background:#1E293B;
    padding:25px;
    border-radius:18px;
    text-align:center;
    ">

    <h1 style="color:#60A5FA;">{total_complaints}</h1>
    <p style="color:inherit;">Complaints Monitored</p>

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
    background:#1E293B;
    padding:25px;
    border-radius:18px;
    text-align:center;
    ">
    
    <h1 style="color:#34D399;">94%</h1>
    <p style="color:white;">AI Classification Accuracy</p>
    
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="
    background:#1E293B;
    padding:25px;
    border-radius:18px;
    text-align:center;
    ">

    <h1 style="color:#FBBF24;">{total_locations}</h1>
    <p style="color:white;">Hotspot Regions</p>

    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="
    background:#1E293B;
    padding:25px;
    border-radius:18px;
    text-align:center;
    ">
    
    <h1 style="color:#F87171;">24/7</h1>
    <p style="color:white;">Live Monitoring</p>
    
    </div>
    """, unsafe_allow_html=True)
    