"""Logic for detecting duplicate complaint submissions."""
from difflib import SequenceMatcher


def is_duplicate(new_text, existing_texts):
    """Check if complaint is duplicate."""
    for text in existing_texts:
        similarity = SequenceMatcher(
            None, new_text.lower(), text.lower()
        ).ratio()

        if similarity > threshold:
            return True

    return False
