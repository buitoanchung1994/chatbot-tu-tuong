import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from google.genai import types

app = Flask(__name__)
CORS(app)

# 1. HƯỚNG DẪN HỆ THỐNG
SYSTEM_INSTRUCTION = """
Bạn là Chuyên gia Tư tưởng cao cấp Quân khu 7. 
BẮT BUỘC TRẢ LỜI BẰNG TIẾNG VIỆT 100%.
Phong thái: Đanh thép, chuẩn mực quân đội, gần gũi chiến sĩ.
Nhiệm vụ: Tư vấn tư tưởng, đường lối Đảng và chính sách pháp luật.
"""

# 2. KHỞI TẠO CLIENT
API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

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

        # GỬI YÊU CẦU ĐẾN GEMINI 1.5 FLASH (ỔN ĐỊNH)
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                temperature=0.7,
            ),
            contents=[user_message + " (Trả lời bằng tiếng Việt)"]
        )

        return jsonify({"response": response.text})

    except Exception as e:
        error_msg = str(e)
        print(f"Lỗi: {error_msg}")
        if "429" in error_msg:
            return jsonify({"response": "Báo cáo đồng chí, lưu lượng truy cập đang quá tải. Vui lòng đợi 30 giây rồi thử lại."})
        return jsonify({"response": "Báo cáo đồng chí, hệ thống đang bận cập nhật dữ liệu. Vui lòng thử lại sau."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
