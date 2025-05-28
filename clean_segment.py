# clean_segment.py
import re

def clean_and_segment(text):
    cleaned = re.sub(r'\s+', ' ', text).strip()
    cleaned = re.sub(r'[^\x00-\x7F]+', '', cleaned)
    segments = re.split(r'(?<=[.?!])\s+', cleaned)
    return [s.strip() for s in segments if s.strip()]

# Example usage
if __name__ == "__main__":
    from main import extract_text
    raw_text = extract_text("samples/test.pdf")  # or .docx
    segments = clean_and_segment(raw_text)
    for i, s in enumerate(segments, 1):
        print(f"{i}: {s}")
