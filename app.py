from flask import Flask, render_template, request, send_file, jsonify
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    data = request.get_json()
    user_text = data.get('text', '')
    if not user_text.strip():
        return jsonify({'error': 'Empty text'}), 400
    filename = f"static/speech.mp3"
    convert = gTTS(text=user_text, lang='en')
    convert.save(filename)

    return send_file(filename, mimetype="audio/mpeg")

if __name__ == '__main__':
    app.run(debug=True)
