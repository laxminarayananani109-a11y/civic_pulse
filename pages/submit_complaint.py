import streamlit as st

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

location = st.text_input("Location")

if st.button("Submit Complaint"):

    if not description or not location:
        st.error("Please fill all fields")
    else:
        st.success("Complaint submitted successfully!")