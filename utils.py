import re
import string

def extract_email(content):
    match = re.search(r'<(.*?)>', content)
    return match.group(1) if match else None

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def mask_pii(text):
    patterns = {
        'EMAIL': r'\b[\w\.-]+@[\w\.-]+\.\w+\b',
        'PHONE': r'\b\d{10}\b',
        'NAME': r'\b(name|your_name)\b',
    }

    masked_text = text
    masked_entities = []

    for entity_type, pattern in patterns.items():
        for match in re.finditer(pattern, masked_text, flags=re.IGNORECASE):
            start, end = match.start(), match.end()
            original = masked_text[start:end]
            masked_text = masked_text[:start] + "[MASKED]" + masked_text[end:]
            masked_entities.append({
                "position": [start, start + len("[MASKED]")],
                "classification": entity_type,
                "entity": original
            })

    return masked_text, masked_entities
