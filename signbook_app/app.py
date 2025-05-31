from flask import Flask, render_template, request, redirect
import os
from main import extract_text  # your existing function
from clean_segment import clean_and_segment

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    segments = []
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            raw_text = extract_text(file_path)
            segments = clean_and_segment(raw_text)
    return render_template('index.html', segments=segments)

if __name__ == "__main__":
    app.run(debug=True)
