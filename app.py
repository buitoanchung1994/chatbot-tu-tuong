import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Cấu hình API Groq
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

@app.route('/')
def home():
    return "HỆ THỐNG AI QK7 - TRỰC CHIẾN 24/7"

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
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "system", 
                    "content": (
                        "Bạn là Chuyên gia Tư tưởng của Quân khu 7. "
                        "NHIỆM VỤ: Chỉ trả lời bằng tiếng Việt 100%. "
                        "PHONG CÁCH: Quân đội, nghiêm túc, đanh thép, rõ ràng. "
                        "XƯNG HÔ: Gọi người dùng là 'đồng chí', xưng là 'tôi'. "
                        "NỘI DUNG: Tư vấn tư tưởng, chính trị, kỷ luật và lối sống quân nhân."
                    )
                },
                {"role": "user", "content": user_input}
            ],
            "temperature": 0.4
        }
        
        response = requests.post(GROQ_URL, headers=headers, json=payload, timeout=30)
        res_data = response.json()

        if "choices" in res_data:
            reply = res_data['choices'][0]['message']['content']
            return jsonify({"response": reply})
        
        return jsonify({"response": "Báo cáo: Kết nối gián đoạn, mời đồng chí thử lại."})

    except Exception as e:
        return jsonify({"response": f"Lỗi hệ thống: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
