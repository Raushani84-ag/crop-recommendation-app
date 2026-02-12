import streamlit as st
import base64

import json
import pandas as pd


# Load JSON Data

with open("agro-climatic-data-district-wise.json") as f:
    data = json.load(f)

# Convert JSON to DataFrame

rows = []

for zone in data["agro_climatic_zones"]:
    for district in zone["districts"]:
        rows.append({
            "zone_id": zone["zone_id"],
            "zone_name": zone["zone_name"],
            "district": district,
            "rainfall_mm": zone["characteristics"]["rainfall_mm"],
            "soil_type": zone["characteristics"]["soil_type"],
            "temperature": zone["characteristics"]["temperature"],
            "water_availability": zone["characteristics"]["water_availability"],
            "suitable_crops": zone["suitable_crops"]
        })

df = pd.DataFrame(rows)

# Streamlit UI

# Background Image Placeholder
def add_bg_image():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1500382017468-9049fed747ef");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_image()

# Layout

st.title("🌾AI-Based Crop Recommendation System")

# District Selection

selected_district = st.selectbox(
    "Select District",
    sorted(df["district"].unique())
)

# Filter selected district row
district_data = df[df["district"] == selected_district].iloc[0]


# Create 2 Columns
left_col, right_col = st.columns([2, 1])

# LEFT SIDE (Agro Details)
with left_col:

    st.markdown("## Agro-Climatic Zone")

    st.markdown(
        f"""
        <div style="
            background-color: #d2b48c;
            padding:20px;
            border-radius:10px;
            color:black;
        ">
            <h4>{district_data['zone_name']}</h4>
            <p><b>Rainfall:</b> {district_data['rainfall_mm']}</p>
            <p><b>Soil Type:</b> {district_data['soil_type']}</p>
            <p><b>Temperature Pattern:</b> {district_data['temperature']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# RIGHT SIDE (Crop Recommendation)

with right_col:

    st.markdown("###  🌱Recommended Crops")

    for crop in district_data["suitable_crops"]:
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(90deg, #0f5132, #198754);
                padding:15px;
                margin-bottom:10px;
                border-radius:10px;
                color:white;
                font-weight:bold;
            ">
                {crop}
            </div>
            """,
            unsafe_allow_html=True
        )
