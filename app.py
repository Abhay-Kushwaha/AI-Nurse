from flask import Flask, render_template, send_file
from gtts import gTTS
import os

app = Flask(__name__)

TEXT_TO_SPEAK = "Important Note: Symptoms can vary in severity and may not appear in all individuals.If you suspect you or someone you know may have typhoid fever, seek medical attention immediately.  "

@app.route('/')
def home():
    tts = gTTS(text=TEXT_TO_SPEAK, lang='en')
    audio_file = "static/speech.mp3"
    tts.save(audio_file)
    
    return render_template('index.html')

@app.route('/speak')
def speak():
    return send_file("static/speech.mp3")

if __name__ == '__main__':
    app.run(debug=True)
