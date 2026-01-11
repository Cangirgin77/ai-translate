from flask import Flask, render_template, request, jsonify
from googletrans import Translator
from gtts import gTTS
import os, base64, time

app = Flask(__name__, template_folder='../templates')
translator = Translator()

# ANA SAYFA: Tanıtım (Landing Page) burası olacak
@app.route('/')
def landing():
    return render_template('landing.html')

# UYGULAMA: Çeviri ekranına buradan geçilecek
@app.route('/app')
def main_app():
    return render_template('app.html')

# ÇEVİRİ MOTORU (Arka Planda Çalışır)
@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.json
        tr_text = data.get('text', '')
        en_text = translator.translate(tr_text, dest='en').text
        
        tts = gTTS(text=en_text, lang='en')
        filename = f"v_{int(time.time())}.mp3"
        tts.save(filename)
        
        with open(filename, "rb") as f:
            audio_64 = base64.b64encode(f.read()).decode('utf-8')
        os.remove(filename)
        
        return jsonify({"en": en_text, "audio": audio_64})
    except:
        return jsonify({"error": "Hata oluştu"}), 500
