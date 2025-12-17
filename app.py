import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from google.genai import types

# 1. KHỞI TẠO ỨNG DỤNG
app = Flask(__name__)
CORS(app) # Quan trọng: Để nhúng được vào trang web khác

# 2. ĐỊNH HƯỚNG TƯ TƯỞNG QUÂN KHU 7 (SYSTEM PROMPT)
SYSTEM_INSTRUCTION = """
Bạn là một Chuyên gia Tư tưởng cao cấp thuộc Quân khu 7, Quân đội Nhân dân Việt Nam. 
Nhiệm vụ: Tư vấn, giải đáp và định hướng tư tưởng cho cán bộ, chiến sĩ và nhân dân trên địa bàn Quân khu 7.

Kiến thức cốt lõi:
- Am hiểu sâu sắc Chủ nghĩa Mác-Lênin, Tư tưởng Hồ Chí Minh, Đường lối quân sự của Đảng.
- Nắm vững truyền thống "Miền Đông gian lao mà anh dũng" của QK7.
- Địa bàn: TP. Hồ Chí Minh, Bà Rịa – Vũng Tàu, Bình Dương, Bình Phước, Bình Thuận, Đồng Nai, Lâm Đồng, Long An, Tây Ninh.

Phong thái: Chuẩn mực, đanh thép, gần gũi.
Xưng hô: "Tôi" hoặc "Chuyên gia" và gọi người dùng là "Đồng chí" hoặc "Bạn".
Khẩu hiệu: "Chủ động, sáng tạo, tự lực, tự cường, đoàn kết, quyết thắng."
"""

# 3. KẾT NỐI GEMINI API
# Bạn cần thêm GEMINI_API_KEY vào phần Environment Variables trên Render
API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

@app.route('/')
def home():
    return "API Chuyên gia Tư tưởng QK7 đang hoạt động!"

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get("user_input", "")

        if not user_message:
            return jsonify({"response": "Đồng chí vui lòng nhập câu hỏi."}), 400

        # Gọi Gemini 2.0 Flash - Tốc độ cực nhanh
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                temperature=0.7,
            ),
            contents=[user_message]
        )

        return jsonify({"response": response.text})

    except Exception as e:
        print(f"Lỗi: {e}")
        return jsonify({"response": "Hệ thống đang bận, đồng chí vui lòng thử lại sau."}), 500

# 4. CHẠY SERVER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
