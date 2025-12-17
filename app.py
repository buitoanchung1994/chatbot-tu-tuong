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
    return "HỆ THỐNG AI QK7 - ĐÃ KÍCH HOẠT CHẾ ĐỘ TIẾNG VIỆT 100%"

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
            "model": "llama3-8b-8192",
            "messages": [
                {
                    "role": "system", 
                    "content": (
                        "Bạn là Chuyên gia Tư tưởng của Quân khu 7, Quân đội Nhân dân Việt Nam. "
                        "NHIỆM VỤ BẮT BUỘC: Chỉ được nói tiếng Việt 100%. Tuyệt đối không dùng tiếng Anh. "
                        "PHONG CÁCH: Trình bày gãy gọn, đanh thép, nghiêm túc. "
                        "XƯNG HÔ: Gọi người dùng là 'đồng chí' và xưng 'tôi' hoặc 'Chuyên gia'. "
                        "NỘI DUNG: Tư vấn về tư tưởng, chính trị, lối sống và kỷ luật quân đội."
                    )
                },
                {"role": "user", "content": f"Hãy trả lời bằng tiếng Việt: {user_input}"}
            ],
            "temperature": 0.4, # Giảm xuống để AI trả lời nghiêm túc, không nói lan man
            "top_p": 0.9
        }
        
        response = requests.post(GROQ_URL, headers=headers, json=payload, timeout=30)
        res_data = response.json()

        if "choices" in res_data:
            reply = res_data['choices'][0]['message']['content']
            # Kiểm tra nếu AI vẫn lỡ tay dùng tiếng Anh thì có thể xử lý tại đây
            return jsonify({"response": reply})
        
        return jsonify({"response": "Báo cáo: Hệ thống đang điều chỉnh, mời đồng chí thử lại."})

    except Exception as e:
        return jsonify({"response": f"Lỗi kết nối nội bộ: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
