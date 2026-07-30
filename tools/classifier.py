def classify_document(text):

    text_lower = text.lower()

    if "invoice" in text_lower or "total amount" in text_lower:
        return "invoice"

    elif "experience" in text_lower or "education" in text_lower:
        return "resume"

    elif "receipt" in text_lower:
        return "receipt"

    else:
        return "unknown"