from utils.duplicate_detector import is_duplicate

existing = [
    "No water supply in Miyapur",
    "Power cut in Kukatpally"
]

print(is_duplicate(
    "No water supply in Miyapur",
    existing
))