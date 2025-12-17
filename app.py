import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from google.genai import types

app = Flask(__name__)
CORS(app)

SYSTEM_INSTRUCTION = """
Bạn là Chuyên gia Tư tưởng Quân khu 7. 
LUÔN LUÔN TRẢ LỜI BẰNG TIẾNG VIỆT.
Phong cách: Đanh thép, chuẩn mực, quân đội.
Không bao giờ trả lời bằng tiếng Anh.
"""

API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get("user_input", "")

        response = client.models.generate_content(
            model="gemini-1.5-flash", # Dùng bản 1.5 để tránh lỗi 429
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                temperature=0.7,
            ),
            contents=[user_message + " (Trả lời bằng tiếng Việt)"]
        )
        return jsonify({"response": response.text})
    except Exception as e:
        # Nếu vẫn lỗi 429, trả về thông báo tiếng Việt
        if "429" in str(e):
            return jsonify({"response": "Báo cáo đồng chí, hệ thống đang tiếp nhận quá nhiều câu hỏi cùng lúc. Vui lòng chờ 30 giây rồi thực hiện lại!"})
        return jsonify({"response": "Hệ thống đang bảo trì, đồng chí vui lòng thử lại sau."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
