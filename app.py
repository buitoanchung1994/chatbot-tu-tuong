import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Khởi tạo API
API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# Cấu hình Model với đường dẫn tuyệt đối
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash" # Thêm models/ để fix 404
)

@app.route('/')
def home():
    return "Hệ thống AI Quân khu 7 đang trực chiến!"

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_input = data.get("user_input", "")
        
        # Thiết lập hướng dẫn hệ thống trực tiếp trong lời gọi
        prompt = f"Bạn là Chuyên gia Tư tưởng Quân khu 7. Trả lời đanh thép bằng tiếng Việt: {user_input}"
        
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        print(f"Lỗi: {str(e)}")
        return jsonify({"response": "Báo cáo đồng chí, hệ thống đang bận. Vui lòng thử lại sau giây lát!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
