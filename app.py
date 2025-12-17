import os
import time
from google import genai
from google.genai.errors import APIError
import chromadb
from flask import Flask, request, jsonify
from flask_cors import CORS 

# --- CẤU HÌNH VÀ KHỞI TẠO ---
app = Flask(__name__)
CORS(app) 

# LẤY KHÓA API TỪ BIẾN MÔI TRƯỜNG (CẦN GENAI_API_KEY TRÊN RENDER)
client = None
if os.environ.get("GENAI_API_KEY"):
    try:
        client = genai.Client() 
    except Exception as e:
        print(f"LỖI KHỞI TẠO CLIENT GEMINI: {e}")

# --- DỮ LIỆU TỪ TRANG WEB QK5 (CẦN THAY THẾ) ---
QK5_KNOWLEDGE_BASE = [
    # **HÃY THAY THẾ TOÀN BỘ NỘI DUNG NÀY BẰNG DỮ LIỆU THỰC TẾ CỦA BẠN**
    "Tư tưởng Hồ Chí Minh về độc lập dân tộc gắn liền với chủ nghĩa xã hội là kim chỉ nam.",
    "Bốn phẩm chất cơ bản của quân nhân: Trung thành với Đảng, tận tụy với nhân dân, sẵn sàng chiến đấu, kỷ luật nghiêm minh.",
    "Vai trò của Cán bộ Chính trị: Chủ trì xây dựng nghị quyết, trực tiếp đối thoại, định hướng tư tưởng.",
    "Khi có áp lực công việc, cá nhân phải phân loại nhiệm vụ, tự phê bình và chủ động báo cáo với cấp ủy/chỉ huy để được phân công lại.",
    "Tổ chức phải tạo điều kiện cho chiến sĩ tham gia hoạt động văn hóa, thể thao để giải tỏa áp lực và củng cố đoàn kết."
]

# --- SYSTEM PROMPT (TÍNH CÁCH CHATBOT) ---
SYSTEM_PROMPT = """
Bạn là "Chuyên gia Tư vấn Tư tưởng và Tâm lý QK5". Bạn được đào tạo chuyên sâu về Công tác Đảng, Công tác Chính trị (CTĐ, CTCT) trong Quân đội và Tư vấn Tâm lý quân nhân (quản lý căng thẳng, áp lực).

Kiến thức của bạn được giới hạn trong [CONTEXT/DOCUMENTATION PROVIDED BELOW], nguồn gốc từ trang web chuyengiatutuongqk5.created.app.

Giọng điệu phải CHUYÊN NGHIỆP, TRÂN TRỌNG, THÂN TÌNH và MANG TÍNH ĐỘNG VIÊN MẠNH MẼ.

Khi trả lời, bạn phải luôn hướng đến việc GẮN KẾT CÁ NHÂN VỚI TẬP THỂ:
1. Ghi nhận và đồng cảm với trạng thái tâm lý của người hỏi.
2. Giải pháp gồm hai phần:
    a) Trách nhiệm Cá nhân (Tự điều chỉnh): Nêu biện pháp mà quân nhân/cán bộ cần chủ động thực hiện (tự phê bình, rèn luyện, phương pháp làm việc khoa học).
    b) Vai trò Hỗ trợ của Tổ chức: Nêu rõ trách nhiệm của Cán bộ Chính trị/Chỉ huy/Đồng đội trong việc hỗ trợ, giám sát, và giải quyết vấn đề.
3. Tái khẳng định niềm tin vào bản lĩnh và sự hỗ trợ của tổ chức.

GUARDRAILS: Nếu thông tin không có trong tài liệu, bạn phải nói: "Tôi không tìm thấy thông tin này trong tài liệu chuyên môn về tư tưởng và tâm lý quân nhân."
"""

global QK5_COLLECTION = None

# --- HÀM NHÚNG DỮ LIỆU (EMBEDDING) ---
def setup_vector_db(knowledge_base, client):
    if not client: return None
    db_client = chromadb.Client()
    collection = db_client.get_or_create_collection("qk5_tu_tuong_" + str(int(time.time()))) 
    embeddings = []; ids = []
    for i, doc in enumerate(knowledge_base):
        try:
            response = client.models.embed_content(
                model="text-embedding-004", content=doc, task_type="RETRIEVAL_DOCUMENT"
            )
            embeddings.append(response['embedding']); ids.append(f"doc_{i}")
        except APIError as e:
            continue
    if embeddings:
        collection.add(embeddings=embeddings, documents=knowledge_base, ids=ids)
    return collection

# --- HÀM XỬ LÝ CHATBOT RAG CHÍNH ---
def get_rag_answer(question, collection, client):
    if not collection or not client: return "Hệ thống AI chưa được khởi tạo hoặc Khóa API không hợp lệ."
    try:
        query_embedding_response = client.models.embed_content(
            model="text-embedding-004", content=question, task_type="RETRIEVAL_QUERY"
        )
        query_embedding = query_embedding_response['embedding']
        results = collection.query(query_embeddings=[query_embedding], n_results=3)
        context = "\n---\n".join(results['documents'][0])
        contents = [{"role": "user", "parts": [{"text": f"[CONTEXT/DOCUMENTATION PROVIDED BELOW]:\n{context}\n---\n[USER_QUESTION]:\n{question}"}]}]
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=contents,
            config=genai.types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
        )
        return response.text
    except APIError as e:
        return f"Lỗi gọi AI: {e}"
    except Exception as e:
        return f"Lỗi xử lý hệ thống: {e}"

# --- ĐỊNH NGHĨA API ROUTE ---
@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    data = request.json
    question = data.get('question')

    if not question:
        return jsonify({"error": "Thiếu tham số 'question'"}), 400

    answer = get_rag_answer(question, QK5_COLLECTION, client)
    return jsonify({"answer": answer})

# --- KHỞI TẠO KHI SERVER BẮT ĐẦU ---
with app.app_context():
    global QK5_COLLECTION
    QK5_COLLECTION = setup_vector_db(QK5_KNOWLEDGE_BASE, client)

if __name__ == '__main__':
    # Chỉ dùng khi chạy local để kiểm tra
    app.run(host='0.0.0.0', port=5000)
