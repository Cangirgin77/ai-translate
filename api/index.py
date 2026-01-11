import os, time, base64
from flask import Flask, render_template, request, jsonify
from googletrans import Translator
from gtts import gTTS

# Vercel'in template klasörünü bulması için yol ayarı
app = Flask(__name__, template_folder='../templates')
translator = Translator()

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/app')
def main_app():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.json
        tr_text = data.get('text')
        
        if not tr_text or len(tr_text.strip()) < 1:
            return jsonify({"error": "Metin yok"}), 400

        # Çeviri işlemi
        en_text = translator.translate(tr_text, dest='en').text
        
        # Sesi üret (Bellekte saklamadan base64'e çeviriyoruz)
        tts = gTTS(text=en_text, lang='en', slow=False)
        filename = f"voice_{int(time.time())}.mp3"
        tts.save(filename)

        with open(filename, "rb") as f:
            audio_base64 = base64.b64encode(f.read()).decode('utf-8')
        
        if os.path.exists(filename): os.remove(filename)

        return jsonify({
            "tr": tr_text,
            "en": en_text,
            "audio": audio_base64
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel için gerekli handler
def handler(request):
    return app(request)
