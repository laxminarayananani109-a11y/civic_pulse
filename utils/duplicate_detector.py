"""Duplicate complaint detection utilities."""
from difflib import SequenceMatcher


def is_duplicate(new_complaint, existing_complaints, threshold=0.8):
    """Check if a complaint is a duplicate of existing complaints."""
    for complaint in existing_complaints:

        similarity = SequenceMatcher(
            None, new_text.lower(), text.lower()
        ).ratio()

        if similarity > threshold:
            return True

    return False
