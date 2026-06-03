import pandas as pd
import secrets
from datetime import datetime, timedelta

locations = {
    "Kukatpally": (17.4948, 78.3996),
    "Ameerpet": (17.4375, 78.4482),
    "LB Nagar": (17.3457, 78.5520),
    "Secunderabad": (17.4399, 78.4983),
    "Hitech City": (17.4435, 78.3772),
    "Miyapur": (17.4969, 78.3562),
    "Uppal": (17.4058, 78.5591),
    "Dilsukhnagar": (17.3688, 78.5247),
    "Kompally": (17.5251, 78.4832),
    "Panjagutta": (17.4283, 78.4524),
    "Gachibowli": (17.4401, 78.3489),
    "Madhapur": (17.4483, 78.3915),
    "Kondapur": (17.4660, 78.3630),
    "Manikonda": (17.4062, 78.3900),
    "Banjara Hills": (17.4126, 78.4482),
    "Jubilee Hills": (17.4316, 78.4071),
}

templates = {
    "Water": [
        "Water supply interrupted for 3 days",
        "Low water pressure affecting households",
        "Drinking water contamination reported",
        "Water leakage from main pipeline",
        "No drinking water available in locality",
    ],
    "Roads": [
        "Large pothole causing accidents",
        "Road damaged after recent rains",
        "Uneven road surface creating traffic issues",
        "Broken road near residential area",
        "Road repair work incomplete",
    ],
    "Electricity": [
        "Frequent power cuts in colony",
        "Street lights not working",
        "Electric pole damaged",
        "Voltage fluctuations affecting homes",
        "Transformer malfunction reported",
    ],
    "Garbage": [
        "Garbage not collected for a week",
        "Overflowing dustbins near market",
        "Garbage dumped near school",
        "Waste accumulation causing foul smell",
        "Illegal dumping of household waste",
    ],
    "Traffic": [
        "Heavy traffic congestion during peak hours",
        "Traffic signal malfunctioning",
        "Illegal parking blocking road",
        "Traffic management required at junction",
        "Roadside encroachment causing congestion",
    ],
}

distribution = {
    "Roads": 130,
    "Water": 120,
    "Garbage": 100,
    "Electricity": 80,
    "Traffic": 70,
}

data = []
start_date = datetime(2025, 6, 1)
cid = 1

for category, count in distribution.items():
    for _ in range(count):
        location = secrets.choice(list(locations.keys()))
        lat, lon = locations[location]

        data.append(
            [
                cid,
                secrets.choice(templates[category]),
category,
                location,
                (start_date + timedelta(days=secrets.randbelow(365))).strftime(
                    "%Y-%m-%d"
                ),
                
                lat,
                lon,
            ]
        )

        cid += 1

df = pd.DataFrame(
    data,
    columns=[
        "id",
        "description",
        "category",
        "location",
        "date",
        "latitude",
        "longitude",
    ],
)

df.to_csv("complaints_500.csv", index=False)

print("Generated:", len(df), "complaints")
