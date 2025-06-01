from flask import Flask, request, render_template
import os
import sys

# Add parent directory to import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import extract_text
from clean_segment import clean_and_segment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentences = None
    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file:
            # Go up one level to find 'samples/' directory
            SAMPLES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "samples"))
            os.makedirs(SAMPLES_DIR, exist_ok=True)

            file_path = os.path.join(SAMPLES_DIR, uploaded_file.filename)
            uploaded_file.save(file_path)

            text = extract_text(file_path)
            sentences = clean_and_segment(text)

    return render_template("upload.html", sentences=sentences)

if __name__ == "__main__":
    app.run(debug=True)
