"""Complaint submission page for Civic Pulse."""
import streamlit as st
from utils.database import add_complaint
from data.hyderabadlocations import HYDERABAD_LOCATIONS

st.set_page_config(page_title="Civic Pulse")

st.title("🏙️ Civic Pulse")
st.subheader("Report a Civic Issue")

description = st.text_area("Complaint Description")

category = st.selectbox(
    "Category",
    [
        "Water Supply",
        "Roads & Potholes",
        "Electricity",
        "Garbage",
        "Traffic",
        "Public Safety",
    ],
)


location = st.selectbox("Select Location", HYDERABAD_LOCATIONS)

address = st.text_input("Landmark / Detailed Address")

severity = st.selectbox("Issue Severity", ["Low", "Medium", "High"])

if st.button("Submit Complaint"):

    if not description or not address:
        st.error("Please fill all fields")

    else:

        add_complaint(description, category, location)

        st.success("Complaint submitted successfully!")
