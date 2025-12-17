import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai  # Chuyển sang thư viện chuẩn để ổn định hơn

app = Flask(__name__)
CORS(app)

# 1. CẤU HÌNH API
API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# 2. HƯỚNG DẪN HỆ THỐNG
SYSTEM_PROMPT = "Bạn là Chuyên gia Tư tưởng Quân khu 7. Luôn trả lời bằng tiếng Việt, đanh thép và chuẩn mực."

# Khởi tạo model bằng thư viện generativeai chuẩn
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_PROMPT
)

@app.route('/')
def home():
    return "Hệ thống AI Quân khu 7 đang trực chiến!"

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get("user_input", "")

        if not user_message:
            return jsonify({"response": "Đồng chí chưa nhập câu hỏi."}), 400

        # Gọi API lấy phản hồi
        response = model.generate_content(user_message + " (Trả lời bằng tiếng Việt)")
        
        return jsonify({"response": response.text})

    except Exception as e:
        error_msg = str(e)
        print(f"Lỗi: {error_msg}")
        if "429" in error_msg:
            return jsonify({"response": "Báo cáo đồng chí, hệ thống đang quá tải. Vui lòng thử lại sau 30 giây."})
        return jsonify({"response": f"Báo cáo đồng chí, hệ thống gặp lỗi kết nối (404). Vui lòng kiểm tra lại cấu hình model."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
