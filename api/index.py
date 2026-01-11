import os, time, base64
from flask import Flask, render_template, request, jsonify
from googletrans import Translator
from gtts import gTTS

# Vercel'de çalışması için template klasörünü dışarıda aramasını söylüyoruz
app = Flask(__name__, template_folder='../templates')
translator = Translator()

# 1. LANDING PAGE (Tanıtım Sayfası)
@app.route('/')
def landing():
    return render_template('landing.html')

# 2. UYGULAMA PANELİ (Çeviri Paneli)
@app.route('/app')
def main_app():
    return render_template('index.html')

# 3. ÇEVİRİ VE SES ÜRETİM MOTORU
# Not: Vercel "serverless" çalıştığı için mikrofonu sunucuda değil, 
# senin bilgisayarında çalıştırıp metni buraya göndereceğiz.
@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.json
        tr_text = data.get('text')
        
        if not tr_text:
            return jsonify({"error": "Metin yok"}), 400

        # Bağlamı koruyarak çevir
        en_text = translator.translate(tr_text, dest='en').text
        
        # Sesi üret
        filename = f"audio.mp3"
        tts = gTTS(text=en_text, lang='en', slow=False)
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

# Vercel için gerekli
def handler(request):
    return app(request)

if __name__ == '__main__':
    app.run(port=5002)
