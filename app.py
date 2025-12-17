import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Cho phép tất cả các nguồn truy cập để tránh lỗi CORS khi nhúng web
CORS(app)

# Cấu hình các tham số hệ thống
API_KEY = os.environ.get("GEMINI_API_KEY")
MODEL_NAME = "gemini-1.5-flash"

@app.route('/')
def home():
    return "AI QK7 ONLINE - HỆ THỐNG SẴN SÀNG"

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # 1. Lấy dữ liệu từ phía Web
        data = request.json
        user_input = data.get("user_input", "")
        
        if not user_input:
            return jsonify({"response": "Đồng chí chưa nhập nội dung báo cáo."})

        # 2. Xây dựng URL gọi Google API trực tiếp (v1beta)
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"
        
        # 3. Thiết lập nội dung gửi đi (Prompt Engineering)
        # Ép buộc AI đóng vai Chuyên gia và chỉ nói tiếng Việt
        payload = {
            "contents": [{
                "parts": [{
                    "text": f"Bạn là Chuyên gia Tư tưởng Quân khu 7. Bạn có phong cách nói chuyện đanh thép, nghiêm túc, đúng tác phong quân đội. Mọi câu trả lời của bạn phải bằng tiếng Việt. Nội dung đồng chí đó hỏi là: {user_input}"
                }]
            }],
            "generationConfig": {
                "temperature": 0.7,
                "topP": 0.8,
                "topK": 40,
                "maxOutputTokens": 1024,
            }
        }

        # 4. Gửi yêu cầu sang máy chủ Google
        response = requests.post(url, json=payload, timeout=30)
        res_data = response.json()

        # 5. Phân tích kết quả trả về
        if "candidates" in res_data and len(res_data["candidates"]) > 0:
            bot_text = res_data["candidates"][0]["content"]["parts"][0]["text"]
            return jsonify({"response": bot_text})
        
        # 6. Xử lý các lỗi phản hồi cụ thể từ Google
        if "error" in res_data:
            error_msg = res_data["error"].get("message", "")
            if "API_KEY_INVALID" in str(res_data):
                return jsonify({"response": "Báo cáo: API Key không hợp lệ. Đồng chí hãy kiểm tra lại cấu hình trên Render."})
            return jsonify({"response": f"Báo cáo: Lỗi từ máy chủ Google ({error_msg})"})

        return jsonify({"response": "Báo cáo: Hệ thống gặp phản hồi lạ từ Google. Vui lòng thử lại."})

    except Exception as e:
        print(f"Lỗi hệ thống: {str(e)}")
        return jsonify({"response": f"Báo cáo: Lỗi hệ thống nội bộ ({str(e)})"})

if __name__ == "__main__":
    # Chạy trên cổng do Render cung cấp
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
