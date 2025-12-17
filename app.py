import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sử dụng phiên bản v1 thay vì v1beta để ổn định
API_KEY = os.environ.get("GEMINI_API_KEY")
URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"

@app.route('/')
def home():
    return "AI QK7 ONLINE - VERSION 2.0"

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_input = data.get("user_input", "")
        
        # Cấu hình gửi tin nhắn chuẩn v1
        payload = {
            "contents": [{
                "parts": [{
                    "text": f"Bạn là Chuyên gia Tư tưởng Quân khu 7. Hãy trả lời bằng tiếng Việt, phong cách quân đội: {user_input}"
                }]
            }]
        }
        
        response = requests.post(URL, json=payload, timeout=30)
        res_data = response.json()

        # Kiểm tra phản hồi
        if "candidates" in res_data:
            reply = res_data['candidates'][0]['content']['parts'][0]['text']
            return jsonify({"response": reply})
        
        # Bẫy lỗi chi tiết để báo cáo đồng chí
        error_msg = res_data.get('error', {}).get('message', 'Lỗi phản hồi không xác định')
        return jsonify({"response": f"Báo cáo: Máy chủ Google phản hồi lỗi: {error_msg}"})

    except Exception as e:
        return jsonify({"response": f"Báo cáo: Lỗi kết nối nội bộ: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
