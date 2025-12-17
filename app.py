import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Cấu hình kết nối Groq
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

@app.route('/')
def home():
    return "HỆ THỐNG AI QK7 - ĐANG TRỰC CHIẾN (GROQ)"

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_input = data.get("user_input", "")
        
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": "Bạn là Chuyên gia Tư tưởng Quân khu 7. Trả lời bằng tiếng Việt, phong cách quân đội, đanh thép, nghiêm túc."},
                {"role": "user", "content": user_input}
            ]
        }
        
        response = requests.post(GROQ_URL, headers=headers, json=payload, timeout=30)
        res_data = response.json()

        if "choices" in res_data:
            reply = res_data['choices'][0]['message']['content']
            return jsonify({"response": reply})
        
        return jsonify({"response": "Báo cáo: Hệ thống đang điều chỉnh, vui lòng thử lại."})

    except Exception as e:
        return jsonify({"response": f"Lỗi kết nối: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
