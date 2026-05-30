import streamlit as st
from utils.database import add_complaint

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
        "Public Safety"
    ]
)

location = st.selectbox(
    "Location",
    [
        "Hyderabad",
        "Miyapur",
        "Gachibowli",
        "Uppal",
        "Kukatpally",
        "Ameerpet",
        "Hitech City"
    ]
)

if st.button("Submit Complaint"):

    if not description or not location:
        st.error("Please fill all fields")

    else:

        add_complaint(
            description,
            category,
            location
        )

        st.success("Complaint submitted successfully!")