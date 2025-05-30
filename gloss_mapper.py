import re

def to_gloss(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r"\b(am|is|are|was|were|the|a|an|to|of|and|in|on|for|with|at|from|by|about)\b", "", sentence)
    sentence = re.sub(r"[^\w\s]", "", sentence)
    words = sentence.strip().split()
    return " ".join(words).upper()

# Example usage
if __name__ == "__main__":
    sentences = [
        "I am going to the school.",
        "She is working on a project.",
        "They went to the market!"
    ]
    for i, s in enumerate(sentences, 1):
        gloss = to_gloss(s)
        print(f"{i}: {gloss}")
