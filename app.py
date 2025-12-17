import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from duckduckgo_search import DDGS

app = Flask(__name__)
CORS(app)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

def get_live_knowledge(query):
    """AI tự động đi tìm hiểu thông tin chính thống trên web"""
    try:
        with DDGS() as ddgs:
            # Ưu tiên tìm trên các trang qdnd.vn, mod.gov.vn, chinhphu.vn
            search_query = f"{query} site:qdnd.vn OR site:chinhphu.vn OR site:mod.gov.vn"
            results = ddgs.text(search_query, max_results=3)
            return "\n".join([r['body'] for r in results])
    except:
        return "Không có dữ liệu mới nhất, sử dụng kiến thức nội bộ."

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_input = data.get("user_input", "")
        
        # Bước học tập thời gian thực
        context = get_live_knowledge(user_input)
        
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "system", 
                    "content": (
                        "Bạn là Chuyên gia Tư tưởng Quân khu 7. "
                        "NHIỆM VỤ: Tư vấn chính trị, tư tưởng, kỷ luật sắt. "
                        f"KIẾN THỨC CẬP NHẬT: {context}\n"
                        "PHONG CÁCH: Đanh thép, nghiêm túc, chuẩn mực quân đội. "
                        "XƯNG HÔ: Gọi người dùng là 'đồng chí', xưng 'tôi'. Trả lời tiếng Việt 100%."
                    )
                },
                {"role": "user", "content": user_input}
            ],
            "temperature": 0.2
        }
        
        headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        return jsonify({"response": response.json()['choices'][0]['message']['content']})
    except Exception as e:
        return jsonify({"response": "Báo cáo: Lỗi kết nối sở chỉ huy."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
    
