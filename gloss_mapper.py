
#gloss_mapper.py
import re

def to_gloss(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r"\b(am|is|are|was|were|the|a|an|to|of|and|in|on|for|with|at|from|by|about)\b", "", sentence)
    sentence = re.sub(r"[^\w\s]", "", sentence)
    words = sentence.strip().split()
    return [word.upper() for word in words]


