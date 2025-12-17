import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "AI QK7 ONLINE"

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
        data = request.json
        u_input = data.get("user_input", "")
        
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        payload = {"contents": [{"parts": [{"text": f"Bạn là Chuyên gia QK7. Trả lời tiếng Việt: {u_input}"}]}]}
        
        r = requests.post(url, json=payload)
        res_data = r.json()
        
        if "candidates" in res_data:
            return jsonify({"response": res_data['candidates'][0]['content']['parts'][0]['text']})
        return jsonify({"response": "Hệ thống đang bảo trì API."})
    except Exception as e:
        return jsonify({"response": f"Lỗi: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
