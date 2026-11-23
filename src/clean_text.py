import re


def clean_text(text):

    # Convert text to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r'[^a-z0-9\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()