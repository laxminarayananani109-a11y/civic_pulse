from difflib import SequenceMatcher


def is_duplicate(new_complaint, existing_complaints, threshold=0.8):
    for complaint in existing_complaints:
        similarity = SequenceMatcher(
            None, new_complaint.lower(), complaint.lower()
        ).ratio()

        if similarity > threshold:
            return True

    return False
