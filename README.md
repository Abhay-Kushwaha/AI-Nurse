# Talking AI Cartoon

Talking Cartoon is a Flask-based web application that animates a cartoon character while playing a generated speech. The application takes a predefined text, converts it into speech, and plays a video animation alongside the generated audio.

## **Features**
- 🎤 **Text-to-Speech Conversion** – Converts predefined text into audio.
- 🎥 **Animated Cartoon** – Displays a cartoon video that plays while the speech is active.
- 🚀 **Automatic Speech Playback** – The audio plays when the page loads or when the user clicks a button.

## **Future Modifications**
- 🗣️ **Dynamic Text Input** – Allow users to enter their own text for speech.
- 🎭 **Multiple Cartoon Characters** – Option to choose different animated characters.
- 🏃 **Real-Time Lip Syncing** – Synchronize mouth movements with the generated speech.
- 🌍 **Multi-Language Support** – Convert and speak text in different languages.

## **How to Run the Project**
Follow these steps to run the project locally:

### **1. Clone the Repository**
```sh
git clone https://github.com/your-username/talking-cartoon.git
cd talking-cartoon
```
### **2. Create a Virtual Environment**
```sh
python -m venv myenv
```
### **3. Activate the Virtual Environmenty**
Windows
```sh
myenv\Scripts\activate
```
Mac/Linux
```sh
source myenv/bin/activate
```
### **4. Install Required Dependencies**
```sh
pip install -r requirements.txt
```
### **5. Run the Flask App**
Windows
```sh
python app.py
```
### **6. Open in Browser**
Go to: http://127.0.0.1:5000
The talking cartoon animation will start playing!
## **Technologies Used**
- Python 🐍 (Flask, gTTS)
- JavaScript 🏗️ (for dynamic media control)
- HTML & CSS 🎨 (for UI design)