# clean_segment.py
import re

def clean_and_segment(text):
    cleaned = re.sub(r'\s+', ' ', text).strip()
    cleaned = re.sub(r'[^\x00-\x7F]+', '', cleaned)
    segments = re.split(r'(?<=[.?!])\s+', cleaned)
    return [s.strip() for s in segments if s.strip()]


