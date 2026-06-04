"""AI-powered complaint classification utilities."""

def classify_complaint(text):
    """Classify a complaint text into a category."""
    text = text.lower()

    if "water" in text or "tap" in text or "supply" in text or "pipeline" in text:
        return "Water Supply"

    if "road" in text or "pothole" in text or "street" in text:
        return "Roads & Potholes"

    if "electricity" in text or "power" in text or "current" in text:
        return "Electricity"

    if "garbage" in text or "waste" in text or "trash" in text:
        return "Garbage"

    if "traffic" in text or "signal" in text or "jam" in text:
        return "Traffic"

    return "Other"
