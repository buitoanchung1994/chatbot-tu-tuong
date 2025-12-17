import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Hệ thống kiến thức cốt lõi được trích xuất từ tài liệu đồng chí cung cấp
KNOWLEDGE_BASE = """
QUY TRÌNH NGHIỆP VỤ:
1. Nắm tư tưởng: Qua quan sát biểu hiện, tổ 3 người, chiến sĩ bảo vệ, nhật ký, mạng xã hội.
2. Quản lý tư tưởng: Phân loại nhóm đối tượng, phối hợp gia đình - đơn vị - địa phương.
3. Định hướng: Giáo dục chính trị, nêu gương, giải thích chính sách pháp luật.
4. Giải quyết: Gặp gỡ riêng, chân tình, dứt điểm vướng mắc, báo cáo cấp trên.

NHÓM TÌNH HUỐNG TRỌNG ĐIỂM (Tập 1, 2, 3):
- Vi phạm kỷ luật: Vay nợ, cờ bạc, dùng chất kích thích, đào bỏ ngũ.
- Tâm lý: Nhớ nhà, lo sợ huấn luyện cường độ cao, băn khoăn khi biên chế xa.
- Gia đình: Vợ con đi theo tà đạo, người thân ốm đau, nợ nần ở quê.
- Nguy cơ cao: Tự tử, tự sát (biểu hiện: tắm rửa sạch sẽ, cho đồ đạc, viết thư tuyệt mệnh).
"""

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_input = data.get("user_input", "")
        
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "system", 
                    "content": (
                        f"Bạn là CHUYÊN GIA TƯ TƯỞNG QUÂN ĐỘI cấp cao. "
                        f"DỮ LIỆU NGHIỆP VỤ CỦA BẠN: {KNOWLEDGE_BASE} "
                        "NHIỆM VỤ: Khi cán bộ đưa ra tình huống, bạn phải trả lời theo cấu trúc: "
                        "1. Nhận định tình huống (Mức độ nguy hiểm). "
                        "2. Gợi ý các bước xử lý (Theo đúng tài liệu 100 tình huống). "
                        "3. Lời khuyên tâm sự (Cách dùng từ khéo léo với bộ đội). "
                        "PHONG CÁCH: Nghiêm túc, đanh thép nhưng giàu lòng nhân ái của người chỉ huy."
                    )
                },
                {"role": "user", "content": user_input}
            ],
            "temperature": 0.2
        }
        
        headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        return jsonify({"response": response.json()['choices'][0]['message']['content']})
    except:
        return jsonify({"response": "Báo cáo: Lỗi kết nối sở chỉ huy."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
