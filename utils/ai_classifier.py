def classify_complaint(text):
    text = text.lower()

    if any(word in text for word in ["water", "tap", "supply", "pipeline"]):
        return "Water Supply"

    elif any(word in text for word in ["road", "pothole", "street"]):
        return "Roads & Potholes"

    elif any(word in text for word in ["electricity", "power", "current"]):
        return "Electricity"

    elif any(word in text for word in ["garbage", "waste", "trash"]):
        return "Garbage"

    elif any(word in text for word in ["traffic", "signal", "jam"]):
        return "Traffic"

    else:
        return "Other"