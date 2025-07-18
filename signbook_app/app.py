from flask import Flask, request, render_template
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import extract_text
from clean_segment import clean_and_segment
from gloss_mapper import to_gloss
from gloss_to_sigml import gloss_to_sigml

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentences = []
    sigml_url = None

    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file:
            
            SAMPLES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "samples"))
            os.makedirs(SAMPLES_DIR, exist_ok=True)
            file_path = os.path.join(SAMPLES_DIR, uploaded_file.filename)
            uploaded_file.save(file_path)

           
            text = extract_text(file_path)

           
            sentences = clean_and_segment(text)

          
            glosses = []
            for sentence in sentences:
                glosses.extend(to_gloss(sentence))

            sigml_snippets = gloss_to_sigml(glosses)
            sigml_text = '<?xml version="1.0" encoding="utf-8"?>\n<sigml>\n' + ''.join(sigml_snippets) + '</sigml>'

         
            SIGML_DIR = os.path.join(app.root_path, "static", "sigml")
            os.makedirs(SIGML_DIR, exist_ok=True)
            sigml_file_path = os.path.join(SIGML_DIR, "latest.sigml")
            with open(sigml_file_path, "w", encoding="utf-8") as f:
                f.write(sigml_text)

           
            sigml_url = f"https://vhg.cmp.uea.ac.uk/tech/jas/std/?sigml_url=/static/sigml/latest.sigml"

    return render_template("upload.html", sentences=sentences, sigml_url=sigml_url)

if __name__ == "__main__":
    app.run(debug=True)
