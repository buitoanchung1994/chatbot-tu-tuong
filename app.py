import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Hệ thống kiến thức cốt lõi được trích xuất từ tài liệu đồng chí cung cấp
KNOWLEDGE_BASE = "A.NHÓM TÌNH HUỐNG TƯ TƯỞNG NẢY SINH TRONG THỰC HIỆN NHIỆM VỤ HUẤN LUYỆN , SẴN SÀNG CHIẾN ĐẤU (15 TÌNH HUỐNG)

Tình huống 1 : Kết thúc thời gian huấn luyện chiến sĩ mới, một số chiến sĩ băn khoăn lo lắng sợ biên chế sang lực lượng Hải quân, Cảnh sát biển vì phải vừa xa nhà, vừa khó khăn vất vả.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị, đánh giá tình hình tư tưởng trong đơn vị, xác định các chủ trương, biện pháp khắc phục.
- Phân công cán bộ gặp gỡ số chiến sĩ không an tâm tư tưởng, giáo dục động viên làm rõ quyền lợi, nghĩa vụ trách nhiệm của người chiến sĩ cách mạng trong thực hiện nhiệm vụ bảo vệ Tổ Quốc .
- Báo cáo, xin ý kiến chỉ đạo của cấp trên .
- Tổ chức sinh hoạt đơn vị giáo dục định hướng tư tưởng cho bộ đội; phổ biến rõ nhiệm vụ, những tiêu chuẩn đã chọn và chỉ tiêu để các chiến sĩ nắm những điều kiện thuận lợi, khó khăn và ché độ được hưởng để bộ đội an tâm tư tưởng, sẵn sàng thực hiện và hoàn thành mọi nhiệm vụ được giao, nhận thức đúng vinh dự, trách nhiệm khi được thực hiện nhiệm vụ trực tiếp bảo vệ chủ quyền và toàn vẹn lãnh thổ thiêng liêng của Tổ quốc.
- Phối hợp chặt chẽ với gia đình, địa phương, người thân của số quân nhân trên để động viên, định hướng tư tưởng cho bộ đội an tâm, sẵn sàng nhận và thực hiện mọi nhiệm vụ.
- Chỉ đạo chi đoàn tổ chức diễn đàn về chủ đề biển, đảo khơi dậy tinh thần yêu nước của tuổi trẻ; phát động thi đua sẵn sàng nhận và hoàn thành mọi nhiệm vụ được giao, tổ chức đăng kí tự nguyện tham gia bảo vệ chủ quyền biển, đảo.
- Phân công cán bộ theo dõi, kèm cặp, giúp đỡ từng người, từng tổ; sử dụng cách chiến sĩ bảo vệ của đơn vị nắm tình hình, chủ động dự kiến các vấn đề nảy sinh như đào ngũ, vắng mặt trái phep để có các biện pháp ngăn chặn và xử lý kịp thời.

Tình huống 2 : Kết thúc thời gian huấn luyện tân binh, đơn vị tổ chức biên chế và lựa chọn chiến sĩ đi học tiểu(khẩu) đội trưởng, một số chiến sĩ đẵ vắng mặt trái phép.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị, xác định nguyên nhân, nhận định, đánh giá tình chất, tác hại, mức độ ảnh hưởng của sự việc để trao đổi, thống nhất biện pháp giải quyết, phân công cán bộ phụ trách và báo cáo cấp trên xin ý kiến chỉ đạo.
- Tổ chức sinh hoạt đơn vị quán triệt nâng cao nhận thức về nhiệm vụ , ổn định tình hình tư tưởng bộ đội.
- Phân công cán bộ, phối hợp gia đình, địa phương, bạn bè thân thuộc tìm, gọi, động viên quân nhân vắng mặt trở lại đơn vị.
- Chỉ đạo tiến hành lập biên bản vắng mặt trái phép, quản lý quân trang, vật chất của cá nhân vắng mặt ( có biên bản).
- Trực tiếp hoặc cử cán bộ gặp gỡ các đồng chí có mối quan hệ gần gũi thân thiết với quân nhân vắng mặt để nắm tình hình (tình hình tư tưởng, lý do vắng mặt, thời gian vắng mặt ,hoàn cảnh gia đình …)
- Khi quân nhân quay trở lại đơn vị, phân công cán bộ kèm cặp , giáo dục , động viên , giúp đỡ quân nhân đó tiến bộ, trưởng thành (biện pháp này là chính)
- Gặp gỡ quân nhân nắm tình hình tư tưởng mọi mặt, đặc biệt là trong thời gian quân nhân vắng mặt có vi phạm pháp luật và các qui định của địa phương không, từ đó có biện pháp giải quyết kịp thời.
- Triển khai quân nhân vắng mặt trái phép viết bản tưởng trình, kiểm điểm và tổ chức sinh hoạt rút kinh nghiệm, xét kỉ luật theo đúng Điều lệnh Quản lý bộ đội, giúp quân nhân nhận ra khuyết điểm, xác định quyết tâm sửa chữa khuyết điểm, đồng thời căn cứ vào tính chất , mức độ vi phạm xác định hình thưc kỷ luật (không nhất thiết trường hợp nào cũng xác định kỷ luật).
- Thông báo với gia đình, địa phương về trường hợp vắng mặt trái phép đã trở lại đơn vị , đề nghị tiếp tục phối hợp quản lý, giáo dục quân nhân .
- Tăng cường các biện pháp quản lý, duy trì chặt chẽ chết độ ngày, tuần; tổ chức hoạt động giờ nghỉ , ngày nghỉ.

Tình huống 3 : Sau vụ việc mất an toàn trong huấn luyện ném lựu đạn đã được rút kinh nghiệm, xác định là do thực hành động tác sai yếu lĩnh, nhưng một số hạ sĩ quan, chiến sĩ còn lại có biểu hiện lo lắng, sợ kiểm tra thực hành nội dung “3 tiếng nổ”
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị, thống nhất các biện pháp giải quyết (trong hội ý, cán bộ đơn vị phản ảnh, báo cáo tình hình tư tưởng, tâm trạng của số hạ sĩ quan , chiến sĩ có biểu hiện băn khoăn, lo lắng và công tác chuẩn bị cho nhiệm vụ kiểm tra “3 tiếng nổ”
- Gặp gỡ số hạ sĩ quan, chiến sĩ có biểu hiện băn khoăn, lo lắng để giáo dục, động viên, phân tích cho bộ đội hiểu nguyên nhân vụ việc mất an toàn đã xảy ra trong đơn vị, động viên cho bộ đội an tâm sẽ không xảy ra mất an toàn nếu anh em thực hiện đúng yếu lĩnh động tác và chấp hành nghiêm qui tắc bảo đảm an toàn trong kiểm tra.
- Tổ chức sinh hoạt đơn vị, giáo dục định hướng tư tưởng cho bộ đội tin tưởng vào quy tắc bảo đảm an toàn trong huấn luyện, các yếu lĩnh động tác đã được huấn luyện; nêu một số vụ việc mất an toàn trong huấn luyện, làm rõ nguyên nhân để bộ đội rút kinh nghiệm.
- Báo cáo cấp trên xin ý kiến chỉ đạo.
- Tăng cường các biện pháp huấn luyện, rèn luyện kỹ thuật, chiến thuật và chuẩn bị tốt tâm lý cho bộ đội như:
+ Duy trì nghiêm túc chặt chẽ, đúng qui trình huấn luyện các nội dung “3 tiếng nổ”; tổ chức luyện tập thuần thục động tác thực hành cho bộ đội .
+ Tổ chức cho bộ đội xem những bộ phim chiến lệ, videoclip diễn tập.
+ Trước khi vào nội dung kiểm tra, cử một số cán bộ (trung đội trưởng , tiểu đội trưởng) thực hành trước để bộ đội quan sát, tạo tâm lý an tâm, tin tưởng vào sự an toàn trong kiểm tra.
Phân công cán bộ theo dõi, kèm cặp giúp đỡ ổn định tư tưởng, tâm lý cho bộ đội trong kiểm tra.

Tình huống 4 : Đại đội làm nhiệm vụ huấn luyện chiến sĩ mới được 1 tháng , một đồng chí chiến sĩ mới lợi dụng bữa ăn trưa kêu mệt không đi ăn ở nhà một mình rối “tự thương” bằng cách dùng dao chặt ngón tay trỏ của bàn tay phải (ngón tay bóp còn súng)
Gợi ý biện pháp xử lý
- Nhanh chóng sơ cứu, băng bó vết thương, bảo quản ngón tay, đưa lên quân y tuyến trên ; phân công cán bộ, chiến sĩ đi cùng, không để chiến sĩ tiếp tục hành động tự thương . 
- Nhanh chóng hội ý chỉ huy đại đội; nhận định sơ bộ tình hình diễn biến tư tưởng trong toàn đơn vị; báo cáo cấp trên xin ý kiến chỉ đạo.
Tổ chức sinh hoạt đơn vị, làm rõ nguyên nhân, động cơ hành động tự thương; khẳng định hành vi tự thương với lý do gì cũng là hành vi trốn tránh nghĩa vụ quân sự là vi phạm Pháp luật Nhà nước, qua đó rút kinh nghiệm chung trong cán bộ, chiến sĩ toàn đơn vị.
- Phối hợp chặt chẽ và phục vụ tốt các cơ quan chức năng trong điều tra và xét xử theo quy định của kỷ luật quân đội, pháp luật Nhà nước.
- Thông báo cho gia đình và địa phương về việc quân nhân tự thương làm cơ sở cho việc phối hợp giáo dục và quản lý quân nhân sau khi hoàn thành nghĩa vụ quân sự.
- Thường xuyên làm tốt công tác nắm, quản lý, dự báo, giải quyết tư tưởng trong đơn vị , nhất là quản lý chặt chẽ, dìu dắt, giúp đỡ số quân nhân có biểu hiện chưa an tâm tư tưởng .
- Phát huy vai trò của tổ chức quần chúng , hội đồng quân nhân, tổ tư vấn tâm lý, pháp lý trong việc giáo dục, động viên, tư vấn kỹ năng giải quyết các vấn đề tư tưởng nảy sinh của bộ đội, đưa bộ đội vào các hoạt động chung của đơn vị.
Tình huống 5 : Sau vụ việc mất an toàn trong huấn luyện bay và một số vụ tai nạn máy bay trên thế gới, một số hạ sĩ quan, chiến sĩ có biểu hiện không tin tưởng vào vũ khí trang bị, phương tiện kỹ thuật quân sự và sợ huấn luyện bay
Gợi ý biện pháp xử lý
- Báo cáo cấp trên xin ý kiến chỉ đạo.
- Nắm lại tình hình tư tưởng của số hạ sĩ quan, chiến sĩ sau vụ tai nạn huấn luyện bay và các vụ tai nạn bay trên thế giới gần đây.
- Hội ý cấp ủy, chỉ huy đơn vị, thống nhất các biện pháp giải quyết (trong hội ý cán bộ đơn vị phản ánh, báo cáo tình hình tư tưởng, tâm trạng của số hạ sĩ quan, chiến sĩ có biểu hiện băn khoăn, lo lắng).
- Phân công cán bộ gặp gỡ số hạ sĩ quan, chiến sĩ có biểu hiện băn khoăn, lo lắng phân tích bộ đội hiểu được nguyên nhân vụ việc mất an toàn trong huấn luyện bay và xác suất các vụ mất an toàn bay là rất hiếm, động viên bộ đội an tâm thực hiện nhiệm vụ.
- Tổ chức giảng bình rút kinh nghiệm huấn luyện bay và cho bộ đội xem phim tư liệu về các cuộc chiến tranh của ta, tham quan bay huấn luyện để bộ đội yên tâm, tin tưởng vào khả năng vũ khí trang bị, phương tiện kỹ thuật quân sự của ta.
- Tổ chức sinh hoạt đơn vị, giáo dục định hướn g tư tưởng cho bộ đội , xây dựng niềm tin vào vũ khí trang bị, phương tiện kĩ thuật quân sự, bản lĩnh, ý chí, trình độ, kỹ năng xử lý của người quân nhân cách mạng trong thực hiện nhiệm vụ…
- Phân công cán bộ theo dõi, kèm cặp, giúp đỡ, ổn định tư tưởng, tâm lý cho quân nhân trong huấn luyện.

Tình huống 6 : Sau vụ việc tai nạn chết đuối (chiến sĩ say rượu tự ngã) ở hồ gần đơn vị, mặc dù đơn vị đã tiến hành các biện pháp nghiệp vụ (lập biên bản, giám định pháp y, kết luật vụ việc và phối hợp với gia đình địa phương mai táng chu đáo), song gia đình đi xem bói, thầy bói nói : “Cháu bị chết oan nên gọi hồn không lên”. Tin theo lời thầy bói, gia đình đã lên đơn vị khiếu kiện.
Gợi ý biện pháp xử lý
- Đại diện chỉ huy đơn vị đón tiếp và nắm nguyện vọng của gia đình chiến sĩ.
- Trao đổi thống nhất trong cấp ủy,chỉ huy đơn vị, phân công cán bộ phụ trách giải quyết vụ việc và ổn định tình hình đơn vị.
- Báo cáo cấp trên xin ý kiến chỉ đạo, mời cơ quan chức năng xuống đơn vị phối hợp giải quyết vụ việc.
- Mời một số cán bộ, chiến sĩ trực tiếp chứng kiến vụ việc và một số chiến sĩ cùng quê với gia đình lên cùng với chỉ huy đơn vị làm việc với gia đình chiến sĩ.
- Cung cấp cho gia đình một số thông tin về kết quả làm việc của cơ quan chức năng như : Biên bản vụ việc, kết quả giám định pháp y, các chế độ chính sách đơn vị đã chi trả với chiến sĩ và các hoạt động hỗ trợ của cán bộ, chiến sĩ đơn vị đối với gia đình (nếu có); trao đổi , chia sẻ cùng gia đình về những đau thương mất mát; cùng với các thành phần trong buổi làm việc phân tích để gia đình hiểu rõ sự thật, động viên gia đình không tin vào bói toán, mê tín dị đoan sẽ làm cho gia đình thêm khổ đau … (chú ý trong khi làm việc với gia đình cần có biên bản ghi lại diễn biến, kết quả làm việc và ý kiến của gia đình, tránh về sau gia đình tiếp tục có ý kiến với đơn vị).
- Tổ chức sinh hoạt đơn vị, thông báo cho cán bộ, chiến sĩ kết quả làm việc của cơ quan chức năng, ổn định tình hình tư tưởng, động viên cán bộ, chiến sĩ không mê tín dị đoan ; từ vụ việc trên cần nêu cao ý thức chấp hành kỷ luật, vận động bỏ thuốc lá, không uống rượu, bia; quán triệt và thực hiện nghiêm túc các quy định về bảo đảm an toàn trong thực hiện nhiệm vụ.
- Phân công cán bộ theo dõi nắm bắt, quản lý tình hình tư tưởng của bộ đội để có biện pháp giải quyết kịp thời.
- Quan tâm , chăm lo đời sống vật chất, tinh thần của cán bộ, chiến sĩ; tổ chức tốt các hoạt động vui chơi giải trí trong giờ nghỉ, ngày nghỉ cho bộ đội.
- Tổng hợp tình hình báo cáo cấp trên.

Tình huống 7 : Đại đội thực hành kiểm tra bắn đạn thật, một vài loạt đạn đầu bắn không đạt yêu cầu, một số chiến sĩ trong đơn vị có biểu hiện hoang mang, lo lắng.
Gợi ý biện pháp xử lý
- Báo cáo chỉ huy tiểu đoàn về kết quả bắn của các loạt đạn đầu và tình hình tâm lý , tư tưởng của đơn vị.
- Gặp gỡ số chiến sĩ đã bắn các loạt đạn đầu và người dẫn bắn để tìm hiểu nguyên nhân kết quả bắn không đạt yêu cầu.
- Hội ý nhanh trong chỉ huy về nguyên và biện pháp giải quyết
- Nếu do súng hiệu chỉnh chưa tốt phải đổi súng và cho nhân viên chuyên môn kĩ thuật bắn kiểm tra xác định súng tốt mới cho bắn tiếp.
- Nếu do việc lập danh sách bắn chưa khoa học phải lựa chọn các đồng chí vững tâm lý , có kết quả huấn luyện giỏi bắn trước (lập lại danh sách bắn)
- Nếu do thời tiết không thuận lợi, mưa to, gió lớn, báo cáo cấp trên xin ngừng kiểm tra.
- Tập trung đại đội rút kinh nghiệm, thông báo rõ nguyên nhân và biện pháp khắc phục ; nhắc nhở, động viên bộ đội bình tĩnh, tự tin, trung thành với yếu lĩnh động tác đã được tập luyện.
- Chọn một số đồng chí cán bộ, chiến sĩ có yếu lĩnh, động tác và kết quả bắn tốt lên bắn loạt tiếp theo để lấy lại niềm tin cho các loạt bắn tiếp theo.
- Động viên bộ đội trung thành với yếu lĩnh động tác, tiếp tục bắn theo kế hoạch; duy trì nghiêm kỷ luật trường  bắn, làm tốt công tác cổ động thao trường, động viên, biểu dương, khích lệ kịp thời các chiến sĩ bắn giỏi.

Tình huống 8 : Trong thực hành huấn luyện của đại đội đã xảy ra mất an toàn ( có chiến sĩ bị tử vong) gây hoang mang trong đơn vị
Gợi ý biện pháp xử lý
- Người chỉ huy trực tiếp huấn luyện ra lệnh tạm dừng huấn luyện; tổ chức bảo vệ hiện trường; sơ bộ nắm tình hình và báo cáo chỉ huy cấp trên.
- Nhanh chóng hội ý, thống nhất trong cấp ủy, chỉ huy đơn vị đánh giá tình hình, xác định nguyên nhân ban đầu và biện pháp xử lý.
- Thông báo ngay cho gia đình thân nhân chiến sĩ tử vong.
- Phối hợp chặt chẽ với cấp trên tiến hành điều tra, kết luận và làm rõ nguyên nhân xảy ra mất an toàn chết người; thống nhất biện pháp giải quyết hậu quả.
- Cán bộ các cấp thường xuyên bám sát mọi hoạt động, động viên, nhắc nhở bộ đội ổn định tu tưởng, tâm lý; không để bộ đội hoảng loạn, lộn xộn, phát ngôn không đúng gây xáo trộn trong đơn vị.
- Tiến hành giải quyết hậu quả theo quy định đúng chức năng, nhiệm vụ, quyền hạn và điều kiện thực tế của đơn vị.
- Động viên cán bộ, chiến sĩ đơn vị bằng vật chất, tinh thần chia sẻ, giúp đỡ với gia đình quân nhân tử vong; phối hợp với gia đình tổ chức an táng chu đáo.
- Tổ chức sinh hoạt chi ủy, chi bộ, đội ngũ cán bộ và đơn vị để thông báo kết luận điều tra của cấp trên; kiểm điểm làm rõ trách nhiệm , rút ra bài học kinh nghiệm trong công tác lãnh đạo, chỉ đạo và tổ chức thực hiện nhiệm vụ huấn luyện trong thời gian tiếp theo bảo đảm an toàn tuyệt đối; xem xét xác định trách nhiệm và xử lý kỷ luật cán bộ đảng viên và chiến sĩ có liên quan(nếu có) thực hiện tốt các chế độ, chính sách cho quân nhân.

Tình huống 9 : Trong quá trình triển khai ném lựu đạn, đánh bộc phá, chỉ huy trung đoàn phát hiện khoảng 1/5 số chiến sĩ mới của Đại đội 1 có biểu hiện lo lắng, đi tiểu nhiều lần trong quá trình chờ đợi; một số đồng chí khi tiếp xúc với lựu đạn,  bộc phá có biểu hiện run rẩy
Gợi ý biện pháp xử lý
Đây là biểu hiện tâm lý, chứng tỏ quá trình huấn luyện bộ đội chưa thành thạo động tác , chưa tin tưởng, tâm lý chưa vững, dễ mất an toàn, vì vậy :
- Cho ngừng ném lựu đạn, đánh bộc phá.
- Nắm tư tưởng số chiến sĩ có biểu hiện nói trên.
- Kiểm tra lại yếu lĩnh động tác của chiến sĩ đó.
- Hội ý chỉ huy, cần thiết cho số chiến sĩ đó tiếp tục huấn luyện lại, khi đã đảm bảo sự vững vàng , tin tưởng, quyết tâm thì tiến hành kiểm tra.
- Khi tiến hành kiểm tra cần có cán bộ có kinh nhiệm hướng dẫn, bảo đảm an toàn.
- Cho một số chiến sĩ có kết quả giỏi làm mẫu.
- Thường xuyên tở chức phong trào thi đua huấn luyện giỏi trong đơn vị.

Tình huống 10 : Trong đại đội có chiến sĩ lấy lý do sức khỏe yếu, xin đi điều trị tại bệnh xá để không phải tham gia đợt huấn luyện chiến sĩ sắp tới, đã tác động xấu đến nhận thức về nhiệm vụ của một số đồng chí khác .
Gợi ý biện pháp xử lý
- Trao đổi thống nhất trong lãnh đạo, chỉ huy đơn vị về biện pháp xử lý; phân công cán bộ phụ trách, quan tâm, sâu sát động viên chăm sóc các đồng chí đó.
- Tiến hành kiểm tra sức khỏe của chiến sĩ. Nếu ốm thật, đề nghị quân y kiểm tra mức độ bệnh tình chăm sóc điều trị chu đáo.
- Trường hợp do ngại huấn luyện thì trực tiếp gặp gỡ, nắm nguyên nhân tại sao đồng chí đó ngại tham gia huấn luyện .Chú ý : phương pháp nắm bắt phải khéo léo, mềm dẻo thông qua tâm sự , trò chuyện để nắm bắt tâm tư, tình cảm, vướng mắc của chiến sĩ.
- Nếu do kế hoạch huấn luyện chưa khoa học, hoặc do thời tiết quá mức chịu đựng của bộ đội … phải báo cáo điều chỉnh.
- Nếu do phương pháp của cán bộ cần rút kinh nghiệm kịp thời.
- Nếu do sức khỏe của chiến sĩ, có thể bố trí vị trí huấn luyện phù hợp
- Trường hợp do lười biếng phải quan tâm giáo dục động viên.
- Giáo dục, động viên nâng cao nhận thức của chiến sĩ về trách nhiệm, nghĩa vụ đối với công tác huấn luyện của đơn vị, tạo điều kiện để giúp chiến sĩ đó tháo gỡ khó khăn gặp phải trong huấn luyện.
- Phát huy vai trò của tổ chức, nhất là tổ 3 người, tiểu đội, trung đội, đoàn thanh niên, hội đồng quân nhân và các mối quan hệ bạn bè thân thiết, đồng hương, người thân, gia đình, người yêu (nếu có) để giáo dục, động viên chiến sĩ có nhận thức tốt về nhiệm vụ, tích cực tham gia huấn luyện.
- Hướng dẫn chỉ đạo tiểu đội, trung đội sinh hoạt rút kinh nghiệm về công tác quản lý tư tưởng bộ đội; xây dựng động cơ, trách nhiệm trong nhiệm vụ huấn luyện; phát động thi đua trong học tập như “kíp xe học tập giỏi”, tổ học tập giỏi … động viên chiến sĩ tích cực tham gia.
- Duy trì nghiêm túc nề nếp chế độ huấn luyện ở đơn vị, thường xuyên tổ chức hội thao, hội thi,kịp thời biểu dương tập thể, cá nhân có thành tích trong huấn luyện, làm tốt công tác cổ động thao trường.
- Tổng hợp tình hình báo cáo cấp trên.

Tình huống 11 : Sau vụ việc mất an toàn trong huấn luyện bay, đơn vị tổ chức đưa tro cốt liệt sĩ phi công từ máy bay về gia đình, lúc từ máy bay xuống đã có người chụp ảnh đưa lên mạng (hình ảnh hai quân nhân bê túi du lịch , trong đó có đựng tro cốt liệt sĩ) , dẫn đến một số báo chí, trang mạng bình luận, phát tán, xuyên tạc … có chiến sĩ trong đơn vị biểu hiện không đồng tình với cách thức đó.
Gợi ý biện pháp xử lý
- Trao đổi, thống nhất trong cấp ủy , chỉ huy đơn vị nhận định tình hình , xác định tính chất , mức độ ảnh hưởng của nguồn thông tin trên đối với cán bộ, chiến sĩ và hậu phương gia đình phi công.
- Báo cáo cấp trên xin ý kiến chỉ đạo; phân công cán bộ phụ trách thực hiện các biện pháp tháo gỡ và sinh hoạt thống nhất tư tưởng cán bộ, chiến sĩ trong đơn vị.
- Tiến hành gặp gỡ một số chiến sĩ đã được tiếp xúc với các trang mạng và có biểu hiện không đồng tình cách thức tổ chức đưa di cốt liệt sĩ của chỉ huy đơn vị để nắm tình hình; phân tích , động viên để các đồng chí thấy được sự xuyên tạc, chống phá của các thế lực phản động trên mạng hiện nay.
- Tổ chức sinh hoạt đơn vị ổn định tình hình mọi mặt, thông báo cho cán bộ , chiến sĩ đơn vị về bản chất sự việc đã được đơn vị, gia đình thống nhất và thể theo nguyện vọng gia đình; mọi thủ tục nghi lễ được tiến hành trang trọng, các chế độ chính sách đối với phi công hy sinh trong khi thực hiện nhiệm vụ được thực hiện đúng quy định ;đồng thời phân tích, động viên cán bộ, chiến sĩ đơn vị không tin theo những lời lẽ bình luận, xuyên tạc ,bóp méo sự thật của các trang mạng xã hội về việc đơn vị tổ chức đưa tro cốt liệt sĩ; quán triệt và thực hiện nghiêm các qui định về quản lý, sử dụng, cung cấp thông tin, nghiêm cấm sử dụng các phương tiện (điện thoại di động, máy ảnh, máy quay và các phương tiện kỹ thuật khác) để ghi lại các hình ảnh liên quan đến hoạt động của quân đội, tự ý đưa lên facebook và các trang mạng.
- Phối hợp chặt chẽ với các cơ quan chức năng, có các biện pháp tháo gỡ các thông tin trên mạng, không để kẻ xấu lợi dụng, xuyên tạc chống phá;
- Duy trì và quản lý tốt tình hình chính trị nội bộ, giáo dục nâng cao ý thức cảnh giác không để địch lợi dụng , lôi kéo , lừa gạt; thực hiện tốt công tác tuyên truyền, giáo dục; xây dựng đơn vị an toàn gắn với địa bàn an toàn; đẩy mạnh hoạt động thi đua quyết thắng, văn hóa văn nghệ, thể dục thể thao , bảo đảm và nâng cao đời sống văn hóa tinh thần cho bộ đội.
- Tổ chức rút kinh nghiệm trong đội ngũ cán bộ đơn vị về cách thức tổ chức các nghi thức đối với cán bộ, chiến sĩ hy sinh bảo đảm chặt chẽ, trang trọng, chu đáo, đúng nghi thức , không để bị lợi dụng, xuyên tạc…
- Tổng hợp tình hình báo cáo cấp trên theo quy định.

Tình huống 12 : Chính trị viên đại đội nhận được thông tin do một số tiểu đội trưởng và chiến sĩ bảo vệ phản ánh, do căng thẳng trong thực hiện nhiệm vụ huấn luyện – sẵn sàng chiến đấu, mốt số chiến sĩ đang có ý định đào ngũ.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị, nhận định, đánh giá tính chất, tác hại, nguyên nhân ,mức độ ảnh hưởng của sự việc để trao đổi, thống nhất biện pháp giải quyết, phân công cán bộ phụ trách và báo cáo cấp trên xin ý kiến chỉ đạo.
- Tìm hiểu ,nắm chăc những chiến sĩ có ý định đào ngũ, gặp gỡ động viên, nắm tâm tư nguyện vọng, những khó khăn, vướng mắc trong quá trình thực hiện nhiệm vụ; giáo dục ý nghĩa , yêu cầu nhiệm vụ huấn luyện, sẵn sàng chiến đấu, vinh dự, trách nhiệm của quân nhân trong thực hiện nhiệm vụ, những hậu quả, tác hại của việc vi phạm kỷ luật ,nhất là đào ngũ, bỏ ngũ, vắng mặt trái phép đối với quân nhân và gia đình.
- Tổ chức sinh hoạt giáo dục nhiệm vụ chung trong đơn vị, tập trung quán triệt nhiệm vụ huấn luyện, sẵn sàng chiến đấu, nêu cao ý thức chấp hành kỷ luật, chống đào ngũ, bỏ ngũ ,vắng mặt trái phép, trên cơ sở đó xây dựng niềm tự hào và ý thức trách nhiệm trong thực hiện nhiệm vụ.
- Thông qua sinh hoạt, học tập, công tác để giáo dục, quán triệt bộ đội nhận rõ những hình thức kỷ luật đối với những quân nhân đào ngũ, bỏ ngũ, vắng mặt trái phép…
- Thường xuyên làm tốt công tác phân loại đánh giá, dự báo tình hình tư tưởng; tập trung quản lý chặt chẽ tư tưởng, các mối quan hệ và hoàn cảnh gia đình của từng quân nhân ; trọng tâm là những chiến sĩ có biểu hiện thiếu an tâm tư tưởng.
- Trao đổi, thông tin với gia đình các quân nhân có ý định đào ngũ để phối hợp động viên , quản lý tư tưởng.
- Đẩy mạnh thi đua, nâng cao chất lượng huấn luyện, sẵn sàng chiến đấu; kịp thời biểu dương động viên, nhân rộng gương tập thể, cá nhân tiêu biểu trong thực hiện nhiệm vụ.
- Phân công cán bộ đơn vị và chiến sĩ bảo vệ thường xuyên gần gũi, tâm sự nắm chắc tâm tư tình cảm và chia sẻ những khó khăn, vất vả với bộ đội, quản lý chặt chẽ tình hình tư tưởng ,nhất là các đối tượng có ý định đào ngũ, phản ánh, báo cáo với đơn vị để có biện pháp giải quyết kịp thời.
- Duy trì chặt chẽ nền nếp chế độ ngày, tuần; quản lý chặt chẽ quân số, tư tưởng, kỷ luật nhất là giờ nghỉ, ngày nghỉ, những thời điểm nhạy cảm …Thường xuyên tổ chức các trò chơi quân sự trong huấn luyện, các hoạt động cổ động thao trường, quan tâm chăm lo cải thiện đời sống vật chất , văn hóa tinh thần cho bộ đội .

Tình huống 13 : Các ngày lễ tết (Tết Nguyên đán, Tết Chol Chnam Thmay của đồng bào Khmer Nam Bộ, Ngày Quốc Khánh 2-9 …) đơn vị trực sẵn sàng chiến đấu một số chiến sĩ có biểu hiện buồn chán vì không được về thăm gia đình.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị nhận định, đánh giá tình hình tác động đến tư tưởng của bộ đội , thống nhất biện pháp giải quyết; phân công cán bộ, tích cực bám nắm bộ đội, quản lý tư tưởng, kỷ luật kịp thời xử lý các tình huống có thể xảy ra.
- Báo cáo tình hình tư tưởng của bộ đội, xin ý kiến chỉ đạo của cấp trên.
- Tiếp tục tổ chức sinh hoạt, quán triệt chỉ thị mệnh lệnh của người chỉ huy cấp trên, truyền thống quân đội, nhiệm vụ của đơn vị, kế hoạch trực, làm cho cán bộ chiến sĩ hiểu rõ nhiệm vụ trực sẵn sàng chiến đấu, âm mưu, thủ đoạn của các thế lực thù địch; trách nhiệm crua cán bộ , chiến sĩ đối với nhiệm vụ bảo vệ tổ quốc, bảo vệ sự bình yên cho nhân dân đón tết, vui chơi lễ hội; cách tốt nhất là 100% quân số của đơn vị đều có mặt để trực sẵn sàng chiến đấu, tuyệt đối không để xảy ra tình trạng thiếu công bằng, dân chủ trong giải quyết phép, tranh thủ.
- Thường xuyên theo dõi, kiểm tra các hoạt động của đơn vị, nắm chắc tình hình tư tưởng phân loại tư tưởng từng đối tượng, gặp gỡ giáo dục động viên, thuyết phục những chiến sĩ cá biệt phân công cán bộ theo dõi, giúp đỡ.
- Đội ngũ cán bộ, đảng viên thường xuyên bám sát mọi hoạt động của đơn vị; chăm lo tốt đời sống vật chất,tinh thần cho bộ đội; nhất là tổ chức các hoạt động thể dục thể thao; văn hóa văn nghệ và vui chơi giải trí … cho bộ đội.
- Đề nghị chỉ huy cấp trên và phối hợp gia đình địa phương thăm, tặng quà cho những gia đình cán bộ, chiến sĩ gặp khó khăn (nếu có); tổ chức gặp mặt, chúc mừng cán bộ, chiến sĩ trong dịp ngày lễ, tết.
- Viết thư hoặc gọi điện thông báo, biểu dương thành tích, gửi lời chúc mừng năm mới tới gia đình cán bộ, chiến sĩ, tạo điều kiện thuận lợi cho từng chiến sĩ được gọi điện chút tết ông bà, cha mẹ, người thân.
- Sau khi hết trực sẵn sàng chiến đấu, căn cứ vào tình hình nhiệm vụ và tiêu chuẩn phép còn lại đề nghị giải quyết đi phép, đi tranh thủ cho bộ đội.

Tình huống 14 : Khi tiểu đoàn nhận nhiệm vụ khó khăn phức tạp , cán bộ , chiến sĩ có biểu hiện hoang mang lo lắng ,dao động về tư tưởng …và đã xuất hiện tình trạng quân số vắng mặt trái phép ngày càng tăng.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy chỉ huy đơn vị nhận định tình hình xác định chủ trương, biện pháp giải quyết
- Nhanh chóng tổ chức sinh hoạt quán triệt giáo dục nâng cao nhận thức cho cán bộ ,chiến sĩ trong đơn vị hiểu sâu sắc về mục đích, mục đích, ý nghĩa, yêu cầu và tầm quan trọng của nhiệm vụ; kết quả hoàn thành nhiệm vụ của đơn vị trong thời gian qua; thấy rõ niềm vinh dự , tự hào khi được chỉ huy cấp trên tin tưởng giao nhiệm vụ cho đơn vị …; trên cơ sở đó xây dựng niềm tin, động cơ, trách nhiệm và ý chí quyết tâm hoàn thành tốt nhiệm vụ được giao.
- Đánh giá , phân loại tư tưởng cán bộ, chiến sĩ, phân công cán bộ gặp gỡ để nắm chắc tình hình và động viên bộ đội hiểu rõ nhiệm vụ; kịp thời ngăn chặn những biểu hiện tư tưởng ngại khó,ngại khổ ,… chủ động định hướng giải quyết, ổn định tình hình đơn vị.Tổng hợp báo cáo, xin ý kiến chỉ đạo của cấp trên.
- Phân công những cán bộ có trình độ, năng lực,phẩm chất đạo đức, tinh thần trách nhiệm tốt chỉ huy, phụ trách những nhiệm vụ khó khăn, phức tạp để làm gương cho cán bộ, chiến sĩ yên tâm và noi theo.
- Phát huy tốt hoạt động của chiến sĩ dân vận, chiến sĩ bảo vệ duy trì sinh hoạt tổ, tiểu đội, thông qua đó tìm hiểu sâu kỹ về nguyên nhân đào ngũ.
- Tăng cường các biện pháp giáo dục, quản lý bộ đội, chống đào ngũ, vắng mặt trái phép nhanh chóng cho gọi số quân nhân vắng mặt trái phép trở lại đơn vị tiếp tục công tác.
- Khi quân nhân trở lại đơn vị, tổ chức cho viết bản tường trình, kiểm điểm và tổ chức sinh hoạt chặt chẽ từ cấp tiểu đội đến cấp đại đội, quá trình sinh hoạt phải lấy giáo dục thuyết phục là chính, làm rõ tình chất, mức độ vi phạm và xét đề nghị xử lý kỷ luật theo đúng Điều lệnh Quản lý bộ đội.
- Tổ chức phát động đợt thi đua đột kích, tập trung làm rõ ý nghĩa, tầm quan trọng  và yêu cầu của nhiệm vụ; lòng tự hào và trách nhiệm được trên giao; xác định mục tiêu, nội dung, biện pháp sát thực nhằm nâng cao nhận thức, trách nhiệm, xây dựng ý chí quyết tâm, chủ động khắc phục khó khăn ;ý thức chấp hành kỷ luật, quan tâm đảm bảo đời sống cho cán bộ, chiến sĩ; phát huy vai trò tiền phong của cán bộ, đảng viên, số chiến sĩ có thành tích trong thực hiện chức trách nhiệm vụ; tổ chức cho cán bộ, chiến sĩ viết đăng ký quyết tâm thực hiện nhiệm vụ.
- Đẩy mạnh các hoạt động tuyên truyền cổ động trong thực hiện nhiệm vụ; thường xuyên gần gũi bộ đội, nắm chắc tâm tư tình cảm và chia sẻ những khó khăn vất vả, nhưng cũng là vinh dự tự hào khi được thực hiện nhiệm vụ.
- Duy trì chặt chẽ, nghiêm túc nề nếp sinh hoạt đơn vị (rút kinh nghiệm , chấn chỉnh những sai phạm; chủ động làm công tác tư tưởng; quản lý chặt chẽ tình hình mọi mặt của đơn vị, không để dư luận xấu xảy ra trong đơn vị).

Tình huống 15 : Đơn vị đang thực hiện nhiệm vụ hành quân diễn tập, chỉ huy đơn vị phát hiện một số chiến sĩ bị say nắng nóng, có biểu hiện mệt mỏi, choáng váng nhưng vẫn phải cố gắng thực hiện nhiệm vụ vì đang trong tình huống diễn tập
Gợi ý biện pháp xử lý
- Nhanh chóng hội ý chỉ huy đơn vị, báo cáo xin phép cấp trên cho đơn vị tạm dừng hành quân.
- Tổ chức cho lực lượng quân y đơn vị tiến hành các biện pháp (cho nghỉ ngơi nơi thoáng mát, tiến hành các biện pháp hạ thân nhiệt …) .Những trường hợp bị say nắng, nóng, cùng với việc tiến hành các biện pháp sơ cứu ban đầu, phải nhanh chóng đưa đi cấp cứu ở tuyến quân y gần nhất.
- Chỉ huy và đội ngũ cán bộ trong đơn vị căn cứ vào kế hoạch huấn luyện, diễn tập của cấp trên và diễn biến của tình hình thời tiết để báo cáo cấp trên có biện pháp điều chỉnh nội dung, chương trình, thời gian huấn luyện phù hợp, bảo đảm sức khỏe cho bộ đội.
- Tăng cường các biện pháp huấn luyện thể lực, chăm lo bảo đảm đời sống vật chất tinh thần, trang bị cho bộ đội các biện pháp phòng chống say nắng, nóng; giáo dục không để cán bộ, chiến sĩ hoang mang, lo lắng, tin tưởng vào nội dung , chương trình và các khoa mục huấn luyện; đẩy mạnh các hoạt động thi đua, xây dựng quyết tâm phấn đấu hoàn thành tốt nhiệm vụ huấn luyện.
- Phân công đội ngũ cán bộ theo dõi, ổn định tình hình tư tưởng, tâm lý cho bộ đội trong thực hiện nhiệm vụ
- Tổng hợp tình hình báo cáo cấp trên theo quy định.

B.NHÓM TÌNH HUỐNG TƯ TƯỞNG NẢY SINH TRONG CÔNG TÁC VÀ SINH HOẠT TẠI ĐƠN VỊ ( 31 TÌNH HUỐNG )

Tình huống 16 : chỉ huy đại đội nắm được thông tin từ chiến sĩ bảo vệ phản ảnh .Hằng tháng đồng chí Trung đội trưởng Trung đội 1 tổ chức sinh hoạt trung đội để thống nhất thu một phần tiều phụ cấp của chiến sĩ làm quỹ vốn trung đội, có lập danh sách ký nhận là tự nguyện đóng góp; nhiều chiến sĩ bộc lộ tâm lý không thoải mái với cách làm trên nhưng vẫn phải đóng góp vì sợ đồng chí trung đội trưởng có thành kiến với bản thân mình.
Gợi ý biện pháp xử lý
- Trao đổi trong chỉ huy đạo đội, thống nhất biện pháp xử lý, phân công cán bộ phụ trách.
- Gặp gỡ đồng chí trung đội trưởng để nắm tình hình, thông báo ý kiến phản ảnh của các chiến sĩ và yêu cầu làm rõ .Trường hợp đồng chí trung đội trưởng không nhận, cần phải tiếp tục các biện pháp kiểm tra, xác minh khi có đủ cơ sở mới kết luận.Trừng hợp đồng chí trung đội trưởng nhận có thu tiền như trên thì xử lý théo các bước sau :
- Trực tiếp gặp gỡ đối thoại với chiến sĩ của Trung đội 1 để nắm tình hình tư tưởng, tâm tư nguyện vọng của chiến sĩ về việc thu tiền của trung đội.
- Yêu cầu đông chí trung đội trưởng báo cáo giải trình việc thu tiền phụ cấp của chiến sĩ , công khai việc sử dụng, so sánh giữa báo cáo với sổ sách, chứng từ liên quan.
- Căn cứ vào kết quả kiểm tra, các nội dung chỉ tiêu không rõ ràng ,không đúng mục đích sử dụng chỉ huy đại đội cần xem xét, truy thu để trả lại tiền cho chiến sĩ.
- Yêu cầu đồng chí trung đội trưởng viết tường trình, kiểm điểm và tự xác định hình thức kỷ luật theo quy định của Điều lệ Đảng và Điều lệnh Quản lý bộ đội.
- Tổ chức sinh hoạt chi bộ thông báo kết quả kiểm tra, xác minh và tình hình xử lý kỷ luật đối với đồng chí trung đội trưởng; sinh hoạt đơn vị quán triệt các quy điịnh về việc cấm tự ý thu tiền phụ cấp của chiến sĩ khi không được sự nhất trí của cấp có thẩm quyền; giáo dục , động viên cán bộ, chiến sĩ phát huy dân chủ, kịp thời báo cáo, phản ảnh với chỉ huy đại đội các vi phạm trong đơn vị.
- Rút kinh nghiệm chung trong cấp ủy , làm rõ trách nhiệm của đồng chí cán bộ đại đội được phân công phụ trách Trung đội 1; tiếp tục theo dõi ,giúp đỡ đồng chí trung đội trưởng xác định trách nhiệm hoàn thành tốt chức trách nhiệm vụ.
- Báo cáo kết quả xử lý và giải quyết với cấp trên theo quy định.

Tình huống 17 : Một số chiến sĩ cứ đến thứ bảy, chủ nhật thường hay bỏ đơn vị về nhà chơi, nhưng chỉ bị xử phạt lao động một vài lần là xong, đã làm nảy sinh dư luận trong đơn vị cho rằng : chỉ huy đơn vị “nặng nề thành tích”, không dám báo cáo cấp trên.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị, thống nhất biện pháp xử lý, phân công cán bộ phụ trách.
- Gặp gỡ một số cán bộ, chiến sĩ trong đơn vị để làm rõ dư luận nói trên.
- Nếu dư luận là đúng, tổ chức sinh hoạt cấp ủy, đội ngũ cán bộ kiểm điểm trách nhiệm của lãnh đạo, chỉ huy trong việc xây dựng chính quy, rèn luyện kỉ luật ( cần thiết ra nghị quyết chuyên đề để khắc phục) .Xác định rõ trách nhiệm của cấp ủy, chỉ huy, chính trị viên và đội ngũ cán bộ, đảng viên.
- Tổ chức sinh hoạt đơn vị, giáo dục, định hướng nhận thức cho cán bộ, chiến sĩ chống bệnh thành tích trong thực hiện nhiệm vụ, nêu cao ý thức tự giác chấp hành kỷ luật và các quy định trong đơn vị.
- Chỉ đạo chi đoàn tổ chức diễn đàn về các chủ đề liên quan đến việc giáo dục, rèn luyện và ý thức chấp hành kỷ luật của thanh niên trong xây dựng đơn vị.
- Rút kinh nghiệm chung trong đội ngũ cán bộ về phương pháp quản lý bộ đội và duy trì kỷ luật.
- Báo cáo cấp trên về tình hình tư tưởng, kỷ luật và các biện pháp xử lý của đơn vị.

Tình huống 18 : Khi bầu cấp ủy trong Đại đội chi bộ nhiệm kỳ 2015 -2017 , đồng chí chính trị viên phó đại đội( Bí thư chi đoàn) không trúng cấp ủy đã có biểu hiện buồn chán , hiệu quả trong công việc thấp.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị trao đổi thống nhất nội dung, biện pháp xử lý sự việc.
- Báo cáo cấp trên xin ý kiến chỉ đạo.
- Chính trị viên(bí thư chi bộ) gặp gỡ đồng chí chính trị viên phó đại đội, phân tích để nhận thức đúng về kết quả bầu cử và sự tín nhiệm của đảng viên trong chi bộ đối với đồng chí , nói rõ quan điểm của chi bộ là không thành kiến và mặc cảm đối với những đồng chí bầu không trúng cấp ủy do cơ cấu; phân tích, định hướng, động viên đồng chí an tâm tư tưởng, tiếp tục thực hiện tốt chức trách nhiệm vụ chính trị viên phó, đặc biệt vần phải phấn đấu thực hiện tốt chức trách nhiệm vụ được giao.
- Gắn với nội dung sinh hoạt chi bộ để giáo dục cán bộ, đảng viên quán triệt và thực hiện nghiêm nguyên tắc tập trung dân chủ ,phát huy tốt chức trách nhiệm vụ,nêu cao ý thức trách nhiệm trong xây dựng đơn vị, quân tâm tạo điều kiện giúp đỡ đồng chí đồng đội hoàn thành nhiệm vụ.
- Chính trị viên và đại đội trưởng thường xuyên quan tâm tạo điều kiện giúp đỡ đồng chí chính trị viên phó khắc phục những khuyết điểm (nếu có) về cá tính, phương pháp; đặc biệt là những nhiệm vụ mà đồng chí chính trị viên phó phụ trách.
- Báo cáo cấp trên về kết quả nắm, xử lý giải quyết tình hình tư tưởng ở đại đội.

Tình huống 19 : Chỉ huy tiểu đoàn nắm được thông tin đồng chí Nguyễn Văn C, nhân viên bán căng tin của tiểu đoàn thường cho chiến sĩ vay tiền với lãi suất cao, song hợp thức bằng việc cho chiến sĩ ký nợ mua các sản phẩm hàng hóa. Tuy tự nguyện chấp nhận song số chiến sĩ vay lãi bức xúc mà không dám báo cáo với đơn vị.
Gợi ý biện pháp xử lý
- Trao đổi trong chỉ huy đơn vị thống nhất biện pháp giải quyết, phân công cán bộ phụ trách.
- Tiến hành gặp gỡ riêng với một số chiến sĩ thường nợ căng tin để tìm hiểu, nắm tình hình.
- Gặp gỡ trực tiếp đồng chí C. thông báo dư luận của chiến sĩ phản ảnh; yêu cầu đồng chí báo cáo rõ sự việc. Trường hợp đồng chí C. không nhận, cần phải tiếp tục điều tra, xác minh có đủ cơ sở mới kết luận. Trường hợp đồng chí C. nhận là có thật sự việc như trên, xử lý theo quy trình.
- Yêu cầu đồng chí C. báo cáo về việc đồng chí cho vay lãi và các hình thức hợp thức hóa bằng việc bán hàng; số % cho vay lãi, số cán bộ, chiến sĩ đã vay lãi của đồng chí.
- Căn cứ vào báo cáo và kết quả kiểm tra xác minh, chỉ huy tiểu đoàn báo cáo với cấp trên và cơ quan tài chính, xem xét truy thu số tiền cho vay lãi của đồng chí C,để trả lại cho chiến sĩ.
- Triển khai cho đồng chí C. viết tường trình kiểm điểm, chỉ đạo tiến hành xử lý kỷ luật theo quy định. Trường hợp cần thiết phải thuyên chuyển công tác khác.
- Gặp gỡ các đồng chí vay lãi, thông báo kết quả kiểm tra xác minh và xử lý đối với đồng chí nhân viên bán căng tin; kiểm điểm, nhắc nhở, định hướng các đồng chí không tham gia vay lãi, thực hành tiết kiệm trong chi tiêu.
- Chỉ đạo các đơn vị rà soát, báo cáo số chiến sĩ nợ căng tin của các đơn vị, số nợ nhiều nhất, nợ ít nhất, biện pháp phối hợp giải quyết đối với số chiến sĩ nợ nhiều không có khả năng thanh toán…
- Chỉ đạo các đơn vị thuộc quyền, tổ chức sinh hoạt rút kinh nghiệm chung, đồng thời quán triệt các chỉ thị ,quy định của cấp trên.
- Tổng hợp kết quả giải quyết vụ việc báo cáo cấp trên theo quy định.

Tình huống 20 : Một số đồng chí sĩ quan, quân nhân chuyên nghiệp trong tiểu đoàn có thái độ bức xúc và phả ứng trước việc chỉ huy trung đoàn có những quy định về việc cán bộ sử dụng xe máy mà các đồng chí cho là “quá khắt khe”. Các đồng chí trên đã đối phó bằng cách gửi xe máy ở nhà dân để sử dụng.
Gợi ý biện pháp xử lý
- Trao đổi trong chỉ huy đơn vị, thống nhất biện pháp giải quyết , phân công cán bộ phụ trách giải quyết tư tưởng đối với cán bộ .
- Chỉ đạo tổ chức sinh hoạt, quán triệt cho sĩ quan, quân nhân chuyên nghiệp nhận thức đầy đủ sâu sắc các chỉ thị, quy định của cấp trên; mục đích, ý nghĩa và sự cần thiết phải thực hiện những quy định trên, chỉ rõ thực chất việc quản lý chặt chẽ phương tiện chính là biện pháp cần thiết để quản lý con người, bảo đảm an toàn giao thông. Việc quản lý này có lãnh đạo ,chỉ đạo và được vận dụng trong những thời điểm, công việc cần thiết ; dân chủ lấy ý kiến về những nội dung chưa phù hợp trong các quy định của trung đoàn.
- Rà soát , bổ sung quy định cho phù hợp, báo cáo xin ý kiến cấp trên về nội dung quy định.
- Chỉ đạo các đơn vị tăng cường biện pháp quản lý chặt chẽ các mối quan hệ của đội ngũ cán bộ trong đơn vị, nhất là quản lý các phương tiện cán bộ trong đơn vị sử dụng; có biện pháp xử lý nghiêm khắc đối với các đồng chí vi phạm.
- Thông báo cho địa phương biết quy định của đơn vị để phối hợp quản lý.
- Tổng hợp kết quả giải quyết tư tưởng của cán bộ báo cáo cấp trên theo quy định.

Tình huống 21 : Qua nắm bắt từ dư luận trong đơn vị và một số người dân gần đơn vị phản ảnh trong đơn vị có hai chiến sĩ sử dụng ma túy, tuy nhiên vẫn thấy hai chiến sĩ học tập, công tác bình thường.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị nhận định đánh giá tình hình, thống nhất biện pháp giải quyết ; báo cáo cấp trên xin ý kiến chỉ đạo.
- Cử cán bộ gặp gỡ hai chiến sĩ được cho là đã sử dụng ma túy và một số người dân gần đơn vị để kiểm tra, xác minh thông tin ; khéo léo quan sát, tìm hiểu xem hai chiến sĩ có những dấu hiệu nghiện không, động viên chiến sĩ thành khẩn báo cáo đúng sự thật.
- Kiên trì theo dõi mọi hoạt động của chiến sĩ trong thực hiện nhiệm vụ, nhất là giờ nghỉ , ngày nghỉ; thông qua bạn bè, đồng hương và các mối quan hệ của chiến sĩ trong đơn vị để nắm tình hình.
- Liên lạc với gia đình, địa phương, các mối quan hệ xã hội của chiến sĩ trước khi nhập ngũ để nắm tình hình( có thể cử cán bộ về gia đình địa phương để nắm tình hình)
- Trường hợp chiến sĩ thừa nhận, phải báo cáo cấp trên, cho tiến hành các xét nghiệm để có cơ sở xử lý và giải quyết.
- Trường hợp chiến sĩ không khai nhận, cần có các biện pháp theo dõi như:
- Phân công cán bộ đơn vị và sử dụng chiến sĩ bảo vệ bí mật theo dõi quá trình sinh hoạt , công tác của hai chiến sĩ đó.
- Duy trì chặt chẽ thời gian sinh hoạt, học tập, công tác.
- Khi có những dấu hiệu nghi ngờ, báo cáo cấp trên kết hợp với quân y đơn vị để tiến hành các xét nghiệm, xác minh.
- Tổ chức sinh hoạt toàn đơn vị, giáo dục định hướng chung cho cán bộ, chiến sĩ nếu cao ý thức tu dưỡng, rèn luyện, không vi phạm pháp luật, kỷ luật và các tệ nạn xã hội …
- Cần chú ý : Khi kiểm tra, xác minh phải khéo léo, kiên trì, khoa học, tránh áp đặt, quy chụp gây tâm lý bức xúc cho chiến sĩ và ảnh hưởng đến nhiệm vụ của đơn vị.
Tình huống 22 : Trong đơn vị thời gian gần đây có ba quân nhân chuyên nghiệp thường xuyên tham gia chơi lô đề , cá độ dẫn đến nợ tiền không có khả năng chi trả , gây dư luận xấu trong đơn vị và địa bàn đóng quân.
Gợi ý biện pháp xử lý
- Hội ý trao đổi cấp ủy, chỉ huy đơn vị, thống nhất nhận định, đánh giá, đề xuất nội dung biện pháp giải quyết và phân công cán bộ phụ trách .
- Báo cáo cấp trên, đề nghị cơ quan bảo vệ an ninh phối hợp với đơn vị điều tra, xác minh làm rõ sự việc; đối tượng, tính chất, mức độ, nguyên nhân, phối hợp với địa phương để tiếp cận, nắm các đối tượng có liên quan, chú ý cần phải khéo léo, có căn cứ chính xác .
- Trực tiếp gặp gỡ những quân nhân vi phạm để nắm tình hình (chơi lô đề ở đâu, thời gian vay, số tiền, nơi vay, lãi suất, hiện nay còn nợ bao nhiêu, khả năng trả nợ của bản thân và gia đình , nguồn trả nợ lấy ở đâu …); phân tích đúng, sai ,tác hại, ảnh hưởng của hành vi vi phạm đó đối với bản thân và gia đình , ảnh hưởng đến uy tính và thành tích của đơn vị, triển khai viết tường trình kiểm điểm, thông báo và phối hợp cùng gia đình động viên, giúp đỡ quân nhân giải quyết.
- Căn cứ vào tường trình và kết quả sơ bộ đã tìm hiểu , điều tra , tiếp tục làm rõ những vấn đề còn mâu thuẫn. Tổ chức sinh hoạt xét kỷ luật ở các cấp, nội dung sinh hoạt cần đạt được : Chỉ rõ tính chất, mức độ, ảnh hưởng của sự việc (đối với cá nhân và tập thể) ; xác định nguyên nhân khách quan và chủ quân dẫn đến việc vay nặng lãi; xác định rõ trách nhiệm của tổ chức và cá nhân; hình thức xử lý kỷ luật; đề xuất các biện pháp khắc phục…
- Tăng cường công tác quản lý duy trì chặt chễ nề nếp , chế độ quy định. Cử cán bộ ,đảng viên có uy tín kèm cặp, giúp đỡ; phát huy vai trò chiến sĩ bảo vệ, chiến sĩ dân vận trong nắm diễn biến tư tưởng của quân nhân vi phạm, tiếp tục cùng gia đình giáo dục, động viên, quản lý quân nhân vi phạm.
- Về số nợ của quân nhân: Phối hợp với chính quyền địa phương, các cơ quan chức năng và chủ nợ xác định và khoanh nợ với số lãi đúng quy địn h của pháp luật. Yêu cầu quân nhân trả hết nợ, nếu không có khả năng trả nợ thì động viên gia đình, bạn bè, đồng chí, đồng đội trong đơn vị giúp đỡ.
- Sinh hoạt đơn vị thông báo kết quả giải quyết và quán triệt giáo dục chung trong đơn vị. Đưa nội dung này vào sinh hoạt định kỳ của chi bộ để nhắc nhở thường xuyên; tổ chức các hoạt động thể dục thể thao,vui chơi giải trí, văn hóa văn nghệ thu hút cán bộ chiến sĩ tham gia ,đồng thời cán bộ các cấp phải thường xuyên gần gũi, động viên, nắm bắt tư tưởng bộ đội để có biện pháp giải quyết kịp thời, không để bị bất ngờ.

Tình huống 23: Qua thực hiện chế độ kiểm tra quân tư trang cá nhân, đơn vị phát hiện có chiến sĩ tàng trữ tranh, ảnh, băng, đĩa hình có nội dung đồi trụy
Gợi ý biện pháp xử lý
- Lập biên bản và thu hồi ngay tranh, ảnh, băng, đĩa hình đó.
- Trao đổi trong cấp ủy, chỉ huy thống nhất biện pháp giải quyết, phân công cán bộ phụ trách.
- Gặp gỡ quân nhân vi phạm nắm tình hình điều tra rõ nguồn gốc sản phẩm không lành mạnh đó từ đâu ra để có biện pháp ngăn chặn không để xâm nhập vào đơn vị; triển khai viết tường trình kiểm điểm và yêu cầu cam kết, hứa quyết tâm không tái phạm khuyết điểm tương tự.
- Căn cứ vào tính chất mức độ vi phạm và thái độ sau khi được cấp trên gặp gỡ để xem xét xử lý kỷ luật cho phù hợp. Nếu quân nhân nhận ra khuyết điểm, có thái độ thành khẩn phấn đầu sửa chữa tiến bộ có thể chỉ phê bình nhắc nhở làm bài học rút kinh nghiệm chung trong đơn vị.
- Tổ chức tiêu hủy công khai số tang vật bị thu giữ trước toàn đơn vị.
- Tổ chức sinh hoạt đơn vị giáo dục nhiệm vụ, phân tích những tác hại của các loại ấn phẩm đồi trụy, định hướng tư tưởng cho cán bộ, chiến sĩ đơn vị không vi phạm các tệ nạn xã hội.
- Phát huy có hiệu quả các thiết chế văn hóa ở đơn vị, đồng thời tổ chức tốt các hoạt động văn hóa văn nghệ, thể dục thể thao, tạo sân chơi lành mạnh trong các giờ nghỉ, ngày nghỉ thu hút cán bộ, chiến sĩ tham gia; xây dựng môi trường văn hóa tốt đẹp, lành mạnh ở đơn vị.
- Thường xuyên duy trì nghiêm nề nếp chế độ ngày, tuần, nhất là chế độ kiểm tra quân tư trang cá nhân.
- Phát huy vai trò của các tổ chức quần chúng, hội đồng quân nhân, chiến sĩ bảo vệ, tổ tư vấn pháp lý, của đội ngũ cán bộ các cấp; nhất là cán bộ chính trị trong giáo dục, quản lý tình hình tư tưởng, các mối quan hệ của cán bộ, chiến sĩ trong đơn vị; sâu sát nắm chắc đặc điểm từng quân nhân trong đơn vị, nhất là những quân nhân ít tham gia các hoạt động phong trào, kịp thời phát hiện và định hướng cho bộ đội trong việc tìm đọc sách báo, thưởng thức các sản phẩm văn hóa tốt đẹp, lành mạnh trong đơn vị.
- Tổng hợp tình hình đơn vị báo cáo cấp trên theo quy định.

Tình huống 24: Số chiến sĩ chậm tiến trong đơn vị mặc dù đã được giáo dục và phân công cán bộ kèm cặp, giúp đỡ nhưng chưa có sự chuyển biến, tiến bộ gây dư luận không tốt trong đơn vị.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị nhận định, đánh giá nguyên nhân số chiến sĩ chưa chuyển biến tiến bộ; phân công cán bộ phụ trách; báo cáo cấp trên xin ý kiến chỉ đạo.
- Rà soát nắm chắc số lượng, chất lượng chiến sĩ chậm tiến; xác định rõ nguyên nhân chưa chuyển biến, tiến bộ (do phương pháp chỉ huy, quản lý giáo dục của đơn vị chưa tốt, do ý thức chủ quan của các chiến sĩ, do sự tác động của gia đình, bạn bè…) qua đó xác định biện pháp khắc phục.
- Lãnh đạo, chỉ huy đơn vị tiếp tục gặp gỡ, giáo dục riêng, phân tích để số chiến sĩ chậm tiến đó nhận thức rõ đúng, sai; nêu những kết quả mà số chiến sĩ chậm tiến đã đạt được trước đây và thành tích mà tập thể đã ghi nhận cũng như niềm tin của đồng chí, đồng đội trong đơn vị đã dành cho họ.
- Tạo điều kiện cho các đồng chí đó sửa chữa nhũng hạn chế, khuyết điểm trong thực hiện nhiệm vụ, phấn đấu tiến bộ.
- Duy trì chặt chẽ nề nếp chế độ ngày, tuần; mở rộng và phát huy dân chủ trong đơn  vị; phát huy vai trò của các tổ chức quần chúng, hội đồng quân nhân, tổ tư vấn pháp lý tham giao giáo dục, giúp đỡ số chiến sĩ đó tiến bộ.
- Tổ chức diễn đàn thanh niên về các chủ đề; Chấp hành kỷ luật; ý thức trách nhiệm trong xây dựng đơn vị …
- Chỉ đạo đội ngũ cán  bộ các cấp, kiên trì kèm cặp, giúp đỡ số chiến sĩ chậm tiến tiếp tục phấn đấu vươn lên.
-  Tiếp tục giao nhiệm vụ phù hợp với khả năng, sở trường của số chiến sĩ chậm tiến để thử thách và theo dõi việc phấn đấu vươn lên.

Tình huống 25: Trong đơn vị có quân chấp hành nề nếp chế độ không nghiêm, thường xuyên uống rượu, bia say gây mất trật tự trong đơn vị, mặc dù đã xử lý kỷ luật nhiều lần nhưng không tiến bộ, làm ảnh hưởng đến tập thể quân nhân và xây dựng nề nếp chính quy của đơn vị.
Gợi ý biện pháp xử lý
- Hội ý trong cấp ủy, chỉ huy đơn vị, nhận định nguyên nhân, thống nhất biện pháp giải quyết. Tổng hợp báo cáo, xin ý kiến chỉ đạo của cấp trên.
- Tổng hợp các lần vi phạm, kết luận đúng nguyên nhân, nhất là lý do tại sao đơn vị đã xử lý kỷ luật nhiều lần mà đồng chí này vẫn tái phạm (do buồn chán về chuyện gia đình, người yêu; công tác quản lý lỏng lẻo, hình thức kỷ luật không mang tính răn đe; tiến hành quy trình xét kỷ luật chưa đúng, có biểu hiện trù dập dẫn đến quân nhân này có biểu hiện bất mãn, thách thức đối với tổ chức hoặc do nguyên nhân khác?).
- Gặp gỡ quân nhân (ghi lại biên bản) nắm thực chất lý do, nguyên nhân quân nhân hay ra ngoài uống rượu; quân nhân đề xuất nguyện vọng với đơn vị. Phân tích rõ mức độ ảnh hưởng của việc vi phạm đó đến quá trình thực hiện nhiệm vụ của đơn vị và bản thân.
- Trao đổi thông tin với gia đình quân nhân (nếu gần có thể mời lên đơn vị) để có biện pháp phối hợp giáo dục động viên quân nhân tiến bộ.
- Phân công cán bộ thường xuyên theo dõi, kèm cặp, giúp đỡ quân nhân; phát huy vai trò của tổ chức quần chúng, hội đồng quân nhân, tổ tư vấn tâm lý, pháp lý, chiến sĩ bảo vệ, chiến sĩ dân vận, mô hình câu lạc bộ quân nhân…, trong giáo dục, quản lý và động viên quân nhân khác tiến bộ.
- Đề cao vai trò gương mẫu của đội ngũ cán bộ, đảng viên; cán bộ cấp trên quan tâm gần gũi, chân thành góp ý, động viên cấp dưới thực hiện nhiệm vụ.
- Đổi mới nâng cao chất lượng các buổi sinh hoạt đơn vị; tăng cường giáo dục chính trị tư tưởng, pháp luật, kỷ luật; phối hợp chặt chẽ với đoàn thể của địa phương trong tổ chức các hoạt động văn hóa văn nghệ, các buổi tọa đàm, trao đổi trong đơn vị về tác hại của uống rượu, bia.
- Duy trì chặt chẽ nề nếp, chế độ ngày, tuần, tăng cường các biện pháp quản lý hành chính, hạn chế việc đi lại của quân nhân ra ngoài đơn vị.

Tình huống 26: Trong đơn vị có vụ việc cán bộ trung đội tự tử, tự sát, do vậy một số chiến sĩ có biểu hiện hoang mang, dao động trong thực hiện nhiệm vụ.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy thống nhất nhận định và biện pháp giải quyết, phân công đồng chí trong cấp ủy tìm hiểu mức độ của dư luận trên; báo cáo cấp trên xin ý kiến chỉ đạo.
- Phân công cán bộ tìm hiểu, rà soát lại tình hình để thống nhất biện pháp giải quyết trong đơn vị.
- Sinh hoạt đơn vị;
+ Lấy kết quả điều tra của cơ quan có thẩm quyền về vụ việc cán bộ (trung đội, đại đội) tự tử, tự sát để quán triệt cho toàn thể đơn vị; nói rõ cho đơn vị hành động dại dột, không xứng đáng với vị trí của người cán bộ.
+ Giáo dục nâng cao nhận thức, trách nhiệm cho cán bộ, chiến sĩ về nhiệm vụ đơn vị, ổn định tình hình tư tưởng mọi mặt.
+ Xây dựng tinh thần đoàn kết thống nhất trong đơn vị.
- Gặp gỡ số chiến sĩ có biểu hiện hoang mang, dao động kịp thời nhắc nhở, động viên, giao nhiệm vụ, xác định rõ nhiệm vụ giữ vững, phát huy thành tích đã đạt được, hoàn thành tốt nhiệm vụ trong thời gian tới.
- Phối hợp với gia đình, người thân, bạn bè của số chiến sĩ có biểu hiện hoang mang, dao động để giáo dục, động viên, xây dựng quyết tâm trong thực hiện nhiệm vụ.
- Kiên quyết xử lý với những biểu hiện tuyên truyền, xuyên tạc gây hoang mang trong đơn vị.
- Chỉ đạo cho cán bộ các cấp tăng cường công tác kiểm tra nắm chắc tình hình trong đơn vị, nhất là những nơi chiến sĩ có biểu hiện hoang mang, dao động. Phát huy vai trò của các tổ chức hội đồng quân nhân, chi đoàn thanh niên, tổ tư vấn pháp lý, chiến sĩ bảo vệ trong việc phân tích, dự báo, đánh giá diễn biến tình hình tư tưởng để động viên, giải quyết kịp thời.

Tình huống 27: Sau buổi học tập chính trị, trung đội trưởng lên báo cáo với chỉ huy đơn vị phát hiện một lá thư tuyệt mệnh của chiến sĩ (viết bằng mực đỏ), nội dung bức thư nói lên sự thất vọng về bố (bỏ mẹ đi với “bồ”), sự hổ thẹn với bạn bè vì bị người yêu bỏ cùng những “áp lực” trong mùa huấn luyện chiến sĩ mới… và những lời dặn mẹ sau khi con “đi”…
Gợi ý biện pháp xử lý
- Cử cán bộ giám sát mọi hoạt động của chiến sĩ đó (khi xác minh đúng quân nhân viết thư tuyệt mệnh).
- Hội ý cấp ủy, chỉ huy đơn vị thống nhất nhận định, đánh giá tình hình sự việc, phân công cán bộ đơn vị phụ trách. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ quân nhân có viết thư tuyệt mệnh, để nắm thêm về hoàn cảnh gia đình và tâm tư của quân nhân, nội dung:
+ Việc tự tử là hành động dại dột của bản thân gây mất mát cho gia đình và hậu quả xấu cho đơn vị và xã hội.
+ Làm cho đồng chí đó thấy với tư cách là một quân nhân, một người con, đồng chí đó có thể góp ý tác động để xây dựng gia đình hạnh phúc.
+ Nói rõ trách nhiệm của đơn vị, của đồng chí đồng đội để đồng chí đó hiểu và yên tâm công tác từ đó bỏ ý định dại dột nêu trên.
+ Thể hiện sự thương yêu, tin tưởng quân nhân đố sẽ có đủ nghị lực vượt qua.
- Phương pháp tiếp xúc, trao đổi: Phải thực sự chân tình, thể hiện tình cảm như người anh trong gia đình, làm cho chiến sĩ hiểu rõ việc chỉ huy đơn vị muốn biết “việc riêng của gia đình” là thể hiện tình cảm, trách nhiệm của chỉ huy đơn vị đối với quân nhân; tránh dùng những lời nói dễ tác động làm nảy sinh biểu hiện mặc cảm, tự ti, xấu hổ của quân nhân về việc của gia đình mình. Đối với chỉ huy đơn vị, phải là chỗ dựa tin cậy về tinh thần của quân nhân; đồng thời lựa chọn những cán bộ có kinh nghiệm trong cuộc sống gia đình, tranh thủ ý kiến của những người lớn tuổi trong và ngoài đơn vị tham gia tư vấn, chỉ dẫn cho quân nhân có những tác động tích cực đến bố và mọi người có liên quan trong gia đình.
- Gặp gỡ trực tiếp (điều kiện cho phép) hoặc qua điện thoại để trao đổi, thông báo với bố, mẹ của quân nhân về việc quân nhân viết thư tuyệt mệnh và những công việc đơn vị đã làm đối với chiến sĩ; đề nghị gia đình phối hợp với đơn vị động viên quân nhân yên tâm tư tưởng, hoàn thành tốt nhiệm vụ được giao.
- Căn cứ vào tình hình thực tế, phối hợp với địa phương tạo điều kiện giúp đỡ hậu phương gia đình và động viên con em yên tâm thực hiện nghĩa vụ quân sự.
- Phát huy vai trò của tổ chức quần chúng, hội đồng quân nhân, tổ tư vấn pháp lý, chiến sĩ bảo vệ, những người thân, đồng hương trong đơn vị để giáo dục, động viên, quản lý tư tưởng của quân nhân, tránh những suy nghĩ và hành động tiêu cực nảy sinh như tự tử, tự sát và các vi phạm kỷ luật.
- Đưa quân nhân vào các hoạt động chung của đơn vị như: các hoạt động thể dục thể thao; văn hóa văn nghệ; quan tâm đời sống vật chất, tinh thần bộ đội.
- Phân công cán bộ, chiến sĩ (thân thiết, cùng quê) thường xuyên quan tâm gần gũi, động viên, giúp đỡ quân nhân yên tâm tư tưởng, xác định trách nhiệm, hoàn thành tốt nhiệm vụ của đơn vị giao; tạo điều kiện thuận lợi để quân nhân tham gia giải quyết những vấn đề nảy sinh trong gia đình.

Tình huống 28: Qua nắm tình hình, phát hiện có chiến sĩ mắc bệnh trầm cảm, trong công tác, sinh hoạt có những biểu hiện bất thường, ngại tiếp xúc với mọi người, có lúc phát ngôn tiêu cực và bất mãn trong cuộc sống…
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị trao đổi, thốn g nhất cách xử lý; báo cáo xin ý kiến chỉ đạo của chỉ huy cấp trên.
- Phối hợp chặt chẽ với quân y đơn vị nắm theo dõi, đưa chiến sĩ bị mắc bệnh trầm cảm đi khám, điều trị ở các tuyến viện theo quy định.
- Tham khảo để hiểu rõ hơn về nguyên nhân và biểu hiện của những người trầm cảm; dự kiến các biện pháp xử lý phù hợp.
- Phân công cán bộ gặp gỡ quân nhân nắm tâm tư, nguyện vọng và động viên quân nhân tích cực tham gia các hoạt động của đơn vị.
- Cử cán bộ, chiến sĩ theo dõi chặt chẽ mọi lời nói, thái độ, hành động của chiến sĩ đó, đề phòng những hành động tiêu cực xảy ra.
- Trong thực hiện nhiệm vụ thường xuyên phân công đồng đội kèm cặp, giúp đỡ; không nên giao các công việc nặng, nguy hiểm và không được căng thẳng, tạo sức ép cho quân nhân đó.
- Phát huy vai trò các tổ chức như chi đoàn thanh niên, hội đồng quân nhân, chiến sĩ dân vận, chiến sĩ bảo vệ để thường xuyên động viên, chia sẻ, tổ chức các hoạt động thu hút quân nhân tham gia; không xa lánh chiến sĩ trầm cảm.
- Chủ động thông báo, phối hợp với gia đình, để tìm hiểu, có biện pháp giáo dục, động viên và quản lý chiến sĩ.

Tình huống 29: Trong đơn vị có hiện tượng thiếu dân chủ, không công khai sử dụng quỹ vốn dẫn đễn cán bộ, chiến sĩ thiếu niềm tin vào cấp ủy, chỉ huy, xảy ra mất đoàn kết nội bộ, kết quả thực hiện nhiệm vụ của đơn vị thấp.
Gợi ý biện pháp xử lý
- Cấp ủy, chỉ huy đơn vị nghiêm túc nhận khuyết điểm, thống nhất biện pháp giải quyết.
- Chỉ huy đơn vị báo cáo giải trình, kiểm điểm trách nhiệm trước cấp ủy cấp mình.
- Kiểm tra, xác minh làm rõ lý do không thực hiện việc công khai quỹ vốn đơn vị.
- Rà soát, bổ sung sửa đổi quy chế, quy định về công tác tài chính, thực hiện nghiêm túc chế độ công khai minh bạch quỹ vốn của đơn vị hằng tháng theo quy định; tiếp tục quán triệt, phổ biến quy chế và triển khai kiểm tra, giám sát của cán bộ, chiến sĩ đơn vị trong thời gian tới.
- Tổ chức sinh hoạt đơn vị, thông báo kết quả kiểm điểm về việc để thiếu dân chủ trong sử dụng quỹ vốn của đơn vị.
- Đổi mới phương pháp, tác phong của từng cán bộ trong giải quyết các mối quan hệ công tác, nhất là quan hệ với cấp trên, cấp dưỡi. Phát huy tính gương mẫu của đội ngũ cán bộ trong chấp hành các chỉ thị, nghị quyết, quy chế, quy định.
- Thường xuyên nắm tình hình tư tưởng, dư luận của cán bộ, chiến sĩ đơn vị; có các biện pháp quản lý, tạo điều kiện để bộ đội phát huy dân chủ tham gia góp ý cho chỉ huy đơn vị và thực hiện quy chế dân chủ, không để các vấn đề tiêu cực, ảnh hưởng xấu trong đơn vị.

Tình huống 30: Chính trị viên đại đội nắm được tin từ chiến sĩ bảo vệ, Trung đội 1 có hiện tượng một số chiến sĩ do gia đình có điều kiện kinh tế khá giả, có mối quan hệ tốt với trung đội trưởng nên thường được “ưu tiên” hơn  trong thực hiện nhiệm vụ; một số chiến sĩ trong trung đội đã nảy sinh tư tưởng bất bình, tuy nhiên không dám ý kiến với trung đội trưởng.
Gợi ý biện pháp xử lý
- Trao đổi thống nhất trong chỉ huy đơn vị; thống nhất biện pháp xử lý
- Tiến hành các biện pháp kiểm tra xác minh sự việc.
+ Phân công đồng chí cán bộ đại đội phụ trách Trung đội 1 xuống dự sinh hoạt với trung đội, đối thoại nắm tình hình tư tưởng và mối quan hệ của trung đội trưởng với các chiến sĩ trong trung đội.
+ Gặp gỡ một số chiến sĩ trong Trung đội 1, khéo léo gợi mở để chiến sĩ trình bày tâm sự của mình.
+ Yêu cầu đồng chí trung đội trưởng báo cáo tình hình tư tưởng, cung cấp thông tin về tình hình trung đội. Trường hợp đồng chí trung đội trưởng thành khẩn nhận khuyết điểm thì nhắc nhở, định hướng để đồng chí khắc phục. Trường hợp đồng chí không nhận khuyết điểm thì tiếp tục tổ chức kiểm tra xác minh làm rõ sự việc (kể cả kiểm tra đảng viên có dấu hiệu vi phạm), khi có kết quả, căn cứ vào tính chất mức độ, tiến hành kiểm điểm, xử lý về Đảng và chính quyền.
- Tổ chức sinh hoạt đơn vị để giáo dục định hướng chung; nhắc nhở cán bộ, chiến sĩ trong đơn vị về quyền dân chủ và sự bình đẳng trong mọi hoạt động của đơn vị, nhất là trong phân công nhiệm vụ và giải quyết các mối quan hệ cán bộ với chiến sĩ đơn vị; động viên cán bộ, chiến sĩ đơn vị phát huy dân chủ, nêu cao tinh thần đoàn kết giúp đỡ nhau trong thực hiện nhiệm vụ.
- Quản lý nắm chắc tình hình tư tưởng của cán bộ, chiến sĩ, quan tâm chăm lo đời sống vật chất tinh thần, xây dựng môi trường văn hóa tốt, đẹp, lành mạnh trong đơn vị.
- Báo cáo tình hình tư tưởng và kết quả giải quyết tư tưởng của đơn vị lên cấp trên theo quy định.

Tình huống 31: Trong tiểu đoàn xuất hiện dư luận chiến sĩ cho rằng chất lượng bữa ăn giảm sút, không bằng đơn vị bạn; thậm chí có ý kiến cho rằng đã có sự bớt xén tiêu chuẩn.
Gợi ý biện pháp xử lý
- Hội ý chỉ huy đơn vị, trao đổi, đánh giá tình hình, thống nhất biện pháp giải quyết, phân công cán bộ phụ trách thực hiện.
- Chỉ đạo tổ kiểm tra kinh tế của tiểu đoàn tiến hành kiểm tra sổ sách, nghiệp vụ, kiểm tra đối chiếu thực tế việc duy trì xuất nhập tay ba trong ngày của các bộ phận trực ban, quản lý và thủ kho.
- Kiểm tra việc cải tiến, chế biến món ăn, tinh thần trách nhiệm của bộ phận phục vụ, việc chia các khẩu phần, suất ăn trong các bữa ăn…
- Trong tường hợp kiểm tra, xác minh có dấu hiện bớt xén tiêu chuẩn chế độ của bộ đội, phải tiến hành lập biên bản và có kết luận rõ ràng, nếu bớt xén nhiều tiêu chuẩn của bộ đội cần truy thu, có hình thức xử lý kỷ luật phù hợp.
- Trong trường hợp kiểm tra xác minh không có cơ sở để kết luận có sự bớt xén tiêu chuẩn của bộ đội cũng cần phải thông báo cho bộ đội biết, qua đó nhắc nhở đề cao trách nhiệm tốt hơn trong công tác phục vụ.
- Tổ chức sinh hoạt tiểu đoàn thông báo kết quả kiểm tra, xác minh và thông báo rõ biện pháp xử lý, giải quyết của chỉ huy tiểu đoàn; động viên cán bộ, chiến sĩ nêu cao ý thức trách nhiệm trong xây dựng bếp ăn, thực hiện tốt chức trách nhiệm vụ trong trực ban, trực nhật và chế độ kiểm tra xuất nhập tay ba; kịp thời phát hiện và phản ánh với chỉ huy các cấp khi phát hiện các biểu hiện tiêu cực, bớt xén tiêu chuẩn của bộ đội…
- Duy trì nghiêm nề nếp chế độ tài chính công khai theo quy định; chỉ đạo tổ chức cho các đơn vị nấu đối chứng vào các ngày thứ bảy, chủ nhật, tổ chức hội thi nấu ăn để rút kinh nghiệm nâng cao chất lượng bữa ăn của bộ đội.
- Phân công trách nhiệm cán bộ phụ trách, thường xuyên bám nắm, theo dõi, chỉ đạo tổ chức quản lý bếp ăn chặt chẽ, không để xảy ra thất thoát, bớt xén tiêu chuẩn của bộ đội.

Tình huống 32: Chiến sĩ A. thường xuyên có tác phong chậm, đồng chí tiểu đội trưởng đã xử phạt bằng cách: “Bắt vác 1 khẩu súng chạy vòng quanh sân bóng đại đội”, sự việc diễn ra trước sự chứng kiến của các gia đình quân nhân lên thăm con em họ trong ngày nghỉ chủ nhật; nhiều chiến sĩ trong đơn vị và gia đình quân nhân có những phản ứng khác nhau trước việc chiến sĩ A. bị xử phạt
Gợi ý biện pháp xử lý
- Chỉ huy đại đội ra lệnh dừng ngay việc xử phạt chiến sĩ.
- Triệu tập, gặp gỡ đồng chí trung đội trưởng, tiểu đội trưởng (đã ra lệnh xử phạt chiến sĩ A.) và chiến sĩ A.
- Yêu cầu các đồng chí trung đội trưởng và tiểu đội trưởng báo cáo rõ sự việc và nhận thức của đồng chí về việc xử phạt như trên.
- Phân tích làm rõ trách nhiệm của đồng chí trung đội trưởng trong công tác quản lý, chỉ huy trung đội và đồng chí tiểu đội trưởng về phương pháp, cách thức xử phạt để gây phản cảm như trên.
- Phân tích cho chiến sĩ A. nhận rõ nhược điểm của mình, động viên viên chiến sĩ cần cố gắng hơn trong rèn luyện tác phong quân nhân.
- Phân công cán bộ đơn vị gặp gỡ, trao đổi, nắm tình hình dư luận và sự phản ứng của các gia đình quân nhân về sự việc trên, nhận thiếu sót về hành động nói trên của đồng chí tiểu đội trưởng.
- Tổ chức sinh hoạt riêng đối với đội ngũ cán bộ đơn vị, rút kinh nghiệm về phương pháp quản lý giáo dục rèn luyện chiến sĩ thuộc quyền; tránh các biểu hiện áp đặt chủ quan, gia trưởng, gây ức chế cho chiến sĩ…
- Tổ chức sinh hoạt đơn vị, rút kinh nghiệm chung về việc xử phạt của đồng chí tiểu đội trưởng đồng thời động viên cán bộ, chiến sĩ nêu cao ý thức trách nhiệm trong việc rèn luyện tác phong quân nhân và ý thức chấp hành nghiêm pháp luật, kỷ luật quân đội và các quy định của đơn vị.
- Phân công cán bộ đơn vị quản lý nắm chắc tình hình tư tưởng của chiến sĩ A., không để các biểu hiện phát sinh về tư tưởng.

Tình huống 33: Trong buổi sinh hoạt ngày chính trị văn hóa tinh thần hằng tháng ở đơn vị (cấp trên đến dự và chủ trì sinh hoạt), bộ đội không có ý kiến phát biểu.
Gợi ý biện pháp xử lý
- Cán bộ cơ sở hợp thống nhất nhận định các nguyên nhân: ở đơn vị có hiện tượng mất dân chủ; bộ đội không dám ý kiến vì sợ cán bộ trù dập; bộ đội đã có ý kiến nhiều lần nhưng đơn vị không giải quyết hoặc giải quyết không dứt điểm; phương pháp duy trì của người chủ trì chưa tốt do vậy bộ đội không có ý kiến phát biểu… xem do nguyên nhân nào là chính.
- Chỉ đạo đơn vị tổ chức cho bộ đội đóng góp ý kiến thẳng thắn, dân chủ.
- Trước khi xuống dự và chủ trì sinh hoạt, cấp trên rà soát, xem xét các ý kiến trước đó đơn vị đã giải quyết như thế nào, để có biện pháp gợi mở, định hướng phát biểu trong sinh hoạt.
- Quán triệt rõ mục đích yêu cầu, nội dung sinh hoạt dân chủ trên các mặt quân sự, chính trị, kinh tế và đời sống, trong đó tập trung gợi ý vào các nội dung có liên quan trực tiếp đến quyền lợi, tiêu chuẩn, các mối quan hệ của bộ đội như: Công tác bảo đảm cải tiến , chế biến món ăn, vệ sinh nhà ăn, nhà bếp, thái đội của người phục vụ, người được phục vụ; chế độ tiêu chuẩn được đọc báo, nghe tin, thông báo chính trị; tiêu chuẩn đi phép, tranh thủ, quân tư trang cá nhân, tiều lương, phụ cấp; mối quan hệ đoàn kết cán binh trong đơn vị; các vấn đề về phát huy dân chủ quân sự trong huấn luyện, sẵn sàng chiến đấu; biện pháp giáo dục quản lý, xử lý kỷ luật của đơn vị đối với chiến sĩ…
- Làm cho cán bộ, chiến sĩ đơn vị đó thấy đây là quyền lợi và trách nhiệm của anh em; mọi ý kiến đều được giải đáp chính đáng, mọi nhu cầu theo quy định đều được đảm bảo đầy dủ (ví dụ một số đề nghị đã được giải quyết) không ai có quyền trù dập, phân biệt đối xử với người có ý kiến.
- Để giảm bớt căng thẳng trong sinh hoạt, chủ trì sinh hoạt có thể gợi ý, mời bộ đội tham gia 1-2 tiết mục văn nghệ.
- Động viên bộ đội, phát huy dân chủ, lấy tinh thần xung phong phát biểu ở từng bộ phận với chỉ định một số cá nhân phát biểu, các vấn đề bộ đội ý kiến, chủ trì sinh hoạt cần có phần tổng hợp để giải quyết theo phạm vi quyền hạn hoặc báo cáo cấp có thẩm quyền để giải quyết…
- Kết thúc buổi sinh hoạt chỉ huy đơn vị cần trao đổi, rút kinh nghiệm trong tổ chức sinh hoạt và phát huy dân chủ trong đơn vị.
- Thường xuyên quan tâm chăm lo đến đời sống vật chất tinh thần của bộ đội, phát huy vai trò của các tổ chức và hội đồng quân nhân trong xây dựng đơn vị.
- Tổng hợp kết quả sinh hoạt ngày chính trị văn hóa tinh thần báo cáo với cấp trên theo quy định.

Tình huống 34: Qua nguồn tin nắm được ở đơn vị A, khi có cấp trên đến dự ngày chính trị văn hóa tinh thần với chiến sĩ mới, đơn vị có hiện tượng “bồi dưỡng ý kiến” và quán triệt chỉ được nói ưu điểm, còn khuyết điểm để nội bộ tự giải quyết, đáng lư ý các khuyết điểm đó đã được góp ý và không có sự chuyển biến.
Gợi ý biện pháp xử lý (với cương vị là cấp trên)
- Đây là tìn huống phản ánh đơn vị có biểu hiện dân chủ hình thức; cán bộ có biểu hiện “bệnh thành tích”, che giấu khuyết điểm, nếu kéo dài, tình hình đơn vị sẽ mất ổn định, chiến sĩ sẽ không tin cán bộ, ảnh hưởng đến chất lượng hoàn thành nhiệm vụ của đơn vị.
- Xác minh lại nội dung của nguồn tin đó.
- Nếu đúng, trao đổi thống nhất trong lãnh đạo, chỉ huy bàn biện pháp xử lý.
- Tìm hiểu xem nguyên nhân của hiện tượng trên là gì, do cán bộ có nhiều sai phạm hay đơn vị có nhiều khuyết điểm mà chỉ huy muốn giấu cấp trên? Khi tìm hiểu rõ nguyên nhân, nắm chắc tình hình cần thực hiện như sau:
+ Chỉ thị cho chỉ huy đơn vị báo cáo trung thực tình hình của đơn vị.
+Trực tiếp cùng cơ quan nghe chỉ huy đơn vị cấp dưới báo cáo tình hình, chỉ đạo tổ chức đảng, chỉ huy đơn vị sinh hoạt tìm ra biện pháp khắc phục, xác định trách nhiệm của cán bộ các cấp; sai ở đâu, sửa ở đó, cán bộ sai thì kiểm tra nhắc nhở cán bộ; nếu cần có thể chỉ thị kiểm tra đảng viên, tổ chức đảng đột xuất, vi phạm đến mức kỷ luật thì xử lý kỷ luật.
+ Chỉ đạo cho đơn vị sinh hoạt toàn thể đơn vị (có thể giao cơ quan hoặc trực tiếp dự) giải đáp thấu đáo những vướng mắc mà lâu nay tồn tại ở đơn vị, đồng thời giáo dục, quán triệt cho mọi quân nhân trong đơn vị nâng cao tinh thần trách nhiệm trong thực hiện nhiệm vụ, tích cực đóng góp xây dựng đơn vị.
- Duy trì nghiêm nề nếp sinh hoạt đối thoại dân chủ theo quy định, phát huy hiệu quả hòm thư góp ý và các kênh thông tin phản ảnh từ chiến sĩ (hộp thư thoại) có thể công khai số điện thoại của lãnh đạo chỉ huy, cơ quan chính trị để cán bộ chiến sĩ có điều kiện phản ảnh; thường xuyên dự các buổi sinh hoạt chính trị văn hóa tinh thần của các đơn vị thuộc quyền, tăng cường đối thoại trực tiếp với bộ đội. Bảo đảm đầy đủ các chế độ tiêu chuẩn, quyền lợi của bộ đội theo quy định.
- Nắm tư tưởng, giải quyết kịp thời tâm tư nguyện vọng chính đáng của bộ đội. Thuông xuyên theo dõi nắm chắc tình hình đơn vị, chỉ đạo giải quyết kịp thời những vướng mắc, giúp đơn vị trong quá trình thực hiện nhiệm vụ.

Tình huống 35: Trong đơn vị có tin đồn sai sự thật về tình hình an ninh chính trị, trật tự an toàn xã hội trên một số địa bàn trong nước, đã gây hoang mang tư tưởng bộ đội
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị nhận định tình hình, xác định nguồn gốc mức độ ảnh hưởng của tin đồn và biện pháp giải quyết; báo cáo xin ý kiến chỉ đạo của cấp trên.
- Tìm hiểu xác định nguyên nhân của tin đồn sai sự thật (do quân nhân trong đơn vị nhận thức sai hay phần tử xấu bên ngoài bịa đặt) để ngăn chặn và có biện pháp xử lý kịp thời, không để lan rộng, kéo dài.
- Phân loại, nắm chắc và tiến hành tốt công tác tư tưởng đối với những đồng chí có biểu hiện hoang mang, dao động.
- Tổ chức sinh hoạt đơn vị thông báo cho cán bộ, chiến sĩ biết về nguồn tin đồn sai sự thật trên và hiểu rõ đâu là nguồn tin chính thống và nguồn tin không chính thống; giáo dục, quán triệt quan điểm, chủ trương, chính sách của Đảng và Nhà nước ta về mục tiêu, phương hướng nhiệm vụ xây dựng và bảo vệ Tổ quốc; trên cơ sở đó, định hướng tư tưởng, xây dựng niềm tin, thái độ, trách nhiệm của mỗi quân nhân trước những tác động tiêu cực nảy sinh…
- Thường xuyên quán triệt sâu, kỹ về nhiệm vụ của quân đội và đơn vị; âm mưu “diễn biến hòa bình”, “phi chính trị hóa” quân đội của các thế lực thù địch; kiên quyết phản bác những luận điệu sai trái; chủ động phát hiện, nắm chắc tình hình, ngăn chặn tư tưởng lệch lạc, không để những vấn đề tiêu cực, xâm nhập vào đơn vị; giữ vững niềm tin cho mọi cán bộ, chiến sĩ, yên tâm hoàn thành tốt mọi nhiệm vụ được giao.
- Tăng cường tuyên truyền giáo dục các chỉ thị, nghị quyết của Đảng, chính sách và luật pháp của Nhà nước, kỷ luật của đội, chế độ quy định của đơn vị; phát huy hiệu quả hoạt động tuyên truyền thông qua hệ thống thiết chế văn hóa, chế độ đọc báo, thông báo chính trị, nghe đài, xem truyền hình; thường xuyên củng cố niềm tin, ổn định tình hình trong đơn vị.
- Phối hợp chặt chẽ với cấp ủy, chính quyền và các tổ chức đoàn thể địa phương trong công tác tuyên truyền, giáo dục; xây dựng đơn vị an toàn gắn với địa bàn an toàn; đẩy mạnh hoạt động thi đua quyết thắng, văn hóa văn nghệ, thể dục thể thao, bảo đảm và nâng cao đời sống văn hóa tinh thần cho bộ đội.
- Duy trì và quản lý tốt tình hình chính trị nội bộ, giáo dục, nâng cao ý thức cảnh giác không để địch lợi dụng, lôi kéo, lừa gạt.

Tình huống 36: Gần đến thời hạn xuất ngũ, trong đơn vị có nhiều chiến sĩ băn khoăn sau khi xuất ngũ sẽ khó tìm việc làm…
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị thống nhất đánh giá tình hình và biện pháp giải quyết.
- Nắm chắc tình hình tư tưởng của bộ đội, những băn khoăn của số chiến sĩ chuẩn bị xuất ngũ để có biện pháp giáo dục, định hướng kịp thời.
- Tổ chức sinh hoạt đơn vị giới thiệu các chế độ, chính sách ưu đãi học nghề, tìm hiểu các ngành nghề, cơ hội việc làm, nơi làm việc, nắm sở trường, khả năng của từng quân nhân để tham gia phù hợp; phổ biến những nghề nên học mà xã hội đang cần, nêu những gương chiến sĩ đi trước đã chọn nghề hợp với năng khiêu, giờ đang có việc làm và thu nhập ổn định.
- Báo cáo và đề nghị cấp trên mời cán bộ của trường dạy nghề từ đơn vị tư vấn hướng nghiệp, học nghề cho bộ đội.
- Chỉ đạo đoàn thanh niên tổ chức diễn đàn, tạo đàm để đoàn viên, thanh niên tham gia trao đổi, trình bày nguyện vọng, định hướng nghề nghiệp hoặc tổ chức cho chiến sĩ tham quan các cơ sở dạy nghề để họ lựa chọn nghề học cho phù hợp.
- Tổng hợp tình hình báo cáo cấp trên.

Tình huống 37: Sau hội nghị tổng kết phong trào thi đua Quyết thắng, có dư luận cho rằng; việc lựa chọn, bình bầu khen thưởng Chiến sĩ thi đua, Đơn vị quyết thắng không đúng người, đúng thành tích vì trên thực tiế sau hội nghị một số cá nhân và tập thể được khen thưởng không giữ vững và phát huy được thành tích, làm ảnh hưởng đến sự phấn đấu chung của đơn vị.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị thống nhất nhận định về dư luận trong đơn vị, phân công cán bộ xác minh, làm rõ sự việc.
- Tiến hành kiểm tra nắm lại quy trình thủ tục đề nghị khen thưởng của các cấp (đóng góp ý kiến của các tổ chức quần chúng và hội đồng quân nhân, kết quả xét đề nghị khen thưởng ở từng cấp…)
- Tổ chức cho đơn vị, thông báo việc kiểm tra xác minh và quy trình thủ tục tiến hành đề nghị khen thưởng, đưa vấn đề dư luận phản ảnh ra tập thể, động viên cán bộ, chiến sĩ có thắc mắc về khen thưởng phát biểu ý kiến.
- Trường hợp phát hiện những sai sót trong quy trình, thủ tục, tiêu chuẩn đề nghị xem xét khen thưởng; căn cứ vào chức năng nhiệm vụ và thẩm quyền để đề nghị cấp trên xem xét lại thành tích khen thưởng hoặc khen thưởng bổ sung theo quy định, song phải đảm bảo đúng tiêu chuẩn, quy trình và phát huy dân chủ.
- Phát huy vai trò của tổ thi đua, các tổ chức quần chúng, hội đồng quân nhân, phát huy dân chủ trong mọi hoạt động của đơn vị; đẩy mạnh các hoạt động thi đua trong đơn vị, động viên tinh thần hăng hái thi đua trong thực hiện các nhiệm vụ.
- Tổng hợp tình hình đơn vị báo cáo cấp trên theo quy định.

Tình huống 38: Trong đơn vị có đồng chí cán bộ trung đội thời gian gần đây có những phát ngôn tiêu cực, chất lượng thực hiện chức trách, nhiệm vụ thấp đã viết đơn xin xuất ngũ.
Gợi ý biện pháp xử lý
- Trao đổi thống nhất trong cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng của cán bộ, thống nhất biện pháp giải quyết; phân công cấp ủy viên phụ trách; báo cáo cấp trên xin ý kiến chỉ đạo.
- Lãnh đạo, chỉ huy gặp gỡ trực tiếp đối thoại, tìm hiểu nguyên nhân, nắm tư tưởng của cán bộ, xác định rõ nguyên nhân cán bộ có phát ngôn tiêu cực và viết đơn xin xuất ngũ; nhắc nhở đồng chí cán bộ cần nhận thức đúng, không phát ngôn tiêu cực gây dư luận không tốt trong đơn vị, vi phạm kỷ luật phát ngôn; động viên cán bộ cần cân nhắc kỹ việc xin xuất ngũ là một quyết định quan trọng, ảnh hưởng rất lớn đến sự nghiệp của bản thân và gia đình…
- Tạo điều kiện thuận lợi để đồng chí đó khắc phục khó khăn phấn đấu tiến bộ, qua đó động viên cán bộ rút đơn xin xuất ngũ.
- Căn cứ vào tình hình cụ thể, nếu những phát ngôn tiêu cực, gây dư luận xấu, có thể triển khai việc kiểm điểm, xử lý theo quy định của Điều lệnh Quản lý bộ đội.
- Phân công cán bộ liên lạc với gia đình, địa phương (điều kiện cho phép có thể cử cán bộ trực tiếp về gia đình) để nắm tình hình và phối hợp cùng gia đình, địa phương giáo dục, động viên cán bộ.
- Quan tâm giải quyết cho cán bộ đi phép, đi tranh thủ, báo cáo đề nghị trợ cấp khó khăn (nếu có) …; tổ chức tốt việc bồi dưỡng nâng cao phẩm chất đạo đức và năng lực công tác; phân công cấp ủy viên theo dõi, giúp đỡ đồng chí cán bộ trong thực hiện chức trách, nhiệm vụ…
- Tổ chức sinh hoạt đội ngũ cán bộ trong đơn vị và sinh hoạt chi ủy, chi bộ rút kinh nghiệm chung và đóng góp ý kiến cho đồng chí cán bộ trung đội khắc phục khó khăn, giải quyết vướng mắc, phấn đấu tiến bộ.

Tình huống 39: Qua hòm thư góp ý, một số quân nhân phản ảnh về việc đơn vị thu tiền phụ cấp để củng cố, xây dựng cảnh quan môi trường là chưa đúng quy định, đề nghị chỉ huy đơn vị giải thích.
Gợi ý biện pháp xử lý
- Chỉ huy đơn vị sơ bộ nắm lại nguyên nhân trao đổi thống nhất trong lãnh đạo, chỉ huy đơn vị về biện pháp giải quyết.
- Phân công cán bộ tiến hành điều tra, xác minh và kiểm tra lại toàn bộ quy định, quy trình, kế hoạch, chủ trương tiến hành xây dựng cảnh quan môi trường.
- Khi xác định rõ nguyên nhân đúng như dư luận phản ảnh tiến hành xử lý:
+ Hội ý cấp ủy chỉ huy đơn vị, thống nhất nhận định đánh giá, kết luận rõ sự việc, xác định phương hướng giải quyết.
+ Tiến hành gặp chỉ huy đơn vị có cán bộ, bộ phận làm sai quy định, triển khai viết tường trình kiểm điểm.
+ Tổ chức sinh hoạt các tổ chức để kiểm điểm, xem xét xử lý theo đúng quy định của Điều lệ Đảng, Điều lệnh Quản lý bộ đội, truy thu tiền để trả lại bộ đội.
+ Tổ chức sinh hoạt thông báo kết quả việc tiếp thu ý kiến, cách giải quyết của lãnh đạo, chỉ huy và rút kinh nghiệm chung.
+ Tổng hợp tình hình báo cáo cấp trên.
- Nếu dư luận phản ảnh không đúng, tiến hành các bước:
+ Tổ chức sinh hoạt đơn vị thông báo chủ trương của cấp ủy, chỉ huy đơn vị về xây dựng cảnh quan, môi trường; kết quả kiểm tra, kết luận của các tổ chức trong đơn vị về ý kiến phản ảnh không đúng.
+ Phân công cán bộ đơn vị kiểm tra, xác minh cá nhân, nhóm quân nhân phản ảnh sai sự thật, mục đích, động cơ của việc phản ảnh sai sự thật.
+ Nếu xác định rõ các đối tượng, căn cứ vào tính chất, mức độ, chỉ đạo, hướng dẫn cách tổ chức tiến hành kiểm điểm, xử lý kỷ luật theo quyền hạn.
+ Tổ chức sinh hoạt thông báo kết quả việc tiếp thu ý kiến, cách giải quyết của lãnh đạo, chỉ huy, quán triệt chủ trương xây dựng cảnh quan, môi trường đơn vị và rút kinh nghiệm chung.
- Ổn định tư tưởng trong đơn vị, duy trì nghiêm các chế độ sinh hoạt, hoạt động.
- Tổng hợp tình hình báo cáo cấp trên.

Tình huống 40: Sau hội nghị chi đoàn giới thiệu một số đoàn viên ưu tú để chi bộ xem xét đề nghị kết nạp vào Đảng, có dư luận cho rằng; việc lựa chọn, giới thiệu các đồng chí này chưa đảm bảo tiêu chuẩn.
Gợi ý biện pháp xử lý
- Hội ý Ban chấp hành chi đoàn thống nhất nhận định và biện pháp giải quyết, phân công đồng chí trong Ban chấp hành chi đoàn tìm hiểu nguyên nhân của dư luận trên.
- Báo cáo chi ủy, Bí thư chi bộ xin ý kiến chỉ đạo.
- Phân công cán bộ tìm hiểu, rà soát lại văn bản liên quan, kiểm tra lại quy trình làm việc, các khâu, các bước của Ban chấp hành chi đoàn trong tiến hành xem xét tiêu chuẩn giới thiệu kếp nạp Đảng.
+ Xem lại việc thực hiện hướng dẫn của cơ quan chính trị về việc lựa chọn nhân sự đã đúng chưa? Chưa đúng ở khâu nào?
+ Xem xét xem việc lựa chọn có dân chủ không; rà soát trong số đoàn viên ưu tú được chi đoàn giới thiệu có trường hợp nào có sự định hướng, gợi ý của chỉ huy cấp trên không?
+ Gặp gỡ trực tiếp số đoàn viên ưu tú được xem xét đề nghị kết nạp Đảng, trao đổi nắm chắc động cơ phấn đấu, ý thức trách nhiệm, kết quả hoàn thành nhiệm vụ và mối quan hệ với đồng chí; kiểm tra lại kết quả phấn đấu của những đoàn viên này.
+ Yêu cầu chiến sĩ bảo vệ kiểm tra lại xem có đồng chí nào giấu giếm khuyết điểm không?
- Tổ chức sinh hoạt chi đoàn:
+ Quán triệt cho toàn thể chi đoàn về quy trình lựa chọn đoàn viên giới thiệu kết nạp Đảng, tiêu chuẩn trở thành người đảng viên Đảng Cộng sản Việt Nam; khẳng định việc lựa chọn là đúng (hoặc chỉ ra cả những chỗ chưa đúng).
+ Giáo dục động cơ cho đoàn viên phấn đấu, các ý kiến liên quan đến đề nghị giới thiệu kếp nạp Đảng phải đưa ra sinh hoạt chi đoàn.
+ Xây dựng tinh thần đoàn kết thống nhất trong chi đoàn. Động viên toàn thể đoàn viên tiếp tục cố gắng phấn đấu đạt được kết quả tốt hơn trong học tập, công tác.
- Tổ chức rút kinh nghiệm trong Ban chấp hành chi đoàn, làm rõ trách nhiệm sai sót của từng cá nhân (nếu có).
- Gặp gỡ số đoàn viên ưu tú được giới thiệu kết nạp Đảng, nhắc nhở, động viên, giao nhiệm vụ, phát huy thành tích đã đạt được, hoàn thành tốt nhiệm vụ trong thời gian tới.
- Kiên quyết xử lý với những biểu hiện tiêu cực, những ý kiến không đúng nơi, đúng chỗ gây dư luận không tốt trong đơn vị.

Tình huống 41: Trong đơn vị nhiều chiến sĩ có nguyện vọng chuyển quân nhân chuyên nghiệp phục vụ lâu dài trong quân đội nhưng chỉ tiêu và nhu cầu sử dụng của đơn vị có hạn, nên một số đồng chí không được đáp ứng nguyện vọng nảy sinh tư tưởng, buồn chán…
Gợi ý biện pháp xử lý
- Chính trị viên và người chỉ huy nắm chắc tình hình, trao đổi, thống nhất cách xử lý.
- Gặp gỡ phân tích cho chiến sĩ hiểu được tiêu chuẩn, điều kiện trở thành quân nhân chuyên nghiệp, chỉ tiêu trên giao.
- Biểu dương nguyện vọng của chiến sĩ là chính đáng, cầu tiến bộ nhưng do yếu tố khách quan nên không thể thực hiện được, qua đó động viên anh em tích cực phấn đấu hoàn thành nghĩa vụ quân sự, trở thành người công dân tốt cho xã hội, sau này ổn định nghề nghiệp, tham gia xây dựng các tổ chức chính trị, đoàn thể xã hội ở địa phương; tư vấn, định hướng cho chiến sĩ về nghề nghiệp trong tương lai…
- Chỉ đạo hội đồng quân nhân sinh hoạt đối thoại dân chủ để mọi quân nhân trong đơn vị nắm chắc những tiêu chuẩn, điều kiện trở thành quân nhân chuyên nghiệp; chỉ rõ những đồng chí được chuyển quân nhân chuyên nghiệp là những đồng chí có phẩm chất đạo đức tốt, tự nguyện phục vụ lâu dài trong quân đội, có chuyên môn nghiệp vụ phù hợp với chỉ tiêu giao.
- Phân công cán bộ theo dõi, giúp đỡ, tư vấn định hướng nghề nghiệp cho chiến sĩ sau khi hoàn thành nghĩa vụ quân sự.
- Báo cáo cấp trên về nguyện vọng của anh em.

Tình huống 42: Trong chi bộ có trường hợp đảng viên vi phạm kỷ luật từ chối viết bản tự kiểm điểm, có biểu hiện phát ngôn tiêu cực, bất mãn trong đơn vị.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị thống nhất biện pháp giải quyết.
- Bí thư chi bộ gặp gỡ đảng viên vi phạm tìm hiểu tâm tư nguyện vọng, tình cảm cá nhân và gia đình, nguyên nhân dẫn đến những sai phạm. Nếu nguyên nhân từ phía gia đình thì phối hợp cùng với gia đình để giải quyết, đồng thời động viên đảng viên đó chấp hành nghiêm các quy định của đơn vị tránh tái phạm. Nếu nguyên nhân là do nhận thức cá nhân hoặc do mâu thuẫn trong quan hệ công tác và sinh hoạt ở đơn vị dẫn đến có thái độ bất hợp tác thì phải tiến hành giải quyết mâu thuẫn và xem xét xử lý kỷ luật. Thuyết phục đảng viên viết tường trình kiểm điểm (làm cho đảng viên hiểu rõ quy trình, mục đích của việc viết kiểm điểm, xét kỷ luật là nhằm giúp đồng chí đó tiến bộ).
- Chỉ đạo các tổ chức quần chúng, hội đồng quân nhân, tổ đảng tham gia đóng góp ý kiến cho đảng viên vi phạm kỷ luật.
- Tùy theo tính chất mức đội vi phạm để xác định các hình thức xem xét kiểm điểm và xử lý như: Kiểm tra đảng viên có dấu hiệu vi phạm, tổ chức sinh hoạt chi bộ xét kỷ luật…
- Sau khi xem xét, xử lý đảng viên phải gia thời hạn cho đảng viên phấn đấu tiến bộ, phân công cấp ủy theo dõi, kèm cặp, giúp đỡ đảng viên phấn đấu tiến bộ, khắc phục khuyết điểm.
- Trường hợp đảng viên vi phạm khuyết điểm vẫn không viết kiểm điểm, chi bộ vẫn tổ chức xem xét kỷ luật theo quy định của Điều lệ Đảng (trong hồ sơ kỷ luật phải lưu các văn bản xác minh việc đảng viên vi phạm kỷ luật, ghi rõ đảng viên không viết kiểm điểm).
- Tổ chức sinh hoạt đơn vị, giáo dục, định hướng tư tưởng cho cán bộ, chiến sĩ nêu cao ý thức chấp hành kỷ luật, xây dựng mối đoàn kết thống nhất, quyết tâm xây dựng đơn vị vững mạnh toàn diện.
- Báo cáo kết quả kiểm điểm xử lý của chi bộ đối với đảng viên vi phạm lên cấp trên.

Tình huống 43: Chuẩn bị đến đại hội chi bộ nhiệm kỳ, qua dư luận đơn vị phản ảnh có một số đảng viên công tác ở chi bộ lâu năm đã vận động số đảng viên mới ra trường về chi bộ công tác không bầu đồng chí đại đội trưởng vào cấp ủy nhiệm kỳ mới, số đảng viên được vận động tỏ ra băn khoăn, lo lắng.
Gợi ý biện pháp xử lý
- Đây là tình huống mang tính chính trị, phản ánh tính đoàn kết thống nhất trong nội bộ không tốt, đảng viên lợi dụng sự kiện đại hội chi bộ và quyền dân chủ để hạ uy tín cán bộ, nếu không chủ động giải quyết tốt, rất có thể đại hội chi bộ sẽ không thành công, ảnh hưởng đến uy tín của cán bộ và thành tích của đơn vị.
- Bí thư chi bộ trao đổi với đại đội trưởng về tình hình nội bộ đơn vị, trao đổi những vấn đề về phẩm chất, năng lực, phương pháp, tác phong công tác của đồng chí đại đội trưởng.
- Hội ý cấp ủy, thống nhất nhận định, đánh giá tình hình và biện pháp giải quyết.
- Báo cáo xin ý kiến chỉ đạo của cấp trên.
- Căn cứ vào mức độ và tính chất cụ thể để tiến hành kiểm tra, xác minh số đảng viên đứng ra vận động và số đảng viên được vận động không bầu đồng chí đại đội trưởng vào cấp ủy nhiệm kỳ mới.
+ Nếu dư luận đúng thì tiến hành kiểm tra đảng viên có dấu hiệu vi phạm Điều lệ Đảng.
+ Nếu không đúng cũng cần tiến hành các bước lãnh đạo tư tưởng phù hợp. Bí thư chi bộ gặp gỡ số đảng viên này; khi gặp gỡ cần linh hoạt, gặp từng người hoặc bộ phận; trao đổi chân thành, không gây căng thẳng, áp đặt, chủ quan, khéo léo gợi mở để đảng viên bộc lộ quan điểm cá nhân; cần phân tích về quyền, trách nhiệm của đảng viên trong đại hội, nhất là trong bầu cử, động viên họ quán triệt quan điểm xây dựng tập thể, vì tập thể, tự phê bình và phê bình thẳng thắn nhưng phải có tinh thần thương yêu đồng chí; cần đóng góp trực tiếp giúp cán bộ nhận rõ khuyết điểm, kiên quyết khắc phục, phấn đấu hoàn thành tốt chức trách nhiệm vụ, không nên vì động cơ cá nhân mà ảnh hưởng đến uy tín tập thể. Động viên các đồng chí đảng viên mới về bình tĩnh, giữ vững lập trường, thực hiện đúng quyền và nghĩa vụ của đảng viên, tham gia bầu cử người đủ tiêu chuẩn, phù hợp với cơ cấu vào cấp ủy.
- Chỉ đạo sinh hoạt tổ chức quần chúng và hội đồng quân nhân trong đơn vị theo quy trình chuẩn bị đại hội chi bộ.
- Tổ chức sinh hoạt chi bộ tiến hành quy trình giới thiệu nhân sự bầu cấp ủy nhiệm kỳ mới, cần phát huy dân chủ của đảng viên trong giới thiệu nhân sự (có thể chỉ định một số đảng viên lâu năm phát biểu); gợi ý để đồng chí đại đội trưởng phát biểu nêu lên ưu điểm, hạn chế trong phương pháp, tác phong công tác cũng như hứa hẹn sự phấn đấu trong thời gian tới; quán triệt với chi bộ về trách nhiệm của đảng viên trong bầu cử cấp ủy nhiệm kỳ mới.
- Mở rộng và phát huy dân chủ trong đơn vị, thườn g xuyên quan tâm đến đời sống vật chất và tinh thần của cán bộ, chiến sĩ trong đơn vị.
- Phân công cấp ủy, chi bộ thường xuyên gần gũi, nắm tình hình tư tưởng của đội ngũ cán bộ, đảng viên trước khi tổ chức đại hội để có biện pháp định hướng và xử lý kịp thời.
- Lưu ý, khi tình hình tư tưởng của cán bộ, đảng viên chưa ổn định, khả năng tiến hành đại hội không đạt mục đích, yêu cầu thì tổng hợp tình hình, xin ý kiến chỉ đạo của cấp trên, dừng lại chưa tổ chức đại hội, cần thiết có thể phải báo cáo điều chỉnh cán bộ.

Tình huống 44: Đơn vị mất vũ khí quân dụng chưa rõ nguyên nhân, một số cán bộ, chiến sĩ có liên quan (trung đội trưởng, nhân viên quân khí, chiến sĩ đảm nhiệm canh gác buổi tối hôm mất vũ khí) có biểu hiện băn khoăn lo lắng, thiếu yên tâm vì liên đới trách nhiệm.
Gợi ý biện pháp xử lý
*Đây là vụ việc đặc biệt nghiêm trọng liên quan đến công tác tổ chức chỉ huy, quản lý vũ khí, trang bị kỹ thuật, tình hình chính trị nội bộ trong đơn vị; khi điều tra, xử lý cần bám sát sự chỉ đạo của cấp trên và cơ quan chức năng.
- Chỉ huy đơn vị tiến hành triệu tập các thành phần có liên quan (trực chỉ huy, trực ban, trung đội trưởng, nhân viên quân khí, số chiến sĩ làm nhiệm vụ canh gác…) để lập biên bản vụ việc. Tìm hiểu, nắm bắt tình hình, cung cấp các thông tin có liên quan phục vụ cho việc điều tra, xác minh; động viên các đồng chí an tâm tư tưởng, không hoang mang dao động, có thái độ hợp tác với cấp trên và cơ quan chức năng, nghiêm cấm việc đào ngũ, bỏ ngũ, vắng mặt trái phép.
- Báo cáo cấp trên, đề nghị cử cơ quan chức năng xuống cùng đơn vị tiến hành các biện pháp điều tra, xác minh làm rõ vụ việc.
- Trao đổi, thống nhất trong cấp ủy, chỉ huy đơn vị về các biện pháp xử lý, phân công cán bộ thực hiện các nhiệm vụ (phục vụ điều tra, xác minh; làm công tác tư tưởng…).
- Tổ chức sinh hoạt đơn vị, ổn định tình hình mọi mặt, động viên cán bộ, chiến sĩ tích cực hợp tác với cơ quan chức năng trong việc điều tra, xác minh làm rõ vụ việc; tiếp tục quán triệt và thực hiện nghiêm túc các quy định trong quản lý và sử dụng vũ khí quân dụng.
- Chủ động phối hợp với cấp ủy, chính quyền, cơ quan chức năng của địa phương trên địa bàn có liên quan đến vụ việc để giải quyết, xử lý đúng nguyên tắc, quy định của pháp luật.
- Phân công cấp ủy phụ trách công tác bảo vệ chính trị nội bộ, chiến sĩ bảo vệ tiến hành rà soát, nắm lại chất lượng chính trị trong nội bộ đơn vị; quản lý nắm chắc tình hình diễn biến tư tưởng của cán bộ, chiến sĩ, nhất là số cán bộ, chiến sĩ có liên quan trực tiếp đến vụ việc; không để những đột biến về tư tưởng có thể xảy ra trong đơn vị.
- Tổng hợp tình hình báo cáo cấp trên.

Tình huống 45: Đơn vị mất con dấu chưa rõ nguyên nhân, cán bộ hành chính, nhân viên văn thư bảo mật và chiến sĩ công vụ có biểu hiện băn khoăn lo lắng, thiếu yên tâm vì sợ liên đới trách nhiệm.
Gợi ý biện pháp xử lý
*  Đây là vụ việc đặc biệt nghiêm trọng, không giải quyết nhanh, dứt điểm có thể các phần tử xấu lợi dụng làm giả hồ sơ, giấy tờ…, khi điều tra, xử lý cần bám sát sự chỉ đạo của cấp trên và cơ quan chức năng.
- Báo cáo cấp trên, đề nghị cử co quan chức năng xuống cùng đơn vị tiến hành các biện pháp điều tra, xác minh làm rõ vụ việc.
- Chỉ huy đơn vị tiến hành triệu tập các thành phần có liên quan (trực chỉ huy, trực ban, cán bộ hành chính, nhân viên văn thư bảo mật, những người có liên quan để lập biên bản vụ việc. Tìm hiểu, nắm bắt tình hình, cung cấp các thông tin có liên quan phục vụ cho việc điều tra, xác minh; động viên các đồng chí an tâm tư tưởng, không hoang mang, dao động, có thái độ hợp tác với cấp trên và cơ quan chức năng, nghiêm cấm việc đào ngũ, bỏ ngũ, vắng mặt trái phép.
- Trao đổi, thống nhất trong cấp ủy, chỉ huy đơn vị về các biện pháp xử lý, phân công cán bộ thực hiện các nhiệm vụ (phục vụ điều tra, xác minh; làm công tác tư tưởng…)
- Tổ chức sinh hoạt đơn vị, ổn định tình hình mọi mặt; động viên cán bộ, chiến sĩ tích cực hợp tác với các cơ quan chức năng trong việc điều tra, xác minh làm rõ vụ việc; tiếp tục quán triệt và thực hiện nghiêm túc các quy định trong quản lý và sử dụng con dấu, tài liệu.
- Chủ động phối hợp với cấp ủy, chính quyền, cơ quan chức năng của địa phương trên  địa bàn có liên quan đến vụ việc để giải quyết, xử lý đúng nguyên tắc, quy định của pháp luật.
- Phân công cấp ủy phụ trách công tác bảo vệ chính trị nội bộ, chiến sĩ bảo vệ tiến hành rà soát, nắm lại chất lượng chính trị trong nội bộ đơn vị; quản lý nắm chắc tình hình diễn biến tư tưởng của cán bộ, chiến sĩ, nhất là số cán bộ, chiến sĩ có liên quan trực tiếp đến vụ việc; không để những đột biến về tư tưởng có thể xảy ra trong đơn vị.
- Tổng hợp tình hình báo cáo cấp trên.

Tình huống 46: Đơn vị đến giờ ăn cơm, một số chiến sĩ bỏ ăn, lên ban chỉ huy tiểu đoàn báo cáo vì lý do không đảm bảo vệ sinh, chất lượng bữa ăn kém nên kiên quyết không ăn cơm.
Gợi ý biện pháp xử lý
- Phân công cán bộ xuống bếp ăn, kiểm tra, xác minh, nắm cụ thể tình hình chất lượng bữa ăn.
- Nếu đúng chất lượng bữa ăn không bảo đảm:
+ Thay mặt chỉ huy đơn vị nhận lỗi với cán bộ, chiến sĩ về sự việc trên; thông báo biện pháp khắc phục.
+ Khắc phục ngay để bảo đảm thời gian bữa ăn; tránh để ảnh hưởng tới sức khỏe bộ đội.
+ Chỉ đạo tổ chức sinh hoạt làm rõ nguyên nhân dẫn đến chất lượng bữa ăn không bảo đảm; quy rõ trách nhiệm thuộc về chỉ huy, trợ lý hậu cần, quản lý, bộ phận phục vụ và những người có liên quan. Nếu tính chất, mức đội ảnh hưởng lớn thì chỉ đạo các tổ chức xem xét thi hành kỷ luật…
+ Tổ chức sinh hoạt đơn vị hoặc thông qua giao ban hội ý hằng ngày để thông báo cho bộ đội biết rõ lý do, nguyên nhân và cách giải quyết của đơn vị; biểu dương đồng chí đã phát hiện và phản ảnh; động viên bộ đội nêu cao tinh thần trách nhiệm xây dựng bếp nuôi quân giỏi, quản lý tốt.
- Trường hợp kiểm tra thấy vệ sinh thực phẩm bảo đảm, chất lượng bữa ăn tốt, cơ bản không đúng như ý kiến phản ảnh của một số chiến sĩ:
+ Chỉ đạo đại đội (trung đội) có các chiến sĩ phản ảnh không đúng sự thật, làm rõ nguyên nhân, động cơ của phản ứng nói trên, nhắc nhở, chấn chỉnh, cần thiết xem xét kỷ luật theo Điều lệnh Quản lý bộ đội.
+ Tổ chức sinh hoạt rút kinh nghiệm, không để hiện tượng đó tái diễn.
- Chỉ đạo đơn vị phát huy vai trò của các kíp trực chỉ huy, trực ban, trực nhật, tổ kinh tế thường xuyên kiểm tra, thực hiện tốt việc “xuất, nhập tay ba” và kinh tế công khai trong tổ chức quản lý bếp ăn cho bộ đội.
- Tổ chức nấu đối chứng để so sánh chất lượng bữa ăn; bồi dưỡng nghiệp vụ cho nhân viên nấu ăn, chiến sĩ hậu cần, nếu cần thiết phải thay thế người khác.
- Tổng hợp tình hình báo cáo cấp trên.

C.NHÓM TÌNH HUỐNG TƯ TƯỞNG NẢY SINH TRONG GIẢI QUYẾT CÁC MỐI QUAN HỆ QUÂN NHÂN (18 TÌNH HUỐNG)

Tình huống 47: Chỉ huy tiểu đoàn nhận được tin nhắn không rõ địa chỉ (tin nhắn rác) phản ảnh cán bộ trung đội của Đại đội 2 có biểu hiện băn khoăn, lo lắng vì mỗi khi trong trung đội có chiến sĩ vắng mặt trái phép chỉ huy đại đội thường cử trung đội trưởng đi gọi quân nhân vắng mặt trái phép trở lại đơn vị nhưng không báo cáo cấp trên, do vậy không có giấy tờ và tiền công tác, khi về địa phương và gia đình làm việc gặp nhiều khó khăn.
Gợi ý biện pháp xử lý
- Hội ý trong chỉ huy tiểu đoàn, thống nhất biện pháp xử lý, phân công cán bộ xác minh giải quyết sự việc.
- Cán bộ tiểu đoàn xuống làm việc với ban chỉ huy đại đội và các đồng chí trung đội trưởng, thông báo nội dung thông tin phản ảnh về tình hình đơn vị; yêu cầu chỉ huy đại đội cử trung đội trưởng đi gọi quân nhân vắng mặt trái phép trở lại đơn vị nhưng khong báo cáo cấp trên. Trường hợp đại đội và đội ngũ cán bộ trung đội không nhận có hiện tượng tren, cần phải tiếp tục các biện pháp kiểm tra, xác minh khi có đủ cơ sở mới kết luận. Trường hợp chỉ huy đại đội xác nhận có hiện tượng trên thì xử lý theo các bước sau :
+ Yêu cầu chỉ huy đại đội và số cán bộ trung đội được cử đi gọi quân nhân vắng mặt trái phép báo cáo rõ tình hình đơn vị trong thời gian gần đây, số chiến sĩ vắng mặt trái phép, số lần cán bộ trung đội trưởng đi công tác, số tiền trung đội trưởng phải bỏ ra cho nhiệm vụ này.
+ Căn cứ vào báo cáo giải trình của đại đội, chỉ huy tiểu đoàn kết luận, định hướng cho đội ngũ cán bộ nhận thức đúng về công tác quản lý cán bộ; việc giao nhiệm vụ cho cán bộ ra ngoài doanh trại phải được cấp có thẩm quyền cho phép, đặc biệt việc về địa phương gọi quân nhân vắng mặt trái phép phải có đầy đủ giấy tờ để làm việc với địa phương và gia đình.
- Tổ chức sinh hoạt đội ngũ cán bộ trong tiểu đoàn, rút kinh nghiệm chung về công tác quản lý bộ đội, phế phán bệnh thành tích, che giấu khyết điểm, báo cáo không trung thực tình hình đơn vị, đồng thời tiếp tục quán triệt các chỉ thị, quy định của trên và bồi dưỡng nâng cao trách nhiệm và phương pháp quản lý giáo dục bộ đội.

Tình huống 48: Chỉ huy đại đội nắm được thông tin đồng chí trung đội trưởng khi đi kiểm tra phát hiện chiến sĩ Nguyễn Văn A. làm nhiệm vụ canh gác của trung đội đang tụ tập uống rượu với một số chiến sĩ ở đơn vị khác, đồng chí trung đội trưởng đã có những lời nói cứng nhắc, số chiến sĩ uống rượu có thái độ phản ứng và có hành vi hành hung đồng chí trung đội trưởng.
Gợi ý biện pháp xử lý
- Chỉ huy đại đội nhanh chóng có mặt tại khu vực xảy ra xô xát, ngăn chặn vụ việc, tách riêng số chiến sĩ uống rượu với trung đội trưởng; thuyết phục số chiến sĩ uống rượu bình tĩnh, không manh động, không được hành hung cán bộ, cần thiết có biện pháp cưỡng chế nhằm ngăn chặn các hành vi gây nguy hiểm.
- Tổ chức lực lượng canh gác thay thế; phân công cán bộ theo dõi, nắm tình hình, không để những bộc phát nảy sinh từ số chiến sĩ đã uống rượu.
- Khi số chiến sĩ uống rượu hành hung cán bộ đã tỉnh táo, tiến hành xử lý theo quy trình.
+ Chỉ đạo trung đội trưởng triển khai cho chiến sĩ A. viết tường trình, tổ chức kiểm điểm và xử lý kỷ luật theo quy định của Điều lệnh Quản lý bộ đội.
+ Sinh hoạt đội ngũ cán bộ để rút kinh nghiệm chung về phương pháp quản lý bộ đội và cách thức xử lý trong trường hợp quân nhân bị kích động bơi rượu, bia.
- Tổ chức sinh hoạt toàn đại đội để giáo dục, rút kinh nghiệm chung, tăng cường các biện pháp quản lý bộ đội nhất là trong giờ nghỉ, ngày nghỉ, quản lý các hoạt động của căng tin đơn vị, cấm bán rượu, bia, thuốc lá…
- Báo cáo kết quả xử lý với cấp trên theo quy định.

Tình huống 49: Chiến sĩ A. làm nhiệm vụ canh gác băn khoăn, lo lắng lên báo cáo với chính trị viên đại đội nội dung: Trong phiên gác tối hôm trước, vô tình đồng chí phát hiện một số chiến sĩ sắp hoàn thành nghĩa vụ quân sự tham gia đánh bạc và dọa đồng chí nếu báo cáo đại đội thì sẽ bị đánh.
Gợi ý biện pháp xử lý
- Trao đổi thống nhất trong chỉ huy đơn vị; phân công cán bộ phụ trách giải quyết.
- Gặp gỡ chiến sĩ A. động viên đồng chí báo cáo rõ sự thật, có biện pháp bảo vệ đối với chiến sĩ A.
- Tiến hành các biện pháp theo dõi, tổ chức lực lượng để bắt quả tang số chiến sĩ hay đánh bài ăn tiền; khi bắt quả tang số chiến sĩ đánh bài, tiến hành các biện pháp:
+ Lập biên bản vụ việc, biên bản thu hồi tiền (vật chất) thu được từ việc đánh bài.
+ Chỉ đạo cho trung đội trưởng triển khai các đồng chí tham gia đánh bài ăn tiền viết kiểm điểm, tường trình để xem xét, kiểm điểm xử lý (chú ý lấy kiểm điểm, rút kinh nghiệm là chủ yếu, nếu tái phạm thì xử lý kỷ luật theo quy định của Điều lệnh Quản lý bộ đội).
	- Tổ chức sinh hoạt đơn vị để giáo dục cán bộ, chiến sĩ nhận thức đúng về những ảnh hưởng và tác hại của việc đánh bài ăn tiền và các tệ nạn xã hội; động viên cán bộ, chiến sĩ nêu cao ý thức chấp hành nghiêm pháp luật của Nhà nước, kỷ luật của Quân đội, kiên quyết đấu tranh với những hiện tượng đánh bài ăn tiền, xây dựng mối đoàn kết thống nhất trong đơn vị.
	- Phân công cán bộ theo dõi, quản lý nắm bắt tình hình tư tưởng bộ đội, việc chấp hành kỷ luật và các quy định của đơn vị.

Tình huống 50: Đồng chí Nguyễn Văn A. – Trung đội trưởng thường có thái đội thẳng thắng đấu tranh với các biểu hiện sai trái trong đơn vị, tuy nhiên đồng chí A. đã bị một số đồng chí sĩ quan, quân nhân chuyên nghiệp trong tiểu đoàn không ủng hộ, ngược lại còn cho rằng đồng chí A. có tư tưởng “nịnh bợ” để lấy lòng cấp trên. Đồng chí A. bức xúc trước sự việc trên và lên báo cáo với chỉ huy đại đội.
Gợi ý biện pháp xử lý
- Trao đổi trong chỉ huy đại dội, thống nhất biện pháp giải quyết.
- Gặp gỡ Trung đội trưởng A. nắm lại tình hình, động viên đồng chí giữ vững lập trường, quan điểm của mình, không bức xúc, không bị kích động, những việc làm tốt và thái độ thẳng thắn của đồng chí sớm muộn sẽ được tập thể đơn vị ghi nhận, chỉ huy đại đội sẽ phản ảnh báo cáo về hiện tượng này với cấp trên và sinh hoạt quán triệt đơn vị nhận thức đúng việc này.
- Báo cáo và đề nghị chỉ huy tiểu đoàn tổ chức rút kinh nghiệm chung đối với mọi sĩ quan, quân nhân chuyên nghiệp của đơn vị.
- Giáo dục, định hướng cho đội ngũ cán bộ trong đơn vị nâng cao nhận thức trách nhiệm và kiên quyết đấu tranh phê bình những biểu hiện sai trái góp phần xây dựng đơn vị vững mạnh toàn diện.

Tình huống 51: Qua dư luận trong đơn vị phản ảnh, có đồng chí cán bộ đại đội “bật đèn xanh” cho cán bộ tiểu đội quân phiệt với chiến sĩ mới, nếu chấp hành nề nếp chế độ không nghiêm.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị thống nhất biện pháp giải quyết; phân công cấp ủy phụ trách.
- Xác minh làm rõ việc dư luận phản ảnh, động viên cán bộ báo cáo trung thực về việc làm của mình, nếu đúng như vậy thì: Cấp ủy, chỉ huy đơn vị gặp gỡ trực tiếp đồng chí tiểu đội trưởng quân phiệt với chiến sĩ mới, phân tích làm rõ tính chất sai phạm của hai đồng chí, tác hại và hậu quả của việc làm trên đối với công tác quản lý, giáo dục bộ đội… Nếu cán bộ thành khẩn nhận khuyết điểm thì căn cứ vào tính chất, mức độ vi phạm để chỉ đạo việc rút kinh nghiệm chung trong đội ngũ cán bộ đơn vị về phương pháp giáo dục, quản lý bộ đội; nhắc nhở đối với chiến sĩ mới, việc làm như vậy là vi phậm kỷ luật quân đội, bản chất, truyền thống Quân đội nhân dân Việt Nam; yêu cầu đội ngũ cán bộ quán triệt và thực hiện nghiêm quy định về cấm quân phiệt với bộ đội.
- Tổ chứ cho cán bộ trung đội, tiểu đội gặp gỡ xin lỗi số chiến sĩ bị quân phiệt; động viên chiến sĩ an tâm thực hiện nhiệm vụ.
- Tổ chức sinh hoạt đơn vị ổn định tình hình tư tưởng của cán bộ, chiến sĩ, quán triệt các quy định về cấm quân phiệt với bộ đội, động viên cán bộ, chiến sĩ phát huy dân chủ, thương yêu, giúp đỡ lẫn nhau, chấp hành nghiêm nề nếp, chế độ quy định và kỷ luật quân đội; đơn vị sẽ có biện pháp xử lý nghiêm những cán bộ vi phạm kỷ luật.
- Cấp ủy, chỉ huy đơn vị phân công cán bộ, đảng viên dìu dắt quần chúng tiến bộ theo hướng mỗi cán bộ, đảng viên giúp đỡ hai đến ba chiến sĩ, nếu chiến  sĩ còn vi phạm kỷ luật, cán bộ, đảng viên đó chưa hoàn thành nhiệm vụ.
- Tổ chức học tập giáo dục truyền thống của dân tộc, quân đội, đơn vị về tinh thần đoàn kết để mọi quân nhân trong đơn vị gắn bó, thương yêu giúp đỡ nhau.
- Trường hợp kết quả xác minh là dư luận phản ảnh không đúng cần tổ chức sinh hoạt đơn vị rút kinh nghiệm chung, thông qua sinh hoạt nhắc nhở đơn vị phát huy dân chủ, phản ảnh chính xác, tránh làm ảnh hưởng đến uy tín của cán bộ và gây dư luận không tốt trong đơn vị.
- Tổng hợp tình hình báo cáo cấp trên.

Tình huống 52: Đại đội nắm được qua dư luận về đồng chí trung đội trưởng mới ra trường, trong một lần chị gái chiến sĩ lên thăm đơn vị đã nảy sinh tình cảm và có ý định “tán tỉnh”; kể từ đó đồng chí trung đội trưởng thường xuyên tự ý giải quyết cho chiến sĩ đó đi tranh thủ hoặc bố trí công việc nhẹ nhàng nhằm “lấy lòng” bạn gái … đã gây dư luận không tốt trong đơn vị.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị thống nhất biện pháp giải quyết, tiến hành xác minh làm rõ sự việc.
- Nếu đúng như dư luận đã nêu, chỉ đạo đồng chí trung đội trưởng viết bản kiểm điểm, tường trình, chấm dứt ngay những việc làm tương tự. Phân tích cho đồng chí thấy rõ lỗi vi phạm của bản thân là lạm quyền, đối xử thiếu công bằng với chiến sĩ, gây ảnh hưởng xấu đến tư tưởng, tâm lý của đơn vị.
- Gặp gỡ chiến sĩ để làm rõ, xác minh chính xác sự việc. Giáo dục chiến sĩ nhận thức đúng vấn đề. Khi xảy ra sự việc trên phải báo cáo ngay với chỉ huy đại đội, không để sự việc xảy ra ảnh hưởng đến kết quả thực hiện nhiệm vụ và gây ra dư luận không tốt trong đơn vị.
- Tiến hành tổ chức sinh hoạt chi bộ kiểm điểm và tùy theo mức độ có thể xử lý kỷ luật và công khai kết quả xử lý, để rút kinh nghiệm chung, động viên cán bộ vi phạm tích cực tu dưỡng, rèn luyện, sữa chữa khuyết điểm, phấn đấu vươn lên.
- Chỉ huy đại đội tăng cường công tác kiểm tra, quản lý cán bộ, chiến sĩ ở đơn vị thường xuyên và đột xuất; đồng thời thực hiện nghiêm túc chế độ điểm danh, điểm quân số ở đơn vị.
- Thường xuyên tổ chức tốt hoạt động ngày chính trị văn hóa tinh thần; đối thoại dân chủ với chiến sĩ, mở hộp thư thoại để tiếp thu đầy đủ tâm tư, nguyện vọng của chiến sĩ, kịp thời giải quyết thỏa đáng các vấn đề tư tưởng xảy ra.

Tình huống 53: Đơn vị xuất hiện một số cấn bộ không tích cực trong công tác và trong rèn luyện kỷ luật… Cho rằng có cố gắng mấy cũng không được “cất nhắc”, “bổ nhiệm” vì trong đơn vị có hiện tượng cán bộ “chạy chức” hoặc do thân quen nên thường được “cất nhắc”, “bổ nhiệm”.
Gợi ý biện pháp xử lý
- Trao đổi trong lãnh đạo, chỉ huy đơn vị để thống nhất nhận định đánh giá thực trạng tình hình và biện pháp xử lý.
- Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ số cán bộ có tư tưởng nêu trên để tìm hiểu nguyên nhân thiếu tích cực trong công tác rèn luyện, những ý kiến đề đạt của các đồng chí đó đối với cấp ủy, chỉ huy đơn vị về công tác cán bộ, nhất là những trường hợp phẩm chất đạo đức, năng lực hạn chế mà vẫn được đề bạt, bổ nhiệm.
- Nếu những ý kiến đề đạt đó có cơ sở thì cần rà soát lại quy trình tổ chức kiểm điểm trong cấp ủy, cán bộ chủ trì (trường hợp cụ thể cần thiết có thể kiểm tra đảng viên, tổ chức đảng có dấu hiệu vi phạm kỷ luật), bàn biện pháp khắc phục triệt để sai phạm trên.
- Nếu không có căn cứ hoặt chỉ vin vào đó để làm việc cầm chừng thì tổ chức sinh hoạt cấp ủy, chi bộ (đảng bộ) quán triệt tình hình nhiệm vụ, nhu cầu tổ chức biên chế, tiêu chuẩn, nguyên tắc, quy chế, quy trình công tác cán bọ; động viên cán bộ tích cực tu dưỡng phẩm chất đạo đức, lối sống, nâng cao trách nhiệm và năng lực thực tiễn hoàn thành xuất sắc nhiệm vụ được giao; khẳng định lãnh đạo chỉ huy đơn vị luôn tạo điều kiện để cán bộ phấn đấu tiến bộ, thực hiện đúng quy trình, bảo đảm dân chủ, công khai, công bằng trong công tác cán bộ, không dung túng cho những sai phạm và bệnh “chạy chức”, “chạy quyền” trong đơn vị.
- Kịp thời phát hiện, nhắc nhở, chấn chỉnh và có biện pháp xử lý với những trường hợp phấn đấu cầm chừng, thiếu tích cực, hiệu quả công tác thấp. Đồng thời biểu dương, nhân rộng và phát huy vai trò của những tập thể, cá nhân công tác, rèn luyện tốt. Đẩy mạnh các hoạt động xây dựng môi trường văn hóa lành mạnh, tạo dư luận tập thể tích cực trong đơn vị.
- Khéo léo lựa chọng chủ đề tổ chức diễn đàn sĩ quan trẻ phù hợp, nhằm giáo dục nâng cao ý thức trách nhiệm, định hướng động cơ học tập, rèn luyện, công tác đúng đắn. Đồng thời đấu tranh, phê phán những nhận thức, hành động lệch lạc, sai trái.

Tình huống 54: Trong đơn vị có một số chiến sĩ giữa hai địa phương mất đoàn kết, có biểu hiện gây gỗ đánh nhau, tạo sự chia rẻ trong đơn vị.
Gợi ý biện pháp xử lý
- Trao đổi thống nhất trong cấp ủy, chỉ huy đơn vị xác định biện pháp khắc phục; phân công cán bộ phụ trách, báo cáo cấp trên xin ý kiến chỉ đạo.
- Triển khai cho cán bộ tiểu đội, trung đội trực tiếp quản lý số chiến sĩ mất đoàn kết báo cáo tình hình sự việc và hướng giải quyết.
- Tìm hiểu xác minh nguyên nhân gây mất đoàn kết, xác định đối tượng cầm đầu, đối tượng quá khích…, triển khai cho những quân nhân gây gổ mất đoàn kết tường trình toàn bộ sự việc, làm cơ sở cho xác minh và xử lý kỷ luật.
- Gặp gỡ, giáo dục riêng đối với số chiến sĩ của từng địa phương, vừa kiểm tra xác minh nguyên nhân, vừa giáo dục tinh thần đoàn kết, đồng chí, đồng đội, tôn trọng phong tục tập quán, văn hóa của từng địa phương trong đơn vị.
- Căn cứ vào tính chất mức độ, hậu quả của việc mất đoàn kết trong đơn vị và kết quả kiểm tra, xác minh để tiến hành xử lý kỷ luật theo quy định. Những đối tượng cầm đầu, quá khích nếu cần thiết có thể điều động, thuyên chuyển đi đơn vị khác.
- Chỉ đạo sinh hoạt tiểu đội, trung đội và sinh hoạt toàn đơn vị, tạo điều kiện để chiến sĩ hai địa phương có mâu thuẫn phát biểu ý kiến, qua đó giáo dục, định hướng tư tưởng xây dựng mối đoàn kết thống nhất trong đơn vị, cán bộ, chiến sĩ đoàn kết, thống nhất, coi nhau như anh em một nhà, thương yêu, đùm bọc, giúp đỡ lẫn nhau cùng tiến bộ.
- Phân công cán bộ theo dõi giúp đỡ đơn vị, không để chiến sĩ giữa hai địa phương trong đơn vị tái phạm.
- Chỉ đạo tổ chức các hoạt động giao lưu văn hóa văn nghệ, thể dục thể thao, diễn đàn thanh niên… để tăng cường mối đoàn kết thống nhất trong đơn vị.

Tình huống 55: Qua dư luận đơn vị phản ảnh, đồng chí trung đội trưởng thường cho chiến sĩ gọi điện thoại di động rồi thu tiền cước cao hơn nhiều lần so với giá cước thực tế; số chiến sĩ gọi điện không ý kiến nhưng tỏ thái độ thiếu tôn trọng trung đội trưởng.
Gợi ý biện pháp xử lý
- Trao đổi thống nhất trong cấp ủy, chỉ huy đơn vị về biện pháp xử lý, phân công cán bộ phụ trách kiểm tra xác minh sự việc.
- Tiến hành gặp gỡ đồng chí trung đội trưởng và số chiến sĩ đã gọi điện để kiểm tra, nắm tình hình động viên họ thành khẩn nhận rõ việc làm của mình. Nếu kết quả xác mih là đúng thì tiến hành các bước xử lý:
+ Tổng hợp số chiến sĩ đã dùng điện thoại của đồng chí trung đội trưởng (số lần gọi, số tiền cước phí chênh lệch so với giá bưu điện).
+ Triển khai cho đồng chí trung đội trưởng viết tường trình, kiểm điểm, chỉ đạo cán bộ trả lại tiền chênh lệch giá cước đã thu của chiến sĩ. Căn cứ vào tính chất mức độ của việc vi phạm và thái độ sau khi vi phạm của cán bộ để xem xét việc xử lý kỷ luật cán bộ.
+ Tổ chức sinh hoạt đơn vị thông báo kết quả kiểm điểm và công khai việc trả lại tiền chênh lệch thu cước phí điện thoại các chiến sĩ; nhắc nhở các chiến sĩ cần chú ý về cách ứng xử, thái độ tôn trọng cấp trên; quán triệt cho toàn đơn vị phát huy dân chủ, thẳng thắn đấu tranh với các biểu hiện sai trái trong đơn vị.
+ Đề nghị với cấp trên liên hệ với bưu điện lắp đặt điện thoại cố định để phục vụ nhu cầu chính đáng của chiến sĩ, có quy chế quản lý chặt chẽ, bảo đảm bí mật quân sự, tổ chức thu tiền đúng theo giá cước hiện hành.
- Nếu qua tìm hiểu, xác minh mà dư luận không đúng sự thật thì chỉ huy đơn vị phải chỉ đạo cho cán bộ tìm hiểu xác minh mục đích, động cơ sự việc đó. Từ đó tổ chức sinh hoạt xem xét, xử lý kỷ luật nghiêm túc đối với những người vi phạm và quán triệt chung trong toàn đơn vị để rút kinh nghiệm, ổn định tình hình đơn vị.
- Tổng hợp tình hình báo cáo cấp trên.

Tình huống 56: Đơn vị xảy ra hiện tượng chiến sĩ bị mất đồ dùng cá nhân. Chiến sĩ A. đã tỏ ý nghi ngờ chiến sĩ B. và có những lời “bóng gió” … làm chiến sĩ B. rất bức xúc và phát ngôn tiêu cực “sẵn sàng chết để chứng minh sự trong sạch…” Tiểu đội trưởng đã lên báo cáo với chỉ huy đại đội về sự việc trên.
Gợi ý biện pháp xử lý
- Đây là vấn đề nhạy cảm, dễ phát sinh hành động tiêu cực, nên khi phát hiện có sự việc, cần nhanh chóng hội ý cấp ủy, chỉ huy thống nhất biện pháp xử lý. Trong tình huống này, có thể chỉ huy đơn vị đã nắm được tình hình trong thời gian gần đây có xảy ra một vài trường hợp quân nhân của đơn vị báo cáo bị mất tiền nhưng đang theo dõi mà chưa xử lý vự việc, hoặc có thể chỉ huy đơn vị chưa nắm được tình hình trên.
- Gặp riêng chiến sĩ B. để động viên yên tâm tin tưởng vào cách giải quyết của đơn vị.
- Gặp gỡ, yêu cầu chiến sĩ A. báo cáo cụ thể về sự việc và ý kiến đề xuất đơn vị giúp đỡ, chấn chỉnh đồng chí A. không được có lời nói, việc làm nghi ngờ đồng đội của mình…
- Tập trung đơn vị động viên đồng chí nào trót lỡ lấy của đồng chí đồng đội thì tự giác trả lại, nếu không thì tiến hành kiểm tra quân tư tranh. Nếu cán bộ phát hiện và tìm ra được số tài sản của các chiến sĩ đã bị mất thì lập biên bản xét kỷ luật theo quy định.
- Trường hợp kiểm tra quân tư tranh không phát hiện được thì tổ chức điều tra, tập trung vào các đối tượng có nghi vấn, các quân nhân thường xuyên la cà ở các hàng quán, quân nhân vi phạm kỷ luật, quân nhân có các mối quan hệ phức tạp…; phối hợp với cấp trên, các đơn vị bạn, địa phương nơi đơn vị đóng quân điều tra, nắm bắt tình hình; hạn chế sự nghi kỵ, hoang mang trong đơn vị.
- Tổ chức sinh hoạt đơn vị (từ tiểu đội đến đại đội) quán triệt yêu cầu xây dựng đơn vị an toàn, độn g viên chiến sĩ gửi tiền, các tài sản quý cho đơn vị giữ hộ; thi hành kỷ luật các quân nhân vi phạm và xem xét những cán bộ, chiến sĩ liên đới trách nhiệm. Đồng thời, biểu dương những tập thể cá nhân đã tích cực tham gia giải quyết vụ việc có hiệu quả.
- Duy trì nghiêm các chế độ trong ngày, tuần; các chế độ trực chỉ huy, trực ban, canh gác; hoạt động của các chiến sĩ bảo vệ; hoạt động chấm điểm thi đua và chế độ sinh hoạt của đơn vị.
- Tổng hợp tình hình và báo cáo cấp trên.

Tình huống 57: Ở đơn vị có hiện tượng khi chiến sĩ được đi phép theo chế độ, cán bộ đại đội có “gợi ý” để lại tiền ăn “làm quỹ vốn đơn vị”. Số chiến sĩ được đi phép đồng ý nhưng tâm lý không thoải mái, có biểu hiện nghi ngờ việc làm trên của cán bộ để trục lợi cá nhân.
Gợi ý biện pháp xử lý
- Trao đổi trong cấp ủy chỉ huy đơn vị, thống nhất biện pháp giải quyết, trong tình huống này có hai trường hợp xảy ra.
+ Nếu đơn vị không có chủ trương mà cán bộ đơn vị đòi giữ lại tiền ăn của chiến sĩ đi tranh thủ để tiêu xài riêng thì đó là sai phạm phải kiểm điểm, xử lý kỷ luật.
+ Nếu đây là chủ trương của đơn vị, số tiền thu được nhập quỹ chung thì cũng là việc làm không đúng phải khắc phục. Trong trường hợp này pahri công khai, hoàn trả lại tiền ăn cho bộ đội và nghiêm túc rút kinh nghiệm (kể cả khi anh em tự nguyện không nhận số tiền đó).
- Sinh hoạt đơn vị, phổ biến, quán triệt các văn bản quy định của cấp trên có liên quan đến sự việc trên; thống nhất chủ trương của đơn vị, không thu tiền ăn khi bộ đội đi phép, tranh thủ… Duy trì thực hiện tốt quy chế dân chủ ở cơ sở, công khai minh bạch các chế độ tiêu chuẩn; quan tâm đời sống vật chất, tinh thần của bộ đội, tạo bầu không khí dân chủ, đoàn kết, gắn bó, tin tưởng trong đơn vị.
- Theo dõi dư luận của đơn vị sau khi đại đội đã sinh hoạt thống nhất để có biện pháp giải quyết tiếp theo.

Tình huống 58: Trong đại đội có chiến sĩ vắng mặt trái phép, khi đơn vị điện thông báo với gia đình thì gia đình cho biết, lý do vắng mặt trái phép là do bị trung đội trưởng đánh, gia đình chiến sĩ ra điều kiện “nếu trở lại đơn vị thì đơn vị không được xử phạt”/
Gợi ý biện pháp xử lý
- Yêu cầu đồng chí trung đội trưởng báo cáo sự việc chiến sĩ vắng mặt trái phép và tình hình tư tưởng của trung đội.
- Hội ý cấp ủy, chỉ huy thống nhất nhận định, đề xuất biện pháp giải quyết; báo cáo cấp trên.
- Cử cán bộ (từ đại đội trở lên) có đủ khả năng thực hiện nhiệm vụ về địa phương (cơ quan quân sự huyện, xã…), gia đình đề nghị phối hợp với đơn vị gặp, giải thích, động viên quân nhân vắng mặt trái phép trở lại đơn vị. Đây là khâu quan trọng trong giải quyết vụ việc này. Lưu ý, cán bộ đi giải quyết vụ việc phải nắm chắc diễn biến sự việc, lỗi phạm của cán bộ trung đội trưởng và các quân nhân; có phương pháp mềm dẻo khéo léo, lấy động viên thuyết phục là chính, thậm chí phải lấy danh dự của mình để bảo đảm với gia đình là không ai trù dập con em họ.
- Làm cho địa phương và gia đình hiểu rõ việc cán bộ đánh chiến sĩ là vi phạm kỷ luật quân đội, đơn vị có trách nhiệm xem xét, xử lý theo điều lệnh quy định, song việc chiến sĩ bị đánh không báo cáo với cán bộ đại đội, tiểu đoàn mà tự ý bỏ về cũng là vi phạm; việc nhận ra lỗi phạm nhanh chóng trở về đơn vị công tác sẽ được xem xét giảm nhẹ, khi xử lý kỷ luật nếu vì lý do cán bộ quân phiệt mà cố tình trốn tránh nghĩa vụ quân sự sẽ bị xử lý theo pháp luật.
- Khi chiến sĩ đã về đơn vị, nhanh chóng triển khai cán bộ trung đội trưởng và chiến sĩ vi phạm viết tường trình, kiểm điểm, tổ chức sinh hoạt các cấp theo quy định, tập trung phân tích và làm rõ nguyên nhân mức đội, tính chất vụ việc và xử lý kỷ luật theo quy định.
- Sau khi đã thực hiện xong các nội dung trên, thông báo về gia đình (có thể cả địa phương) biết, đồng thời đề nghị gia đình tiếp tục phối hợp cùng đơn vị để giáo dục, động viên quân nhân yên tâm phục vụ tại ngũ và tích cực rèn luyện để trở thành quân nhân tốt.
- Khi vụ việc này xử lý và giải quyết xong để nhằm ngăn chặn không có vụ việc tương tự tái diễn, đơn vị tổ chức thông báo vụ việc và quán triệt chung trong toàn đơn vị về quan điểm của cấp ủy, chỉ huy đơn vị trong quản lý, rèn luyện chiến sĩ, nếu có vi phạm sẽ tiến hành xử lý theo quy định của Điều lệnh Quản lý bộ đội, nghiêm cấm cán bộ có hành động quân phiệt với chiến sĩ.
- Phân công cán bộ giúp đỡ quân nhân vắng mặt trái phép tiến bộ.
- Báo cáo kết quả giải quyết lên cấp trên.

Tình huống 59: Trong đại đội có hiện tượng một số cán bộ, đảng viên thấy đúng không bảo vệ, thấy sai không đấu tranh, không phản ảnh, báo cáo vì sợ cán bộ đơn vị trù dập.
Gợi ý biện pháp xử lý
- Cấp ủy, chỉ huy đơn vị hội ý, trao đổi nhận định tình hình, thống nhất biện pháp giải quyết. Đây là biểu hiện của những cán bộ, đảng viên tính đấu tranh tự phê bình và phê bình kém, đồng thời còn là biểu hiện thiếu dân chủ, độc đoán, gia trưởng của chỉ huy đơn vị, ảnh hưởng đến kết quả xây dựng chi bộ trong sạch vững mạnh, đơn vị vững mạnh toàn diện có thể dẫn tới mất đoàn kết, cục bộ, bè phái trong đơn vị.
- Gặp gỡ trao đổi với cán bộ có biểu hiện độc đoán, gia trưởng, mất dân chủ.
+ Nếu là trung đội trưởng hoặc cấp phó đại đội thì chính trị viên nên trao đổi với đại đội trưởng về sự việc đó, thống nhất bàn biện pháp xử lý. Trước hết, trên cương vị bí thư chi bộ, chính trị viên gặp gỡ phân tích để cán bộ đó nhận thức ra vấn đề và tích cực sữa chữa khuyết điểm; thường xuyên theo dõi, giúp đỡ đồng chí đó tu dưỡng, rèn luyện phẩm chất đạo đức, phương pháp tác phong công tác. Nếu vẫn vi phạm thì tổng hợp báo cáo cấp trên và xử lý theo thẩm quyền.
+ Nếu là đại đội trưởng: Chính trị viên phải khéo léo, lựa lời, chọn thời điểm để góp ý với đại đội trưởng. Cùng đại đội trưởng trao đổi thẳng thắn và bàn biện pháp khắc phục. Nếu không thấy chuyển biến thì tổ chức sinh hoạt chi bộ và báo cáo cấp trên.
- Chi bộ xác định chủ trương biện pháp lãnh đạo thường kỳ, cần thiết thì ra nghị quyết lãnh đạo chuyên đề; thực hiện đúng nề nếp, nguyên tắc tổ chức sinh hoạt của cấp ủy, chi bộ. Đổi mới phương pháp lãnh đạo, tổ chức thực hiện nghiêm nhiệm vụ của chi ủy, chi bộ và chỉ huy đơn vị (việc đánh giá, nhận xét phải cụ thể, đúng người, đúng việc, khách quan, công khai, dân chủ) đề cao trách nhiệm của chi ủy, chi bộ và chỉ huy đơn vị (việc đánh giá, nhận xét phải cụ thể, đúng người, đúng việc, khách quan, công khai, dân chủ) đề cao trách nhiệm nêu gương của cán bộ chủ trì trong tự phê bình và phê bình; phát huy vai trò cán bộ khi chủ trì điều hành không khí cởi mở; gắn tinh thần tự phê bình và phê bình với kết quả phân loại và khen thưởng của đảng viên.
- Chỉ đạo các tổ chức quần chúng duy trì nghiêm nề nếp chế độ sinh hoạt đóng góp s kiến cho cán bộ, đảng viên về phẩm chất đạo đức, lối sống, về mối quan hệ đoàn kết cán binh và tinh thần trách nhiệm trong xây dựng đơn vị.
- Thường xuyên làm tốt việc giáo dục, quán triệt nâng cao nhận thức cho cán bộ, đảng viên. Duy trì thực hiện có hiệu quả nguyên tắc tập trung dân chủ, quy chế dân chủ ở cơ sở, công khai, minh bạch mọi chế độ tiêu chuẩn; giải đáp thấu đáo có tình, có lý mọi ý kiến của cán bộ, đảng viên; tổ chức tốt ngày chính trị và văn hóa tinh thần, chăm lo thực sự đến đời sống vật chất, tinh thần cán bộ, chiến sĩ.
- Kịp thời phát hiện, nhắc nhở, chấn chỉnh và có biện pháp xử lý với những cán bộ đảng viên có biểu hiện quân phiệt, trù dập cấp dưới; nâng cao chất lượng kiểm tra giám sát của chi bộ đối với cán bộ, đảng viên, biểu dương, nhân rộng và phát huy vai trò của những nhân tố tích cực; đẩy mạnh các hoạt động thi đua, xây dựng môi trường văn hóa lành mạnh trong đơn vị.

Tình huống 60: Trong tiểu đoàn có đại đội trưởng và chính trị viên cùng đại đội mâu thuẫn mất đoàn kết với nhau, dẫn đến chất lượng hoàn thành nhiệm vụ thấp, gây dư luận không tốt trong đơn vị.
Gợi ý biện pháp xử lý
- Hội ý đảng ủy, chỉ huy đơn vị, đánh giá tính chất, nguyên nhân, mức độ ảnh hưởng của việc mất đoàn kết đối với cán bộ chủ trì; trao đổi, thống nhất biện pháp giải quyết; báo cáo cấp trên xin ý kiến chỉ đạo.
- Phân công cán bộ tiểu đoàn cùng với cấp ủy, chỉ huy đại đội xác minh, nắm cụ thể tính chất mức độ mâu thuẫn và nguyên nhân mất đoàn kết.
- Trực tiếp gặp hai đồng chí cán bộ để nắm tình hình cụ thể; phân tích để từng đồng chí nhận thức đúng vai trò của cán bộ chủ trì đối với kết quả thực hiện nhiệm vụ chính trị và xây dựng đơn vị…
- Tổ chức cho chi bộ sinh hoạt để cán bộ, đảng viên đóng góp và hai đồng chí đóng góp thẳng thắn cho nhau. Nếu hai đồng chí đó không nhận ra được khuyết điểm, trách nhiệm của mình, thì chỉ đạo cấp ủy, chi bộ tổ chức sinh hoạt kiểm tra đảng viên có dấu hiệu vi phạm kỷ luật, mất đoàn kết nội bộ; sau kiểm tra có kết luận và xét kỷ luật (nếu thấy cần thiết).
- Thông báo tình hình vụ việc trên đến đảng viên là cán bộ đại đội thuộc đảng bộ tiểu đoàn; nếu việc mâu thuẫn mất đoàn kết trong cán bộ các cấp diễn ra phổ biến thì cần ra nghị quyết chuyên đề để lãnh đạo khắc phục tình trạng trên.
- Phân công trong đảng ủy, chỉ huy tiểu đoàn thường xuyên theo dõi (dự hội nghị chi bộ, giao ban, hội họp,…) hướng dẫn, giúp đỡ cán bộ đại đội thực hiện tốt chức trách, nhiệm vụ…
- Trường hợp mâu thuẫn lớn không thể khắc phục thì đề nghị cấp trên có thẩm quyền điều động đối với một hoặc cả hai đồng chí đó.

Tình huống 61: Trong tiểu đoàn có hiện tượng cán bộ đại đội “thành kiến” với cán bộ trung đội, dẫn đến cán bộ bị “thành kiến” có biểu hiện bất mãn, làm việc cầm chừng, xin đi đơn vị khác.
Gợi ý biện pháp xử lý
- Phân công cán bộ xác minh, làm rõ nguyên nhân những bất đồng, “thành kiến” của cán bộ đại đội với trung đội.
- Trao đổi thống nhất trong đảng ủy, chỉ huy tiểu đoàn, nhận định, đánh giá nguyên nhân, mức độ ảnh hưởng của sự việc, thống nhất biện pháp giải quyết.
- Gặp riêng từng đối tượng để nắm rõ nguyên nhân; phân tích rõ vị trí, vai trò, trách nhiệm của từng đồng chí trong xây dựng chi bộ, trong chỉ huy đơn vị, chấn chỉnh ngay những sai sót, hạn chế trong giải quyết các mối quan hệ công tác và trong đoàn kết nội bộ.
- Tổ chức cho hai đồng chí đó gặp gỡ, đối thoại, trao đổi trực tiếp, góp ý thẳng thắn, chân thành những vấn đề nảy sinh trong quan hệ công việc, nhận rõ những sai sót trong ứng xử với đồng chí đồng đội, với cấp trên, cấp dưới, qua đó xây dựng mối đoàn kết giữa hai đồng chí cán bộ.
- Trường hợp thật cần thiết (không giáo dục, thuyết phục được) phải chỉ đạo tổ chức sinh hoạt cấp ủy, chi bộ đơn vị đó để kiểm điểm, rút kinh nghiệm, nhằm ổn định tình hình tư tưởng của cán bộ. Báo cáo, đề nghị cấp trên xem xét điều chuyển vị trí công tác mới đối với một hoặc cả hai đồng chí đó.
- Tổ chức sinh hoạt riêng đối với đội ngũ cán bộ trong tiểu đoàn, rút kinh nghiệm trong giải quyết các mối quan hệ cấp trên cấp dưới, trong xây dựng mối đoàn kết thống nhất trong đơn vị.
- Thường xuyên quan tâm giáo dục, bồi dưỡng cán bộ, nắm chắc các mối quan hệ của cán bộ; chăm lo xây dựng đoàn kết nội bộ, xây dựn g đảng bộ trong sạch vững mạnh gắn với đơn vị vững mạnh toàn diện.
- Báo cáo kết quả giải quyết lên cấp trên.

Tình huống 62: Trong đại đội có hiện tượng một số chiến sĩ nhập ngũ trước bắt nạt (ăn hiếp) chiến sĩ mới, một số chiến sĩ mới có biểu hiện lo lắng
Gợi ý biện pháp xử lý
- Chỉ huy đại đội kiểm tra, thông báo ngay cho cán bộ trung đội (tiểu đội, khẩu đội) có chiến sĩ mất đoàn kết để có biện pháp phối hợp ngăn chặn, giải quyết kịp thời;
- Hội ý cấp ủy, chỉ huy đơn vị trao đổi, thống nhất cách xử lý; phân công cán bộ phụ trách việc chỉ đạo giải quyết; báo cáo sự việc và đề xuất biện pháp giải quyết lên cấp trên.
- Xác định người cầm đầu nhóm quân nhân tham gia bắt nạt (ăn hiếp) chiến sĩ mới, triển khai viết tường trình, kiểm điểm và xem xét xử lý kỷ luật theo quy định của Điều lệnh Quản lý bộ đội.
- Tổ chức sinh hoạt đại đội giáo dục, rút kinh nghiệm chung, giúp chiến sĩ nhận thức được việc làm đó sẽ làm ảnh hưởng tới mối đoàn kết trong đơn vị, ảnh hưởng tới truyền thống của đơn vị, quân đội; giáo dục truyền thống dân tộc, quê hương, quân đội, tinh thần đoàn kết giúp đỡ thương yêu đồng chí đồng đội, nhất là động viên các chiến sĩ đi trước phải có trách nhiệm dìu dắt, giúp đỡ chiến sĩ mới phấn đấu tiến bộ.
- Tổ chức diễn đàn, tọa đàm, trao đổi trong đơn vị về các chủ đề: dân chủ và kỷ luật, truyền thống và mối quan hệ đoàn kết trong đơn vị. Khi chiến sĩ hoàn thành nghĩa vụ quân sự thì nên tổ chức bàn giao thế hệ để chiến sĩ sắp xuất ngũ báo cáo kết quả xây dựng đơn vị, động viên, nhắn nhủ các chiến sĩ ở lại đoàn kết, thương yêu nhau, phấn đấu xây dựng đơn vị, hoàn thành tốt nhiệm vụ được giao; buổi bàn giao thế hệ mời địa phương, đơn vị kết nghĩa vào dự, có kết hợp văn nghệ và trao thưởng để tạo không khí vui vẻ…
- Phát huy vai trò của các tổ chức trong đơn vị, chỉ đạo tổ chức các hoạt động giao lưa văn hóa văn nghệ, thể dục thể thao (có tổ chức chặt chẽ) tạo không khí đoàn kết, thống nhất, không để từ mâu thuẫn nhỏ nảy sinh thành mâu thuẫn lớn trong đơn vị.
- Phân công cán bộ và chiến sĩ bảo vệ theo dõi nắm chắc các mối quan hệ giữa cán bộ với chiến sĩ, chiến sĩ với chiến sĩ, nhất là khi thực hiện các nhiệm vụ phân tán, nhỏ lẻ, giờ nghỉ, ngày nghỉ, xa sự quản lý, chỉ huy của đơn vị.
- Duy trì chặt chẽ các nề nếp chế độ trong ngày, trong tuần, thực hiện tốt chế độ phản ảnh, báo cáo tình hình tư tưởng và mối quan hệ đoàn kết nội bộ, đoàn kết quân dân.

Tình huống 63: Một số chiến sĩ cảnh vệ lên báo cáo chỉ huy đại đội đã nhận được thông tin có chiến sĩ A. chuẩn bị xuất ngũ đang có ý định trả thù vì những mâu thuẫn trong thời gian quân nhân đó chấp hành lệnh phạt giam.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị, đánh giá tính chất, tác hại của sự việc, thống nhất biện pháp giải quyết và báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ chiến sĩ cảnh vệ nắm chắc tính chất, nguyên nhân, đối tượng, đơn vị cụ thể; động viên chiến sĩ cảnh vệ an tâm công tác, tiếp tục thực hiện các nhiệm vụ duy trì điều lệnh, kỷ luật trong đơn vị.
- Thông báo ngay cho cán bộ quản lý chiến sĩ A. biết để có biện pháp quản lý, giáo dục và phối hợp giải quyết. Có thể cùng với đơn vị gặp gỡ riêng chiến sĩ A. để tìm hiểu nguyên nhân, giáo dục chiến sĩ thấy việc làm đó là vi phạm kỷ luật, phát luật, ảnh hưởng đến đơn vị, gia đình, địa phương và bản thân; tạo điều kiện để các quân nhân gặp gỡ, đối thoại hòa giải, xây dựng mối đoàn kết quân nhân.
- Chỉ huy đơn vị quản lý chiến sĩ A., quản lý chặt chẽ bộ đội, vũ khí trang bị, duy trì nghiêm nề nếp chế độ, tổ chức kiểm tra điểm nghiệm quân tư trang, kịp thời thu giữ hung khí (nếu có); tổ chức sinh hoạt ổn định tình hình đơn vị, quán triệt các quy định về xử phạt để giáo dục, răn đe quân nhân; phân công cán bộ, chiến sĩ bảo vệ theo dõi nắm chắc tình hình, quản lý chặt chẽ mọi hoạt động của bộ đội, nhất là chiến sĩ cá biệt.
- Báo cáo với chỉ huy trung đoàn để chỉ đạo các đơn vị có biện pháp quản lý giáo dục chung trong toàn đơn vị.

Tình huống 64: Một số quân nhân trong đơn vị có biểu hiện mất đoàn kết với quân nhân đơn vị bạn đóng quân gần đó, dẫn đến một số quân nhân đơn vị bạn có ý định trả thù, làm cho một số chiến sĩ lo sợ khi ra ngoài đơn vị.
Gợi ý biện pháp xử lý
- Chỉ huy đơn vị trao đổi, thống nhất biện pháp xử lý.
- Gặp gỡ quân nhân có mâu thuẫn với quân nhân của đơn vị bạn để tìm hiểu rõ nguyên nhân.
- Tổ chức sinh hoạt đơn vị để giáo dục chung, đồng thời cử cán bộ gặp gỡ trao đổi với chỉ huy đơn vị bạn để nắm tình hình và phối hợp quản lý, giáo dục quân nhân.
- Duy trì nghiêm túc chế độ ngày, tuần, quản lý chặt chẽ quân nhân của đơn vị, đặc biệt là trong giờ nghỉ, ngày nghỉ; quân nhân ra ngoài đơn vị phải được giáo dục, có cán bộ chỉ huy, không được có biểu hiện gây gổ, xô xát làm xấu hình ảnh “Bộ đội Cụ Hồ”.
- Phối hợp chặt chẽ với chính quyền, cơ quan chức năng và nhân dân địa phương trong việc phát hiện thông báo cho đơn vị và giúp đơn vị xử lý kịp thời các mâu thuẫn giữa quân nhân hai đơn vị.
- Tăng cường những hoạt động giao lưu, kết nghĩa giữa cán bộ, chiến sĩ hai đơn vị.
- Tổng hợp tình hình báo cáo cấp trên theo quy định.

D. NHÓM TÌNH HUỐNG TƯ TƯỞNG NẢY SINH TRONG QUAN HỆ QUÂN DÂN (11 TÌNH HUỐNG)

Tình huống 65: Trong thời gian đi giúp nhân dân địa phương, tiểu đội trưởng (mặc quân phục) đã say rượu, có những lời nói và hành động không tốt; một số thanh niên địa phương đã lợi dụng chụp ảnh, quay video clip và đưa thông tin lên trang mạng Internet. Đồng chí tiểu đội trưởng tỏ ra hoang mang, lo lắng và lên báo cáo với chỉ huy đại đội.
Gợi ý biện pháp xử lý
- Trao đổi nhanh trong chỉ huy đại đội, thống nhất biện pháp xử lý và phân công cán bộ phụ trách giải quyết vụ việc.
- Báo cáo cấp trên xin ý kiến chỉ đạo và đề nghị cử cán bộ và cơ quan chức năng phối hợp với đơn vị để giải quyết vụ việc, trước hết là bóc gỡ thông tin nói trên.
- Gặp gỡ đồng chí tiểu đội trưởng để nắm lại tình hình, yêu cầu báo cáo cụ thể về sự việc.
- Cùng với cấp trên và cơ quan chức năng làm việc với chính quyền cơ quan chức năng địa phương để tiến hành các biện pháp giáo dục số thanh niên có liên quan.
- Tiến hành kiểm điểm và xử lý kỷ luật đồng chí tiểu đội trưởng theo quy định.
- Tổ chức sinh hoạt đơn vị để giáo dục, định hướng, rút kinh nghiệm chung trong toàn đơn vị về các yêu cầu khi thực hiện nhiệm vụ dân vận và việc nêu cao ý thức giữu gìn phẩm chất, tư cách “Bộ đội Cụ Hồ”.
- Tổng hợp báo cáo với cấp trên về kết quả giải quyết và xử lý vụ việc theo quy định.

Tình huống 66: Khi đơn vị làm nhiệm vụ tuyên truyền vận động quần chúng, giải tán một bộ phận nhân dân biểu tình quá khích, đập phá nhà xưởng của người Trung Quốc làm việc tại Việt Nam, trong số đó có gia đình, người thân, hàng xóm của một số quân nhân trong đơn vị; số quân nhân trên có biểu hiện băn khoăn, lo lắng vì không biết phải ứng xử như thế nào cho phù hợp.
Gợi ý biện pháp xử lý
- Trao đổi, thống nhất trong cấp ủy, chỉ huy đơn vị về biện pháp giải quyết; phân công cán bộ phụ trách; báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ quân nhân, phân tích cho quân nhân hiểu hành động đập phá nhà xưởng của người Trung Quốc là vi phạm pháp luật, gây hậu quả xấu cho nền kinh tế, làm xấu hình ảnh Việt Nam đối với quốc tế; ảnh hưởng trực tiếp đến việc làm của công nhân trong đó có gia đình, người thân các đồng chí; định hướng chó quân nhân cần có nhận thức đúng, tiếp tục thực hiện nhiệm vụ, trước hết là tuyên truyền, thuyết phục gia đình, người thân và hàng xóm không theo kẻ xấu kích động; phát hiện và báo cáo cho cơ quan chức năng bắt giữ những kẻ cầm đầu.
- Tổ chức sinh hoạt, định hướng đơn vị tiếp tục thực hiện nhiệm vụ tuyên truyền, thuyết phục vận động nhân dân không tham gia biểu tình quá khích; không phân biệt, đối xử với chiến sĩ có gia đình, người thân trong số những người biểu tình.
- Phân công cán bộ theo dõi, kèm cặp giúp đỡ đề phòng các tình huống có thể nảy sinh như đào ngũ, vắng mặt trái phép vì quân nhân có thể mặc cảm, tự ty hoặc bị kích động từ số những người biểu tình hoặc chiến sĩ trong đơn vị.
- Phối hợp chặt chẽ với đoàn thể, chính quyền địa phương và nhân dân để thực hiện nhiệm vụ và quản ly tư tưởng, kỷ luật của cán bộ, chiến sĩ đơn vị.

Tình huống 67: Trong đại đội có dư luận về đồng chí A. là cán bộ trung đội đã có vợ, thời gian gần đây có quan hệ bất chính với một phụ nữ đã có chồng gần đơn vị.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chi ủy đơn vị thống nhất, nhập định, đánh giá tình hình, xác định biện pháp giải quyết; phân công cán bộ xác minh làm rõ thông tin về dư luận; báo cáo xin ý kiến chỉ đạo của cấp trên.
- Gặp gỡ đồng chí A. để nắm rõ các mối quan hệ, động viên cán bộ nếu có khuyết điểm thì thành thật báo cáo với đơn vị.
- Nắm các kênh thông tin: từ cấp trên cung cấp, từ đồng chí đồng đội, chiến sĩ bảo vệ, chiến sĩ dân vận của đơn vị và các tổ chức đoàn thể, nhân dân địa phương để tiến hành xác minh, làm rõ.
- Trường hợp cán bộ thành khẩn khai nhận hoặc qua xác minh kết luận là đúng thì triển khai viết tường trình kiểm điểm, căn cứ vào tính chất hậu quả vi phạm và thái độ sau vi phạm để xử lý kỷ luật theo quy định, báo cáo kết quả xử lý về cấp trên để thông báo đến đảng viên là sĩ quan cấp ủy trong toàn đảng bộ.
- Gặp gỡ cá nhân, gia đình cô gái có quan hệ bất chính với đồng chí A. để thông báo tình hình hôn nhân và khuyết điểm của đồng chí A., đề nghị chấm dứt mối quan hệ.
- Nếu dư luận không đúng, tập trung đơn vị thông báo về kết quả điều tra kết luận của các tổ chức trong đơn vị về đồng chí A., động viên đồng chí A. tiếp tục tu dưỡng phẩm chất đạo đức, yên tâm công tác.
- Tổ chức điều tra, xác minh ai là người tung tin sai sự thật, mục đích, động cơ tung tin…
- Nếu xác định rõ đối tượng, mục đích tung dư luận xấu thì thi hành kỷ luật theo quyền hạn.
- Ổn định tư tưởng trong đơn vị, duy trì nghiêm các nề nếp, chế độ sinh hoạt, hoạt động của đơn vị, tăng cường các biện pháp quản lý cán bộ, đảng viên nhất là ngày nghỉ, giờ nghỉ, ngoài doanh trại.
- Tổng hợp tình hình báo cáo cấp trên.

Tình huống 68: Bí thư chi đoàn địa phương nơi đơn vị đóng quân cho biết, thanh niên địa phương “cấm vận gái làng” không được quan hệ, tiếp xúc với quân nhân của đơn vị vì có những mâu thuẫn giữa một số thanh niên địa phương và quân nhân đơn vị chưa được giải quyết.
Gợi ý biện pháp xử lý
- Nhận định: Đây là vụ việc phức tạp, nếu không kịp thời ngăn chặn và có biện pháp giải quyết triệt để có thể sẽ dẫn đến xung đột, thậm chí gây hậu quả nghiêm trọng, ảnh hưởng đế mối quan hệ đoàn kết quân dân…
- Cảm ơn địa phương đã cung cấp thông tin và đề nghị phối hợp, tạo điều kiện giải quyết.
- Trao đổi thống nhất trong cấp ủy, trong chỉ huy: Nhận định, thẩm tra, xác minh kết luận tình hình, thống nhất biện pháp giải quyết.
- Đánh giá phân loại chiến sĩ; gặp gỡ số chiến sĩ địa phương yêu cầu tường trình làm rõ mâu thuẫn với thanh niên địa phương, xác định tính chất, mức độ lỗi vi phạm, tổ chức giáo dục kiểm điểm và xử lý kỷ luật theo quy định.
- Làm việc với cấp ủy chính quyền, đoàn thể địa phương, thông báo kết quả giáo dục, xử lý kỷ luật số quân nhân vi phạm.
- Tổ chức sinh hoạt đơn vị: Giáo dục về nhiệm vụ, bản chất truyền thống quân đội, đơn vị, mối quan hệ gắn bó máu thịt với nhân dân; về nếp sống văn minh trong quan hệ, ứng xử, giao tiếp với nhân dân; thông báo tình hình địa bàn; yêu cầu và trách nhiệm của quân nhân trong xây dựng đơn vị an toàn, địa bàn an toàn…
- Phối hợp với các tổ chức diễn đàn, tọa đàm, gặp gỡ, hòa giải giữa thanh niên đơn vị với thanh niên của địa phương; tuyên truyền về nếp sống có văn hóa, quan hệ ứng xử, tình bạn, tình yêu; tổ chức các hoạt động giao lưu văn hóa văn nghệ, thể dục thể thao… tổ chức kết nghĩa giữa đơn vị với các tổ chức đoàn thể địa phương.
- Thường xuyên đánh giá, rút kinh nghiệm về kết quả xây dựng địa bàn (quan hệ quân dân); duy trì nề nếp phản ảnh, nắm tình hình với địa phương; chủ động trong công tác quản lý bộ đội.

Tình huống 69: Đại đội đang thực hiện nhiệm vụ hành quân dã ngoại kết hợp làm công tác dân vận tại địa bàn xã X. nhưng vì một lý do nào đó… nhân dân không cho bộ đội vào đóng quân trong nhà dân.
Gợi ý biện pháp xử lý
- Cấp ủy, chỉ huy đơn vị nhanh chóng trao đổi, thống nhất cách xử lý; phân công cán bộ phụ trách; báo cáo cấp trên xin ý kiến chỉ đạo.
- Triển khai cho bộ đội tạm dừng hành quân yêu cầu cán bộ trung đội, cán bộ tiểu đội tăng cường công tán quản lý bộ đội.
- Phân công cán bộ thâm nhập địa bàn, phối hợp với cấp ủy, chính quyền và đoàn thể địa phương nắm tình hình, nguyên nhân cụ thể để có cơ sở tuyên truyền, thuyết phục nhân dân tin tưởng cho đơn vị.
- Khi các gia đình đồng ý cho bộ đội vào đóng quân ở nhà dân, phải quán triệt, giáo dục cho bộ đội hiểu rõ yêu cầu của gia đình đối với bộ đội ở trong nhà, tình hình cụ thể của địa phương, thực hiện nghiêm các quy định, tôn trọng phong tục tập quán của địa phương, không vi phạm kỷ luật quan hệ đoàn kết quân dân, luôn thể hiện tư thế tác phong của “Bộ đội Cụ Hồ”.
- Tổ chức cho đơn vị tích cực thực hiện nghiêm nhiệm vụ huấn luyện, kết hợp giúp địa phương củng cố cơ sở vật chất hạ tầng, xây dựng cơ sở chính trị, tuyên truyền vận động nhân dân, giúp đỡ gia đình chính sách, gia đình nghèo, dạy học cho các cháu học sinh… hằng ngày tổ chức phát tin thi đua, đồng thời phối hợp với địa phương tổ chức các hoạt động giáo dục truyền thống, giao lưu văn hóa, văn nghệ tăng cường tinh thần đoàn kết quân dân.
- Kết thúc thời gian thực hiện nhiệm vụ hành quân dã ngoại kết hợp làm công tác dân vận tại địa bàn, nhanh chóng nắm tình hình, giải quyết triệt để mọi vướng mắc với gia đình người dân và địa phương (nếu có).
- Chỉ đạo từ tiểu đội đến đại đội sinh hoạt đánh giá kết quả, rút kinh nghiệm đề nghị khen thưởng.

Tình huống 70: Đại đội có chiến sĩ đánh nhau với thanh niên địa phương tại địa bàn đơn vị thực hiện nhiệm vụ huấn luyện dã ngoại (hoặc dã ngoại làm công tác dân vận).
Gợi ý biện pháp xử lý
- Chỉ huy đơn vị kịp thời ngăn chặn không cho vụ việc phát triển xấu, báo cáo cấp trên về tình hình vụ việc (trường hợp phức tạp phải thông báo và phối hợp với cấp ủy, chính quyền địa phương để ngăn chặn).
- Hội ý thông nhất trong cấp ủy, chỉ huy đại đội sơ bộ nắm tình hình, nguyên nhân và dự kiến biện pháp giải quyết.
- Lãnh đạo, chỉ huy đại đội trao đổi thống nhất với cấp ủy, chính quyền địa phương về nội dung vụ việc, tính chất, mức độ tác hại, nguyên nhân và biện pháp giải quyết, khắc phục hậu quả.
- Tổng hợp tình hình báo cáo chỉ huy cấp trên và xin ý kiến chỉ đạo.
- Quản lý chặt chẽ người và vũ khí trang bị, chỉ đạo, hướng dẫn và tổ chức tiến hành xử lý vụ việc:
+ Trường hợp do chiến sĩ trong đơn vị chủ động gây ra: Chỉ huy đại đội tiến hành xem xét xử lý kỷ luật chiến sĩ vi phạm theo đúng quy định Điều lệnh Quản lý bộ đội; gặp gỡ cấp ủy, chính quyền địa phương nắm tình hình sau vụ việc xảy ra và thông báo kết quả xử lý kỷ luật chiến sĩ vi phạm; tổ chức cho chiến sĩ vi phạm kỷ luật gặp gỡ thanh niên địa phương bị đánh để xin lỗi, bồi thường thiệt hại (nếu cần thiết có thể ngừng hoạt động dã ngoại của chiến sĩ đó đưa về doanh trại).
+ Trường hợp do thanh niên địa phương chủ động gây ra: Chỉ huy đại đội cung cấp thông tin cho chính quyền địa phương; thông báo ý kiến của lãnh đọa, chỉ huy cấp trên về biện pháp xử lý, khắc phục hậu quả; đề nghị chính quyền địa phương xem xét, xử lý kiên quyết đối tượng vi phạm.
- Tổ chức sinh hoạt rút kinh nghiệm trong đại đội; phối hợp với cấp ủy, chính quyền địa phương trong công tác giáo dục, quản lý các mối quan hệ đoàn kết nhân dân; cùng với chi đoàn địa phương tổ chức các hoạt động giao lưu văn hóa văn nghệ, thể dục thể thao để cho cán bộ, chiến sĩ đơn vị và thanh niên địa phương gần gũi và hiểu nhau hơn.
- Phát huy vai trò của chiến sĩ bảo vệ, chiến sĩ dân vận, kịp thời báo cáo chỉ huy đơn vị xử lý nhanh gọn các vấn đề nảy sinh trong quá trình thực hiện nhiệm vụ.

Tình huống 71: Trong đợt hành quân huấn luyện dã ngoại kết hợp làm công tác dân vận, đại đội được bố trí ở nhà dân, sau 3 ngày chủ một gia đình có bốn chiến sĩ ở đã gặp và trình báo với ban chỉ huy đại đội về việc gia đình mất 1 triệu đồng đề nghị động viên bốn đồng chí đó, nếu lấy thì trả lại vì gia đình rất khó khăn.
Gợi ý biện pháp xử lý
- Đây là tình huống khá phức tạp, nhạy cảm, liên quan đến danh dự của chiến sĩ và mối quan hệ đoàn kết quân dân. Trong xử lý và giải quyết phải khéo léo, thận trọng, tránh sự suy diễn, chủ quan, quy chụp…
- Đại diện chỉ huy đơn vị tiếp nhận ý kiến, đề nghị gia đình cung cấp cho đơn vị những căn cứ làm cơ sở cho việc điều tra, xác minh, trao đổi với gia đình về các khả năng có thể mất tiền do nhầm lẫn trong chi tiêu, hoặc do con em của gia đình lấy…
- Hội ý cấp ủy, chỉ huy nhận định đánh giá tình hình và thống nhất biện pháp giải quyết.
- Báo cáo cấp trên xin ý kiến chỉ đạo.
- Tiến hành các biện pháp điều tra, xác minh vụ việc:
+ Phân công cán bộ đơn vị gặp riêng từng chiến sĩ để vận động, thuyết phục chiến sĩ, nếu có lấy tiền của gia đình thì tự giác nhận lỗi và trả lại cho gia đình người dân.
+ Triền khai cho bốn chiến sĩ viết bản tường trình, ghi rõ thời gian, địa điểm, sinh hoạt ngủ nghỉ, làm gì, cùng ai, ở đâu? (bốn đồng chí viết tường trình độc lập, không được trao đổi thống nhất).
+ Đối chiếu tường trình của từng đồng chí, chất vấn những vấn đề mâu thuẫn không trùng khớp trong tường trình để điều tra, động viên chiến sĩ thành khẩn nhận khuyết điểm.
- Trường hợp điều tra xác minh được chiến sĩ có lấy cắp tiền của nhà dân, cán bộ đơn vị dẫn chiến sĩ trực tiếp đến chủ gia đình trả lại tiền đã mất và xin lỗi gia đình.
- Triển khai chiến sĩ viết kiểm điểm và tổ chức sinh hoạt đơn vị xét kỷ luật theo quy định và rút kinh nghiệm về mối quan hệ đoàn kết quân dân trong toàn đơn vị.
- Trường hợp bốn đồng chí chứng minh được mình không lấy cặp cũng phải tổ chức sinh hoạt đơn vị để rút kinh nghiệm chung và bàn biện pháp khắc phục; tránh sử dụng các biện pháp quy chụp thiếu cơ sở khi kết luận vụ việc.
- Ban chỉ huy đơn vị thống nhất các biện pháp giải quyết (có thể sử dụng nguồn quỹ vốn đơn vị để giúp đỡ gia đình giải quyết khó khăn).
- Tổ chức sinh hoạt đơn vị để giáo dục nâng cao nhận thức về kỷ luật dân vận, lòng tự trọng cá nhận, quán triệt và thực hiện tốt 12 điều kỷ luật trong quan hệ quân dân, chấp hành tốt các quy định trong công tác dân vận.

Tình huống 72: Qua dư luận đơn vị nắm được, một đồng chí đại đội trưởng có biểu hiện “hợp đồng” giúp các chủ quán đòi nợ chiến sĩ thuộc quyền để “ăn hoa hồng” đã gây dư luận không tốt trong đơn vị.
Gợi ý biện pháp xử lý
- Đây là sự việc nhạy cảm, liên quan đến phẩm chất, uy tín của cán bộ, khi tiến hành cần thận trọng, khách quan, kiểm tra xác minh chặt chẽ, khoa học.
- Chính trị viên xác minh lại nguồn dư luận về đồng chí đại đội trưởng, nếu đúng sự thật thì tiến hành trao đổi thẳng thắn, chân tình với đồng chí đại đội trưởng. Thông báo về dư luận trong đơn vị, kết quả kiểm tra xác minh; phân tích về sự việc trên đã ảnh hưởng không tốt đến tình hình đơn vị và uy tín của cán bộ. Đề nghị đồng chí chấm dứt việc làm trên, giao cho chính trị viên chấn chỉnh việc nợ nần hàng quán của chiến sĩ, đôn đốc chiến sĩ trả nợ sòng phẳng (đây là cách làm tốt nhất để giúp đồng chí đại đội trưởng tự phê bình, khắc phục khuyết điểm).
- Trường hợp đồng chí đại đội trưởng không nhận lỗi thì đồng chí chính trị viên phải báo cáo cấp trên xin ý kiến chỉ đạo, cùng với cấp trên có biện pháp xác minh, chứng minh sự phản ảnh của dư luận là đúng sự thật.
- Ủy ban kiểm tra cấp trên có biện pháp kiểm tra đảng viên có dấu hiệu vi phạm kỷ luật.
- Tổ chức sinh hoạt đơn vị, ổn định tình hình tư tưởng, dư luận của cán bộ, chiến sĩ; nhắc nhở cán bộ, chiến sĩ nêu cao ý thức tu dưỡng, rèn luyện đạo đức, lối sống, không rượu chè, cờ bạc, la cà, nợ nần hàng quán.
- Tăng cường công tác giáo dục chính trị tư tưởng, nâng cao chất lượng xây dựng nề nếp chính quy, rèn luyện kỷ luật. Tổ chức các hoạt động thể dục thể thao, vui chơi giải trí, văn hóa văn nghệ thu hút cán bộ, chiến sĩ tham gia, đồng thời cán bộ các cấp phải thường xuyên gần gũi động viên, nắm bắt tư tưởng của chiến sĩ để có biện pháp giải quyết kịp thời.
- Phối hợp với chính quyền đoàn thể địa phương thông báo, nhắc nhở, vận động nhân dân (các hàng quán) chấp hành nghiêm quy định của Nhà nước về việc kinh doanh và các hoạt động kinh doanh; không cho bộ đội vay nợ nặng lãi, không làm ảnh hưởng xấu đến mối quan hệ quân dân và tình hình an ninh trật tự trên địa bàn.
- Báo cáo kết quả giải quyết vụ việc lên cấp trên.

Tình huống 73: Cán bộ trung đội trưởng có biểu hiện “gợi ý” nhận tiền, quà của gia đình chiến sĩ mới, kèm theo những “hứa hẹn” về sự quan tâm, tạo điều kiện giúp đỡ đã gây dư luận không tốt trong đơn vị và gia đình chiến sĩ.
Gợi ý biện pháp xử lý
- Đây là biểu hiện vi phạm phẩm chất đạo đức của cán bộ trong đơn vị, nếu không ngăn chặn, chấn chỉnh kịp thời sẽ ảnh hưởng xấu đến niềm tin, uy tín của cán bộ đối với chiến sĩ và gia đình, địa phương.
- Trao đổi thống nhất trong cấp ủy, chỉ huy đơn vị, thống nhất biện pháp giải quyết; xác định lại nguồn thông tin (gặp gỡ riêng một số quân nhân), kết luận sự việc.
- Khi đã có đủ cơ sở, gặp gỡ cán bộ trung đội yêu cầu trung thực báo cáo về sai phạm của mình, phân tích, chỉ rõ tác hại của những hành vi sai trái đó đã ảnh hưởng xấu đến uy tín của cán bộ, chỉ huy đơn vị; phê bình, nhắc nhở, yêu cầu phải xin lỗi về vấn đề này. Căn cứ mức độ phậm lỗi để xem xét, xử lý, bảo đảm nghiêm túc, có tính giáo dục, thuyết phục cao.
- Gặp gỡ gia đình và chiến sĩ đã được trung đội trưởng gợi ý nhận tiền, tặng quà để nói rõ việc làm trên là sai, không đúng với bản chất, truyền thống của quân đội ta (tạo điều kiện để trung đội trưởng xin lỗi gia đình), đồng thời thông báo cho gia đình đã xử lý kỷ luật đồng chí vi phạm; nêu rõ quan điểm của lãnh đạo, chỉ huy đơn vị là mọi cán bộ, chiến sĩ đều được đối xử bình đẳng, khen thưởng, cử đi học nếu hoàn thành xuất sắc nhiệm vụ, và ngược lại đơn vị không bao che khuyết điểm và cũng không cho phép có các vi phạm, cán bộ, chiến sĩ vi phạm kỷ luật sẽ bị xử lý nghiêm.
- Sinh hoạt đơn vị quán triệt nâng cao nhận thức của bộ đội về các chỉ thị, quy định liên quan đến lỗi phạm trên và vấn đề khiếu nại, tố cáo; xây dựng tinh thần đấu tranh phê bình và tự phê bình; phát huy dân chủ trong đơn vị; công khai minh bạch các chế độ tiêu chuẩn; quan tâm đến đời sống vật chất, tinh thần của bộ đội, tạo bầu không khí dân chủ, đoàn kết, tin cậy lẫn nhau trong đơn vị.
- Phân công cán bộ đại đội kèm cặp, giúp đỡ đồng chí trung đội trưởng đồng thời thường xuyên nắm chắc các mối quan hệ cán binh, quan hệ quân dân của cán bộ, chiến sĩ trong đơn vị để có biện pháp giáo dục, định hướng kịp thời.

Tình huống 74: Trong tiểu đoàn có quân nhân từ trần do tai nạn rủi ro trong lao động đã được giải quyết đủ các chế độ chính sách theo quy định. Gia đình quân nhân lên kiến nghị với tiểu đoàn công nhận quân nhân đó là liệt sĩ.
Gợi ý biện pháp xử lý
- Trao đổi thống nhất trong đảng ủy, chỉ huy tiểu đoàn, nhận định tình hình, thống nhất đề xuất biện pháp giải quyết (đây là vụ việc liên đến chế độ chính sách đã được quy định trong các văn bản của Nhà nước, phải được co quan chức năng có thẩm quyền giải quyết các vấn đề có liên quan đối với gia đình). Tổng hợp báo cáo, xin ý kiến chỉ đọa của cấp trên.
- Phối hợp với cơ quan chức năng của đơn vị (bảo vệ, chính sách…) nắm các văn bản của Nhà nước và quân đội về thực hiện chế độ chính sách đối với quân nhân từ trần, các trường hợp được công nhận là thương binh, liệt sĩ…
- Chỉ huy đơn vị làm việc với gia đình có quân nhân từ trần (mời cơ quan chức năng của trung đoàn dự), chia sẻ với mất mát và nguyện vọng của gia đình, thông báo các chế độ chính sách hiện hành về việc công nhận thương binh, liệt sĩ, báo cáo với gia đình là đơn vị đã giải quyết đúng quy định (lưu ý, đây là vấn đề nhạy cảm do đó phải giải quyết thấu tình, đạt lý; không gây ức chế, hoặc thiếu sự quan tâm của đơn vị, khi làm việc với gia đình phải có nhật ký tiếp nhận và cách giải quyết cần thiết, lập biên bản làm việc để làm tài liệu lưu trữ).
- Nếu gia đình vẫn chưa đồng ý cách giải quyết thì giới thiệu để gia đình gặp sư đoàn (Bộ chỉ huy quân sự tỉnh), Quân khu để được giải quyết.
- Phân công cán bộ thường xuyên quan tâm, động viên; bảo đảm nơi ăn, nghỉ, sinh hoạt thuận lợi, hướng dẫn một số quân nhân (đồng hương đồng đội của tử sĩ) gần gũi chia sẻ, động viên gia đình.
- Sinh hoạt giáo dục, quán triệt các nội dung về chế độ chính sách đang thực hiện để cán bộ, chiến sĩ nắm và thực hiện.
- Báo cáo kết quả giải quyết về cấp trên.

Tình huống 75: Đơn vị nắm được thông tin, một số chiến sĩ do nợ hàng quán của dân quá khả năng thanh toán đã có ý định bỏ trốn khỏi đơn vị để “chạy nợ”/
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị, nhận định, đánh giá tình hình đơn vị, xác định số lượng chiến sĩ nợ hàng quán nhiều nhất, ít nhất của đơn vị hiện nay là bao nhiêu? Dự báo một số trường hợp có thể nảy sinh ý định đào ngũ, bỏ ngũ nhằm “chạy nợ”; những hậu quả tiếp theo của sự việc trên có thể xảy ra như: mất an toàn giao thông, trộm cắp…, qua đó trao đổi, thống nhất biện pháp giải quyết và báo cáo cấp trên xin ý kiến chỉ đạo.
- Triển khai các biện pháp quản lý chặt số quân nhân nói trên.
- Yêu cầu các chiến sĩ có nợ nần tự giác báo cáo bằng văn bản số nợ căng tin đơn vị, nợ hàng quán của dân cũng như các khoản nợ khác…, phowng hướng sử dụng nguồn tiền để trả nợ (tiền phụ cấp, tiền thanh toán chế độ xuất ngũ, tiền gia đình hỗ trợ…)
- Cử cán bộ đi nắm số nợ của chiến sĩ ở căng tin đơn vị, các hàng quán của dân, đối chiếu với phần tự khai của chiến sĩ để có biện pháp giải quyết…
- Gặp gỡ số chiến sĩ nói trên, nắm tình hình, gợi mở để chiến sĩ tâm sự, báo cáo số nợ, phương hướng giải quyết và tình hình tư tưởng; động viên chiến sĩ chấp hành nghiêm kỷ luật, nghiêm cấm bỏ trốn khỏi đơn vị, cần có thái độ tích cực hợp tác với chỉ huy đơn vị và gia đình để giải quyết.
- Liên lạc với gia đình để trao đổi thống nhất các biện pháp phối hợp giải quyết; một số trường hợp nợ quá khả năng thanh toán có thể mời gia đình lên cùng với đơn vị để phối hợp giải quyết không để chiến sĩ nảy sinh tư tưởng bỏ trốn khỏi đơn vị để chạy nợ (khi làm việc với gia đình quân nhân cần có văn bản ghi chép chặt chẽ, tránh ý kiến của gia đình sau khi chiến sĩ hoàn thành nghĩa vụ quân sự…)
- Tổ chức sinh hoạt đơn vị quán triệt nhiệm vụ, định hướng tư tưởng cho chiến sĩ sắp hoàn thành nghĩa vụ quân sự; biểu dương các đồng chí tiết kiệm trong chi tiêu giúp đỡ gia đình, người thân; phê bình nhắc nhở các đồng chí nợ quá khả năng thanh toán làm ảnh hưởng đến bản thân, gia đình và đơn vị; giáo dục động viên cán bộ, chiến sĩ đơn vị, nhất là số chiến sĩ sắp hoàn thành nghĩa vụ quân sự nêu cao ý thức chấp hành nghiêm kỷ luật đơn vị, ý thức tiết kiệm trong chi tiêu, tích cực hợp tác chặt chẽ với đơn vị trong thanh toán các chế độ chính sách ra quân…
- Sau khi giải quyết xong, cần tổ chức sinh hoạt rút kinh nghiệm, kiểm điểm làm rõ trách nhiệm những cán bộ thiếu trách nhiệm trong công tác quản lý, giáo dục bộ đội để bộ đội nợ quá khả năng thanh toán.
- Cùng với cơ quan chính trị cấp trên làm việc với địa phương thống nhất các biện pháp phối hợp giải quyết nợ đọng của chiến sĩ với các hàng quán của dân, định hướng, nhắc nhwor một số hàng quán không cho bộ đội vay nợ quá khả năng chi trả.
- Phân công đảng viên, cán bộ giáo dục kèm cặp chiến sĩ thuộc quyền không để tái diễn tình trạng trên.

Đ. NHÓM TÌNH HUỐNG TƯ TƯỞNG NẢY SINH TỪ PHÍA HẬU PHƯƠNG, GIA ĐÌNH VÀ XÃ HỘI (25 TÌNH HUỐNG)

Tình huống 76: Chỉ huy tiểu đoàn phát hiện thấy đồng chí Nguyễn Văn B., y sĩ của tiểu đoàn thời gian gần đây tham gia bán hàng đa cấp và thường xuyên mời chào cán bộ, chiến sĩ đơn vị tham gia mua các sản phẩm của công ty để có cơ hội làm giàu. Một số cán bộ, chiến sĩ trong đơn vị có những phản ứng khác nhau trước việc làm trên của đồng chí B.
Gợi ý biện pháp xử lý
- Trao đổi trong chỉ huy tiểu đoàn, thống nhất biện pháp giải quyết, phân công cán bộ phụ trách.
- Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ đồng chí B., yêu cầu báo cáo sự việc đồng chí đã tham gia chào mời mua hàng đa cấp tại đơn vị (bao nhiêu cán bộ, chiến sĩ đã tham gia và mua sản phẩm…), hình thức, điều kiện tham gia bán hàng; phân tích cho đồng chí hiểu, không được tổ chức các hoạt động kinh doanh trong đơn vị; yêu cầu đồng chí không tham gia và chấm dứt hoạt động bán hàng đa cấp tại đơn vị.
- Kiểm tra, nắm lại tình hình đơn vị. Trường hợp đơn vị đã có cán bộ, chiến sĩ tham gia bán hàng đa cấp và mua các sản phẩm, phải phối hợp với cơ quan cấp trên và công ty bán hàng đa cấp để giải quyết.
- Tổ chức sinh hoạt đơn vị, giáo dục, định hướng cho cán bộ, chiến sĩ về yêu cầu nhiệm vụ huấn luyện, sẵn sàng chiến đấu; có nhận thức đúng về mặt trái của hình thức kinh doanh đa cấp, những hoạt động lợi dụng uy tín của quân đội và các đồng chí cán bộ để chào bán các sản phẩm và dụ dỗ người tham gia vào mạng lưới để hưởng hoa hồng; nhắc nhở cán bộ, chiến sĩ đơn vị không tham gia vào mạng lưới này.
- Căn cứ vào tình hình thực tiễn, tiến hành kiểm điểm, rút kinh nghiệm đối với đồng chí B. vì đã tùy tiện tham gia và chào mời cán bộ, chiến sĩ đơn vị bán hàng đa cấp.
- Báo cáo kết quả xử lý sự việc lên cấp trên.

Tình huống 77: Đồng chí B., trung đội trưởng mới ra trường được một năm, công tác ở đơn vị xa gia đình, có nguyện vọng xin chuyển vùng công tác nhưng cấp trên chưa đồng ý vì chưa đủ thời gian công tác 5 năm đã nảy sinh tư tưởng buồn chán, hiệu quản công việc thấp.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đại đội, thống nhất biện pháp giải quyết, phân công cán bộ phụ trách giải quyết tư tưởng.
- Gặp gỡ đồng chí B. nắm điều kiện hoàn cảnh gia đình, tâm tự, nguyện vọng, phân tích để đồng chí có nhận thức đúng về yêu cầu nhiệm vụ và quy định để xét chuyển vùng; giáo dục, động viên, định hướng để đồng chí xác định rõ lập trường tư tưởng, an tâm công tác, sẵn sàng nhận và hoàn thành mọi nhiệm vụ được gia, không nên nảy sinh tư tưởng buồn chán trong công việc.
- Trường hợp hoàn cảnh đồng chí B. là đặc biệt khó khăn, phải cử cán bộ xác minh, báo cáp cấp trên để giải quyết (không chờ phải đủ 5 năm).
- Tổ chức sinh hoạt phổ biến, quán triệt các chủ trương, chính sách về công tác cán bộ, rút kinh nghiệm chung trong đội ngũ cán bộ của đơn vị về quan điểm, lập trường, tư tưởng, trách nhiệm trong thực hiện nhiệm vụ.
- Phân công cán bộ đại đội kèm cặp, theo dõi, giúp đỡ, quan tâm thăm hỏi gia đình và tạo điều kiện giúp đỡ đồng chí B. thực hiện tốt nhiệm vụ.
- Tổng hợp kết quả nắm, giải quyết tư tưởng của cán bộ báo cáo cấp trên theo quy định.

Tình huống 78: Chính trị viên đại đội được chiến sĩ bảo vệ báo cáo: Chiến sĩ A. có người yêu nói lời chia tay, mặc dù đã cố gắng thuyết phục nhiều lần nhưng “cô ấy” vẫn quyết định chia tay với lời lẽ chế giễu: “Anh đừng bận tâm về em nữa, lính như anh lấy gì nuôi em, em đã có “nửa” của mình rối”; do vậy chiến sĩ A. tỏ ra buồn chán, trầm tư và thường có những phát ngôn tiêu cực và bế tắc trong cuộc sống.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị, nhận định, đánh giá tính chất, mức độ ảnh hưởng của sự việc, nếu giải quyết không khéo có thể chiến sĩ sẽ suy nghĩ bế tắc, tiêu cực, đào ngũ, bro ngũ thậm chí tự tử, tự sát…; trao đổi, thống nhất biện pháp giải quyết, phân công cán bộ phụ trách.
- Gặp gỡ chiến sĩ A. để động viên, định hướng tư tưởng tập trung vào một số vấn đề như:
+ Bằng tình cảm, sự gần gũi chân tình để gợi mở chiến sĩ bộc bạch hết suy nghĩ và hành động của mình.
+ Động viên chiến sĩ hiểu thêm về ý nghĩa của tình yêu đích thực, tình yêu phải xuất phát từ hai phía và trong xã hội các lứa đôi từ khi yêu nhau cho đến khi kết duyên là cả một quá trình tìm hiểu lâu dài và kỹ lưỡng, quá trình đó có thể có những điểm không hợp nhau dẫn đến chia tay nhau là chuyện bình thường.
+ Việc cô gái có những lời nói có tính chất chế giễu, chứng tỏ cô gái đó không có sự hiểu biết, cảm thông, chia sẻ với yêu cầu, nhiệm vụ của người chiến sĩ…
+ Động viên chiến sĩ không nên suy nghĩ tiêu cực, bế tắc, trước mắt là phải hoàn thành nghĩa vụ quân sự, vững vàng về bản lĩnh người thanh niên, người quân nhân cách mạng, một người thanh niên thông minh, khỏe mạnh, có hoài bão, ước mơ, lại được rèn luyện trong quân đội, có tình yêu trong sáng nhất định đồng chí sẽ tìm được hạnh phúc đích thực.
- Phối hợp với gia đình chiến sĩ, nếu cần thiết có thể cử cán bộ về gặp gia đình trao đổi, cung cấp về tình hình tư tưởng của chiến sĩ, hoặc thông tin cho gia đình biết để phối hợp làm tốt công tác giáo dục, động viên, quản lý tư tưởng của chiến sĩ.
- Phát huy vai trò của các tổ chức quần chúng, hội đồng quân nhân, tổ tư vấn tâm lý trong việc giáo dục, động viên, tư vấn kỹ năng giải quyết các vấn đề trong cuộc sống…, đưa chiến sĩ vào các hoạt động chung của đơn vị như văn hóa văn nghệ, thể dục thể thao…
- Phân công cán bộ và chiến sĩ bảo vệ của đơn vị theo dõi nắm tình hình tư tưởng của chiến sĩ A., để có các biện pháp giáo dục và xử lý kịp thời.
- Báo cáo kết quả giải quyết sự việc lên cấp trên.

Tình huống 79: Khi đơn vị nắm được thông tin, chiến sĩ thuộc quyền là người dân tộc thiểu số sau khi có người yêu (cùng quê) lên thăm đã có ý định đào ngũ để cùng với người yêu bỏ đi làm ăn xa, không về địa phương.
Gợi ý biện pháp xử lý
- Chính trị viên và người chỉ huy trao đổi tình hình, xác định nguyên nhân nảy sinh ý định đào ngũ của chiến sĩ, thống nhất cách xử lý, phân công cán bộ theo dõi, kèm cặp giúp đỡ, giáo dục động viên và ngăn chặn không để chiến sĩ đào ngũ.
- Chính trị viên gặp gỡ chiến sĩ nắm tình hình tư tưởng, tâm tư nguyện vọng của chiến sĩ; phân tích cho chiến sĩ hiểu rõ tác hại của việc đào ngũ đối với tương lai của bản thân, gia đình, địa phương, đơn vị; xác định trách nhiệm xây dựng đơn vị, thực hiện nghĩa vụ quân sự…
- Phân công cán bộ và chiến sĩ bảo vệ (tốt nhất là người cùng quê, cùng dân tộc) của đơn vị thường xuyên theo dõi, nắm chắc các biểu hiện về tư tưởng, nhất là trong giờ nghỉ, ngày nghỉ, kịp thời phản ảnh, báo cáo; tạo điều kiện để chiến sĩ thực hiện và hoàn thành tốt nhiệm vụ.
- Chỉ huy đơn vị tìm cách liên lạc và trao đổi với người yêu chiến sĩ, giải thích rõ hậu quả của việc đào ngũ sẽ ảnh hưởng rất lớn đến tương lai của hai người, gia đình và con cháu sẽ thấy thất vọng khi có một người con, người chồng, người cha đào ngũ.
- Phối hợp cùng gia đình chiến sĩ và người yêu động viên chiến sĩ an tâm tư tưởng thực hiện tốt nhiệm vụ.
- Phát huy vai trò của tổ chức quần chúng, tổ tư vấn tâm lý pháp luật, bạn bè, đồng hương giúp đỡ tạo điều kiện thuận lợi để chiến sĩ yên tâm học tập, công tác.
- Có thể tổ chức tọa đàm, diễn đàn chủ đề: “Trách nhiệm của người chiến sĩ Quân đội nhân dân Việt Nam với Tổ quốc”, trong tọa đàm đi sâu vào giáo dục truyền thống văn hóa của dân tộc, quân đội, quê hương, tính kỷ luật, tự giác, nghiêm minh.
- Thường xuyên làm tốt công tác giáo dục, đảm bảo tốt đời sống văn hóa tinh thần cho bộ đội.
- Báo cáo kết quả giải quyết sự việc lên cấp trên.

Tình huống 80: Một số chiến sĩ trước khi nhập ngũ vào đơn vị đã có người yêu, sau 3 tháng công tác chiến sĩ đó báo cáo với chỉ huy đơn vị xin phép về cưới vợ để có người giúp đỡ cho gia đình trong thời gian đồng chí đó làm nghĩa vụ quân sự.
Gợi ý biện pháp xử lý
- Chính trị viên gặp gỡ chiến sĩ để nắm tâm tư, nguyện vọng, kiểm tra thông tin xem có đúng sự thật hay không? Nếu đúng sự thật, động viên chiến sĩ khắc phục khó khăn, xác định tốt nhiệm vụ, an tâm công tác; giáo dục, giải thích cho chiến sĩ hiểu rõ quy định đối với hạ sĩ quan, chiến sĩ trong thời gian tại ngũ không được kết hôn (nếu chiến sĩ chưa đủ 20 tuổi mà kết hôn còn vi phạm Điều 8 Luật Hôn nhân và gia đình năm 2014 (nam từ đủ 20 tuổi, nữu từ đủ 18 tuổi mới được kết hôn); động viên, chia sẻ với chiến sĩ nguyện vọng cưới vợ để có người giúp đỡ gia đình là chính đáng, song không nhất thiết phải cưới thì mới giúp đỡ được gia đình; đồng thời đây là thời gia thử thách tình yêu thêm tốt đẹp, hạnh phúc thêm bền vững…, chiến sĩ tuổi còn ít, đang thực hiện nghĩa vụ quân sự, sau về cưới vợ cũng chưa muộn để chiến sĩ an tâm tư tưởng…
- Cử cán bộ tìm hiểu rõ hoàn cảnh gia đình chiến sĩ từ đó có biện pháp giải quyết thỏa đáng hơn.
- Điện thoại hoặc trực tiếp gặp gỡ, trao đổi với gia đình và người yêu chiến sĩ về yêu cầu, nhiệm vụ của đơn vị, nhiệm vụ của quân nhân; quy định đối với hạ sĩ quan, chiến sĩ trong thời gian tại ngũ không được kết hôn; phân tích chỉ rõ điều kiện thuận lợi, khó khăn đề nghị gia đình phối hợp với đơn vị để động viên chiến sĩ yên tâm công tác.
- Nếu gia đình quân nhân có hoàn cảnh khó khăn, đơn vị đề nghị với cấp ủy, chính quyền, đoàn thể địa phương có biện pháp giúp đỡ gia đình trong thời gian chiến sĩ đó thực hiện nghĩa vụ quân sụ. Riêng đơn vị nên có biện pháp giúp đỡ về công sức, vật chất, tinh thần để gia đình đồng chí đó khắc phục khó khăn, động viên con em yên tâm công tác.
- Phát huy vai trò của các tổ chức trong đơn vị (hội đồng quân nhân, đoàn thanh niên, tổ tư vấn pháp lý…) động viên, tư vấn cho chiến sĩ kiến thức về hôn nhân gia đình.
- Phân công cán bộ, chiến sĩ đơn vị nắm diễn biến tư tưởng, quan tâm, giúp đỡ, động viên chiến sĩ đó khắc phục khó khăn, an tâm công tác, hoàn thành nghĩa vụ quân sự.

Tình huống 81: Đơn vị có đồng chí A. là quân nhân chuyên nghiệp có quan hệ tình yêu đôi lứa chân chính nhưng gia đình phản ảnh vì người yêu đồng chí A. không có việc làm ổn định, gia đình người yêu đồng chí A. không “môn đăng hậu đối” do vậy đã có biểu hiện buồn chán, hiệu quả công việc thấp.
Gợi ý biện pháp xử lý
- Trao đổi trong chỉ huy đơn vị, đánh giá tình hình tư tưởng của quân nhân, những vi phạm có thể nảy sinh, thống nhất biện pháp giải quyết, phân công cán bộ phụ trách.
- Gặp gỡ đồng chí A. trao đổi, nắm tình hình khéo léo gợi mở để đồng chí tâm sự về tình yêu và nguyện vọng của mình; phân tích, chia sẻ, tôn trọng tình yêu đích thực, quyền tự do yêu đương chân chính và tiến tới hôn nhân của đồng chí; đồng thời động viên đồng chí lắng nghe những lời khuyên của bố mẹ cũng chỉ muốn những điều tốt đẹp nhất cho con em mình…, qua đó đồng chí sẽ có quyết định hợp lý nhất, an tâm thực hiện nhiệm vụ, không vì lý do cá nhân mà làm ảnh hưởng đế nhiệm vụ của đơn vị.
- Có thể cử cán bộ về gặp gia đình hoặc gọi điện để nắm tình hình, trao đổi với gia đình về tình hình tư tưởng và nguyện vọng của quân nhân, phối hợp cùng gia đình để động viên quân nhân có quyết định hợp lý nhất, an tâm thực hiện nhiệm vụ.
- Nếu đồng chí A. quyết tâm đi đến hôn nhân với người yêu thì động viên gia đình tôn trọng quyết định của con em họ, tạo điều kiện thuận lợi để đồng chí đi đến hôn nhân, giúp đỡ đồng chí A. về vật chất, tinh thần để khắc phục khó khăn khi có gia đình riêng.
- Phân công cán bộ thường xuyên gần gũi, tâm sự, động viên đồng chí A., kịp thời nắm phản ảnh, xử lý các vấn đề nảy sinh về tư tưởng, không để xảy ra những tình huống bất ngờ.

Tình huống 82: Trong thời gian chiến sĩ A. đang thực hiện nghĩa vụ quân sự thì bố mẹ ly hôn, chiến sĩ A. có biểu hiện buồn chán.
Gợi ý biện pháp xử lý
- Việc xử lý tình huống này cần căn cứ cụ thể vào mức độ phản ứng của chiến sĩ đối với việc ly hôn của bố mẹ cũng như tính cách của chiến sĩ (là người ngoan ngoãn, hiền lành, sống khép mình; biết quan tâm đến người khác... sẽ có phản ứng khác những đồng chí ham chơi, không trung thực, ích kỷ…). Nếu chiến sĩ là người hiểu biết, có bản lĩnh tốt, buồn nhưng không làm ảnh hưởng đến công tác, học tập thì chỉ cần thường xuyên quan tâm, động viên và hướng cho chiến sĩ tham gia các hoạt động lành mạnh của đơn vị. Nếu việc bố mẹ ly hôn làm chiến sĩ buồn chán, ảnh hưởng đến công tác, học tập thì cần tiến hành tốt các biện pháp tư tưởng.
- Phân công cán bộ gặp gỡ chiến sĩ A. tìm hiểu về nguyên nhân ly hôn, những khó khăn của chiến sĩ A. khi bố mẹ ly hôn, nguyện vọng của chiến sĩ A. và những đề nghị cần đơn vị giúp đỡ. Từ đó chia sẻ, cảm thông với chiến sĩ A.
- Hội ý chỉ huy bàn biện pháp giúp đỡ đồng chí A, như quan tâm gần gũi, động viên tư tưởng, bố trí nhiệm vụ phù hợp (nếu cần thiết). Phân công cán bộ kèm cặp, giúp đỡ, thường xuyên tạo điều kiện để đồng chí A. hoàn thành tốt nhiệm vụ.
- Phối hợp với cơ quan chức năng địa phương để nắm rõ hơn về nguyên nhân việc ly hôn, việc phân chia tài sản có liên quan gì đến quân nhân, thời gia phiên tòa xử lý ly hôn, báo cáo cấp trên giải quyết cho quân nhân đó về dự phiên tòa (nếu cần thiết và có cán bộ đơn vị đưa về).
- Nhắc nhở, định hướng cho cán bộ, chiến sĩ trong đơn vị quan tâm, gần gũi, động viên thương yêu và tạo điều kiện để chiến sĩ A. hoàn thành nhiệm vụ.
- Liên hệ với bố mẹ chiến sĩ A. đề nghị quan tâm và có trách nhiệm chăm lo cho đồng chí A.
- Tổng hợp báo kết quả nắm và giải quyết tư tưởng của chiến sĩ với cấp trên.

Tình huống 83: Trong đại đội có quân nhân tư tưởng không an tâm, buồn phiền vì bố mẹ phân chia tài sản cho các con không công bằng.
Gợi ý biện pháp xử lý
- Hội ý chỉ huy đơn vị thống nhất đánh giá tình hình, phân công cán bộ phụ trách giải quyết tư tưởng. Lưu ý, đây là việc riêng, nhạy cảm của gia đình quân nhân, do đó chủ yêu tác động làm cho quân nhân thuộc quyền hiểu thực chất sự việc, ý kiến đề xuất gia đình “thấu tình, đạt lý”, giữ vững mối quan hệ ruột thịt trong gia đình.
- Gặp quân nhân tìm hiểu, nắm chắc hoàn cảnh gia đình, trước hết là tôn trọng quyết định của bố mẹ; tổ tư vấn tâm lý pháp luật tuyên truyền cho quân nhân nắm chắc Luật Thừa kế, Luật Sở hữa tài sản. Chấp hành nghiêm túc Luật Thừa kế tài sản theo quy định còn quý giá hơn, có tiền cũng không thể mua được; tài sản có thể làm ra nhưng tình cảm gia đình mà mất đi thì rất khó lấy lại được, tình cảm, danh dự là tài sản quý nhất của con người, không bao giờ có thể đánh đổi bằng tiền bạc. Lấy ví dụ, dẫn chứng xác thực để quân nhân nhìn nhận vấn đề, trách mắc phải khuyết điểm nóng vội, duy ý chí, chỉ thấy cái lợi trước mắt, tức thời mà bỏ quên cái lợi lâu dài... quyết định sai lầm từ vấn đề tranh chấp tài sản có thể dẫn đến mất đoàn kết gia đình khiến quân nhân phải hối hận (nếu đơn vị chưa thành lập tổ tư vấn tâm lý, pháp luật thì chính trị viên tiến hành nội dung này).
- Liên hệ, thông báo với gia đình biết về tư tưởng, tình cảm, nguyện vọng của quân nhân trước việc gia đình phân chia tài sản; đề nghị gia đình phối hợp động viên quân nhân hiểu rõ sự việc, yên tâm thực hiện nhiệm vụ.
- Cử cán bộ theo dõi, động viên quân nhân yên tâm tư tưởng, tôn trọng bố mẹ (gia đình), chấp hành nghiêm pháp luật, đề cao trách nhiệm, hoàn thành mọi nhiệm vụ được giao.

Tình huống 84: Trong đại đội có quân nhân A. buồn chán, không yên tâm công tác khi nhận được thông tin gia đình bị thua lỗ trong sản xuất, kinh doanh...
Gợi ý biện pháp xử lý
- Hội ý chỉ huy đơn vị, đánh giá tính chất, mức độ ảnh hưởng của sự việc, thống nhất biện pháp giải quyết.
- Gặp gỡ quân nhân, tìm hiểu thêm hoàn cảnh gia đình, nguyên nhân dẫn đến những thua lỗ trong sản xuất kinh doanh của gia đình; giáo dục, động viên quân nhân hiểu rõ trong kinh doanh không tránh khỏi rủi ro, thua lỗ và chính sau sự thua lỗ gia đình sẽ rút ra được kinh nghiệm cho sự thành công, cách động viên tốt nhất của quân nhân đối với gia đình lúc này là phấn đấu hoàn thành tốt nghĩa vụ quân sự để gia đình yên tâm khôi phục lại sản xuất, kinh doanh, việc buồn chán tức thời là không tránh khỏi, nhưng nếu hành động tiêu cực thì càng làm cho gia đình càng khó khăn hơn.
- Có thể gián tiếp hoặc trực tiếp trao đổi chia sẻ cùng gia đình và thông báo về việc quân nhân (con của gia đình) đang bị phân tán tư tưởng, lo lắng việc gia đình; đề nghị gia đình phối hợp đơn vị động viên quân nhân yên tâm thực hiện nhiệm vụ của đơn vị.
- Phối hợp với địa phương thăm hỏi, động viên gia đình, giúp đỡ về vật chất và tinh thần để gia đình khắc phục khó khăn trước mắt.
- Phân công cán bộ, chiến sĩ, đồng hương... thường xuyên gần gũi, chia sẻ, động viên giúp quân nhân A. ổn định tư tưởng, tránh suy nghĩ tiêu cực ảnh hưởng đến gia đình và đơn vị.
- Phát huy vai trò của các tổ chức quần chúng, hội đồng quân nhân, tổ tư vấn tâm lý, pháp luật trong việc giáo dục, động viên tư tưởng, đưa quân nhân vào các hoạt động chung của đơn vị.

Tình huống 85: Trong đơn vị có một số quân nhân có biểu hiện buồn chán khi có bố (mẹ) ốm điều trị ở bệnh viện nhưng đơn vị chưa giải quyết tranh thủ vì phải trực chiến sẵn sàng chiến đấu.
Gợi ý biện pháp xử lý
- Thay mặt chỉ huy đơn vị gặp gỡ những quân nhân có bố(mẹ) điều trị ở bệnh viện, nắm thêm về tình hình gia đình, tâm tư, nguyện vọng, chia sẻ, đồng cảm về điều kiện hoàn cảnh của gia đình từng đồng chí, động viên các quân nhân hiểu rõ yêu cầu của nhiệm vụ trực sẵn sàng chiến đấu.
- Trao đổi, thống nhất trong chỉ huy đơn vị về tình hình gia đình của các quân nhân và bàn biện pháp giải quyết.
+ Báo cáo, đề xuất và xin ý kiến chỉ đạo của chỉ huy tiểu đoàn. Nếu trường hợp bệnh viện ở gần nơi đơn vị đóng quân thì đề nghị cấp trên cho phép cử cán bộ đi cùng quân nhân có bố mẹ ốm đau ra thăm hỏi, động viên tặng quà gia đình. Nếu bệnh viện ở xa thì gọi điện về người thân trong gia đình để thăm hỏi và động viên.
+ Trong trường hợp bố (mẹ) chiến sĩ bệnh nặng, thời gian sống chỉ tính bằng ngày, giờ thì báo cáo cấp trên cử người thay thế chiến sĩ đó trực sẵn sàng chiến đấu, giải quyết cho chiến sĩ về thăm gia đình (trước khi đi cần quán triệt cụ thể, tỉ mỉ để chiến sĩ giữ nghiêm kỷ luật bảo đảm an toàn, gửi lời thăm hỏi gia đình).
+ Căn cứ vào tình trạng, mức độ bệnh tật của bố (mẹ) quân nhân để sinh hoạt thông báo với cán bộ, chiến sĩ trong đơn vị được biết để gần gũi, động viên, hoặc có thể quyên góp ủng hộ về vật chất...
- Phân công cán bộ trực tiếp giúp đỡ; hướng dẫn cán bộ cấp dưới và các quân nhân trong đơn vị thường xuyên gần gũi thăm hỏi, động viên, chia sẻ giúp đỡ những quân nhân có bố (mẹ) đang nằm viện yên tâm tư tưởng, xác định tốt trách nhiệm và hoàn thành tốt nhiệm vụ.
- Thường xuyên đánh giá đúng kết quả thực hiện nhiệm vụ của các quân nhân có gia đình khó khăn, kịp thời động viên, biểu dương, nhân rộng trong toàn đơn vị những quân nhân hoàn thành xuất sắc nhiệm vụ.
- Sau thời gian trực chiến, căn cứ tình hình nhiệm vụ của đơn vị để đề nghị cấp trên giải quyết tranh thủ, hoặc chế độ nghỉ phép về thăm gia đình cho một số quân nhân có bố(mẹ) đang nằm viện.
- Phát huy vai trò của các tổ chức quần chúng, hội đồng quân nhân, vai trò làm chủ của chiến sĩ làm tốt công tác giáo dục, định hướng và quản lý chặt chẽ tình hình tư tưởng, chống đào ngũ, bỏ ngũ, vắng mặt trái phép, vi phạm kỷ luật.

Tình huống 86: Trong đơn vị có một chiến sĩ sau khi nghỉ phép lên đơn vị có biểu hiện buồn chán, trầm tử, ít tiếp xúc với mọi người, chất lượng hoàn thành nhiệm vụ thấp. Qua tìm hiểu được biết chiến sĩ nghe dư luận là mẹ đã ngoại tình.
Gợi ý biện pháp xử lý
- Trao đổi thống nhất trong chỉ huy đơn vị, phân công cán bộ phụ trách giải quyết tư tưởng; có các biện pháp quản lý thông tin cá nhân, tránh việc để thông tin gia đình chiến sĩ trở thành vấn đề đàm tiếu trong đơn vị.
- Thay mặt chỉ huy đơn vị gặp gỡ quân nhân có biểu hiện buồn chán, để nắm thêm về hoàn cảnh gia đình và tâm tư của quân nhân. Thông qua tâm sự của quân nhân để có hướng giải quyết phù hợp.
+ Nội dung trao đổi, tâm tư với quân nhân cần phải chuẩn bị kỹ, phù hợp với tính cách và nhận thức, hiểu biết của quân nhân. Lúc này chỉ huy đơn vị là một trong những chỗ dựa về tinh thần và có khả năng tư vấn tốt nhất cho quân nhân. Phân tích để cho quân nhân nhận thức rõ trách nhiệm của người con đã đến tuổi trưởng thành, là một trong những người tin cậy, gần gũi, được mẹ thương yêu, quý trọng… Do đó cần có trách nhiệm trực tiếp trao đổi tâm sự với mẹ để nắm thực chất về sự việc như dư luận đưa tin và đưa ra những mong muốn, góp ý của người con đối với mẹ của mình.
+ Về phương pháp tiếp xúc, trao đổi phải thực sự chân tình, thể hiện tình cảm như người anh, người chị, người bạn để dẫn dắt làm cho chiến sĩ hiểu rõ việc chỉ huy đơn vị muốn biết “việc riêng của gia đình” là thể hiện tình cảm, trách nhiệm của chỉ huy đơn vị đối với quân nhân; tránh dùng những lời nói dễ tác động làm nảy sinh mặc cảm, tự ti, xấu hổ của quân nhân về việc của gia đình mình.
- Gặp gỡ trực tiếp (điều kiện cho phép) hoặc qua điện thoại khéo léo trao đổi với mẹ của quân nhân để phản ánh về tư tưởng và chất lượng hoàn thành nhiệm vụ của con mình và đề nghị gia đình phối hợp với đơn vị động viên quân nhân yên tâm tư tưởng, hoàn thành tốt nhiệm vụ được giao.
- Phân công cán bộ, thường xuyên quan tâm gần gũi, động viên quân nhân có sự việc trên; nắm thêm tình hình, để tư vấn cho quân nhân.
- Thông qua kết quả nắm tình hình và căn cứ vào điều kiện cụ thể của gia đình, để có thể phối hợp với địa phương giúp đỡ gia đình ổn định cuộc sống.

Tình huống 87: Đồng chí A. là sĩ quan trong đơn vị có hoàn cảnh gia đình khó khăn: vợ làm công nhân ở một công ty may công việc không ổn định, có hai con bị bệnh nhiểm nghèo hay ốm đau phải đi viện tốn nhiều tiền của. Đồng chí A. có biểu hiện buồn chán, chất lượng công việc hiệu quả thấp, ảnh hưởng tới công việc chung của đơn vị.
Gợi ý biện pháp xử lý
- Chỉ huy đơn vị tiến hành gặp gỡ động viên làm công tác tư tưởng, chia sẻ hoàn cảnh gia đình và nắm tâm tư nguyện vọng của đồng chí A.
- Cử cán bộ về gia đình thăm hỏi, tặng quà gia đình, các con đồng chí A.
- Báo cáo chỉ huy cấp trên về hoàn cảnh gia đình đồng chí A., xin phép vận động quyên góp ủng hộ trong đội ngũ cán bộ ở đơn vị giúp đỡ gia đình đồng chí A.; báo cáo cấp trên có thẩm quyền xem xét có thể nhận vợ đồng chí A. vào làm công nhân viên hợp đồng ở một đơn vị nào đó gần nhà.
- Thường xuyên tạo điều kiện cho đồng chí sĩ quan được đi tranh thủ đúng quy định để có điều kiện giúp đỡ vợ con và gia đình lúc khó khăn; giúp đồng chí trong công việc, động viên đồng chí A. khắc phục khó khăn về gia đình, tiếp tục thực hiện và hoàn thành tốt các nhiệm vụ được phân công.

Tình huống 88: Đồng chí B. là chiến sĩ mới có biểu hiện trầm tư, ít hòa đồng với cán bộ, chiến sĩ trong đơn vị; qua tìm hiểu, một số chiến sĩ cùng tiểu đội cho biết, đồng chí B. thường sử dụng điện thoại để lên facebook chia sẻ về những khó khăn vất vả trong thực hiện nhiệm vụ và đã nhận được nhiều thông tin bình luận cùng những lời khuyên nhủ khác nhau liên quan đến việc thực hiện nghĩa vụ quân sự.
Gợi ý biện pháp xử lý
- Hội ý chỉ huy đơn vị để thống nhất biện pháp giải quyết, phân công cán bộ phụ trách.
- Kiểm tra nắm lại số chiến sĩ còn sử dụng điện thoại không đúng quy định trong đơn vị, xác định nguyên nhân và trách nhiệm của cán bộ quản lý trong việc thực hiện quy định về việc hạ sĩ quan, chiến sĩ không dược sử dụng điện thoại di động trong thời gian tại ngũ.
- Tiến hành gặp gỡ đồng chí B. để nắm tình hình cụ thể. Phân tích để đồng chí thấy được việc chiến sĩ tự ý sử dụng điện thoại di động trong thời gian làm nghĩa vụ quân sự là sai với quy định của đơn vị, lên facebook để tâm sự về nhũng vấn đề trong thực hiện nhiệm vụ quân sự là vi phạm quy định về công tác bảo mật quân sự; mặt khác facebook chính là diễn đàn tự do, các ý kiến bình luận của nhiều đối tượng khác nhau, trong đó có nhiều ý kiến tiêu cực, thiếu tính chất xây dựng sẽ tác động xấu đến nhận thức tư tưởng của chiến sĩ; động viên chiến sĩ cần nghiêm túc rút kinh nghiệm, chấm dứt ngay việc làm trên; động viên chiến sĩ B. gửi điện thoại về nhà hoặc gửi cho chỉ huy đơn vị giữ hộ; tin tưởng vào công tác quản lý, giáo dục, rèn luyện của cán bộ đơn vị.
- Chỉ đạo đơn vị tổ chức cho các chiến sĩ vi phạm quy định về sử dụng điện thoại di động viết tường trình, kiểm điểm; tiến hành sinh hoạt đơn vị kiểm điểm theo phân cấp (căn cứ vào tính chất, mức độ để nhắc nhở, giải quyết phù hợp); đồng thời yêu cầu mọi quân nhân trong đơn vị rút kinh nghiệm, tự giác chấp hành nghiêm quy định của đơn vị.
- Tổ chức tốt các hoạt động vui chơi của đơn vị, nhất là vào giờ nghỉ, ngày nghỉ để cuốn hút bộ đội tự giác tham gia, chủ động phòng ngừa và miễn dịch các tệ nạn xã hội.
- Nội bộ cấp ủy, chỉ huy đơn vị sinh hoạt rút kinh nghiệm, tăng cường công tác bảo vệ chính trị nội bộ; phân công đảng viên giúp đỡ, dìu dắt chiến sĩ thuộc quyền tiến bộ.

Tình huống 89: Chiến sĩ C. trong đơn vị có ông ngoại qua đời trong lúc đôn vị đang làm nhiệm vụ trực sẵn sàng chiến đấu, quân nhân báo cáo xin phép đơn vị về để chịu tang. Đơn vị chưa giải quyết thì quân nhân này có ý định đào ngũ.
Gợi ý biện pháp xử lý
- Hội ý chỉ huy đơn vị, trao đổi thống nhất biện pháp giải quyết; báo cáp cấp trên xin ý kiến chỉ đạo.
- Phân công cán bộ gặp gỡ, động viên, chia buồn với quân nhân và gửi lời thăm hỏi gia đình; nếu đơn vị ở xa, yêu cầu nhiệm vụ trực sẵn sàng chiến đấu cao, không có ai thay thế thì giáo dục cho quân nhân hiểu rõ ý nghĩa, yêu cầu nhiệm vụ sẵn sàng chiến đấu và trách nhiệm của mỗi quân nhân; nguyện vọng được về chịu tang ông ngoại là chính đáng, nhưng do điều kiện đơn vị ở xa, vị trí của chiến sĩ C. không có người thay thế, nên không thể về chịu tang ông ngoại được; động viên quân nhân xác định rõ trách nhiệm, yên tâm thực hiện nhiệm vụ, nếu đào ngũ chỉ làm cho gia đình đã buồn lại buồn thêm.
- Cử cán bộ thường xuyên gần gũi, theo dõi, quản lý chặt chẽ mọi hoạt động của quân nhân, có biện pháp quản lý chống đào ngũ, bỏ ngũ, vắng mặt trái phép.
- Giao nhiệm vụ cho một số đồng chí (nhất là đồng hương, bạn thân, chiến sĩ bảo vệ) thường xuyên gần gũi tâm sự, chia sẻ, động viên cùng yên tâm tham gia công tác thực hiện tốt nhiệm vụ, kịp thời nắm và phản ảnh tình hình tư tưởng.
- Liên hệ, gặp gỡ, chia sẻ cùng gia đình quân nhân, giải thích để gia đình hiểu và cùng đơn vị động viên quan nhân yên tâm công tác.
- Kết thúc đợt trực sẵn sàng chiến đấu, tùy vào điều kiện cụ thể, báo cáo cấp trên giải quyết cho đồng chí C. về thăm gia đình.

Tình huống 90: Đơn vị có một số chiến sĩ theo đạo Thiên Chúa. Gia đình cùng các quân nhân trên đã lên gặp gỡ chỉ huy đơn vị để đề đạt nguyện vọng xin phép đi tham gia lễ ở nhà thờ vào sáng chủ nhật hằng tuần.
Gợi ý biện pháp xử lý
- Trao đổi trong chỉ huy đơn vị thống nhất biện pháp xử lý.
- Phân công cán bộ gặp gỡ gia đình và các chiến sĩ theo đạo Thiên Chúa, phân tích làm rõ nhiệm vụ của các quân nhân thực hiện nghĩa vụ quân sự; phổ biến điều lệnh, quy định của quân đội và đơn vị, nhất là quy định “đối với quân nhân có đạo, trong thời gian phục vụ tại ngũ, mọi sinh hoạt phải chấp hành nghiêm điều lệnh, quy định của quân đội…” Lưu ý, đây là vấn đề nhạy cảm, dễ tác động đến tư tưởng, tình cảm, tâm linh của chiến sĩ theo đạo, do đó phải thận trọng, giải thích hợp tình, hợp lý, làm cho gia đình và chiến sĩ hiểu mỗi quân nhân theo đạo kính Chúa trước hết là phải làm tròn bổn phận của người công dân đối với Tổ quốc “Chúa ở trong tâm”, những chiến sĩ theo đạo nhập ngũ trước đây đều chấp hành nghiêm quy định này…
- Tổ chức sinh hoạt giáo dục chung trong đơn vị, quán triệt các quan điểm, chủ trương, chính sách của Đảng, Nhà nước ta về tôn trọng tự do tín ngưỡng tôn giáo; yêu cầu nhiệm vụ của đơn vị, các quy định của quân đội đối với các chiến sĩ theo đạo, động viên các chiến sĩ theo đạo phát huy truyền thống quê hương “kính Chúa, yêu nước”, sống “tốt đời đẹp đạo”; xây dựng tinh thần đoàn kết trong đơn vị; không để xảy ra phân biệt, kỳ thị giữa chiến sĩ theo đạo với những chiến sĩ khác.
- Duy trì chặt chẽ nề nếp chế độ ngày, tuần; đẩy mạnh các hoạt động thi đua, kịp thời đưa tin người tốt, việc tốt; chú trọng tổ chức các hoạt động văn hóa tinh thần trong các ngày nghỉ, giờ nghỉ để thu hút mọi quân nhân tham gia; xây dựng và củng cố môi trường văn hóa tốt đẹp, lành mạnh trong đơn vị.
- Phát huy hiệu quả hoạt động của chiến sĩ bảo vệ, chiến sĩ dân vận; vai trò của đảng viên, tiểu (khẩu) đội trưởng, tổ 3 người, thường xuyên gần gũi tâm tư tình cảm, giúp đỡ các chiến sĩ an tâm tư tưởng, chấp hành nghiêm quy định của đơn vị.
- Tổng hợp báo cáo kết quả giải quyết tư tưởng của bộ đội lên cấp trên.

Tình huống 91: Sau hai ngày nghỉ cuối tuần có ba quân nhân chuyên nghiệp ở đại đội viết đơn xin xuất ngũ cùng với lý do: điều kiện hoàn cảnh gia đình khó khăn, không có thời gian giúp đỡ gia đình.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình, sơ bộ xác định nguyên nhân, bàn biện pháp giải quyết.
- Tiến hành xác minh lý do ba quân nhân xin xuất ngũ thông qua các biện pháp:
+ Gặp gỡ trực tiếp từng đồng chí, động viên báo cáo lý do xin ra quân.
+ Liên hệ trao đổi với gia đình, địa phương.
+ Thông qua cán bộ chỉ huy trực tiếp để nắm tình hình.
+ Nắm qua dư luận của cán bộ, quân nhân chuyên nghiệp, chiến sĩ trong đơn vị phản ảnh.
- Cần nhận định các tình huống có thể xảy ra để có các biện pháp xử lý phù hợp như:
+ Do điều kiện hoàn cảnh gia đình có khó khăn thực sự.
+ Có khó khăn nhưng chưa đến mức phải xin xuất ngũ nhưng do sự tác động, lôi kéo của bạn bè, người thân…
+ Tham gia vào các tệ nạn xã hội (lô đề, cá độ bóng đá, cờ bạc) không có tiền trả nợ nên lo lắng, xin xuất ngũ.
+ Vi phạm pháp luật Nhà nước, kỷ luật quân đội nhưng đơn vị chưa phát hiện…
- Khi đã có kết quả xác minh nguyên nhân của ba quân nhân xin xuất ngũ, báo cáo cấp trên về tính chất, nguyên nhân và đề xuất các biện pháp giải quyết phù hợp.
- Tổ chức sinh hoạt đơn vị, tập trung giáo dục nhiệm vụ phục vụ quân đội lâu dài của sĩ quan, quân nhân chuyên nghiệp; bồi dưỡng những kiến thức kỹ năng vượt qua những khó khăn trong công việc và cuộc sống gia đình…
- Quản lý nắm chắc tình hình tư tưởng, các mối quan hệ, điều kiện hoàn cảnh gia đình; quan tâm chăm lo đến đời sống vật chất, tinh thần của sĩ quan, quân nhân chuyên nghiệp thuộc quyền.
- Phân công cán bộ phụ trách theo dõi kèm cặp giúp đỡ ba quân nhân trong quá trình thực hiện nhiệm vụ.
- Tổng hợp kết quả xử lý báo cáo với cấp trên.

Tình huống 92: Trong đơn vị có một chiến sĩ nhập ngũ năm thứ hai, từ trước đến nay luôn là cá nhân tiêu biểu. Sau đợt nghỉ phép lên đơn vị có biểu hiện trầm tư, lo lắng, ngại tiếp xúc với đồng đội, chất lượng công việc giảm sút, chấp hành chế độ không nghiêm, có một số lần tự ý bỏ đơn vị về nhà, đơn vị phải cử cán bộ về kết hợp với gia đình vận động mới lên đơn vị, song mức độ chuyển biến chậm và nay đã viết đơn xin ra quân trước hạn.
Gợi ý biện pháp xử lý
- Phân công cán bộ gặp gỡ, tâm sự chân tình, cởi mở, để nắm bắt những tư tưởng nảy sinh và nguyên nhân; gần gũi, động viên, thuyết phục quân nhân.
- Trao đổi thống nhất trong cấp ủy, chỉ huy đơn vị về biện pháp xử lý và phân công cán bộ phụ trách.
- Thông qua gặp gỡ riêng và sinh hoạt đơn vị để giáo dục cho quân nhân hiểu rõ về Luật Nghĩa vụ quân sự, những trường hợp được xét xuất ngũ trước hạn.
- Chỉ đạo cán bộ đại đội, trung đội, tiểu đội kèm cặp, giúp đỡ quân nhân có biểu hiện vi phạm, nghiêm túc sửa chữa khuyết điểm, tiếp tục phấn đấu vươn lên. Đặc biệt là phải giúp đồng chí đó giải quyết trước những khó khăn, bức xúc trong cuộc sống.
- Tiếp tục giao nhiệm vụ phù hợp với khả năng sở trường của quân nhân để thử thách và theo dõi việc phấn đấu của quân nhân..
- Phát huy vai trò chiến sĩ bảo vệ trong theo dõi nắm tình hình; coi trọng động viên các lực lượng khác (đồng hương, cán bộ đoàn…) cùng tham gia giáo dục, giúp đỡ quân nhân đó tiến bộ.
- Phối hợp với gia đình quân nhân và địa phương động viên tư tưởng để quân nhân thực hiện tốt nhiệm vụ trong thời gian tại ngũ còn lại.
- Tổ chức tốt các hoạt động văn hóa văn nghệ, thể dục thể thao, đưa quân nhân vào các hoạt động chung của đơn vị.

Tình huống 93: Trong đại đội có chiến sĩ tự sát (bằng súng AK) trong khi thực hiện nhiệm vụ canh gác. Một số chiến sĩ trong đơn vị có biểu hiện hoang mang, lo lắng trước sự việc trên
Gợi ý biện pháp xử lý
- Nhanh chóng tổ chức đưa chiến sĩ tự sát đi cấp cứu kịp thời (nếu còn sống).
- Báo cáo cấp trên xin ý kiến chỉ đạo.
- Trao đổi nhanh trong chỉ huy, xác định những việc cần làm ngay, phân công cán bộ phụ trách tổ chức thực hiện.
- Chủ động phối hợp với các cơ quan chức năng cấp trên kiểm tra hiện trường, thu thập thông tin giải quyết vụ việc.
- Trường hợp quân nhân đã tử vong tiến hành các biện pháp xử lý như sau:
+ Phối hợp với chỉ huy và cơ quan cấp trên tiến hành lập biên bản vụ việc và biên bản kiểm kê di vật của quân nhân theo đúng quy định; chú ý kiểm tra kỹ các vật lưu trữ và những thông tin để lại làm cơ sở xác định nguyên nhân chiến sĩ tự sát.
+ Thông báo với gia đình chiến sĩ, mời gia đình lên đơn vị phối hợp giải quyết vụ việc.
+ Tạo mọi điều kiện thuận lợi và cung cấp đầy đủ các thông tin liên quan phục vụ chỉ huy và cơ quan cấp trên tiến hành các biện pháp điều tra, xác minh làm rõ nguyên nhân chiến sĩ tự sát (nắm tìm hiểu nguyên nhân thông qua đồng đội, đồng hương và gia đình chiến sĩ).
+ Phối hợp với gia đình, cơ quan chính sách, cử đại diện cán bộ, chiến sĩ đơn vị về tổ chức mai táng và thực hiện đầy đủ, chu đáo việc giải quyết chế độ chính sách theo quy định.
- Tổ chức sinh hoạt ổn định tình hình tư tưởng của đơn vị; động viên cán bộ, chiến sĩ, phổ biến quy định không bàn tán và phát ngôn tùy tiện trong đơn vị; sơ bộ thông báo về vụ việc theo kết luận của cơ quan chức năng, nêu rõ nguyên nhân, hậu quả, tác hại; giáo dục định hướng tư tưởng, tâm lý cho cán bộ, chiến sĩ trong đơn vị không hoang mang, dao động đồng thời chấp hành nghiêm các quy định về quản lý và sử dụng vũ khí quân dụng, không được tự ý tàng trữ, sử dụng vũ khí sai quy định; có các biện pháp theo dõi, quản lý tư tưởng, không để xảy những đột biến, bất ngờ về tư tưởng trong đơn vị.
- Điều tra làm rõ trách nhiệm của lãnh đạo, chỉ huy trong quản lý vũ khí đạn và xem xét xử lý đúng theo Điều lệnh Quản lý bộ đội.
- Thường xuyên quản lý nắm chắc tình hìn htuw tưởng bộ đội và gia đình hậu phương của quân nhân.
- Phát huy vai trò của các tổ chức quần chúng, hội đồng quân nhân và tổ tư vấn tâm lý, pháp lý trong công tác giáo dục, bồi dưỡng kỹ năng sống cho bộ đội; quan tâm chăm lo đời sống vật chất, tinh thần của cán bộ, chiến sĩ trong thực hiện nhiệm vụ.

Tình huống 94: Trong thời gian huấn luyện chiến sĩ mới, chiến sĩ Đ. lên báo cáo với trung đội trưởng, xin phép về tranh thủ vì lý do vợ sinh; đồng chí trung đội trưởng không đồng ý đề nghị với lý do “không thuộc diện quy định”, chiến sĩ Đ. rất buồn và lên báo cáo với chính trị viên đại đội “nếu không giải quyết sẽ đào ngũ”
Gợi ý biện pháp xử lý
- Phối hợp với cơ quan quân sự xã, phường, huyện… và gia đình để xác minh lại thông tin, nếu thông tin chính xác xử lý theo các bước:
- Hội ý cấp ủy, chỉ huy đơn vị, nhận định, đánh giá hoàn cảnh gia đình của chiến sĩ Đ., dự báo về khả năng chiến sĩ sẽ vắng mặt trái phép nếu không có biện pháp giáo dục, quản lý phù hợp, qua đó trao đổi, thống nhất biện pháp giải quyết, phân công cán bộ phụ trách và báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ chiến sĩ Đ., tâm sự, chia sẻ với đồng chí khi vợ sinh con, nhu cầu của đồng chí muốn về thăm vợ con là hoàn toàn chính đáng, tuy nhiên do yêu cầu nheiejm vụ (nhất là trong thời gian huấn luyện chiến sĩ mới) qua đó động viên đồng chí an tâm tư tưởng, thực hiện nhiệm vụ; việc dồng chí có con là một việc vui, xin chúc mừng đồng chí, động viên cố gắng huấn luyện giỏi, bắn giỏi lấy 3 điểm 10 để về tặng cho con. Nhắc nhở đồng chí cần rút kinh nghiệm về phát ngôn với cán bộ cũng như không được có thái độ thách thức tổ chức, việc làm đó là vi phạm kỷ luật quân đội, ảnh hưởng đến phẩm chất “Bộ đội Cụ Hồ”; trong gặp gỡ có thể lấy dẫn chứng một số đồng chí cán bộ trong đơn vị vì phải thực hiện nhiệm vụ mà khi vợ sinh con vẫn hoàn thành tốt nhiệm vụ để giáo dục đồng chí đó.
- Động viên đồng chí đó tích cực huấn luyện nâng cao trình độ chuyên môn, sau huấn luyện chiến sĩ mới nên giải quyết cho đồng chí Đ. về thăm vợ con.
- Liên hệ với gia đình, địa phương thông báo về tình hình tư tưởng và kết quả rèn luyện của chiến sĩ để gia đình biết và phối hợp động viên chiến sĩ an tâm tư tưởng. Điều kiện cho phép, gia đình chiến sĩ gần đơn vị có thể cử cán bộ cùng chiến sĩ có vợ sinh đi cùng về thăm gia đình trong ngày để động viên giải quyết tư tưởng kịp thời.
- Phân công cán bộ thường xuyên quan tâm nắm tình hình tư tưởng, sức khỏe vợ con của đông chí chiến sĩ đó, kịp thời động viên, phản ánh với chỉ huy đơn vị để có biện pháp giải quyết phù hợp không để tường hợp bất ngờ xảy ra.
- Quản lý duy trì chặt chẽ nề nếp chế độ trong ngày, trong tuần, nhất là giờ nghỉ, ngày nghỉ, phân công chiến sĩ bảo vệ, dân vận trong đơn vị thường xuyên theo dõi, bám sát chiến sĩ, ngăn chặn kịp thời khi chiến sĩ đó có ý định vắng mặt trái phép.
- Phát huy vai trò của các tổ chức quần chúng hội đồng quân nhân, tổ tư vấn tâm lý, pháp luật trong việc giáo dục, động viên, quản lý tư tưởng, đưa chiến sĩ vào các hoạt động chung của đơn vị như văn hóa văn nghệ, thể dục thể thao.

Tình huống 95: Dư luận đơn vị phản ảnh với chỉ huy tiểu đoàn, đồng chí cán bộ A. sinh con thứ ba, vi phạm chính sách kế hoạch hóa gia đình nhưng đã “lách luật” bằng cách đưa vợ đi xa quê hương để sinh, sau đó về quê làm thủ tục nhận con nuôi. Một số cán bộ đơn vị có những phản ứng khác nhau về vấn đề trên.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị, thống nhất biện pháp giải quyết.
- Báo cáo cấp trên xin ý kiến chỉ đạo xử lý vụ việc.
- Gặp gỡ đồng chí A. để nắm tình hình, khéo léo gợi mở để cán bộ tâm sự, chia sẻ; thông báo các nội dung dư luận phản ảnh, động viên cán bộ thành khẩn báo cáo với tổ chức.
- Trường hợp cán bộ xác nhận sự việc đúng như dư luận phản ảnh thì triển khai cho cán bộ viết tự kiểm điểm, giải trình rõ và tự nhận hình thức kỷ luật và tiến hành sinh hoạt xem xét kỷ luật (vi phạm quy định kế hoạch hóa gia đình);
+ Tổ chức sinh hoạt đơn vị thông báo kết quả xử lý cho cán bộ đơn vị biết để ổn địn h tình hình tư tưởng của đội ngũ cán bộ trong đơn vị.
+ Nếu có điều kiện có thể tổ chức cho hội phụ nữ thăm hỏi tặng quà, Tết Trung thu có phần quà cho con đồng chí A.
- Trường hợp cán bộ không nhận sự việc như dư luận phản ảnh, thì tiến hành các biện pháp xử lý:
+ Gặp gỡ một số cán bộ, chiến sĩ trong đơn vị để tìm hiểu nắm tình hình.
+ Cử cán bộ về làm việc với địa phương và gia đình để tiến hành các biện pháp thẩm tra, xác minh.
- Căn cứ vào kết quả xác minh, nắm tình hình để có biện pháp xử lý phù hợp theo 2 lỗi vi phạm quy định về kế hoạch hóa gia đình và không trung thực.
- Thông báo kết quả thẩm tra xác minh; hình thức xử lý đảng viên; giáo dục động viên đội ngũ cán bộ chấp hành và thực hiện nghiêm chính sách kế hoạch hóa gia đình; không phát ngôn tùy tiện làm ảnh hưởng đến uy tín của cán bộ và tạo dư luận không tốt trong đơn vị.
- Phân công cán bộ theo dõi, giúp đỡ nắm tình hình tư tưởng và các mối quan hệ của cán bộ.
- Tổng hợp kết quả xử lý báo cáo cấp trên.

Tình huống 96: Trong đơn vị có đồng chí trung đội trưởng (mới ra trường) có quan hệ tình cảm với một bạn gái (gần đơn vị) và đã “đi quá giới hạn”. Bạn gái “ép” đồng chí trung đội trưởng phải tổ chức đám cưới vì đã có “tin vui” nếu không sẽ có ý kiến với chỉ huy đơn vị.
Gợi ý biện pháp xử lý
- Hội ý chỉ huy đơn vị thống nhất biện pháp giải quyết và báo cáo cấp trên xin ý kiến chỉ đạo.
- Tiến hành kiểm tra, xác minh làm rõ mối quan hệ tình cảm của đồng chí trung đội trưởng và cô gái.
+ Gặp gỡ trực tiếp đồng chí trung đội tưởng, động viên báo cáo trung thực về mối quan hệ với cô gái và thông tin về việc đồng chí tỏng quan hệ đã “đi quá giới hạn” và “để lại hậu quả” với cô gái.
+ Gặp gỡ trực tiếp hoặc điện thoại với cô gái và gia đình để kiểm tra, xác minh về mối quan hệ của cô gái và đồng chí trung đội trưởng.
+ Nắm tình hình thông qua dư luận của cán bộ, chiến sĩ đơn vị.
- Trường hợp kết quả kiểm tra xác minh là đúng đồng chí trung đội trưởng có quan hệ tình cảm và đã “đi quá giới hạn”, “để lại hậu quả” thì động viên đồng chí nếu hai người có tình cảm và yêu nhau thực sự thì lựa chọn thời gian tổ chức đám cưới, không để người yêu có ý kiến, làm ảnh hưởng đối với đơn vị và bản thân đồng chí.
- Trường hợp đồng chí trung đội trưởng không nhận trách nhiệm và kết quả xác minh từ phía địa phương và gia đình chưa có cơ sở để khẳng định; đơn vị cần tạo điều kiện về thời gian cho đồng chí trung đội trưởng nghỉ phép để tiến hành xét nghiệm AND (nếu cần). Căn cứ vào kết quả xác minh để có biện pháp xử lý hợp lý.
- Tổ chức sinh hoạt đội ngũ cán bộ trong đơn vị, nhắc nhở mọi người thực hiện tốt mối quan hệ đoàn kết quân nhân, quan hệ nam nữ; giữ gìn phẩm chất, đạo đức, lối sống và phẩm chất tốt đẹp của “Bộ đội Cụ Hồ” trong quan hệ với nhân dân.
- Thường xuyên quan tâm nắm chắc phẩm chất năng lực của cán bộ, các mối quan hệ với gia đình và xã hộ, quan hệ nam nữ của đội ngũ cán bộ, có biện pháp giáo dục định hướng tư tưởng và giải quyết kịp thời các vấn đề nảy sin…
- Tổng hợp tình hình báo cáo cấp trên.

Tình huống 97: Trong đại đội có đồng chí trung đội trưởng xuất thân từ gia đình có tư tưởng phong kiến “trọng nam khinh nữ” đã lập gia đình và có hai con gái, bản thân là con trai duy nhất trong gia đình, thời gian gần đây đồng chí không đi tranh thủ về gia đình và có biểu hiện buồn phiền vì bố mẹ đồng chí “ép” phải sinh thêm con trai.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị thống nhất biện pháp giải quyết; phân công cấp ủy phụ trách.
- Gặp gỡ đồng chí trung đội trưởng để nắm tình hình tư tưởng, tâm tư nguyện vọng của bản thân và gia đình. Phân tích để đồng chí có nhận thức đúng về quyền bình đẳng nam, nữ trong xã hội; việc quan trọng là nuôi dạy các con khôn lớn trưởng thành chứ không phải là con trai hay con gái; việc bố mẹ “ép” đồng chí sinh con thứ ba là còn mang nặng tư tưởng phong kiến “trọng nam khinh nữ” muốn có người để “nối dõi tông đường” nếu đồng chí vi phạm chính sách kế hoạch hóa gia đình là vi phạm kỷ luật; qua đó động viên đồng chí an tâm tư tưởng, động viên thuyết phục gia đình không “ép” buộc sinh con thứ ba.
- Cử cán bộ về gặp gia đình, các tổ chức đoàn thể ở địa phương (hội cựu chiến binh, thanh niên, phụ nữ) phối hợp tuyên truyền, thuyết phục vận động gia đình thực hiện chính sách kế hoạch hóa gia đình; phân tích cho gia đình thấy được nếu con em của gia đình sinh con thứ ba là vi phạm chính sách kế hoạch hóa gia đình phải xử lý kỷ luật, sẽ ảnh hưởng đến quá trình phấn đấu của con em…, qua đó thuyết phục gia đình nhận thức đúng và không “ép” con em họ sinh con thứ ba nữa.
- Tổ chức sinh hoạt đơn vị, giáo dục định hướng chung cho cán bộ, chiến sĩ có nhận thức cơ bản về Luật Hôn nhân và gia đình và việc xử lý kỷ luật khi cán bộ vi phạm chính sách kế hoạch hóa gia đình cũng như những quy định và ảnh hưởng của việc sử dụng các biện pháp can thiệp để lựa chọn giới tính khi sinh; bồi dưỡng kỹ năng ứng xử với gia đình, người thân khi còn có tư tưởng “trọng nam khinh nữ” muốn có người để “nối dõi tông đường”…
- Thường xuyên theo dõi, nắm tình hình tư tưởng và giúp đỡ đồng chí trung đội trưởng hoàn thành tốt nhiệm vụ.
- Báo cáo kết quả giải quyết tư tưởng lên cấp trên.
Tình huống 98: Đại đội có đồng chí A. – nhân viên quân khí (chưa lập gia đình) bố mất sớm, mẹ hay đau ốm, em nhỏ còn đang học, bản thân trước khi nhập ngũ là lao động chính trong gia đình, thời gian gần đây biểu hiện buồn phiền, tư tưởng chán nản, hiệu quả công tác thấp.
Gợi ý biện pháp xử lý
- Trao đổi, thống nhất trong chỉ huy đơn vị, thống nhất biện pháp giải quyết.
- Chính trị viên đại đội gặp gỡ động viên nắm tư tưởng, tâm tư, nguyện vọng và nguyên nhân dẫn đến đồng chí A. có tư tưởng như vậy, động viên đồng chí chia sẻ những khó khăn vướng mắc và những kiến nghị đề xuất của đồng chí với đơn vị.
- Tăng cường các biện pháp quản lý, nắm chắc diễn biến tâm lý, tư tưởng của đồng chí A., nếu cần thiết phải kiến nghị với cấp trên tạm thời cử chỉ huy hoặc nhân viên khác thay thế.
- Nắm điều kiện hoàn cảnh gia đình và tư tưởng của đồng chí A. thông qua các đồng chí cùng quê hương, bạn thân trong đơn vị.
- Điện thoại thăm hỏi, động viên gia đình hoặc có điều kiện cử cán bộ đến trực tiếp gia đình nắm điều kiện hoàn cảnh gia đình của đồng chí A.; thông báo cho gia đình về kết quả hoàn thành nhiệm vụ của đồng chí A., để gia đình cùng đơn vị động viên đồng chí A. yên tâm công tác.
- Trường hợp đồng chí A. nảy sinh tư tưởng do điều kiện hoàn cảnh gia đình, đơn vị cần báo cáo cấp trên và cơ quan chức năng xem xét việc thực hiện chính sách trợ cấp đối với gia đình quân nhân có hoàn cảnh khó khăn.
- Tổ chức sinh hoạt đơn vị thông báo về hoàn cảnh gia đình của đồng chí A., vận động cán bộ, chiến sĩ đơn vị quyên góp ủng hộ vật chất, tinh thần giúp đỡ đồng chí A.
- Phối hợp với gia đình và đề nghị các tổ chức đoàn thể của địa phương cùng đơn vị quan tâm, thăm hỏi, giúp đỡ gia đình đồng chí A. yên tâm công tác, vượt qua khó khăn để hoàn thành nhiệm vụ.
- Quan tâm tạo điều kiện cho đồng chí A. có thời gian về thăm gia đình, động viên mẹ và em nhỏ.
-  Tổng hợp kết quả giải quyết báo cáo cấp trên.

Tình huống 99: Đơn vị có đồng chí quân nhân chuyên nghiệp nghi ngờ vợ “ngoại tình” (qua nghe ngóng dư luận) đã có biểu hiện buồn chán, chất lượng công tác thấp, thường xuyên lên xin chỉ huy đơn vị đi tranh thủ về gia đình.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị, nhận định đánh giá chất lượng công tác của quân nhân, tính chất, tác hại, nguyên nhân, dự kiến các vấn đề có thể nảy sinh nếu không được giải quyết tốt về mặt tư tưởng, qua đó trao đổi, thống nhất biện pháp giải quyết và báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ quân nhân đó nắm rõ lý do tại sao có biểu hiện buồn chán, chất lượng công tác thấp, lý do tại sao thường xuyên xin đi tranh thủ, động viên quân nhân bình tĩnh, xác định rõ ràng, không vì lời đồn đại bên ngoài mà làm ảnh hưởng đến tình cảm vợ chồng và chất lượng công việc.
- Thông qua các đồng chí thường xuyên gần gũi trong học tập công tác và bạn thân để nắm thêm tình hình tư tưởng của quân nhân.
- Liên hệ với bố, mẹ, vợ và các tổ chức đoàn thể ở địa phương của quân nhân (điều kiện cho phép cử cán bộ về gặp trực tiếp) để tìm hiểu nắm tình hình, phối hợp cùng gia đình địa phương giải quyết tư tưởng cho quân nhân.
- Báo cáo cấp trên, có thể đề nghị chế độ nghỉ phép cho quân nhân đó về quê giải quyết, dứt điểm, không lấy lý do đó mà thường xuyên lên xin tranh thủ không đúng quy định và chất lượng thực hiện nhiệm vụ thấp.
- Phát huy vai trò của các tổ chức quần chúng, hội đồng quân nhân, tổ tư vấn pháp lý trong việc giáo dục, động viên, tư vấn kỹ năng giải quyết tư tưởng, đưa quân nhân vào các hoạt động chung của đơn vị.
- Phân công cán bộ thường xuyên gần gũi động viên nắm tình hình kịp thời báo cáo, không để trường hợp bất ngờ xảy ra.

Tình huống 100: Đơn vị có quân nhân trên đường trả phép về đơn vị đã có hành động tố giác đối tượng cướp giật và bị chúng dùng bơm kim tiêm được cho là có HIV đam vào người; khi lên đơn vị có tâm lý hoang mang, lo lắng, nảy sinh ý định bỏ đi khỏi đơn vị, thậm chí có ý định tự tử.
Gợi ý biện pháp xử lý
- Nhanh chóng hội ý chỉ huy đơn vị, nhận định thống nhất biện pháp giải quyết và phân công thực hiện (xem xét đánh gái đúng tính chất phức tạp của vụ việc, nếu không được giải quyết kịp thời rất có thể dẫn đến hậu quả nghiêm trọng như quân nhân sẽ bỏ đi khỏi đơn vị, thâm chí tự tử, tự sát.
- Gặp gỡ để quân nhân báo cáo rõ sự việc, động viên, chia sẻ, khêu gợi để quân nhân cộng tác cùng đơn vị, để xác minh, kiểm tra, kết luận đúng tính chất sự việc, không tự ý có những hành vi tiêu cực và các vi phạm khác.
- Báo cáo kịp thời cấp trên xin ý kiến chỉ đạo về biện pháp giải quyết, khắc phục.
- Điện thoại thông báo cho gia đình biết để có các biện pháp phối hợp giáo dục, động viên và giải quyết vụ việc.
- Cử cán bộ, đảng viên quản lý, kèm cặp, giúp đỡ, nắm tình hình diễn biến tư tưởng, tâm lý của quân nhân không để các diễn biến bột phát nảy sinh.
- Phối hợp với các cơ quan quân y, bảo vệ của cấp trên xét nghiệm, kiểm tra kết luận kết quả đối với quân nhân.
- Tổ chức sinh hoạt đơn vị, biểu dương hành động của quân nhân đó, định hướng nhận thức cho cán bộ, chiến sĩ xây dựng bản lĩnh, lập trường của người quân nhân cách mạng trước những vấn đề nảy sinh tỏng cuộc sống, phân tích làm rõ tác động, hậu quả của những suy nghĩ bột phát, chủ quan, thiếu niềm tin vào khoa học trong xác minh và điều trị các loại bệnh, nêu cao ý thức trách nhiệm với bản thân, gia đình, đơn vị… để mọi quân nhân an tâm công tác.
- Trường hợp có kết quả dương tính với HIV, phối hợp với các cơ quan chức năng cấp trên quản lý và giải quyết theo quy định của Nhà nước và quân đội.
- Phối hợp địa phương, gia đình, đơn vị trong quản lý tư tưởng và chăm lo sức khỏe của quân nhân.







100 TÌNH HUỐNG TƯ TƯỞNG CÓ THỂ NẢY SINH
Ở ĐƠN VỊ VÀ GỢI Ý BIỆN PHÁP XỬ LÝ
CỦA CÁN BỘ CƠ SỞ

I. ĐỐI TƯỢNG SỸ QUAN QUÂN NHÂN CHUYÊN NGHIỆP , CÔNG NHÂN VIÊN QUỐC PHÒNG.
Tình huống 1. Vợ của một đồng chí cán bộ đại đội trong đơn vị bỏ nhà đi theo tà đạo có nhiều hoạt động mê tín dị đoan, làm cho đồng chí băn khoăn, lo lắng, thiếu yên tâm công tác
Gợi ý biện pháp xử lý
- Nắm chắc tình hình tư tưởng vợ, con và hoàn cảnh gia đình của đồng chí cán bộ đại đội, đề xuất cấp ủy, chỉ huy đơn vị có biện pháp giúp đỡ, giải quyết sự việc.
- Hội ý cấp ủy, chi huy đơn vị đánh giá tình hình hoàn cảnh gia đình vợ, con của đồng chí cán bộ đại đội, nguyên nhân đi theo tà đạo, thống nhất biện pháp giải quyết. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ trao đổi, tư vấn cho đồng chí cán bộ đại đội động viên vợ nhanh chóng trở về nhà ổn định cuộc sống, nâng cao cảnh giác với âm mưu, thủ đoạn hoạt động kích động lôi kéo, dụ dỗ của kẻ xấu, làm mất an nình chính trị, trật tự an toàn xã hội; căn cứ tình hình cụ thể cho cán bộ nghỉ phép, nghỉ tranh thủ về giải quyết việc gia đình; nếu có điều kiện phân công cán bộ đơn vị về cùng động viên, phối hợp giải quyết.
- Phối hợp với cấp ủy đảng, chính quyền, đoàn thể địa phương, động viên vợ cán bộ đại đội chấp hành nghiêm đường lối, chủ trương của Đảng, pháp luật Nhà nước, không tham gia tà đạo, mê tín dị đoan.
- Tham mưu và phối hợp với cấp ủy, chính quyền địa phương nắm, quản lý tình hình hoạt động của tà đạo trên địa bà, có biện pháp tuyên truyền cho nhân dân nâng cao cảnh giác, không tham gia hoạt động phi pháp, bảo đảm an ninh chính trị, trật tự an toàn xã hội.
- Tổ chức trao đổi, phổ biến kinh nghiệm cho sĩ quan, quan tâm chuyên nghiệp cho sĩ quan, quân nhân chuyên nghiệp trong đơn vị về phương pháp vận động, quản lý vợ con, chấp hành nghiêm đường lối, chủ trương của Đảng, pháp luật Nhà nước, cảnh giác với âm mưu, thủ đoạn hoạt động tuyên truyền, kích động dụ dỗ của kẻ xấu, ổn định cuộc sống gia đình.
- Thường xuyên quan tâm chăm lo chính sách hậu phương gia đình, động viên vợ con của sĩ quan, quân nhân chuyên nghiệp ổn định cuộc sống, yên tâm công tác.
Tình huống 2. Một số sĩ quan, quân nhân chuyên nghiệp nhận thức chưa đầy đủ đường lối, chủ trương, quan điểm của Đảng, Nhà nước, lấy lý do bận công việc chuyên môn, ít tham gia học tập chính trị
Gợi ý biện pháp xử lý
- Nhận định, đánh giá tình hình tác động tư tưởng của sĩ quan, quân nhân chuyên nghiệp ảnh hưởng đến sự lãnh đạo của chi ủy, chi bộ, kết quả, mức độ hoàn thành nhiệm vụ chính trị của đơn vị.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá thực trạng nhận thức, tư tưởng của sĩ quan, quân nhân chuyên nghiệp, xác định chủ trương, biện pháp khắc phục biểu hiện lười học tập chính trị.
- Phận loại chất lượng chính trị các đối tượng trong đơn vị, nhất là số sĩ quan, quân nhân chuyên nghiệp nhận thức chính trị hạn chế.
- Gặp gỡ giáo dục, quán triệt cho sĩ quan, quân nhân chuyên nghiệp nâng cao ý thức trách nhiệm thực hiện nghiêm nghị quyết, chỉ thị của Đảng, quy chế, quy định về công tác giáo dục chính trị trong quân đội; thường xuyên bồi dưỡng phương pháp học tập, nghiên cứu nâng cao trình độ nhận thức.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm, nâng cao ý thức, trách nhiệm, tự giác nghiên cứu, học tập chính trị, rèn luyện chấp hành nghiêm kỹ luật quân đội, pháp luật Nhà nước.
- Đẩy mạnh phong trào thi đua hoạc tập, nghiên cứu nâng cao trình độ nhận thức chính trị, hiểu biết về đường lối, chủ trương của Đảng, pháp luật Nhà nước, chấp hành nghiêm kỹ luật quân đội, nền nếp xây dựng quân đội chính quy.
- Thường xuyên đổi mới hình thức, biện pháp giáo dục chính trị lôi cuốn sĩ quan, quân nhân chuyên nghiệp tham gia học tập chính trị.
- Chính trị viên, người chỉ huy đơn vị tăng cường kiểm tra đánh giá kết quả việc học tập chính trị của sĩ quan, quân nhân chuyên nghiệp làm cơ sở nhận xét, đánh giá cán bộ, đang viên, nhân viên.
- Đánh giá khách quan, chính xác nhận thức chính trị của sĩ quan, quân nhân chuyên nghiệp, có biện pháp bồi dưỡng kịp thời.
Tình huống 3. Một số sĩ quan trong đơn vị nhiều lần thi bắn sung K54 đạt kết quả thấp, ảnh hưởng thành tích cá nhân, đơn vị, do đó trong quá trình kiểm tra bắn đạn thật có biểu hiện lo lắng, thiếu tự tin
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình chất lượng huấn luyện và kết quả bắn sung ngắn K54 của sĩ quan, xác định nguyên nhân, thống nhất biện pháp bồi dưỡng. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Tổ chức phân loại khả năng bắn K54 của sĩ quan; giáo dục, quán triệt nắm rõ mục tiêu, yêu cầu, chức trách, nhiệm vụ được giao của cán bộ quản lý, chỉ huy đơn vị, qua đó nâng cao ý thức học tập, rèn luyện kỹ năng bắn sung.
- Phân công cán bộ có kinh nghiệm kèm cặp, giúp đỡ kỹ năng, phương pháp bắn sung K54 cho sĩ quan kiểm tra kết quả thấp tin tưởng vào bản thân, kiên trì luyện tập nâng dần kết quả kiểm tra.
- Duy trì nghiêm chế độ, nền nếp huấn luyện quân sự, kiểm tra bắn sung K54 theo quy định của cấp trên; động viên sĩ quan tích cực huấn luyện, tham gia luyện tập, kiểm tra đầy đủ.
- Thường xuyên cổ vũ, động vien sĩ quan nâng cao ý chí trách nhiệm tích cực học tập, luyện tập súng K54 nâng dần kết quả kiểm tra.
Tình huống 4. Trong đơn vị có đồng chí trung đội trưởng biểu hiện bi quan, chán nản, thiếu cố gắng trong công tác, do các cấp ủy đảng đánh giá cán bộ thiếu khách quan, chinh xác
Gợi ý biện pháp xử lý
- Gặp đồng chí trung đội trưởng nắm, tìm hiểu tâm tư, nguyện vọng và những băn khoăn vướng mắc, đề xuất cấp ủy, chỉ huy đơn vị có biệp pháp khắc phục.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá, rà soát lại quy trình, quy định nhận xét, quy hoạch, đề bạt cán bộ đảm bảo khách quan, chính xác, nếu có sai có biện pháp khắc phục. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Trên cơ sở sự chỉ đạo của cấp ủy đảng cấp trên, tổ chức họp cấp ủy, chi bộ đánh giá công  tác cán bộ bảo đảm đúng quy trình, quy định, rút ra những hạn chế, khuyết điểm, xác định nguyên nhân quy trách nhiệm cá nhân, tập thể, có biện pháp khắc phục, rút kinh nghiệm.
- Gặp gỡ trung đội trưởng thông báo kết quả rà soát, đánh giá công tác cán bộ của cấp ủy đảng, hạn chế, khuyết điểm của tập thể, cá nhân, có biện pháp khắc phục, tùy theo mức độ (có thể xử lý kỷ luật cá nhân, tập thể về công tác cán bộ).
- Tổ chức sinh hoạt rút kinh nghiệm cho đội ngũ sĩ quan trong đơn vị đề cao trách nhiệm học tập, tu dưỡng, rèn luyện, nâng cáo trình độ, phẩm chất, năng lực công tác, tin tưởng vào đánh giá, nhận xét cán bộ của cấp ủy đảng, khắc phục biểu hiện bi quan, chán nản, thiếu tự tin trong thực hiện nhiệm vụ.
- Rà soát tham mưu sữa đổi, bổ sung quy chế, quy định, đánh giá, sử dụng cán bộ chi ủy, chi bộ, bảo đảm dân chủ, khách quan, chính xác, quy rõ trách nhiệm cá nhân, tập thể, phát huy trình độ, năng lực của sĩ quan vào cống hiến xây dựng đơn vị vững mạnh.
- Thường xuyên kiểm tra, đánh giá trình độ, phẩm chất, năng lực huấn luyện đội ngũ cán bộ trong đơn vị làm cơ sở phân hướng sử dụng, đề bạt, bổ nhiệm khách quan, chính xác.
- Quan tâm chăm lo đảm bảo đời sống vật chất, tinh thần cho cán bộ sinh hoạt, công tác, yên tâm gắn bó với đơn vị thực  hiện tốt nhiệm vụ được giao.
- Báo cáo cấp trên về kết quả xử lý và tiếp tục theo dõi, bòi dưỡng cán bộ.
Tình huống 5. Bố của một đồng chí đại đội trưởng gần đơn vị thường xuyên gặp gỡ, trao đổi thông tin với một số đối tượng xấu, làm cho sĩ quan, quân nhân chuyên nghiệp trong đơn vị nghi ngờ, thiếu tin tưởng chỉ huy
Gợi ý biện pháp xử lý
- Tổng hợp tình hình an ninh chính trị, trật tự an toàn xã hội trên địa bàn, đề xuất chủ trương, biện pháp với cấp ủy, chỉ huy đơn vị giải quyết.
- Tổ chức hội ý cấp ủy, chỉ huy đơn vị, đánh giá tình hình an ninh chính trị, trật tự an toàn xã hội địa bàn có liên quan, thống nhất biện pháp giải quyết. Báo cáo cấp trên theo quy định.
- Gặp gỡ đồng chí đại đội trưởng, động viên thuyết phục bố của mình chấp hành nghiêm đường lối, chủ trương của Đảng, phâp luật Nhà nước, nâng cao cảnh giác với âm mưu, thủ đoạn hoạt động chống phá của các phần tử cơ hội, chống đối chính trị trên địa bàn; không tin, không nghe kẻ xấu dụ dỗ, lôi kéo làm mất an ninh chính trị, trật tự an toàn xã hội.
- Phối hợp với cấp ủy, chính quyền địa phương tổ chức gặp gỡ bố của đồng chí đại đội trưởng yêu cầu thực hiện tốt trách nhiệm, nghĩa vụ của người công dân; chấp nghiêm đường lối, chủ trương của Đảng,chính sách, pháp luật của Nhà nước, không làm ảnh hưởng đến uy tín, công việc con đang công tác.
- Cùng với cấp ủy đảng, chính quyền địa phương thường xuyên làm tốt công tác nắm, quản lý tình hình an ninh chính trị, trật tự an toàn xã hôi trên địa bàn, tư tưởng, kỹ luật của sĩ quan, quân nhân chuyên nghiệp trong đơn vị; tuyên truyền giáo dục nâng cao ý thức cánh giác, đấu tranh với những hoạt động tuyên truyền, kích động, chống phá của các thế lực thù địch.
- Tổ chức sinh hoạt đơn vị thông báo kết quả gặp gỡ, xử lý sự việc có liên quan, định hướng cho cán bộ.
- Quản lý chặt chẽ tình hình tu tưởng, kỹ luật của sĩ quan, quân nhân chuyên nghiệp trong đơn vị, không để kẻ xấu móc nối, lôi kéo, chia sẽ, chống phá nội bộ.
Tình huống 6. Một số sĩ quan, quân nhân chuyên nghiệp trong đơn vị cho rằng, khi tổ chức liên hoan, giao lưu gặp gỡ có uống rượu, bia phải uống hết mình cho tình cảm, gây tâm lý băn khoăn, lo lắng cho những đồng chí không uống được rượu, bia.
Gợi ý biện pháp xử lý
- Nắm tình hình uống rượu, bia và tâm lý băn khoăn , vướng mắc của sĩ quan, quân nhân chuyên nghiệp trong đơn vị, tham mưu cho lãnh đạo, chỉ huy có chủ trương, giải pháp khắc phục.
- Hội ý cấp ủy, chủ huy đơn vị đánh giá thực trạng, nguyên nhân uống rượu, bia của sĩ quan, quân nhân chuyên nghiệp, gây tâm lý lo lắng trong đơn vị; đề xuất giải pháp giáo dục tuyên truyền.
- Gặp gỡ riêng sĩ quan, quân nhân chuyên nghiệp hay uống rượu, bia giáo dục, quán triệt hiểu rõ tác hại của rượu, bia, ảnh hưởng tới sức khỏe, tác phong công tác, làm mất vẻ đẹp hình ảnh Bộ đội Cụ Hồ, nâng cao ý thức chấp hành nghiêm chế độ nền nếp xây dựng đơn vị chính quy, rèn luyện nghiêm kỹ luật.
- Thường xuyên quán triệt nội dung quy chế, quy định của quân đội liên quan đến sử dụng rượu, bia và đặc điểm yêu cầu, nhiệm vụ đơn vị, phong trào xây dựng môi trường văn hóa; qua đó làm cho sĩ quan, quân nhân chuyên nghiệp tự giác chấp hành.
- Tổ chức phát động phong trào thi đua, đăng ký giao ước chấp hành nghiêm quy định của quân đội liên quan đến sử dụng rượu bia.
- Tăng cường duy trì nghiêm chế độ, nền nếp xây dựng đơn vị chính quy, rèn luyện kỹ luật sĩ quan, quân nhân chuyên nghiệp, nhất là chấp hành nghiêm quy đinh của quân đội liên quan đến sử dụng rượu, bia.
- Tổ chức sinh hoạt rút kinh nghiệm cho sĩ quan, quân nhân chuyên nghiệp trong đơn vị hiểu rõ tác hại của uống rượu, bia, làm ảnh hưởng đến sức khỏe, phẩm chất, tư cách cán bộ, đảng viên, hình ảnh Bộ đội Cụ Hồ; qua đó nâng cao ý thức chấp hành nghiêm các quy định liên quan đến uống rượu, bia của Bộ Quốc phòng.
- Chỉ đạo tổ chức diễn đàn, tọa đàm, giao lưu, sinh hoạt văn hóa, văn nghệ , tuyên truyền quy định liên quan đến uống rượu, bia của Bộ Quốc phòng; định hướng nhận thức, tư tưởng, chấp hành cho sĩ quan, quân nhân chuyên nghiệp.
Tình huống 7. Một đồng chí trung đội trưởng lập gia đình đã nhều năm nhưng chưa có con, mặc dù vợ, chồng đã đi chữa trị ở nhiều bệnh viện nhưng chưa có kết quả, nảy sinh tư tưởng thiếu yên tâm công tác.
Gợi ý biện pháp xử lý
- Xác minh điều kiện, hoàn chảnh gia đình, nguyên nhân hiếm muộn con của cán bộ, tham mưu cho cấp ủy, chỉ huy đơn vị có biện pháp xử lý.
- Hội ý cấp ủy, chỉ huy đơn vị, thống nhất biện pháp giúp đỡ. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ đồng chí trung đội trưởng có hoàn cảnh hiến muộn con, tư vấn đến bệnh viện chuyên ngành để điều trị, động viên tinh thần, tin tưởng vào khoa học hiện đại để chữa trị.
- Quan tâm chăm lo bảo đảm tiêu chuẩn, chế độ, chính sách theo quy định của quân đội cho sĩ quan chữa trị và vận động sĩ quan, quân nhân chuyên nghiệp trong đơn vị hỗ trợ một phần kinh phí giúp đỡ (sau khi báo cáo và có ý kiến chỉ đạo của cấp trên).
- Giáo dục sĩ quan, quân nhân chuyên nghiệp trong đơn vị nâng cao ý thức rèn luyện sức khỏe, ăn uống khoa học, vệ  sinh, xây dựng lối sống lành mạnh, có thể chất tốt, bảo đảm chất lượng cuộc sống và trách nhiệm xây dựng gia đình, đơn vị.
- Căn cứ vào tình hình, điều kiện cụ thể của đơn vị, có thể bố trí công tác cho cán bộ gần gia đình để có điều kiện chữa bệnh có hiệu quả.
- Phối hợp với địa phương, gia đình, cơ quan của vợ cán bộ cùng động viên quan tâm, giúp đỡ phù hợp.
Tình huống 8. Một đồng chí sĩ quan đơn vị vay tiền với lãi xuất cao, tham gia cá độ, đánh bạc không có khả năng thanh toán, dẫn đến bị bệnh trầm cảm, chất lượng thực hiện nhiệm vụ giảm suát
Gợi ý biện pháp xử lý
- Nắm tình hình, số lượng tiền vay của sĩ quan, nguyên nhân hậu quả, tham mưu cho cấp ủy, chỉ huy giải quyết. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Họp cấp ủy, chỉ huy đơn vị đánh giá tình hình vay nặng lãi của sĩ quan, hậu quả, số lượng, nguyên nhân, bàn biện pháp khắc phục.
- Phối hợp với các cơ quan chức năng của đơn vị chỉ đạo sĩ quan quan bằng mọi sự giúp đỡ, hỗ trợ của gia đình, bạn bè nhanh chóng thanh toán số tiền vay mượn, không để phát sinh thêm lãi suất cao càng khó khăn trong xử lý sự việc.
- Trực tiếp bí thư, hoặc phân công đảng viên có uy tín gặp gỡ động viên, giúp đỡ sĩ quan vay tiền không có khả năng thanh toán vượt qua khó khăn, không để nảy sinh tư tưởng và hành động tiêu cực, gây hậu quả xấu.
- Triển khai cho sĩ quan viết bản tường trình, tự kiểm điểm, tổ chức sinh hoạt đơn vị làm rõ tính chất, mức độ sự việc, ảnh hưởng đến uy tín danh dự cá nhân, gia đình, tập thể, đề nghị hình thức kỷ luật (tùy theo mức độ tính chất cụ thể)
- Tổ chức sinh hoạt giáo dục, rút kinh nghiệm cho sĩ quan, quân nhân chuyên nghiệp trong đơn vị hiểu rõ tác hại, hậu qủa của vay nặng lãi nảy sinh tư tưởng, hành động cực đoan đào ngũ, tự tử, tự sát, gia đình ly tán, vượt biên và những việc làm phi pháp khác; qua đó nâng cao ý thức chấp hành pháp luật Nhà nước, kỷ luật quân đội, rèn luyện lối sống trong sạch, lành mạnh, chi tiêu cá nhân có kế hoạch
- Thường xuyên nắm chắc diễn biến tình hình tư tưởng các mối quan hệ, nhất là biểu hiện tham gia cá độ, lô đề, đánh bạc, vay nặng lãi, vi phạm kỹ luật của sĩ quan, quân nhân chuyên nghiệp; qua đó tham mưu cho cấp ủy, chỉ huy giải quyết kịp thời.
- Phối hợp với các tổ chức, lực lượng đơn vị, địa phương tăng cường giáo dục, động viên sĩ quan, quân nhân chuyên nghiệp chi tiêu sinh hoạt tiết kiệm, xây dựng lối sống trong sạch, lành mạnh, chấp hành nghiêm kỷ luật quân đội, quy định đơn vị.
Tình huống 9. Một số cán bộ địa phương trên địa bàn, nhất là vùng sâu, vùng xa, dân tộc thiểu số, khi khách đến nhà hay đưa rượu ra uống rồi mới trao đổi công việc, do đó làm cho sĩ quan, quân nhân chuyên nghiệp làm công tác dân vận thực hiện nhiệm vụ khó khăn, biểu hiện lo lắng.
Gợi ý biện pháp xử lý
- Nắm chắc tình hình, đặc điểm, phong tục tập quán uống rượu của cán bộ địa phương, tham mưu cho cấp ủy, chỉ huy đơn vị có bện pháp khắc phục.
- Hội ý lãnh đạo, chỉ huy đơn vị đánh giá tình hình tập quán uống rượu của cán bộ, nhân dân địa phương, tâm lý của sĩ quan, quân nhân chuyên nghiệp khi đến làm việc với nhân dân; thống nhất biện pháp lãnh đạo, chỉ đạo, giải quyết các mối quan hệ chung, riêng phù hợp tình hình cụ thể.
- Phối hợp với cấp ủy đảng, chính quyền, nhân dân địa phương ban hành quy chế xây dựng đơn vị an toàn, gắn bó với địa bàn; phân tích làm rõ tác hại của rượu bia ảnh hưởng tới sức khỏe, tác phong công tác, nếp sống sinh hoạt văn hóa, nâng cao ý thức chấp hành nghiêm quy định của địa phương, kỷ luật quân đội.
- Tham mưu cho cấp ủy, chính quyền địa phương tổ chức rút kinh nghiệm phong trào xây dựng gia đình văn hóa, làng xã văn hóa, trong đó có quy định về uống rượu bia của địa phương; qua đó giáo dục, tuyên truyền mọi người tự giác chấp hành.
- Phối hợp với các tổ chức đoàn thể địa phương, tổ chức giao lưu, tọa đàm, văn hóa văn nghệ, tuyên truyền tác hại của rượu bia, xây dựng nếp sống văn hóa khu dân cư, làm chuyển biến nhận thức tư tưởng để mọi người tự giác chấp hành.
- Phối hợp với địa phương làm tốt công tác thi đua, khen thưởng, kịp thời biểu dương những cá nhân, tập thể chấp hành nghiêm quy định về uống rượu bia, xây dựng địa phương có môi trường trong sạch, lành mạnh, nếp sống văn hóa; đồng thời phê bình, kiểm điểm nếu có vi phạm kỷ luật.
Tình huống 10. Một số sĩ quan trong đơn vị có biểu hiện che giấu khuyết điểm, chạy theo thành tich, gây dự luận không tốt trong đơn vị
Gợi ý biện pháp xử lý
- Nắm tình hình tư tưởng của sĩ quan, quân nhân chuyên nghiệp và những biểu hiện che giấu khuyết điểm, chạy theo thành tích trong đơn vị, thống nhất biện pháp lãnh đạo, chỉ đạo khắc phục.
- Họp cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật, dư luận sĩ quan, quân nhân chuyên nghiệp, nguyên nhân che giấu khuyết điểm, chạy theo thành tích, thống nhất biện pháp khắc phục.
- Gặp gỡ giáo dục, tuyên truyền cho sĩ quan, quân nhân chuyên nghiệp hiểu rõ tác hại, hậu quả của biểu hiện che giấu khuyết điểm, chạy theo thành tích là vi phạm quy định của quân đội về chế độ báo cáo, xin ý kiến chỉ thị; vi phạm chế độ trách nhiệm của người chỉ huy, ảnh hưởng chất lượng, kết quả xây dựng chi bộ trong sạch vẵng mạnh, đơn vị vững mạnh toàn diện.
- Tổ chức sinh hoạt đơn vị giáo dục, tuyên truyền cho sĩ quan quân nhân chuyên nghiệp nhận thức sâu sắc vị trí, ý nghĩa của đánh giá đúng thực chất tình hình đơn vị để xây dựng chi bộ trong sạch vững mạnh, đơn vị vững mạnh toàn diện; qua đó có biện pháp đấu tranh quan điểm, tư tưởng báo cáo không trung thực, che giấu khuyết điểm của một số sĩ quan, quân nhân chuyên nghiệp trong đơn vị.
- Duy trì nghiêm chế độ báo cáo, phản ánh tình hình về tư tưởng, kỷ luật bộ đội trong đơn vị, nhất là những khó khăn vướng mắc, có biện pháp giúp đỡ kịp thời; phê bình thẳng thắn đối với cá nhân báo cáo không trung thực, chạy theo thành tích.
- Tham mưu đề xuất rà soát bổ sung, sửa đổi các quy định, quy chế báo cáo, xin chỉ thị của các tổ chức, khắc phục biểu hiện che giấu khuyết điểm, chạy theo thành tích, đáp ứng yêu cầu, nhiệm vụ xây dựng đơn vị trong tình hình mới.
- Duy trì nghiêm chế độ nền nếp xây dựng đơn vị chính quy, quản lý tư tưởng, kỷ luật cho sĩ quan, quân nhân chuyên nghiệp, xử lý kịp thời mọi tình huống phát sinh.
- Xử lý nghiêm kỷ luật đối với những trường hợp vi phạm.
Tình huống 11. Một cán bộ trung đội trưởng mới ra trường trong quá trình quản lý, chỉ huy còn để một số chiến sĩ vi phạm kỷ luật vắng mặt trái phép, bị cấp trên phê bình nhắc nhở, làm đồng chí băn khoăn thiếu tự tin về khả năng hoàn thành nhiệm vụ của mình
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật cán bộ, thống nhất biện pháp xây dựng đơn vị vững mạnh toàn diện và phân công từng ủy viên, chỉ huy đại đội phụ trách giúp đỡ các trung đội.
- Gặp gỡ động viên, giúp đỡ đồng chí trung đội trưởng tích cực học tập, rút kinh nghiệm của những cán bộ đi trước về kỹ năng phương pháp quản lý, chỉ huy bộ đội chấp hành kỷ luật quân đội, pháp luật Nhà nước, nâng cao chất lượng, hiệu quả công tác.
- Thường xuyên bồi dưỡng kinh nghiệm, phương pháp quản lý, chỉ huy bồ đội cho trung đội trưởng có tâm lý tự tin vào giáo dục, quản lý, chỉ huy bồ đội, đáp ứng yêu cầu xây dựng đơn vị vững mạnh, đủ sức hoàn thành nhiệm vụ được giao.
- Thường xuyên, quán triệt nghiêm túc các nghị quyết, chỉ thị, quy định của quân đội trong thực hiện nền nếp, chế độ xây dựng quân đội chính quy, quản lý kỹ luật để bộ đội tự giác chấp hành.
- Đẩy mạnh phong trào thi đua quyết thắng trong đơn vị, kịp thời biểu dương tập thể, cá nhân có thành tích, đồng thời xử lý nghiêm kỹ luật đối với các đồng chí vi phạm.
- Thường xuyên quan tâm, theo dõi, giúp đỡ đồng chí trung đội trưởng thực hiện nhiệm vụ trong điều kiện khó khăn phức tạp để đồng chí tự tin vào khả năng hoàn thành nhiệm vụ của mình.
- Phát huy tốt vai trò, trách nhiệm của các tổ chức, lực lượng trong đơn vị, nhất là đoàn thanh niên, hội đồng quân nhân, tham gia vào giáo dục, quản lý bộ đội chấp hành nghiêm
- Đánh giá khách quan, chính xác phẩm chất, năng lực, kết quả hoàn thành nhiệm vụ của cán bộ, làm cơ sở đề bạt, bổ nhiệm.
Tình huống 12. Một đồng chí sĩ quan được giao nhiệm vụ huấn luyện, diễn tập trong điều kiện khó khăn, vất vả đã lấy lý do vợ con ốm đau để xin nghỉ phép, tranh thủ
Gợi ý biện pháp xử lý
- Gặp gỡ đồng chí sĩ quan nắm tình hình, tìm hiểu tâm tư, nguyện vọng và những vướng mắc bất cập trong công tác, tham mưu cho cấp ủy, chỉ huy đơn vị giải quyết.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật, điều kiện hoàn cảnh gia đình của sĩ quan, quân nhân chuyên nghiệp, đặc điểm, yêu cầu, nhiệm vụ của đơn vị, xác định chủ trương, biện pháp lãnh đạo, chỉ đạo tổ chức thực hiện.
- Sinh hoạt đơn vị giáo dục, quán triệt nghị quyết, chỉ thị, kế hoạch, nhiệm vụ của cấp ủy đảng, chỉ huy các cấp, xây dựng ý thức, trách nhiệm cho sĩ quan, quân nhân chuyên nghiệp khắc phục khó khăn hoàn thành tốt nhiệm vụ.
- Động viên sĩ quan xác định tư tưởng, trách nhiệm của người cán bộ, đảng viên, giải quyết hài hòa mối quan hệ chung, riêng để cùng với đơn vị hoàn thành tốt nhiệm vụ huấn luyện, nâng cao khả năng sẵn sàng chiến đấu, đáp ứng yêu cầu, nhiệm vụ được giao.
- Tổ chức sinh hoạt quán triệt rút kinh nghiệm cho đội ngũ cán bộ nắm vững mục tiêu, yêu cầu, nhiệm vụ diễn tập, chỉ thị, hướng dẫn của các cấp ủy đảng, xác định động cơ, trách nhiệm, khắc phục khó khăn tham gia diễn tập có chất lượng
-  Phối hợp với cấp ủy đảng, chính quyền địa phương tổ chức thăm hỏi, động viên gia đình sĩ quan vượt qua hoàn cảnh khó khăn, tạo điều kiện thuận lợi để cán bộ hoàn thành nhiệm vụ, sau đó xin ý kiến cấp trên giải quyết phép, tranh thủ đặc biệt cho bộ đội.
- Thường xuyên tổ chức giáo dục, động viên can bộ chấp hành nghiệm kỷ luật quân đội, quy định đơn vị, tu dưỡng rèn luyện bản thân để thích ứng với điều kiện, môi trường công tác.
- Quan tâm bảo đảm đời sống vật chất, tinh thần cho sĩ quan, quân nhân chuyên nghiệp sinh hoạt công tác, yên tâm gắn bó với đơn vị.
- Xây dựng đơn vị có môi trường trong sạch, lành mạnh, có văn hóa, tinh thần đoàn kết, giúp đỡ lẫn nhau hoàn thành tôt nhiệm vụ.
Tình huống 13. Cuộc cách mạng công nghiệp lần thứ tư đang tác động đến nhiệm vụ bảo vệ tổ quốc. Việc quân đội một số nước lớn được trang bị vũ khí công nghệ cao, vũ khí thông minh, do đó khi tổ chức huấn luyện với vũ khí trang bị trong biên chế của quân đội ta, một số sĩ quan, quân nhân chuyên nghiệp ở đơn vị cơ sở có biểu hiện thiếu tự tin, băn khoăn, lo lắng
Gợi ý biện pháp xử lý
- Trao đổi thống nhất trong lãnh đạo, chỉ huy đơn vị đánh giá tình hình tư tưởng, nhận thức sĩ quan, quân nhân chuyên nghiệp, xác định biện pháp giáo dục, tuyên truyền.
- Tổng hợp tình hình nhận thức, tư tưởng của sĩ quan, quân nhân chuyên nghiệp báo cáo cấp trên, đề xuất nội dung tài liệu có liên quan phục vụ cho việc giáo dục, tuyên truyền, định hướng nhận thức về cách mạng công nghiệp lần thứ tư.
- Gặp gỡ một số sĩ quan, quân nhân chuyên nghiệp băn khoăn về trang bị vũ khí của quân đội ta trước tác động cách mạng công nghiệp lần thứ tư, giáo dục, định hướng, tận dụng phát triển của khoa học vào nhiệm vụ huấn luyện, sẵn sàng chiến đấu, hoạt động quân sự của đơn vị, vượt qua khó khăn hoàn thành nhiệm vụ trong tình hình mới.
- Giáo dục cho sĩ quan, quân nhân chuyên nghiệp nâng cao nhận thức về mối quan hệ giữa yếu tố con người với vũ khí trang bị, trong đó yếu tố con người giữ vai trò quyết định; đồng thời lấy lịch sử truyền thống đấu tranh của dân tộc, quân đội ta, nhất là chiến thắng “Hà Nội - Điện Biên Phủ trên không”, phim, ảnh về huấn luyện, diễn tập với các loại trang bị mới, hiện đại để giáo dục, định hướng, nâng cao nhận thức cho bộ đội, xây dựng niềm tin vào khả năng chiến đấu, chiến thắng của quân đội ta với vũ khí trang bị hiện có.
- Tổ chức cho sĩ quan, quân nhân chuyên nghiệp tham quan, triển lãm một số vũ khí trang bị, công trình quân sự của quân đội ta (nếu có điều kiện) và những sáng kiến, cải tiến kỹ thuật của đơn vị, xây dựng niềm tin vào khả năng, sức mạnh chiến đấu của quân đội.
- Tăng cường giáo dục, bồi dưỡng cho sĩ quan, quân nhân chuyên nghiệp trong đơn vị nâng cao ý thức học tập, huấn luyện, nắm vững tính năng kỹ chiến thuật, sử dụng thành thạo các loại vũ khí trang bị có trong biên chế, phục vụ yêu cầu , nhiệm vụ huấn luyện, sẵn sành chiến đấu.
- Thường xuyên theo dõi, đánh giá khách quan, chính xác nhận thức chính trị của sĩ quan, quân nhân chuyên nghiệp, khả năng vận dụng quan điểm,. đường lối của Đảng và thực tiễn nhiệm vụ huấn luyện, sẵn sàng chiến đấu của đơn vị.
- Tiếp tục theo dõi huấn luyện, tăng cường dự giờ, kiểm tra nhận thức chính trị đối với sĩ quan, quân nhân chuyên nghiệp, báo cáo kết quả lên cấp trên theo quy định.
Tình huống 14. Một sĩ quan được cấp trên giao nhiệm vụ tham gia diễn tập chiến thuật vòng tổng hợp đã có ý định về nhà chăm sóc bố đang nằm viện, chỉ huy đơn vị chưa giải quyết, đồng chí đã dùng dao tự thương
Gợi ý biện pháp xử lý
- Đưa đồng chí sĩ quan tự thương đi bệnh viện cứu chữa, khắc phục hậu quả, động viên tư tưởng.
- Thông qua đồng chí, đồng đội có mối quan hệ gần gũi với sĩ quan tự thương, nắm chắc điều kiện hoàn cảnh gia đình, xác định nguyên nhân sự việc, tham mưu cho cấp ủy, chỉ huy đơn vị có biện pháp giải quyết.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật, điều kiện hoàn cảnh gia đình, nguyên nhân của sĩ quan tự thương, thống nhất biện pháp giải quyết. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ đồng chí sĩ quan tự thương giáo dục, động viên nâng cao nhận thức khắc phục tư tưởng vướng mắc, bất cập, yên tâm điều trị ổn định sức khỏe, vươn lên hoàn thành tốt nhiệm vụ; đồng thời, động viên đồng chí rút kinh nghiệm về phương pháp ứng xử với bản thân trước khó khăn của cuộc sống.
- Căn cứ tính chất, mức độ, ý thức nhận nhiệm vụ của đồng chí sĩ quan tự thương, tiến hành kiểm điểm, kỷ luật theo đúng quy định điều lệnh quân đội.
- Phối hợp với các địa phương, gia đình và đồng chí, đồng đội, động viên giúp đỡ đồng chí sĩ quan tự thương bỏ qua mặc cảm cá nhân, ổn định tâm lý, tư tưởng, tham gia công tác bình thường.
- Tăng cường nắm, quản lý tư tưởng, kỹ luật và các mối quan hệ của cán bộ thuộc quyền, nhất là những đồng chí biểu hiện bất thường, thiếu yên tâm công tác để động viên kịp thời.
- Xây dựng đơn vị có môi trường trong sạch, lành mạnh, có văn hóa, sĩ quan, quân nhân chuyên nghiệp đoàn kết, thương yêu giúp đỡ lẫn nhau hoàn thành nhiệm tốt nhiệm vụ.
- Giải quyết tốt chế độ chính sách về nghỉ phép, nghỉ tranh thủ đúng quy định của quân đội để sĩ quan, quân nhân chuyên nghiệp có điều kiện khó khăn giải tỏa vướng mắc về gia đình, bản thân, chấp hành nghiêm kỷ luật quân đội, quy định đơn vị.
Tình huống 15. Theo lộ trình các doanh nghiệp trong quân đội (tổng công ty) đến năm 2020 sẽ hoàn thành cổ phần hóa, những đồng chí quân nhân chuyên nghiệp dưới 20 năm công tác chưa đủ tuổi nghỉ hưu lo lắng trong giải quyết việc làm.
Gợi ý biện pháp xử lý
- Tuyên truyền, phổ biến các quyết định và chủ trương, chính sách của quân đội cổ phần hóa doanh nghiệp cho đối tượng quân nhân chuyên nghiệp chưa đến tuổi nghỉ hưu có vấn đề về tư tưởng, xác định tinh thần, trách nhiệm và hoàn thành tốt nhiệm vụ.
- Nắm bắt tâm tư, nguyện vọng, hoàn cảnh, điều kiện gia đình của quân nhân chuyên nghiệp trong đơn vị, có biện pháp giải quyết vướng mắc, bất cập kịp thời.
- Gặp gỡ phổ biến, giáo dục, tuyên truyền số quân nhân chuyên nghiệp thuộc đối tượng nghỉ chính sách nâng cao ý thức chấp hành nghiêm quan điểm, chủ trương của Đảng, quân đội về cổ phần hóa doanh nghiệp, xác định tư tưởng, tình cảm chuyển đổi công tác theo quy định của trên.
- Giáo dục, quán triệt cho sĩ quan, quân nhân chuyên nghiệp, công nhân, viên chức quôc phòng trong đơn vị nhận thức đúng và đồng thuận với đường lối , chủ trương, quan điểm của Đảng, pháp luật của Nhà nước, sẵn sàng nhận và hoàn thành nhiệm vụ.
- Bảo đảm đầy đủ tiêu chuẩn, chế độ, chính sách theo đúng quy định của Bộ Quốc phòng cho số sĩ quan, quân nhân chuyên nghiệp, công chức, viên chức quốc phòng nghỉ chế độ.
- Có chính sách đúng với chủ trương của Đảng, Nhà nước, quân đội cho cán bộ quân nhân chuyên nghiệp, công nhân, viên chức quốc phòng sau khi tinh giản biên chế để ổn định đời sống.
- Tổng hợp tình hình và báo cáo cấp trên.
Tình huống 16. Luật bảo hiểm năm 2014 (có hiệu lực năm 2016), từ ngày 01 tháng 01 năm 2018 mỗi năm công tác của quân nhân chuyên nghiệp chỉ được hưởng thêm tỷ lệ 2% thay cho 3% như trước đây; dẫn đến một số quân nhân, nhất là nữ quân nhân chuyên nghiệp chưa đủ điều kiện nghỉ hưu viết đơn hưởng trợ cấp bảo hiểm xã hội một lần.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, tình cảm, nguyện vọng, nguyên nhân quân nhân chuyên nghiệp xin nghỉ việc hưởng chế độ một lần, thống nhất biện pháp xử lý.
- Gặp gỡ phổ biến, hướng dẫn, định hướng cho quân nhân chuyên nghiệp, công nhân, viên chức quốc phòng nghỉ việc hưởng chế độ bảo hiểm xã hội một lần, nắm vững các quy định của pháp luật Nhà nước, quân đội, xác định tư tưởng nhận và hoàn thành nhiệm vụ được giao.
- Giáo dục, quán triệt cho quân đội nhân dân chuyên nghiệp, công nhân, viên chức quốc phòng trong đơn vị có nhân thức đúng đắn với đương lối, chủ trương của Đảng, pháp luật của Nhà nước, kỷ luật quân đội, sẵn sàng chấp hành nghiêm quy định nghỉ chế độ một lần.
- Quan tâm bảo đảm đầy đủ tiêu chuẩn, chế độ chính sách cho số quân nhân chuyên nghiệp, công nhân, viên chức quốc phòng xuất ngũ theo quy định của quân đội để yên tâm nhận nhiệm vụ.
- Kiện toàn tổ chức biên chế đơn vị đúng quy định của quân đội, đáp ứng với yêu cầu, nhiệm vụ xây dựng đơn vị trong điều kiện mới.
Tình huống 17. Đồng chí trung đội trưởng đánh chiến sĩ với lý do chấp hành không nghiệm chế độ, quy định của đơn vị, bố , mẹ của chiến sĩ biết thông tin rất lo lắng và tức giận.
Gợi ý biện pháp xử lý
- Gặp gỡ riêng cán bộ nắm chắc tình hình sự việc, xác định nguyên nhân, biệp pháp giải quyết. Tổng hợp báo cáo cấp trên xin ý kiến chỉ đạo.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng kỷ luật và mối quan hệ cán bộ, chiến sĩ, dư luận của bộ đội và gia đình quân nhân, xác định biện pháp lãnh đạo, chỉ đạo giải quyết vụ việc.
- Gặp gỡ giáo dục đồng chí trung đội trưởng nhận rõ việc làm sai trái, ảnh hưởng đến bản thân, đơn vị, bản chất, truyền thống quân đội, qua đó nâng cao ý thức chấp hành nghiêm kỹ luật quân đội, pháp luật Nhà nước; triển khai cán bộ viết bản tường trình, bản tự kiểm điểm, tổ chức sinh hoạt đơn vị đề nghị hình thức kỹ luật khách quan, chính xác.
- Tổ chức sinh hoạt rút kinh nghiệm cho đội ngũ cán bộ trong đơn vị, phân tích hiểu rõ việc sai trái, ảnh hưởng đến mối quan hệ đoàn kết cán bộ, chiến sĩ, xây dựng đơn vị vững mạnh; nâng cao ý thức chấp hành kỷ luật quân đội, quy định đơn vị; bồi dưỡng kỹ năng, phương pháp giáo dục, quản lý, chỉ huy bộ đội cho đội ngũ cán bộ.
- Tăng cường kiểm tra, phát hiện, xử lý nghiêm minh đối với những cán bộ vi phạm kỷ luật, nhất là quân phiệt với chiến sĩ.
- Duy trì có chất lượng ngày chính trị văn hóa tinh thần, nắm bắt tâm tư, tình cảm, nhu cầu, nguyện vọng của cán bộ, chiến sĩ, có biện pháp giải quyết kịp thời.
Tình huống 18. Một đồng chí sĩ quan thực hiện nhiệm vụ quản lý, thu chi, sử dụng tài chính của đơn vị chưa rõ ràng, minh bạch làm cho sĩ quan, quân nhân chuyên nghiệp nghi ngờ, gây dư luận xấu
Gợi ý biện pháp xử lý
- Xác minh tình hình, nguyên nhân nảy sinh tư tưởng nghi kỵ lẫn nhau trong quản lý tài chính của đơn vị, đề xuất biện pháp với lãnh đạo, chỉ huy xử lý.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng công tác quản lý tài chính, dư luận của sĩ quan, quân nhân chuyên nghiệp, thống nhất biện pháp giải quyết, khắc phục. Căn cứ tính chất, mức độ nhất định để tổng hợp báo cáo cấp trên và xin ý kiến chỉ đạo (nếu sau khi kiểm tra kết quả đúng như dư luận).
- Gặp gỡ phân tích cho đồng chí sĩ quan làm công tác quản lý tài chính nhận rõ sai sót, khuyết điểm, thực hiện công tác quản lý vật chất, tài sản của đơn vị bảo đảm nguyên tắc, chặt chẽ, công khai minh bạch, không làm ảnh hưởng đến uy tín bản thân, chỉ huy đơn vị, gây dư luận không tốt trong nội bộ và yêu cầu có biện pháp khắc phục, đền bù thâm hụt cho đơn vị. Căn  cứ mức độ hậu quả của thâm hụt tài chính chỉ đạo đồng chí sĩ quan viết bản tường trình, bản kiểm điểm, sinh hoạt đơn vị đề nghị hình thức kỷ luật.
- Tổ chức sinh hoạt đơn vị thông báo cho sĩ quan, quân nhân chuyên nghiệp về kết quả kiểm tra công tác tài chính của cấp trên, rút ra bài học kinh nghiệm trong công tác lãnh đạo, chỉ đạo, quản lý tài chính, cơ sở vật chất, bảo đảm đúng nguyên tắc, chặt chẽ, tạo sự đồng thuận, thống nhất cao.
- Nghiên cứu tham mưu đề xuất bổ sung, sữa đổi quy chế, quy định trong công tác quản lý tài chính của đơn vị bảo đảm đúng nguyên tắc, thủ tục, chặt chẽ, đáp ứng với yêu cầu, nhiệm vụ.
- Duy trì ngiêm chế độ dân chủ ở cơ sở, công khai minh bạch về quản lý tài chính, cơ sở vật chất của đơn vị, tạo sự đoàn kết thống nhất trong sĩ quan, quân nhân chuyên nghiệp.
Tình huống 19. Chỉ huy một đơn vị hàng tháng thực hiện nền nếp, chế độ chạy thử xe, nổ máy, bảo quản, bảo dưỡng trang bị kỷ thuật không đúng quy định quân đội, nhưng vẫn quyết toán xăng, dầu, nảy sinh dư luận xấu trong đơn vị
Gợi ý biện pháp xử lý
- Xác minh sự việc vi phạm chế độ, nguyên tắc quán lý vật tư, nhiên liệu của đơn vị, đề xuất với lãnh đạo, chỉ huy, biện pháp giải quyết.
- Hội ý cấp ủy, chỉ huy đánh giá tình hình duy trì chố độ bảo quản, bảo dưỡng phương tiện xe  - máy sẵn sàng chiến đấu của đơn vị, nguyên nhân nảy sinh dư luận không tốt trong nội bộ, thống nhất biện pháp khắc phục, quy trách nhiệm cá nhân phụ trách. Báo cáo cấp trên chỉ đạo.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm về công tác quản lý, bảo quản, bảo dưỡng phương tiện xe - máy sẵn sàng chiến đấu, vật tư, xăng dầu của đơn vị, nhận rõ hạn chế, khuyết điểm của tập thể, trách nhiệm cá nhân, gây dư luận xấu trong nội bộ, xác định biện pháp khắc phục.
- Tổ chức kiểm điểm, kỷ luật cá nhân, tập thể có liên quan (nếu có sai phạm) trong thực hiện chế độ bảo quản, bảo dưỡng vũ khí trang bị, quản lý vật tư và bồi thường số xăng dầu đã quyết toán sai quy định, công khai cho sĩ quan, quân nhân chuyên nghiệp trong đơn vị biết về nguyên nhân, hình thức kỷ luật.
- Tăng cường kiểm tra của chỉ huy đơn vị về việc chấp hành chế độ baopr quản, bảo dưỡng trang bị kỹ thuật, bảo đảm duy trì nổ máy trở thành nền nếp, thường xuyên đúng quy định, đáp ứng yêu cầu, nhiệm vụ huấn luyện, sẵn sang chiến đấu.
- Tham mưu đề xuất bổ sung, sử đổi quy định, quy chế bảo quản, bảo dưỡng phương tiện kỹ thuật sẵn sang chiến đấu của đơn vị, bảo đảm nghiêm túc, chặt chẽ, khắc phục biểu hiện bớt xén xăng dầu.
- Thực hiện nghiêm túc công tác đăng ký, quản lý xăng dầu, nhiên liệu, tài chính, vật chất của đơn vị  đúng quy định, làm cơ sở thanh tra, kiểm tra, đáp ứng yêu cầu, nhiệm vụ huấn luyện, sẵn sang chiến đấu.
Tình huống 20. Một đồng chí quân nhân chuyên nghiệp làm công tác chuyên môn kỹ thuật, theo yêu cầu của trên phải chuyển đổi đơn vị công tác (theo quy định sau 5 năm), dẫn đến nảy sinh tư tưởng thiếu yên tâm công tác.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật quân nhân chuyên nghiệp và việc thực hiện luân chuyển công tác theo quy định của quân đội, xác định nguyên nhân, thống nhất biện pháp giải quyết.
- Gặp gỡ riêng quân nhân chuyên nghiệp diện luân chuyển công tác do yêu cầu nhiệm vụ, giáo dục, giải thích hiểu rõ quy chế, quy định của quân đội đối tượng làm việc trong các ngành quản lý cán bộ, quân đội, nhằm bảo đảm công bằng, khách quan, chính xác.
- Tổ chức giáo dục, quán triệt cho quân nhân chuyên nghiệp trong đơn vị nâng cao hiểu biết về ý nghĩa, mục đích, yêu cầu, quy chế, quy định của công tác luân chuyến công tác của nhân viên chuyên môn kỹ thuật quân đội là trách nhiệm, vinh dự; qua đó sẵn sàng nhận và hoàn thành tốt nhiệm vụ được giao.
- Quán triệt thực hiện nghiêm các quy chế, quy định về công tác luân chuyển quân nhân chuyên nghiệp của quân đội, đơn vị, bảo đảm dân chủ, công khai, chặt chẽ, tạo thống nhất cao trong nội bộ.
- Quan tâm chăm lo đời sống vật chất, tinh thần cho quân nhân chuyên nghiệp yên tâm, gắn bó xây dựng đơn vị vững mạnh.
- Tổng hợp kết quả xử lý báo cáo với cấp trên.
Tình huống 21. Một đồng chí đại đội trưởng đã nhận tiền và hứa xin việc làm cho một số chiến sĩ sau khi hoàn thành nghĩa vụ quân sự, không xin được cũng không trả lại tiền, gây bức xúc, bất bình cho bộ đội và gia đình quân nhân.
Gợi ý biện pháp xử lý
- Xác minh việc cán bộ nhận tiền xin việc làm cho chiến sĩ, số tiền cụ thể, nguyên nhân sự việc; dự kiến các biện pháp giải quyết, khắc phục, tham mưu cho cấp uỷ, chỉ huy đơn vị.
- Họp cấp ủy, chỉ huy đơn vị đánh giá, nhận định tình hình, tính chất, hậu quả việc cán bộ nhận tiền xin việc làm chi chiến sĩ, thống nhất biện pháp khắc phục. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ riêng đồng chí đại đội trưởng phân tích hiểu rõ về khuyết điểm, hậu quả, tác hại của vi phạm; nâng cao ý thức chấp hành kỷ luật quân đội, quy định của đơn vị; triển khai cho cán bộ viết bản tường trình, bản tự kiểm điểm, tổ chức sinh hoạt chi bộ, đơn vị, đề nghị hình thức kỷ luật phù hợp.
- Tổ chức sinh hoạt đơn vị giáo dục, quán triệt, rút kinh nghiệm cho cán bộ, chiến sĩ hiểu rõ về xin việc làm không đúng chủ trương của quân đội, đơn vị, ảnh hưởng đến bản thân, gia đình; qua đó nâng cao ý thức chấp hành kỷ luật quân đội, quy định đơn vị và bằng mọi biện pháp hoàn trả lại tiền cho gia đình chiến sĩ, ổn định tình hình tư tưởng nội bộ.
- Phối hợp với cấp ủy, chính quyền địa phương tiếp xúc, gặp gỡ gia đình có chiến sĩ đưa tiền cho cán bộ nhờ xin việc làm để giải quyết sự việc thấu tình đạt lý, không làm ảnh hưởng đến quan hệ quân nhân, uy tín đơn vị, hình ảnh Bộ đội Cụ Hồ.
- Thường xuyên phổ biến quán triệt, công khai các kế hoạch, quy định về tuyển sinh, tuyển dụng trong quân đội để chiến sĩ được biết, không để lợi dụng uy tín tuyên truyền làm những việc sai trái.
- Tăng cường quản lý chặt chẽ tư tưởng, kỷ luật và các mối quan hệ xã hội của đội ngũ cán bộ trong đơn vị; kịp thời có biện pháp giáo dục, ngăn chặn, nhất là xin việc làm cho chiến sĩ khi ra quân.
- Báo cáo kết quả giải quyết với cấp trên.
Tình huống 22. Một quân nhân chuyên nghiệp do không hài lòng trong phân công nhiệm vụ đối với lãnh đạo, chỉ huy đã viết bài đăng tải xuyên tạc tình hình đơn vị lên mạng xã hội, gây bức xúc cho sĩ quan, quân nhân chuyên nghiệp
Gợi ý biện pháp xử lý
- Xác minh tình hình việc đăng tải thông tin sai trái lên mạng xã hội của đồng chí quân nhân chuyên nghiệp gây dư luận xấu trong đơn vị; tham mưu với cấp ủy, chỉ huy giải quyết.
- Trao đổi trong cấp ủy, chỉ huy đơn vị thống nhất nhận định về tư tưởng, kỷ luật và việc chấp hành quy định sử dụng mạng xã hội của quân nhân chuyên nghiệp trong đơn vị, thống nhất biện pháp xử lý. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ quân nhân chuyên nghiệp giáo dục, quán triệt, nhận thức rõ việc làm sai trái, có biện pháp khắc phục, nâng cao ý thức chấp hành nghiêm Luật an ninh mạng, kỷ luật quân đội, quy định đơn vị, yêu cầu quân nhân gỡ bỏ thông tin sai trái đăng tải lên mạng xã hội; phối hợp với các cơ quan chức năng kiểm tra đề nghị xử lý kỷ luật theo quy định.
- Căn cứ tính chất, hậu quả, mức độ vi phạm, triển khai quân nhân chuyên nghiệp viết bản tường trình, bản kiểm điểm, sinh hoạt đơn vị đề nghị hình thức kỷ luật đúng mức.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho sĩ quan, quân nhân chuyên nghiệp về việc sử dụng mạng xã hội lan truyền thông tin xấu, sai trái, ảnh hưởng đến an ninh, an toàn đơn vị, nâng cao ý thức chấp hành pháp luật Nhà nước, kỷ luật quân đội, quy định đơn vị.
- Phối hợp chặt chẽ với các cơ quan chức năng của đơn vị, tăng cường kiểm tra, quản lý sĩ quan, quân nhân chuyên nghiệp sử dụng internet sai quy định trong đơn vị, kịp thời chấn chỉnh, khắc phục.
- Nắm, quản lý tình hình tư tưởng, kỷ luật và các mối quan hệ xã hội của sĩ quan, quân nhân chuyên nghiệp trong đơn vị có biện pháp giáo dục, nhắc nhở, nhất là việc chia sẽ thông tin sai trái lên mạng xã hội, gây mất đoàn kết nội bộ.
- Duy trì nghiêm chế độ nền nếp sinh hoạt dân chủ trong đơn vị, công khai minh bạch các lĩnh vực theo quy định của quân đội; không để sĩ quan, quân nhân chuyên nghiệp hiểu nhầm, tuyên truyền kích động, xuyên tạc, làm mất đoàn kết nội bộ.
- Thường xuyên tổ chức quán triệt quy định sử dụng internet của quân đội cho sĩ quan, quân nhân chuyên nghiệp; thực hiện tốt công tác quản lý, không để sĩ quan, quân nhân chuyên nghiệp lợi dụng mạng xã hội lén lút tuyên truyền, kích động làm mất an toàn đơn vị.
- Tổng hợp kết quả báo cáo cấp trên.
Tình huống 23. Một số quân nhân chuyên nghiệp làm nhiệm vụ bảo quản vũ khí, súng đạn, nhất là loại đạn có niên hạn sản xuất lâu năm dễ mất an toàn, làm nảy sinh tư tưởng băn khoăn lo lắng
Gợi ý biện pháp xử lý
- Nắm chắc tình hình tư tưởng, kỷ luật quân nhân chuyên nghiệp, thực trạng trang bị, vũ khí, kỹ thuật, công tác bảo đảm an toàn kho tang của đơn vị, tham mưu cho cấp ủy, chỉ huy giải quyết.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình, tư tưởng quân nhân chuyên nghiệp làm công tác bảo quản, bảo dưỡng vũ khí, trang bị kỹ thuật và những yếu tố tác động bảo đảm an toàn kho tàng, thống nhất biện pháp khắc phục.
- Gặp gỡ số quân nhân chuyên nghiệp làm công tác bảo quản vũ khí, trang bị kỷ thuật, động viên ổn định tư tưởng, tâm lý, tự tin vào khả năng chuyên môn nghiệp vụ, quy trình, nguyên tắc bảo quản, bảo dưỡng, sử dụng súng đạn đã được học tập, trang bị.
- Tổ chức tập huấn chiến sĩ quan, quân nhân chuyên nghiệp về quy trình, quy tắc, phương pháp bảo quản, bảo dưỡng vũ khí súng đạn, nắm vững tính năng, niên hạn sử dụng các loại vũ khí, tạo tâm lý thoải mái, yên tâm thực hiện nhiệm vụ được giao.
- Làm tốt công tác rà soát phân loại đạn dược theo phân cấp, quá niên sử dụng, báo cáo cấp trên xử lý.
- Thường xuyên tổ chức kiểm tra bổ sung, củng cố trang thiết bị phục vụ cho công tác bảo quản vũ khí, khí tài bảo đảm an toàn.
- Quan tâm chăm lo bảo đảm chế độ, tiêu chuẩn đời sống vật chất, tinh thần theo quy định của quân đội để cho quân nhân chuyên nghiệp yên tâm, gắn bó với nhiệm vụ.
Tình huống 24. Một đồng chí sĩ quan trong đơn vị mạo danh đăng tải hình ảnh xuyên tạc đời tư của bạn bè lên mạng xã hội, gây bức xúc cho đồng chí, đồng đội
Gợi ý biện pháp xử lý
- Phối hợp với cơ quan chức năng nắm chắc tình hình tư tưởng, kỷ luật, việc sử dụng mạng xã hội của sĩ quan trong đơn vị, đề xuất biện pháp với cấp ủy, chỉ huy đơn vị giải quyết.
- Hội ý chỉ huy đơn vị đánh giá, nhận định tình hình tư tưởng, kỷ luật của sĩ quan đã mạo danh đăng tải hình ảnh xuyên tạc bôi nhọ đồng đội lên mạng xã hội; điều tra, phát hiện danh tính, đơn vị cụ thể, thống nhất biện pháp giải quyết, phân công cán bộ phụ trách.
- Gặp gỡ đồng chí sĩ quan giáo dục nhận rõ việc làm sai trái ảnh hưởng danh dự, uy tín của đồng chí, đồng đội, gây mất đoàn kết nội, làm lộ bí mật quân sự, nâng cao ý thức chấp hành pháp luật Nhà nước, kỷ luật quân đội, quy định của đơn vị về sử dụng internet.
- Yêu cầu đồng chí sĩ quan gỡ bỏ hình ảnh, thông tin sai trái đăng tải lên mạng xã hội; căn cứ tính chất, mức độ vi phạm, chỉ đạo viết bản tường trình, bản tự kiểm điểm, tổ chức sinh hoạt đơn vị đề nghị hình thức kỷ luật; tạo điều kiện để hai đồng chí trao đổi thắng thắn những vấn đề vướng mắc cá nhân và trực tiếp xin lỗi về việc làm sai trái.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho sĩ quan, quân nhân chuyên nghiệp nâng cao ý thức tôn trọng danh dự, uy tín lẫn nhau, tạo sự đoàn kết gắn bó xây dựng đơn vị vững mạnh, giữ gìn hình ảnh tốt đẹp “Bộ đội Cụ Hồ”, chấp hành nghiêm Luật an ninh mạng, kỹ luật quân đội, quy định đơn vị.
- Tăng cường quản lý chặt chẽ tình hình tư tưởng, kỷ luật và các mối quan hệ xã hội sĩ quan, quân nhân chuyên nghiệp để có biện pháp chấn chỉnh, khắc phục kịp thời.
- Quản lý chặt chẽ tình hình chính trị nội bộ đơn vị, không để kẻ xấu móc nối, lôi kéo kích động sĩ quan, quân nhân chuyên nghiệp tham gia đăng tải thông tin lên mạng xã hội, ảnh hưởng bí mật quân sự, bí mật đơn vị.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 25. Một số quân nhân chuyên nghiệp trong đơn vị do cấp trên sắp xếp công việc trái chuyên môn đào tạo, nảy sinh tư tưởng, thiếu yên tâm công tác, chất lượng hoàn thành nhiệm vụ không cao.
Gợi ý biện pháp xử lý
- Nắm, tìm hiểu nguyên nhân nảy sinh tư tưởng của quân nhân chuyên nghiệp khi bố trí trái với chuyên môn ngành đào tạo và những yêu cầu, nguyện vọng cá nhân.
- Hội ý lãnh đạo, chỉ huy đánh giá thực trạng tình hình biên chế, tổ chức của đơn vị và những vấn đề tư tưởng, kỷ luật quân nhân chuyên nghiệp, thống nhất biện pháp giải quyết. Báo cáo cấp trên xin ý kiến cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ giáo dục, động viên đồng chí quân nhân chuyên nghiệp nắm vững tình hình, đặc điểm, yêu cầu, nhiệm vụ, cơ cấu tổ chức biên chế đơn vị và việc sắp xếp một số chức danh không có trong biến chế; qua đó xác định tư tưởng, trách nhiệm, khắc phục khó khăn, hoàn thành tốt nhiệm vụ được phân công.
- Tổ chức sinh hoạt quán triệt, rút kinh nghiệm cho sĩ quan, quân nhân chuyên nghiệp nhận thức đúng về yêu cầu tổ chức biên chế của đơn vị, trình độ chuyên môn đào tạo, nâng cao ý thức chấp hành sự phân công công tác của cấp ủy đảng, chỉ huy.
- Tổ chức tập huấn, bối dững kinh nghiệm, phương pháp công tác cho quân nhân chuyên nghiệp sắp xếp trái chuyên môn, yên tâm hoàn thành nhiệm vụ.
- Thực hiện luân chuyển quân nhân chuyên nghiệp theo quy định của quân đội bảo đảm dân chủ, công khai, công bằng, phát huy trình độ năng lực công tác.
- Quan tâm chăm lo đời sống vật chất, tinh thần, chính sách hậu phương quân đội cho quân nhân chuyên nghiệp phấn khởi, yên tâm gắn bó xây dựng đơn vị.
II. ĐỐI TƯỢNG HẠ SĨ QUAN, CHIẾN SĨ
Tình huống 26. Một số chiến sĩ trong đơn vị khi huấn luyện, diễn tập ở khu vực rừng sau, có nhiều rắn rết, sên vắt, có biểu hiện lo lắng sợ hãi mất an toàn
Gợi ý biện pháp xử lý
- Kiểm tra an toàn địa bàn diễn tập, tìm hiểu nguyên nhân gây tâm lý sợ hãi cho bộ đội, đề xuất biện pháp cho lãnh đạo, chỉ huy đơn vị có biện pháp xử lý.
- Hội ý chỉ huy đơn vị nhận định, đánh giá đặc điểm, tình hình địa bàn diễn tập, tâm lý sợ hãi của bộ đội, thống nhất chủ trương, biện pháp khắc phục những khó khăn tác động.
- Sinh hoạt đơn vị giáo dục, động viên chiến sĩ nắm vững tình hình, đặc điểm địa bàn, phổ biến kinh nghiệm ứng phó với điều kiện khu vực trú quân, bàn cách phòng ngừa sên vắt, xác định tốt tư tưởng, hoàn thành nhiệm vụ được giáo.
- Tổ chức cho quân y đơn vị tập huấn, hướng dẫn phương pháp phòng, chống rắn rết, sên vắt trước khi diễn tập, không để bộ đội sợ hãi và bất ngờ.
- Chủ động phát hiện khắc phục côn trùng xâm nhập khu trú quân của đơn vị bảo đảm an toàn để bộ đội yên tâm hoàn thành tốt nhiệm vụ.
- Tổ chức rèn luyện cho chiến sĩ trong mọi địa bàn, điều kiện, hoàn cảnh, thời tiết phức tạp, xây dựng tinh thần gan dạ, khắc phục khó khăn, sẵn sàng nhận và hoàn thành tốt nhiệm vụ được giao.
- Phân công chiến sĩ cũ trong tiểu đội, giúp đỡ những chiến sĩ mới tham gia luyện tập, huấn luyện tại địa bàn khó khăn, nhanh chóng ổn định tâm lý và tin tưởng vào khả năng hoàn thành tốt nhiệm vụ.
- Tổ chức rút kinh nghiệm sau mỗi lần diễn tập, huấn luyện, có biện pháp khắc phục, xây dựng tâm lý cho chiến sĩ hàn thành nhiệm vụ.
Tình huống 27. Một số đồng chí trong đại đội ngoài thời gian phục vụ chỉ huy còn tham gia lao động, tăng gia sản xuất, có chiến sĩ cho rằng đã được chỉ huy “ưu tiên”, không phải tham gia huấn luyện
Gợi ý biện pháp xử lý
- Nắm chắc tình hình, tư tưởng, dư luận khác nhau chiến sĩ và việc duy trì chế độ, nền nếp xây dựng chính quy của đơn vị, đề xuất cho lãnh đạo, chỉ huy có biện pháp xử lý phù hợp.
- Gặp gỡ giáo dục cho những chiến sĩ có biểu hiện hiểu nhầm trong phân công giao nhiệm vụ cho bộ đội nắm vững đặc điểm, yêu cầu tổ chức biên chế của đơn vị, xây dựng ý thức sẵn sàng nhận và hoàn thành chức trách được giao
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho chiến sĩ nắm vững tổ chức biên chế, yêu cầu, nhiệm vụ đơn vị, chức trách của quân nhân, không để hiểu nhầm, suy bì, tỵ nạnh, nâng cao tinh thần đoàn kết, giúp đỡ lẫn nhau.
- Căn cứ đặc điểm, tình hình cụ thể của đơn vị có thể tổ chức luân chuyển vị trí công tác cho chiến sĩ để mọi quân nhân được tham gia huấn luyện, rèn luyện, đảm đương tốt cương vị chức trách, nhiệm vụ được giao
- Thường xuyên kiểm tra việc bảo đảm quân số, tham gia huấn luyện nghiêm túc, chặt chẽ, nâng cao chất lượng huấn luyện, sẵn sàng chiến đấu.
- Quan tâm bảo đảm tiêu chuẩn chế độ đời sống vật chất, tinh thần cho chiến sĩ yên tâm gắn bó xây dựng đơn vị.
Tình huống 28. Một chiến sĩ trong đơn vị lần đầu tiên nhận nhiệm vụ rà, phá bom mìn trong điều kiện địa hình, thời tiết khắc nghiệt đã có biểu hiện băn khoăn, lo lắng
Gợi ý biện pháp xử lý
- Nắm vững tình hình tâm tư, nguyện vọng của chiến sĩ làm việc trong điều kiện phức tạp, tham mưu cho cấp ủy, chỉ huy có biện pháp khắc phục.
- Hội ý chi ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỹ luật của chiến sĩ trong thực hiện nhiệm vụ rà, phá bom mìn trong điều kiện khó khăn, phức tạp, thống nhất biện pháp giải quyết, phân công cán bộ phụ trách.
- Gặp gỡ giáo dục, động viên những chiến sĩ có tâm lý lo lắng trong thực hiện nhiệm vụ khó khăn phức tạp hiểu rõ vinh dự, trách nhiệm, quyền lợi, nghĩa vụ, xây dựng ý chí quyết tâm hoàn thành tốt nhiệm vụ được giao.
- Thường xuyên giáo dục, tuyên truyền cho chiến sĩ nâng cao ý thức trách nhiệm, khắc phục khó khăn trong thực hiện nhiệm vụ rà, phá bom mìn, thu gom, quản lý vật liệu nổ đúng nguyên tắc, quy định, bảo đảm an toàn.
- Tổ chức bồi dưỡng kinh nghiệm cho những chiến sĩ mới tham gia thực hiện nhiệm vụ lần đầu về vận chuyển, thu gom, phá hủy vật liệu nổ, xây dựng niềm tin vào khả năng bản thân và kỹ năng, quy trình, quy định, quy tắc bảo đảm an toàn, hoàn thành tốt nhiệm vụ được giao.
- Thường xuyên quan tâm bổ sung công tác bảo đảm các trang thiết bị có độ an toàn cao phục vụ cho công tác rà, phá bom mìn.
- Quan tâm bảo đảm tiêu chuẩn, chế độ chính sách cho chiến sĩ yên tâm, gắn bó với nhiệm vụ.
- Tổ chức sinh hoạt rút kinh nghiệm sau mỗi lần thực hiện nhiệm vụ rà, phá bom mìn để cho chiến sĩ tự tin với nhiệm vụ
Tình huống 29. Đồng chí trung đội trưởng phát hiện một chiến sĩ đang canh gác có mang rượu vào uống và đã phạt chiến sĩ uống hết chai rượu và đã bị say dẫn đến quấy rối, làm nhiều quân nhân trong đơn vị bức xúc với cách xủ phạt của đồng chí trung đội trưởng
Gợi ý biện pháp xử lý
- Nhanh chóng ngăn chặn chiến sĩ có biểu hiện quấy rối do say rượu, sử dụng lực lượng khống chế, bố trí quân y kiểm tra chăm sóc sức khỏe; triển khai các biện pháp cấn thiết ổn định tình hình đơn vị; bố trí chiến sĩ thay thế gác.
- Hội ý chỉ huy đơn vị đánh giá, nhận định tình hình tư tưởng, kỷ luật chiến sĩ về phương pháp quản lý, chỉ huy của đồng chí trung đội trưởng, thống nhất biện pháp giải quyết.
- Triển khai cho cán bộ trung đội trưởng và chiến sĩ viết bản tường trình, bản tự kiểm điểm, sinh hoạt đơn vị phân tích hiểu rõ hạn chế, khuyết điểm, hậu quả, tác hại của vi phạm quy định canh phòng, phương pháp quản lý bộ đội của cán bộ; đề nghị hình thức kỷ luật bảo đảm khách quan, chính xác.
- Tổ chức sinh hoạt đơn vị rút kinh nghiện cho cán bộ, chiến sĩ nâng cao ý thức chấp hành nghiêm điều lệnh canh phòng, quy định về uống rượu, bia trong khi thực hiện nhiệm vụ; phương pháp giáo dục, quản lý, chỉ huy bộ đội của đội ngủ cán bộ các cấp.
- Duy trì nghiêm chế độ, nền nếp xây dựng đơn vị chính quy, quản lý chặt chẽ tư tưởng, kỹ luật và các mối quan hệ xã hội của bộ đội để có biện pháp giáo dục khắc phục kịp thời.
- Gặp gỡ đồng chí trung đội trưởng giáo dục, nhận rõ việc việc làm sai trái, có biện pháp khắc phục, sửa chữa; nâng cao kỹ năng, phương pháp giáo dục, quản lý, chỉ huy bộ đội theo đúng quy định quân đội, đơn vị, khắc phục cách xử phạt vi phạm  nhân cách quân nhân.
- Thường xuyên giáo dục cho chiến sĩ nâng cao ý thức, trách nhiệm chấp hành nghiệm kỷ luật quân đội, quy định canh phòng bảo đảm đúng tư thế tác phong quân nhân, bảo đảm an toàn đơn vị và địa bàn đóng quân.
- Quan tâm chăm lo đời sống vật chất, tinh thần cho chiến sĩ yên tâm, gắng bó với nhiệm vụ.
- Báo cáo cấp trên theo quy định
Tình huống 30. Một chiến sĩ xin chỉ huy đơn vị về nhà để cưới vợ, vì “bố mẹ xem bối” đến ngày xuất ngũ cưới thì không được tuổi, làm chiến sĩ thiếu yên tâm công tác
Gợi ý biện pháp xử lý
- Nắm chắc diễn biến tư tưởng, mỗi quan hệ yêu đương của chiến sĩ, tham mưu cho cấp ủy, chỉ huy đơn vị có biện pháp giải quyết tư tưởng.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, nhất là mối quan hệ yêu đương của chiến sĩ, đặc điểm, yêu cầu, nhiệm vụ đơn vị, thống nhất cách thức giáo dục, định hướng tư tưởng cho chiến sĩ và gia đình quân nhân.
- Gặp gỡ giáo dục, động viên chiến sĩ hiểu rõ quy định của quân đội về quyền lợi, nghĩa vụ, trách nhiệm của quân nhân trong thời gian tại ngũ, xác định tư tưởng, hoàn thành tốt nhiệm vụ được giao.
- Viết thư hoặc điện thoại thông báo với gia đình chiến sĩ biết về quy định của quân đội và quyền lợi, nghĩa vụ, trách nhiệm của quân nhân trong thời gian tại ngũ; qua đó động viên, giáo dục con em yên tâm công tác.
- Phát huy vai trò của tổ tư vấn trợ giúp tâm lý, sức khỏe, pháp luật của đơn vị, tuyên truyền, động viên chiến sĩ nắm vững Luật Nghĩa vụ quân sự, quy định của quân đội trong thời gian làm nghĩa vụ quân sự để yên tâm công tác/
- Thường xuyên tổ chức sinh hoạt đơn vị nắm chắc diễn biến tình hình tư tưởng, kỷ luật bộ đội, có biện pháp giúp đỡ, động viên kịp thời.
Tình huống 31. Một chiến sĩ trong đơn vị khi thực hiện nhiệm vụ dã ngoại đã sàm sỡ với một nữ học sinh, làm cho gia đình và học sinh rất bức xúc
Gợi ý biện pháp xử lý
- Phối hợp với cơ quan chức năng của đơn vị và địa phương khắc phục hậu quả cho học sinh bị quân nhân sàm sở ổn định sức khỏe, tinh thần; lập biên bản hiện trường. Báo cáo cấp trên xin ý kiến chỉ đạo xử lý.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình mối quan hệ của chiến sĩ đối với nữ học sinh trên địa bàn và việc duy trì nền nếp, chế độ xây dựng đơn vị chính quy, quản lý kỷ luật bộ đội, thống nhất biện pháp xử lý.
- Phối hợp đơn vị, địa phương và gia đình động viên nữ học sinh ổn định tâm lý, sức khỏe tiếp tục học tập, công tác; đồng thời thống nhất biện pháp giải quyết hậu quả đúng quy định của pháp luật Nhà nước, kỷ luật quân đội, phù hợp với nguyện vọng chính đáng của gia đình.
- Triền khai cho quân nhân viết bản trường trình, bản tự kiểm điểm, tổ chức sinh hoạt đơn vị phân tích rõ hậu quả, tác hại việc làm sai trái, ảnh hưởng đến bản thân, gia đình, tập thể và bản chất, truyền thống quân đội, có biện pháp sửa chữa, khắc phục; đề nghị hình thức kỷ luật chiến sĩ bảo đảm khách quan, chính xác.
- Sinh hoạt đơn vị rút kinh nghiệm cho cán bộ, chiến sĩ giải quyết tốt mối quan hệ tình cảm quân dân, quan hệ nam nữ trong sạch, lành mạnh, nghiêm túc, có văn hóa, nhất là các cháu chưa đến tuổi thành niên; qua đó chấp hành nghiêm pháp luật Nhà nước, kỷ luật quân đội.
- Tăng cường quản lý tình hình tư tưởng, kỷ luật và các mối quan hệ của quân nhân trong mọi hoạt động của đơn vị, nhất là khi làm nhiệm vụ ngoài doanh trại để có biện pháp phòng ngừa, khắc phục.
- Xây dựng đơn vị có nếp sống vui tươi lành mạnh, quan hệ nam, nữ nghiêm túc, có văn hóa, đấu tranh đẩy lùi các tệ nạn xã hội xâm nhập vào đơn vị.
- Thường xuyên kiểm tra, thu gom, loại bỏ các băng hình, ấn phẩm văn hóa thiếu lành mạnh tác động tư tưởng, nhận thức bộ đội.
- Báo cáo cấp trên theo quy định.
Tình huống 32. Một chiến sĩ chấp hành chế độ, nền nếp xây dựng đơn vị chính quy không nghiêm túc, nói năng thô tục, gây mất đoàn kết nội bộ, bức xúc cho bộ đội
Gợi ý biện pháp xử lý
- Xác minh tình hình tư tưởng kỷ luật, phẩm chất đạo đức của chiến sĩ, tham mưu cho cấp ủy, chỉ huy biện pháp giải quyết.
- Hội ý cấp ủy, chỉ huy đơn vị nhận định, đánh giá tình hình tư tưởng, kỷ luật chiến sĩ, nhất là biểu hiện cá biệt, hay vi phạm kỷ luật, thống nhất biện pháp giải quyết.
- Gặp gỡ chiến sĩ hay gây gổ lẫn nhau trong đơn vị giáo dục, hiểu rõ việc làm mất đoàn kết nội bộ, nâng cao ý thức chấp hành kỷ luật quân dội, quy định đơn vị; triển khai cho chiến sĩ viết bản trường trình, kiểm điểm, sinh hoạt đơn vị kiểm điểm và đề nghị hình thức kỷ luật, nghiêm túc, chặt chẽ (nếu đến mức phải xử lý kỷ luật).
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho chiến sĩ nâng cao ý thức chấp hành kỷ luật quân đội, quy định đơn vị, tích cực học tập, rèn luyện nâng cao phẩm chất, đạo đức tư cách người quân nhân cách mạng, giữ gìn phẩm chất tốt đẹp “Bộ đội Cụ Hồ”, tinh thần đoàn kết giúp đỡ lẫn nhau, xây dựng đơn vị vững mạnh.
- Duy trì nghiêm chế độ nền nếp xây dựng đơn vị chính quy, quản lý chặt chẽ tình hình tư tưởng, kỷ luật và các mội quan hệ xã hội của bộ đội, nhất là trong ngày nghỉ, giờ nghỉ, hoạt động ngoài doanh trại để có biện pháp giáo dục kịp thời.
- Tổ chức hoạt động văn hóa tinh thần, tạo không khí vui tươi, lành mạnh để cán bộ, chiến sĩ yên tâm xây dựng đơn vị.
Tình huống 33. Đồng chí tiểu đội trưởng trong đơn vị đánh chiễn sĩ mới, do chấp hành chế độ, nền nếp không nghiêm, làm cho chiến sĩ bỏ đơn vị về nhà
Gợi ý biện pháp xử lý
- Xác minh tình hình, nguyên nhân cán bộ đánh chiến sĩ và diễn biến tư tưởng, đề xuất biện pháp giải quyết với cấp ủy, chỉ huy đơn vị.
- Trao đổi trong cấp ủy, chỉ huy đơn vị đánh giá tình hình, nguyên nhân, hậu quả mất đoàn kết của cán bộ, chiến sĩ, thống nhất biện pháp giải quyết; báo cáo cấp trên xin ý kiến chỉ đạo.
- Phối hợp với gia đình và chính quyền địa phương động viên chiến sĩ lên đơn vị tiếp tục công tác, bỏ qua mặc cảm trong quan hệ cán bộ, chiến sĩ, xác định rõ nhiệm vụ, khắc phục mọi khó khăn, hoàn thành tốt nhiệm vụ.
- Gặp gỡ đồng chí tiểu đội trưởng giáo dục, nhắc nhở hiểu rõ việc làm sai trái trong quan hệ cán bộ, chiến sĩ, có biện pháp khắc phục, sửa chữa, nâng cao ý thức chấp hành kỷ luật quân đội, quy định đơn vị; triển khai cả hai đồng chí viết bản trường trình, bản tự kiểm điểm, sinh hoạt đơn vị đề nghị hình thức kỷ luật trên từng lỗi phạm.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho cán bộ, chiến sĩ, nâng cao ý thức chấp hành pháp luật Nhà nước, kỷ luật quân đội; giải quyết tốt mối quan hệ đồng chí, đồng đội trên quan điểm chân tình, thương yêu, giúp đỡ lẫn nhau, chia sẻ khó khăn trong công tác, rèn luyện, hoàn thành nhiệm vụ.
- Trực tiếp gặp gỡ, hoặc điện thoại trao đổi thông tin tạo sự cảm thông, chia sẽ với những bức xúc của gia đình chiến sĩ, đề cao trách nhiệm quản lý, giáo dục cán bộ thuộc quyền chấp hành nghiêm kỷ luật quân đội, pháp luật Nhà nước.
- Tăng cường kiểm tra chấn chỉnh, phương pháp giáo dục, quản lý bộ đội của cán bộ tiểu đội trưởng thực hiện đúng chức trách, nhiệm vụ và thẩm quyên xử lý kỷ luật.
- Xử lý nghiêm kỷ luật đối với cán bộ tiểu đội quân phiệt với chiến sĩ để răn đe và phòng ngừa.
- Duy trì nghiêm túc chế độ, nền nếp sinh hoạt ngày chính trị văn hóa tinh thần, kịp thời nắm bắt tâm tư, tình cảm, nguyện phọng chiến sĩ, nhất là những vấn đề khó khăn, vướng mắc có biện pháp giải quyết.
- Báo cáo kết quả xử lý vụ việc lên cấp trên theo quy định.
Tình huống 34. Một chiến sĩ biết được người yêu đã nhận lời yêu thương người khác, do đó nảy sinh tư tưởng buồn chán, có ý định tự sát
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình mối quan hệ yêu đương của chiến sĩ, phân công cán bộ theo dõi, thống nhất biện pháp giúp đỡ cho chiến sĩ.
- Gặp gỡ chiến sĩ có biểu hiện tư tưởng chán nản, động viên, giúp đở hiểu biết về quan hệ yêu đương là xuất phát từ tình cảm của đôi bên nam, nữ và tự nguyện đến với nhau, nếu chưa phù hợp thì có quyền lựa chọn người khác; qua đó ổn định tâm lý, tư tưởng tham gia công tác cùng đơn vị.
- Phối hợp với gia đình, người thân, bạn bè động viên, giúp đỡ chiến sĩ vượt qua khó khăn, kìm chế bức xúc trong tình cảm yêu đương, ổn định về tư tưởng, tâm lý, không để có hành động cực đoan, gây hậu quả nghiêm trọng.
- Phối hợp với đoàn thanh niên địa phương tổ chức giao lưu, tọa đàm, văn hóa văn nghệ tuyên truyền Luật Hôn nhân và Gia đình, kỹ năng sống, giúp quân nhân giải quyết vướng mắc về tư tưởng, tình cảm, tình yêu nam, nữ.
- Tăng cường quản lý tư tưởng, kỷ luật chiến sĩ trong mọi hoạt động của đơn vị, nhất là quan hệ yêu đương nam, nữ để chủ động giáo dục, động viên, giúp đở phù hợp.
- Báo cáo cấp trên theo quy định
Tình huông 35. Một chiến sĩ được đơn vị giao nhiệm vụ lao động trong ngày nghỉ đã rủ nhau chặt trộm mía của dân, gây dư luận xấu trong đơn vị và nhân dân
Gợi ý biện pháp xử lý
- Phối hợp với chính quyền địa phương ngăn chặn sự việc xảy ra; lập biên bản sự việc.
- Hội ý chỉ huy đơn vị đánh giá tình hình, tư tưởng kỷ luật và công tác duy trì quản lý, chỉ huy bộ đội của cán bộ các cấp, thống nhất biện pháp giải quyết. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Phối hợp với chính quyền địa phương gặp gỡ gia đình có tài sản bị xâm hại giải quyết có lý có tình, đền bù, khắc phục hậu quả phù hợp.
- Giáo dục, quán triệt cho quân nhân nâng cao ý thức chấp hành kỷ luật quân đội, pháp luật Nhà nước, nhất là kỷ luật dân vận, hiểu rõ tính chất, hậu quả xâm hại tài sản nhân dân, làm ảnh hưởng đến bản thân, đơn vị, bản chất truyền thống Bộ đội Cụ Hồ; triển khai chiến sĩ viết bản trường trình, bản tự kiểm điểm, sinh hoạt đơn vị đề nghị hình thức kỷ luật  đúng quy định của quân đội.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho cán bộ, chiến sĩ, nâng cao ý thức chấp hành kỷ luật quân đội, pháp luật Nhà nước, nhất là kỷ luật dân vận không làm ảnh hưởng đến đơn vị, phẩm chất Bộ đội Cụ Hồ.
- Quản lý chặt chẽ tư tưởng, kỷ luật bộ đội, nhất là hoạt động, công tác ở khu vực địa bàn dân cư để có biện pháp giải quyết kịp thời.
- Tổng hợp tình hình báo cáo cấp trên và địa phương có liên quan
Tình huống 36. Một chiến sĩ trong thời gian ngày nghỉ cuối tuần đã mượn xe máy của người dân gần đơn vị tham gia giao thông xảy ra tai nạn, gây tâm lý lo lắng trong đơn vị
Gợi ý biện pháp xử lý
- Nhanh chóng khắc phục hậu quả tai nạn, đưa chiến sĩ và người bị nạn đi cấp cứu, phối hợp cơ quan chức năng có liên quan lập biên bản, bảo vệ hiện trường. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình ý thức chấp hành kỷ luật, công tác quản lý chiến sĩ sử dụng phương tiện tham gia giao thông, thống nhất biện pháp giải quyết hậu quả sự việc.
- Phối hợp với bệnh viện cứu chữa cho quân nhân và người bị nạn khắc phục hậu quả tai nạn, ổn định sức khỏe, tinh thần, thông báo cho gia đình, người thân giúp đỡ.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho cán bộ, chiến sĩ nhận rõ hậu quả, tác hại của tai nạn giao thông, nâng cao ý thức chấp hành kỷ luật quân đội, quy định đơn vị, tham gia giao thông bảo đảm an toàn.
- Chỉ đạo cho chiến sĩ viết bản trường trình, bản tự kiểm điểm, tổ chức sinh hoạt đơn vị đề nghị hình thức kỷ luật và giải quyết hậu quả tai nạn cho người bị nạn, bồi thường hư hại tài sản cho người dân.
- Tăng cường quan lý cán bộ, chiên sĩ chấp hành nghiêm kỷ luật quân đội, quy định đơn vị về sử dụng phương tiện tham gia giao thông bảo đảm an toàn.
- Phối hợp với cấp ủy, chính quyền địa phương tổ chức tuyên truyền cho nhân dân hiểu rõ quy định của quân đội đối với chiến sĩ không được sử dụng phương tiện xe máy tham gia giao thông để phối hợp giáo dục, quản lý.
- Báo cáo cấp trên kết quả xử lý vụ việc.
Tình huống 37. Một số chiến sĩ hay ra ngoài doanh trại ăn uống, chơi đề, gây nợ nần không có khả năng chi trả, tạo dư luận xấu trong đơn vị và nhân dân
Gợi ý biện pháp xử lý
- Xác minh tình hình, tư tưởng kỷ luật, lối sống sinh hoạt của chiến sĩ trong đơn vị, tham mưu cho cấp ủy, chỉ huy biện pháp giải quyết vụ việc.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng kỷ luật, chi tiêu sinh hoạt của chiến sĩ, phân loại mức độ, tính chấp vay nợ, thống nhất biện pháp giải quyết; phân công cán bộ phụ trách. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ, giáo dục chiến sĩ hiểu rõ khuyết điểm, tác hại, hậu quả của chi tiêu sinh hoạt tự do tùy tiện, gây nợ nần không có khả năng chi trả, ảnh hưởng đến bản thân, gia đình, đơn vị, yêu cầu có biện pháp giải quyết, khắc phục số nợ trên, nâng cao ý thức chấp hành kỷ luật quân đội, quy định đơn vị.
- Triển khai cho chiến sĩ viết bản trường trình, bản tự kiểm điểm, sinh hoạt đơn vị đề nghị hình thức kỷ luật đúng mức; đồng thời phối hợp với gia đình thanh toán số tiền quân nhân vay nợ của chủ quán.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho chiến sĩ nâng cao ý thức chấp hành kỷ luật quân đội, quy định đơn vị; thực hiện chi tiêu sinh hoạt cá nhân có kế hoạch, tiết kiệm, phù hợp với điều kiện hoàn cảnh kinh tế bản thân, gia đình và môi trường công tác.
- Tăng cường duy trì nghiêm chế độ nền nếp xây dựng đơn vị chính quy, quản lý tư tưởng, kỷ luật và các mối quan hệ xã hội, chi tiêu sinh hoạt khoa học, tiết kiệm của chiến sĩ, nhất là hoạt động ngoài doanh trại.
- Cùng với cấp ủy, chính quyền và nhân dân địa phương trên địa bàn phối hợp giáo dục, quản lý bộ đội mua bán, chi tiêu sinh hoạt đúng quy đinh pháp luật, kỷ luật quân đội, phù hợp với điều kiện bản thân.
- Xây dựng đơn vị có môi trường trong sạch, lành mạnh, có văn hóa, bảo đảm đầy đủ vật chất để cán bộ, chiến sĩ yên tâm gắn bó xây dựng đơn vị.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 38. Một số chiến sĩ trong đơn vị lấy lý do có tuổi đời cao hơn tuổi trung đội trưởng, nên có biểu hiện chấp hành mệnh lệnh không nghiêm, gây dư luận xấu trong đơn vị
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật của chiến sĩ, nguyên nhân, thống nhất biện pháp giải quyết.
- Gặp gỡ chiến sĩ “lớn tuổi” giáo dục, quán triệt nâng cao ý thức chấp hành kỷ luật quân đội, mệnh lệnh người chỉ huy; giải quyết tốt mối quan hệ giữa cấp trên với cấp dưới đúng Điều lệnh Quản lý bộ đội.
- Chỉ đạo chiến sĩ viết bản trường trình, bản tự kiểm điểm sinh hoạt các tổ chức trong đơn vị rút kinh nghiệm.
- Yêu cầu đồng chí trung đội trưởng duy trì nghiêm túc chế độ nền nếp xây dựng đơn vị chính quy, giải quyết tốt mối quan hệ cán bộ, chiến sĩ đúng quy định của Điều lệnh Quản lý bộ đội.
- Chỉ đạo tổ chức cho quần chúng trong đơn vị tổ chức giao lưu, tọa đàm, văn hóa văn nghệ, tuyên truyền cho cán bộ, chiến sĩ hiểu biết về Điều lệnh Quản lý bộ đội, chế độ nền nếp xây dựng chính quy, giải quyết tốt mối quan hệ cấp trên với cấp dưới đúng quy định.
- Bồi dưỡng kỷ năng, phương pháp quản lý, chỉ huy bộ đội đúng quy định Điều lệnh Quản lý bộ đội, thực hiện đúng chức trách, nhiệm vụ của cán bộ cấp trên với cấp dưới, giải quyết mối quan hệ có tình, hợp lý, thuyết phục.
- Đông viên cán bộ trong đơn vị tích cực học tập, rèn luyện, nâng cao trình độ, phẩm chất, năng lực, phương pháp, tác phong công tác, gương mẫu trong lời nói, việc làm để cán bộ, chiến sĩ noi theo.
Tình huống 39. Một số chiến sĩ lén lút sử dụng điện thoại thông minh đăng tải xuyên tạc tình hình đơn vị lên mạng xã hội, làm cho gia đình và bạn bè quân nhân khi truy cập, gây bức xúc, lo lắng
Gợi ý biện pháp xử lý
- Nắm tình hình tư tưởng, chấp hành kỷ luật sử dụng internet, mạng xã hội của chiến sĩ, đề xuất biện pháp giải quyết cho cấp ủy, chỉ huy đơn vị.
- Hội ý chỉ huy đơn vị đánh giá việc quản lý quân nhân sử dụng internet, mạng xã hội gây dư luận xấu trong nội bộ, thống nhất biện pháp giải quyết trong cấp ủy, chỉ huy; phân công cán bộ phụ trách.
- Gặp gỡ chiến sĩ chỉ đạo nhanh chóng gỡ bỏ thông tin sai trái trên mạng xã hội, giáo dục, nâng cao ý thức chấp hành Luật An ninh mạng, kỷ luật quân đội, quy định sử dụng internet trong đơn vị; triển khai chiến sĩ viết bản trường trình, bản tự kiểm điểm, tổ chức sinh hoạt đơn vị đề nghị hình thức kỷ luật đúng quy định quân đội.
- Tổ chức sinh hoạt rút kinh nghiệm cho cán bộ, chiến sĩ nhận thức đúng đắn quy định sử dụng mạng xã hội của đơn vị, kỷ luật quân đội, hiểu rõ tác hại của đăng tải thông tin sai trái, ảnh hưởng tư tưởng đồng chí, đồng đội, làm mất đoàn kết nội bộ, lộ bí mật quân đội.
- Thông báo cho gia đình biết quy định của đơn vị về việc sử dụng điện thoại đối với chiến sĩ để phối hợp giáo dục thực hiện.
- Thường xuyên giáo dục, quán triệt sâu sắc các chỉ thị, quy định, hướng dẫn sử dụng internet, mạng xã hội của đơn vị cho chiến sũ thực hiện nghiêm túc, chặt chẽ.
- Làm tốt công tác rà soát chính trị nội bộ không để chiến sĩ sử dụng điện thoại đăng tải hình ảnh tin, bài sai trái làm ảnh hưởng đến an ninh, an toàn đơn vị.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 40. Chỉ huy đơn vị đã phối hợp với gia đình giáo dục thuyết phục một chiến sĩ hay vi phạm kỷ luật, do phương pháp động viên còn cứng nhắc, làm chiến sĩ nản đã uống thuốc trừ sâu tự tử
Gợi ý biện pháp xử lý
- Nhanh chống bằng mọi biện pháp cứu chữa.
- Phối hợp với gia đình, địa phương, bạn bè đồng hương nắm tình hình tư tưởng, kỷ luật, các mối quan hệ của chiến sĩ, nhất là biểu hiện mới phát sinh, tham mưu cho cấp ủy, chỉ huy đơn vị giải quyết.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật, các mối quan hệ của chiến sĩ, nguyên nhân chiến sĩ uống thuốc trừ sâu tự tử, thống nhất biện pháp xử lý.
- Chỉ đạo cho quân y đơn vị phối hợp với bệnh viện và gia đình cứu chữa cho chiến sĩ ổn định sức khỏe, củng cố tâm lý, tinh thần.
- Phân công cán bộ, đảng viên, đồng đội động viên, giúp đở chiến sĩ nhanh chống ổn định sức khỏe, tâm lý, tinh thần; tự nhận thấy sai lầ, khuyết điểm, không nên có hành động tiêu cực, bất mãn ảnh hưởng bản thân, gia đình, đơn vị.
- Tổ chức rút kinh nghiệm trong cán bộ về phương pháp giáo dục, quản lý chỉ huy bộ đội, nắm chắc đặc điểm, tâm lý, trình độ nhận thức bộ đội để có biện pháp phù hợp; không nóng vội, chủ quan, gây hậu quả xấu, nhất là những đồng chí có tư tưởng bất thường, cá biệt.
- Tổ chức sinh hoạt đơn vị đóng góp phê bình nhắc nhở, khắc phục sai lầm, khuyết điểm của chiến sĩ, nếu vi phạm kỷ luật phải xử lý đúng mức.
- Thường xuyên tổ chức tốt hoạt động văn hóa tinh thần, vui chơi giải trí tạo không khí vui tươi, sôi nỗi, xây dựng đơn vị trong sạch, lành mạnh, có văn hóa; cán bộ, chiến sĩ đoàn kết thương yêu, giúp đỡ lẫn nhau, khắc phục khó khăn, hoàn thành tốt nhiệm vụ được giao.
- Duy trì tốt sinh hoạt tổ ba người, sinh hoạt dân chủ cơ sở trong đơn vị lắng nghe tâm tư, nguyện vọng của chiến sĩ để có biện pháp giáo dục, động viên phù hợp.
- Duy trì nghiêm chế độ nền nếp xây dựng đơn vị chính quy, quản lý tư tưởng, kỷ luật bộ đội, nhất là những đồng chí có quan hệ yêu đương nam, nữ không bình thường, gia đình có hoàn cảnh đặc biệt khó khăn; kịp thời có biện pháp ngăn chặn, không để sự việc đáng tiếc xảy ra.

III. ĐỐI TƯỢNG CHIẾN SĨ MỚI
Tình huống 41. Trong quá trình huấn luyện chiến sĩ mới, một số chiến sĩ nữ nhớ gia đình, hay xin gọi điện thoại, thiếu yên tâm tư tưởng trong thực hiện nhiệm vụ
Gợi ý biện pháp xử lý
- Tìm hiểu đặc điểm tâm lý, tình cảm của chiến sĩ nữ, đề xuất cấp ủy, chỉ huy đơn vị cách thức động viên.
- Hội ý chỉ huy đơn vị nhận định, đánh giá tình hình tư tưởng, tình cảm, mối quan hệ gia đình, bạn bè của chiến sĩ nữ, thống nhất biện pháp động viên, giúp đỡ, phân công cán bộ phụ trách.
- Gặp gỡ, động viên chiến sĩ nữ tích cực tham gia các hoạt động huấn luyện, văn hóa văn nghệ, thể dục thể thao, vui chơi giải trí, tạo không khí tích cực, vui tươi, sôi nỗi trong đơn vị, khắc phục biểu hiện buồn chán, nhớ gia đình.
- Thường xuyên giáo dục, động viên chiến sĩ hiểu rõ trách nhiệm, vinh dự, tự hào của người chiến sĩ đứng trong hàng ngũ quân đội, phát huy truyền thống gia đình, quê hương phấn đấu hoàn thành tốt nhiệm vụ được giao.
- Tổ chức hoạt động tọa đàm, giao lưu văn hóa văn nghệ, tổ chức cho chiến sĩ tham quan di tích lịch sử cách mạng (nếu có điều kiện), khơi dậy tình yêu quê hương, đất nước, yên tâm huấn luyện, xây dựng đơn vị vững mạnh, hoàn thành tốt nhiệm vụ.
- Duy trì có hiệu quả các cuộc vận động trong quân đội, phong trào thi đua của đơn vị với những mục tiêu, chỉ tiêu cụ thể, thiết thực; động viên chiến sĩ tích cực tham gia huấn luyện, rèn luyện kỷ luật, xây dựng đơn vị chính quy.
- Tổ chức tốt các hoạt động văn hóa tinh thần, vui chơi giải trí, tạo không khí vui tươi, lành mạnh, đoàn kết, gắn bó giúp đỡ lẫn nhau, tin tưởng vào khả năng của bản thân hoàn thành tốt nhiệm vụ.
- Quan tâm chăm lo bảo đảm đời sống vật chất, tinh thần cho chiến sĩ yên tâm, gắn bó với nhiệm vụ.
Tình huống 42. Luật nghĩa vụ quân sự sửa đổi bổ sung năm 2015 quy định thời gian thực hiện nghĩa vụ của chiến sĩ làm 24 tháng (kéo dài 6 tháng so với luật trước đây), làm cho một số chiến sĩ băn khoăn, lo lắng
Gợi ý biện pháp xử lý
- Tìm hiểu tâm tư, tình cảm, nhu cầu nguyện vọng của chiến sĩ mới với những vấn đề còn vướng mắc, bất cập, đề xuất biện pháp giáo dục, quán triệt.
- Hội ý chỉ huy đơn vị nhận định những vấn đề còn băn khoăn, vướng mắc của chiến sĩ mới, thống nhất biện pháp giáo dục, tuyên truyền, nâng cao nhận thức ý nghĩa của việc kéo dài thời gian trong thực hiện nghĩa vụ quân sự.
- Gặp gỡ giáo dục, tuyên truyền nâng cao nhận thức cho chiến sĩ mới về Luật Nghĩa vụ quân sự (những điểm mới được sửa đổi, bổ sung) về thời gian thực hiện nghĩa vụ quân sự dài hơn so với Luật Nghĩa vụ quân sự trước đây; qua đó xây dựng ý thức, trách nhiệm hoàn thành nhiệm vụ.
- Tổ chức sinh hoạt ngày chính trị văn hóa tinh thần, tọa đàm, trao đổi, quán triệt cho chiến sĩ hiểu biết sâu sắc Luật Nghĩa vụ quân sự sửa đổi năm 2015, những vấn đề mới, ý nghĩa của việc thực hiện; từ đó đề cao ý thức, trách nhiệm thực hiện tốt nhiệm vụ được giao.
- Thường xuyên nắm, quản lý tình hình tư tưởng, kỷ luật bộ đội trong mọi hoạt động của đơn vị, có biện pháp giáo dục, động viên kịp thời.
- Quan tâm bảo đảm đời sống vật chất, tinh thần, nhu cầu chính đáng cho chiến sĩ yên tâm với nhiệm vụ.
Tình huống 43. Một số chiến sĩ mới có biểu hiện sợ hãi khi gác một mình nơi vắng vẻ, nên muốn nhờ đồng đội gác hộ, hay trốn tránh nhiệm vụ
Gợi ý biện pháp xử lý
- Tìm hiểu tâm lý của chiến sĩ mới khi thực hiện nhiệm vụ gác một mình trong điều kiện ban đêm vắng người, đề xuất cho cấp ủy, chỉ huy biện pháp giúp đỡ ổn định tâm lý.
- Gặp gỡ giáo dục, giải thích cho chiến sĩ mới về yêu cầu, nhiệm vụ của đơn vị, những khó khăn vất vả trong huấn luyện, rèn luyện kỷ luật, xây dựng chính quy để củng cổ tư tưởng, tâm lý thực hiện tốt nhiệm vụ canh phòng bảo vệ an toàn đơn vị.
- Tổ chức sinh hoạt rút kinh nghiệm cho chiến sĩ trong đơn vị làm nhiệm vụ canh phòng là trách nhiệm của mỗi quân nhân và chế độ, nền nếp công tác của đơn vị, do đó thường xuyên quán triệt, giáo dục, xác định trách nhiệm, quyết tâm hoàn thành tốt nhiệm vụ.
- Phân công cho chiến sĩ cũ hoặc chiến sĩ gan dạ cùng cặp đội tham gia canh gác củng cố tâm lý và quen dần với môi trường hoạt động.
- Tổ chức giáo dục, rèn luyện cho chiến sĩ thực hiện nhiệm vụ canh phòng trong mọi điều kiện, thời gian, thời tiết phức tạp, xây dựng ý chí vững vàng , khắc phục khó khăn hoàn thành nhiệm vụ.
- Duy trì nghiêm chế độ công tác canh phòng đúng quy định quân đội, bảo đảm tư thế tác phong nghiêm túc, an toàn đơn vị và khu vực đóng quân.
- Xử lý nghiêm kỷ luật đối với những đồng chí vi phạm quy định canh phòng để răn đe cảnh báo, bảo đảm an toàn đơn vị.
Tình huống 44. Trong thời gian đầu nhập ngũ, một số chiến sĩ thường tự ý đi căn tin ăn quà, chấp hành chế độ, nền nếp của đơn vị chưa nghiêm, chất lượng công tác hạn chế
Gợi ý biện pháp xử lý
- Nắm chắc đặc điểm, tâm lý của chiến sĩ mới và việc duy trì chế độ, nền nếp xây dựng đơn vị chính quy, đề xuất các biện pháp giáo dục bộ đội.
- Hội ý cấp ủy, chỉ huy đánh giá đặc điểm, tâm lý của chiến sĩ mới, yêu cầu nhiệm vụ của đơn vị, thống nhất biện pháp giáo dục, quản lý, phân công cán bộ duy trì, kiểm tra.
- Gặp gỡ những chiến sĩ chấp hành chế độ không nghiêm, giáo dục nhận rõ những hạn chế, khuyết điểm trong thực hiện quy định xây dựng chính quy, chi tiêu sinh hoạt cá nhân tùy tiện, thiếu hòa đồng với tập thể; qua đó xây dựng ý thức tự giác rèn luyện, chấp hành nghiêm các quy định của đơn vị đề ra.
- Sinh hoạt đơn vị giáo dục, quán triệt rút kinh nghiệm cho chiến sĩ nâng cao ý thức chi tiêu cá nhân phù hợp với điều kiện bản thân, gia đình; đồng thời xây dựng ý thức chấp hành nghiêm nền nếp xây dựng đơn vị chính quy, kỷ luật quân đội.
- Gặp gỡ riêng động viên những đồng chí có tác phong tự do tùy tiện hòa đồng với mọi sinh hoạt chung của tập thể, tạo sự tôn trọng lẫn nhau, chấp hành chế độ nền nếp chính quy, thực hiện tốt chức trách, nhiệm vụ được giao.
- Nắm, quản lý tư tưởng, kỷ luật bộ đội trong mọi hoạt động của đơn vị, kịp thời nhắc nhở và rút kinh nghiệm trong giao ban, hội ý.
- Quan tâm chăm lo đời sống vật chất, tinh thần, tạo không khí vui tươi lành mạnh cho chiến sĩ yên tâm công tác.
- Đẩy mạnh phong trào thi đua huấn luyện giỏi, kỷ luật nghiêm, biểu dương kịp thời những tập thể, cá nhân có thành tích, xử lý kỷ luật nghiêm túc đối với những chiến sĩ vi phạm quy định của đơn vị.
Tình huống 45. Một đồng chí trung đội trưởng hay quát mắng, miệt thị chiến sĩ trong huấn luyện, tập luyện, làm cho một số đồng chí lo lắng, xa lánh cán bộ, thiếu yên tâm công tác
Gợi ý biện pháp xử lý
- Nắm chắc đặc điểm, tâm lý lo lắng sợ hãi, xa lánh cán bộ của chiến sĩ, phương pháp, tác phong công tác của cán bộ, tham mưu cho cấp ủy, chỉ huy biện pháp khắc phục.
- Hội ý cấp ủy, chỉ huy đơn vị nhận định, đánh giá tình hình, tư tưởng, tâm lý của chiến sĩ, phương pháp tác phong công tác của cán bộ trung đội trưởng, thống nhất phương pháp giải quyết sự việc.
- Gặp gỡ đồng chí trung đội trưởng góp ý về phương pháp, tác phong công tác giáo dục, quản lý, chỉ huy bộ đội, nhất là giải quyết mối quan hệ cán bộ với chiến sĩ.
- Tổ chức sinh hoạt rút kinh nghiệm cho đội ngũ cán bộ trong đơn vị nâng cao ý thức rèn luyện phương pháp, tác phong công tác gần gũi, hòa đồng, đoàn kết gắn bó với chiến sĩ, xứng danh là người anh, người đồng chí, khắc phục khó khăn hoàn thành tốt nhiệm vụ.
- Tăng cường kiểm tra đội ngũ cán bộ thuộc quyền chấp hành nghiêm kỷ luật quân đội, quy định đơn vị, bồi dưỡng phương pháp giáo dục, quản lý, chỉ huy bộ đội đúng quy định của Điều lệnh Quản lý bộ đội.
- Tổ chức tốt hoạt động ngày chính trị văn hóa tinh thần, dân chủ cơ sở để bộ đội phản ánh tâm tư, nguyện vọng, đóng góp xây dựng phương pháp, tác phong công tác cho đội ngũ cán bộ, khắc phục hạn chế, khuyết điểm.
Tình huống 46. Một đồng chí tiểu đội trưởng trong đơn vị hay gạ gẫm chiến sĩ mới mua quà, nếu không mua sẽ phân biệt đối xử, làm cho nhiều chiến sĩ bức xúc
Gợi ý biện pháp xử lý
- Nắm dư luận của chiến sĩ phản ánh về đồng chí tiểu đội trưởng hay gạ gẫm chiến sĩ mua quà; tham mưu cho lãnh đạo, chỉ huy có biện pháp giải quyết vụ việc.
- Hội ý chỉ huy đơn vị nhận định, đánh giá tình hình tư tưởng kỷ luật của tiểu đội trưởng, thống nhất biện pháp giải quyết, phân công cán bộ phụ trách.
- Gặp gỡ đồng chí tiểu đội trưởng giáo dục nhận rõ khuyết điểm, hạn chế, có biện pháp khắc phục, nâng cao ý thức chấp hành nghiêm kỷ luật quân đội, quy định đơn vị, rèn luyện phẩm chất, đạo đức, tư cách người cán bộ, xây dựng tình cảm yêu thương, giúp đỡ chiến sĩ.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho cán bộ tiểu đội trưởng nâng cao tinh thần yêu thương, giúp đỡ lẫn nhau, chia sẻ khó khăn với đồng chí, đồng đội, rèn luyện phẩm chất, đạo đức tư cách người quân nhân, phương pháp tác phong công tác, đáp ứng yêu cầu, nhiệm vụ.
- Thường xuyên kiểm tra cán bộ tiểu đội trưởng trong thực hiện chức trách, nhiệm vụ, kịp thời phát hiện, nhắc nhở, khắc phục những biểu hiện sai trái.
- Nâng cao chất lượng sinh hoạt ngày chính trị văn hóa tinh thần, dân chủ cơ sở, tạo điều kiện cho bộ đội đóng góp xây dựng phương pháp, tác phong công tác cho đội ngũ cán bộ trong đơn vị.
Tình huống 47. Một số chiến sĩ mới cho rằng, hiện nay có gia đình lên thăm con đã “gửi gắm” cho cán bộ, nên được “ưu tiên” trong chấp hành một số chế độ quy định
Gợi ý biện pháp xử lý
- Nắm biểu hiện về sự ganh tỵ, nghi kỵ lẫn nhau trong chiến sĩ về thực hiện các chế độ quy định của quân đội; cần giải quyết tốt mối quan hệ không để ảnh hưởng đến tư tưởng, dư luận bộ đội và kết quả hoàn thành nhiệm vụ của đơn vị.
- Trao đổi trong cấp ủy, chỉ huy đơn vị thống nhất biện pháp khắc phục những biểu hiện nghi kỵ lẫn nhau, làm mất đoàn kết nội bộ, phân công cán bộ làm công tác giáo dục, định hướng nhận thức, tư tưởng cho chiến sĩ.
- Gặp gỡ riêng chiến sĩ định hướng nhận thức tư tưởng, khắc phục biểu hiện so bì thiếu cơ sở trong thực hiện chế độ quy định của quân đội; xây dựng lòng tin đối với đội ngũ cán bộ trong đơn vị, tăng cường đoàn kết thống nhất, hiểu biết lẫn nhau, chấp hành nghiêm kỷ luật quân đội, quy định của đơn vị.
- Tổ chức rút kinh nghiệm cho cán bộ, chiến sĩ trong đơn vị, nêu cao ý thức, trách nhiệm trong thực hiện nhiệm vụ, giải quyết mối quan hệ giữa cán bộ, chiến sĩ, tạo đồng thuận, thống nhất cao, nâng cao ý thức chấp hành nghiêm kỷ luật quân đội, quy định đơn vị.
- Duy trì nghiêm chế độ nền nếp xây dựng đơn vị chính quy, nắm, quản lý tư tưởng, kỷ luật bộ đội, chủ động giải quyết những vấn đề nảy sinh.
- Duy trì có nền nếp hoạt động thể dục, thể thao, vui chơi giải trí trong đơn vị, qua đó hiểu biết, tôn trọng lẫn nhau hoàn thành tốt nhiệm vụ được giao.
- Báo cáo chỉ huy cấp trên.
Tình huống 48. Một nhóm chiến sĩ cũ hay bắt nạt chiến sĩ mới phục vụ sinh hoạt cá nhân (giặt quần áo, rửa bát, dọn vệ sinh) làm cho một số chiến sĩ có biểu hiện lo ngại, thiếu yên tâm công tác
Gợi ý biện pháp xử lý
- Nắm tình hình sự việc xảy ra trong đơn vị, nhất là biểu hiện chiến sĩ cũ bắt nạt chiến sĩ mới, đề xuất cấp ủy, chỉ huy có biện pháp giải quyết.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật chiến sĩ, nhất là mối quan hệ giữa chiến sĩ cũ với chiến sĩ mới; thống nhất biện pháp xử lý, phân công cán bộ theo dõi, quản lý.
- Gặp gỡ những chiến sĩ cũ có biểu hiên bắt nạt chiến sĩ mới, giáo dục, quán triệt hiểu rõ việc làm sai trái, yêu cầu chấm dứt biểu hiện trên, nâng cao ý thức xây dựng mối quan hệ đoàn kết gắn bó, giúp đỡ giữa các chiến sĩ với nhau, hoàn thành nhiệm vụ được giao.
- Căn cứ tính chất, mức độ vi phạm triển khai cho chiến sĩ cũ viết bản tường trình, bản tự kiểm điểm, tổ chức sinh hoạt đơn vị đề nghị phê bình, xử lý phù hợp.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho cán bộ nâng cao ý thức rèn luyện phương pháp giáo dục, huấn luyện bộ đội, gương mẫu, mô phạm, thật sự xứng đáng là người anh, người đồng chí, đồng đội đi trước, thông cảm, chia sẽ, giúp đỡ lẫn nhau; tranh biểu hiện phân biệt đối xử thiếu công bằng giữ các chiến sĩ, gây mất đoàn kết nội bộ.
- Tăng cường kiểm tra cán bộ tiểu đội trưởng thực hiện chức trách, nhiệm vụ, phát hiện những biểu hiện, việc làm sai trái để chấn chỉnh kịp thời.
- Duy trì nghiêm chế độ, nền nếp xây dựng chính quy, quản lý chặt chẽ tình hình tư tưởng, kỷ luật và mối quan hệ của chiến sĩ, chủ động phát hiện những vấn đề nảy sinh, có biện pháp xử lý.
- Tổ chức tốt sinh hoạt ngày chính trị văn hóa tinh thần, dân chủ cơ sở và các hoạt động văn hóa thể dục, thể thao, tạo không khí vui tươi, hòa đồng, biểu hiện tôn trọng giúp đỡ lẫn nhau hoàn thành nhiệm vụ.
Tình huống 49. Một chiến sĩ mới muốn trốn tránh thực hiện nghĩa vụ quân sự đã làm các biểu hiện giả mạo của bệnh tâm thần, gây tâm lý lo lắng trong đơn vị
Gợi ý biện pháp xử lý
- Nắm tình hình tư tưởng, kỷ luật của chiến sĩ, nhất là những đồng chí có biểu hiện bất thường, đề xuất cho cấp ủy, chỉ huy đơn vị giải quyết.
- Hội ý cấp ủy, chỉ huy đơn vị nhận định, đánh giá tình hình tư tưởng, kỷ luật bộ đội, nhất là đối với những đồng chí có biểu hiện bất thường, thống nhất biện pháp xử lý, báo cáo cấp trên xin ý kiến chỉ đạo.
- Phối hợp chặt chẽ với cơ quan cấp trên tổ chức kiểm tra, kết luận trình trạng sức khỏe, tâm lý, tinh thần của chiến sĩ, có biện pháp giải quyết đúng quy định của Luật Nghĩa vụ quân sự và phối kết hợp với gia đình quân nhân động viên bộ đội yên tâm công tác.
- Gặp gỡ chiến sĩ thiếu yên tâm công tác, giáo dục, nhắc nhở hiểu rõ việc làm trốn tránh nghĩa vụ quân sự là sai trái, ảnh hưởng đến ủy tín bản thân, gia đình, quê hương, truyền thống quân đội, phẩm chất Bộ đội Cụ Hồ; đề cao trách nhiệm vinh dự cá nhân, hoàn thành nhiệm vụ được giao.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho chiến sĩ hiểu rõ việc thiếu cố gắng trong rèn luyện, ngại khó, ngại khổ, thiếu lòng tự trọng bản thân khi thực hiện nhiệm vụ quân sự; qua đó nâng cao ý thức thực hiện nghiêm túc Luật Nghĩa vụ quân sự của mọi công dân.
- Thường xuyên nắm, quản lý tư tưởng, kỷ luật và các mối quan hệ xã hội của chiến sĩ để quan tâm giáo dục, động viên khắc phục biểu hiện tư tưởng trốn tránh nghĩa vụ quân sự.
- Phát huy vai trò của tổ ba người, chiến sĩ bảo vệ, bạn bè đồng hương để nắm, phản ánh tâm tư, tình cảm và những vướng mắc bất cập của chiến sĩ có biện pháp giúp đỡ kịp thời.
- Duy trì có chất lượng ngày chính trị văn hóa tinh thần, dân chủ cơ sở để bộ đội phản ánh tư tưởng, tình cảm, nguyện vọng với chỉ huy.
- Tổng hợp tình hình báo cáo cáp trên.
Tình huống 50. Một số chiến sĩ mới hay hút thuốc lá trong doanh trại, lúc đông người ảnh hưởng môi trường, sức khỏe, làm cho cán bộ, chiến sĩ trong đơn vị bất bình, bức xúc
Gợi ý biện pháp xử lý
- Nắm, kiểm tra việc chiến sĩ hay hút thuốc lá trong đơn vị, thu nhập, tổng hợp các văn bản quy định liên quan đến việc hút thuốc lá, đề xuất cấp ủy, chỉ huy đơn vị có biện pháp tuyên truyền, giáo dục.
- Tổ chức họp cấp ủy, chỉ huy đơn vị đánh giá tình hình chiến sĩ sử dụng thuốc lá, công tác bảo vệ sức khỏe, vệ sinh môi trường, thống nhất biện pháp giáo dục, quán triệt và quản lý chấp hành quy định về hút thuốc lá. Báo cáo cấp trên theo phân cấp.
- Gặp gỡ riêng những chiến sĩ hay hút thuốc lá, giáo dục, quán triệt hiểu rõ tác hại tới vệ sinh môi trường, sức khỏe bản thân, ảnh hưởng đồng chí, đồng đội, gia đình vợ con; đồng thời chỉ đạo các tổ chức trong đơn vị tổ chức tọa đàm, trao đổi về tác hại và cách bỏ thuốc lá, nâng cao ý thức chấp hành quy định về hút thuốc lá của quân đội, đơn vị.
- Thường xuyên kiểm tra nhắc nhở, phê bình chiến sĩ chấp hành chưa nghiêm Luật Phòng, chống tác hại của thuốc lá và quy định của quân đội về hút thuốc lá để xây dựng ý thức tự giác chấp hành.
- Phát động thi đua tổ chức cho cán bộ, đoàn viên thanh niên viết giao ước, cam kết không hút thuốc và phổ biến nhân rộng phương pháp bỏ thuốc.
- Động viên cán bộ, chiến sĩ trong đơn vị quyết tâm bỏ thói quen hút thuốc lá, có kế hoạch thay đổi bằng những việc làm, sở thích khác lành mạnh.
- Thường xuyên giáo dục, quán triệt Luật Phòng, chống tác hại của thước là và cập nhật những quy định, hướng dẫn của trên cho cán bộ, chiến sĩ thực hiện, bảo vệ sức khỏe bản thân và vệ sinh môi trường.
Tình huống 51. Một đồng chí tiểu đội trưởng thường xuyên vay tiền của nhiều chiến sĩ trong đơn vị, nhưng không trả, gây bức xúc cho bộ đội
Gợi ý biện pháp xử lý
- Xác minh sự việc đồng chí tiểu đội trưởng hay vay tiền của chiến sĩ không trã, làm rõ nguyên nhân, đề xuất cấp ủy, chỉ huy đơn vị biện pháp giải quyết.
- Hội ý chỉ huy đánh giá, nhận định tình hình tư tưởng, kỷ luật bộ đội và dư luận cán bộ, chiến sĩ trong đơn vị, thống nhất biện pháp giải quyết.
- Gặp gỡ đồng chí tiểu đội trưởng giáo dục nhận rõ khuyết điểm, hạn chế ảnh hưởng uy tín, phẩm chất, đạo đức cán bộ, đơn vị, quy trách nhiệm cá nhân; chỉ đạo đồng chí tiểu đội trưởng trực tiếp xin lỗi đồng chí, đồng đội, yêu cầu bằng mọi biện pháp nhanh chóng trả hết số tiền vay của chiến sĩ.
- Triển khai đồng chí tiểu đội trưởng viết bản trường trình, bản tự kiểm điểm, tổ chức sinh hoạt đơn vị đề nghị hình thức kỷ luật (căn cứ vào số lượng và tính chất vay nợ).
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho cán bộ, chiến sĩ về sự việc cán bộ vay tiền của chiến sĩ không trả; nâng cao ý thức chấp hành kỷ luật quân đội, quy định đơn vị, xây dựng lòng tự trọng cá nhân, rèn luyện phẩm chất tư cách của người cán bộ tiểu đội trưởng.
- Thường xuyên duy trì nghiêm chế độ, nền nếp xây dựng đơn vị chính quy, quản lý tư tưởng, kỷ luật bộ đội, nhất là những biểu hiện bất thường trong chi tiêu sinh hoạt cá nhân, có biện pháp, giáo dục khắc phục kịp thời.

Tình huống 52. Một chiến sĩ mới điều kiện kinh tế gia đình khá giả, được bố mẹ nuông chiều, trong khi đó yêu cầu nhiệm vụ huấn luyện ngày càng cao, áp lực lớn, ý thức rèn luyện hạn chế đã nảy sinh tư tưởng uống thuốc diệt cỏ tự tử
Gợi ý biện pháp xử lý
- Bằng mọi biện pháp ngăn chặn chiến sĩ uống thuốc diệt cỏ tự tử.
- Nắm chắc tình hình tư tưởng, diễn biến tâm lý của chiến sĩ, đề xuất với cấp ủy, chỉ huy biện pháp giải quyết.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình, nguyên nhân nảy sinh tư tưởng tiêu cực của chiến sĩ, thống nhất biện pháp xử lý, phân công cán bộ phụ trách. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Phân công cán bộ, chiến sĩ trong đơn vị thường xuyên gần gũi, giúp đở, động viên quân nhân nhận rõ trách nhiệm bản thân đối với giai đình, với đồng chí, đồng đội, nghiêm túc với bản thân không suy nghĩ và có việc làm tiêu cực nữa để gia đình, đơn vị yên tâm.
- Phối hợp với cấp ủy, chính quyền địa phương và gia đình động viên chiến sĩ ổn định tâm lý, tư tưởng, xác định tốt trách nhiệm, vượt qua mặc cảm bản thân, khắc phụ khó khăn hoàn thành tốt nhiệm vụ được giao.
- Tổ chức rút kinh nghiệm cho cán bộ trong huấn luyện, rèn luyện với cường độ từ thấp đến cao, từ đơn giản đến phức tạp để bộ đội quen dần với môi trường điều kiện khó khăn trong công tác, đáp ứng yêu cầu, nhiệm vụ.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho chiến sĩ hiểu rõ việc rèn luyện, tu dưỡng bản thân, ảnh hưởng đến phẩm chất, đạo đức tư cách người chiến sĩ, ảnh hưởng đến gia đình, chất lượng hiệu quả công tác của cá nhân, nền nếp xây dựng chính quy của đơn vị.
- Quan tâm chăm lo đời sống vật chất, tinh thần tạo không khí vui tươi, lành mạnh cho bộ đội yên tâm công tác.
- Nắm, quản lý tình hình tư tưởng, kỷ luật và các mối quan hệ của chiến sĩ, nhất là biểu hiện bất thường, có biện pháp giáo dục, ngăn chặn kịp thời.
Tình huống 53. Một chiến sĩ huấn luyện nhặt được vật liệu nổ ở thao trường đưa về đơn vị làm gây nổ và bị tai nạn, ảnh hưởng sức khỏe, tâm lý và tư tưởng bộ đội
Gợi ý biện pháp xử lý
- Bằng mọi biện pháp cứu chữa cho chiến sĩ bị tai nạn do vật liệu nổ, ổn định sức khỏe, tâm lý, tinh thần.
- Nắm tình hình sự việc mất an toàn vật liệu nổ của chiến sĩ, đề xuất cấp ủy, chỉ huy biện pháp giải quyết.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá việc quản lý duy trì quy định bảo đảm an toàn trong huấn luyện, vật liệu nổ, tình hình tư tưởng, kỷ luật bộ đội, thống nhật biện pháp xử lý. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Sinh hoạt đơn vị rút kinh nghiệm cho cán bộ, chiến sĩ nâng cao ý thức cấp hành nghiêm quy định sử dụng đạn hơi, thuốc nổ, công tác bảo đảm an toàn thao trường, quy định trong quản lý sử dụng thuốc nổ.
- Tăng cường kiểm tra đơn vị thực hiện quy tắc quản lý, sử dụng, bảo quản vật liệu nổ, bảo đảm an toàn trước, trong và sau mỗi đợt huấn luyện, không để bộ đội tự tiện sử dụng làm mất an toàn đơn vị và địa bản đóng quân.
- Thường xuyên quán triệt chấp hành nghiêm quy định, quy chế quản lý, thu gom, vận chuyển vật liệu nổ, xây dựng đơn vị an toàn, địa bàn an toàn,
- Báo cáo cấp trên theo quy định.

IV. ĐỐI TƯỢNG GIÁO VIÊN
Tình huống 54. Một số giáo viên giảng dạy khoa xã hội nhân văn rất băn khoăn, lo lắng, thiếu tự tin khi ban tổ chức hội thi đưa môn bắn súng K54 làm một trong các nội dung thi giáo viên dạy giỏi cấp nhà trường
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình, chất lượng huấn luyện bắn súng K54 của đội ngũ giáo viên trong nhà trường, thống nhất biện pháp giải quyết. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ giáo viên băn khoăn, lo lắng về khả năng bắn súng K54 động viên hiểu rõ mục tiêu, yêu cầu, tiêu chuẩn của một cán bộ giáo viên dạy giỏi cấp nhà trường, nâng cao ý thức rèn luyện, tu dưỡng kiến thức, năng lực quân sự đáp ứng yêu cầu, nhiệm vụ.
- Phân công cán bộ có kinh nghiệm kèm cặp, giúp đở kỹ năng bắn súng K54 cho giáo viên ôn luyện, xây dựng tâm lý tự tin tham gia thi giáo viên dạy giỏi.
- Nghiên cứu đề nghị sửa đổi quy chế, quy định thi, kiểm tra bắn súng K54 phù hợp với đặc điểm, yêu cầu, nhiệm vụ từng giáo viên, phù hợp với chuyên ngành đào tạo và huấn luyện cho học viên.
- Quản lý chặt chẽ đội ngũ giáo viên trong nhà trường chấp hành nghiêm quy định huấn luyện quân sự bắn súng K54, kịp thời rút kinh nghiệm.
- Quan tâm tạo mọi điều kiện thuận lợi về công tác bảo đảm cho đội ngũ giáo viên luyện tập nâng cao kết quả thi, kiểm tra.
- Báo cáo tổng hợp kết quả theo quy định.
Tình huống 55. Một đồng chí giáo viên thường xuyên gợi ý học viên đưa tiền để nâng điểm giỏi cho các bài thi, kiểm tra, gây tâm lý bức xúc, bất bình cho học viên
Gợi ý biện pháp xử lý
- Phối hợp với cơ quan chức năng và chỉ huy đơn vị quản lý học viên xác minh tình hình chấp hành quy định, quy chế thi, kiểm tra các môn học của nhà trường; đề xuất cấp ủy, chỉ huy biện pháp xử lý.
- Hội ý lãnh đạo, chỉ đạo khoa nhận định, đánh giá tình hình chấp hành quy chế, quy định thi, kiểm tra của nhà trường, ý thức, trách nhiệm của đội ngũ giáo viên trong duy trì quy trình, quy đinh chấp thi các môn học, xác minh giáo viên gợi ý học viên đưa tiền nâng điểm giỏi; thống nhât biện pháp giải quyết. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ đồng chí giáo viên gợi ý học viên đưa tiền nâng điểm giỏi giáo dục nhận rõ khuyết điểm, nâng cao ý thức chấp hành nghiêm kỷ luật quân đội, quy chế thi, kiểm tra của nhà trường, Căn cứ tính chất, mức độ vi phạm, triển khai đồng chí giáo viên viết bản tường trình, bản tự kiểm điểm sinh hoạt khoa rút kinh nghiệm, đề nghị hình thức kỷ luật phù hợp.
- Tổ chức sinh hoạt rút kinh nghiệm cho cán bộ, giáo viên trong khoa về thực hiện quy chế, quy đinh kiểm tra, nâng cao ý thức chấp hành kỷ luật quân đội, quy chế giáo dục, đào tạo của nhà trường, đề cao phẩm chất, đạo đức nghề giáo.
- Thường xuyên quán triệt nâng cao ý thức chấp hành nghiêm các quy định, quy chế thi, kiểm tra của nhà trường cho giáo viên, học viên, làm cơ sở đánh giá, nhận xét chính xác kết quả học tập của học viên.
- Nắm, theo dõi, quản lý chặt chẽ tình hình tư tưởng, kỷ luật và các mối quan hệ của giáo viên, học viên trong nhà trường, bảo đảm thực hiện quy chế thi, kiểm tra của nhà trường nghiêm túc, chặt chẽ.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 56. Một đồng chí giáo viên trong nhà trường khi giản dạy cho sinh viên ngoài quân đội đã cung cấp một số thông tin thiếu chính xác về quan điểm, đường lối đối ngoại của Đảng, Nhà nước ta, có sinh viên chia sẽ lên mạng xã hội, gây dư luận không tốt
Gợi ý biện pháp xử lý
- Xác minh sự việc giáo viên giảng dạy cho đối tượng sinh viên ngoài quân đội, có dư luận xấu đến quân đội, uy tín của nhà trường, đề xuất biện pháp xử lý.
- Trao đổi trong cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật, tính chất, hậu quả vị phạm của đồng chí giảng viên dạy cho đối tượng sinh viên ngoài quân đội, thống nhất biện pháp xử lý; phân công cấp ủy viên phụ trách; báo cáo cấp trên xin ý kiến chỉ đạo.
- Phối hợp với các cơ quan chức năng của đơn vị và cá nhân có liên quan gỡ bỏ thông tin xấu độc trên mạng xã hội và chỉ đạo lực lượng chuyên sâu của đơn vị viết bài khẳng định quan điển đúng đắn của Đảng, Nhà nước ta về hoạt động đối ngoại, đấu tranh phản bác những quan điểm sai trái, xuyên tạc chống phá Đảng, Nhà nước ta.
- Gặp gỡ đồng chí giảng viên vi phạm quy định chung cấp thông tin, trao đổi, nhận rõ khuyết điểm, hạn chế, có biện pháp sửa chữa khắc phục; nâng cao ý thức chấp hành nghiêm kỷ luật quân đội, thực hiện đúng quy chế của nhà trường trong quá trình giảng dạy.
- Tổ chức sinh hoạt rút kinh nghiệm cho đội ngũ giáo viên trong nhà trường nâng cao ý thức chấp hành kỷ luật quân đội, quy chế giáo dục, đào tạo, thực hiện nghiêm túc quy trình, quy định, thông qua phê duyệt giáo án, bài giảng trước khi thông tin, giảng bài cho các đối tượng không để sai sót, vi phạm nguyên tắc. Căn cứ mức độ vi phạm của đồng chí giáo viên để xử lý kỷ luật cho phù hợp.
- Tham mưu, đề xuất bổ sung, sửa đổi quy chế, quy định công tác giảng dạy cung cấp thông tin cho người học phải phù hợp với yêu cầu, nhiệm vụ mới, bảo đảm chặt chẽ, chính xác, nhất là những vấn đề nhạy cảm, liên quan đến công tác quân sự, quốc phòng, an ninh.
- Quản lý chặt chẽ phẩm chất chính trị, trình độ năng lực, đạo đức nghề nghiệp của đội ngũ giáo viên, đáp ứng yêu cầu giáo dục, đào tạo, uy tín, danh dự của nhà trường.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 57. Một cán bộ, giáo viên trong nhà trường cho rằng, mình có trình độ, năng lực nhưng chính sách đãi ngộ của quân đội chưa tương xứng, nên thiếu yên tâm công tác
Gợi ý biện pháp xử lý
- Gặp gỡ đồng chí giảng viên trong khoa nắm bắt tâm tư nguyện vọng, làm cơ sở đề xuất cấp ủy đảng biện pháp giải quyết.
- Hội ý cấp ủy, chỉ huy khoa đánh giá phân loại tư tưởng, trình độ, phẩm chất, năng lực của đội ngũ giáo viên, xác định chủ trương, biện pháp lãnh đạo, chỉ đạo. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Tổ chức sinh hoạt đơn vị, giáo dục, quán triệt cho cán bộ, giảng viên trong nhà trường nhận thức sâu sắc sự quan tâm của quân đội đào tạo, giáo dục, bồi dưỡng phát triển trưởng thành; qua đó nâng cao tinh thần trách nhiệm, trau dồi phẩm chất đạo đức nghề nghiệp, chấp hành nghiêm kỷ luật quân đội, quy định của nhà trường, yên tâm với nhiệm vụ.
- Quan tâm chăm lo đời sống vật chất, tinh thần và chính sách hậu phương quân đội cho đội ngũ giáo viên yên tâm cống hiến xây dựng đơn vị.
- Thường xuyên quản lý chặt chẽ tình hình tư tưởng, kỷ luật, trình độ năng lực, đạo đức nghề nghiệp của đội ngũ giáo viên, kịp thời bồi dưỡng, động viên hoàn thành tốt nhiệm vụ.
- Tổng hợp tình hình báo cáo cấp trên theo quy định.
Tình hướng 58. Một số cán bộ quản lý lợp học trong nhà trường có biểu hiện tác động giáo viên để nâng điểm giỏi cho học viên, gây bất bình trong lớp học, ảnh hưởng chất lượng đào tạo
Gợi ý biện pháp xử lý
- Xác minh thông tin về tác động của cán bộ quản lý học viên đối với giáo viên để nâng điểm giỏi cho học viên; đề xuất cho cấp ủy, chỉ huy chủ trương, giải pháp giải quyết.
- Hội ý cấp ủy, chỉ huy đơn vị đề xuất với nhà trường chỉ đạo các bộ môn, khoa, rà soát, đánh giá lại quy trình, quy định thi, kiểm tra của nhà trường và việc đánh giá chất lượng học tập của học viên, thống nhất biện pháp giải quyết.
- Trường hợp không có đơn mà chỉ có dự luận thì chỉ sinh hoạt đơn vị quán triệt nhắc nhở, gặp gỡ riêng cán bộ quản lý học viên nghiêm túc rút kinh nghiệm, sửa chữa khuyết điểm, tổng hợp đề xuất biện pháp giải quyết.
- Trường hợp có đơn thư phản ánh và xác minh sự việc có chứng cứ, cơ sở thì gặp gỡ cán bộ giáo dục, nhận rõ khuyết điểm tự ý nâng điểm giỏi cho học viên không đúng quy chế; căn cứ mức độ, hậu quả vi phạm quy chế để triển khai viết bản tường trình, bản tự kiểm điểm, tổ chức sinh hoạt đơn vị đề nghị hình thức kỷ luật.
- Sinh hoạt đơn vị thông báo tình hình xem xét kỷ luật cho cán bộ, giáo viên trong nhà trường về việc thực hiện chưa nghiêm quy chế, quy định thi, kiểm tra của nhà trường, qua đó nghiêm túc rút kinh nghiệm, nâng cao chất lượng giáo dục, đào tao,
- Tăng cường kiểm tra, giám sát của cơ quan chứ năng trong thực hiện quy định, quy chế thi, kiểm tra của nhà trường, bảo đảm đánh giá khách quan, nghiêm túc, chặt chẽ trình độ, năng lực học viên.
- Quản lý chặt chẽ tình hình tư tưởng, kỷ luật và các mố quan hệ công tác của cán bộ, học viên trong nhà trường, kịp thời nhắc nhở khắc phục hạn chế, khuyết điểm trong thi, kiểm tra.
Tình huống 59. Một đồng chí chỉ huy khoa giáo viên trong nhà trường có biểu hiện lợi dụng quyền hạn đánh giá, đề bạt, bổ nhiệm cán bộ thiếu khách quan, chính xác, ưu ai cho những đồng chí thân quen, gây tâm trạng bất bình trong đơn vị.
Gợi ý biện pháp xử lý
- Nắm chắc tình hình công tác nhận xét, đánh giá, quy hoạch, đề bạt cán bộ cấp ủy đảng, đề xuất cấp ủy, chỉ huy khoa biện pháp giải quyết.
- Hội ý cấp ủy, chỉ huy khoa đánh giá, ra soát quy trình, quy định, nhận xét, đề bạt, bổ nhiệm cán bộ của cấp ủy đảng, chỉ huy, quy rõ trách nhiệm cá nhân, tập thể có liên quan (nếu có).
- Tổ chức sinh hoạt rút kinh nghiệm trong cấp ủy, chỉ huy khoa về thực hiện quy trình, quy định trong công tác cán bộ, những hạn chế, khuyết điểm, quy rõ trách nhiệm cá nhân, tập thể, qua đó có biện pháp khắc phục.
- Nâng cao chất lượng sinh hoạt chi bộ, đơn vị, phát huy dân chủ, đề cao kỷ luật trong thực hiện quy chế, quy định công tác cán bộ bảo đảm nhận xét, đánh giá, đề bạt bổ nhiệm đúng quy trình, nguyên tắc thủ tục, lựa chọn những đồng chí có trình độ, phẩm chất năng lực xây dựng đơn vị.
- Thường xuyên kiểm tra, rà soát thực hiện quy trình, quy đinh đề bạt, bổ nhiệm cán bộ của đơn vị, bảo đảm khách quan, chính xác, tạo thống nhất cao trong cấp ủy đảng.
- Cấp ủy đảng thường xuyên làm tốt công tác lãnh đạo, chỉ đạo, kiểm tra đánh giá khách quan, chính xác đội ngũ cán bộ và đưa ra khỏi nguồn những đồng chí không đủ tiêu chuẩn phẩm chất, năng lực.
Tình huống 60. Một số đồng chí giáo viên có biểu hiện so sánh chế độ chính sách đãi ngộ của quân đội với bên ngoài dân sự, nên có tư tưởng chuyển ngành, làm việc cầm chừng
Gợi ý biện pháp xử lý
- Nắm chắc tình hình tâm tư nguyện vọng của đội ngũ giáo viên trong nhà trường và công tác bảo đảm tiêu chuẩn, chế độ chính sách của quân đội, đề xuất cấp ủy, chỉ huy đơn vị biện pháp giải quyết.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tâm tư nguyện vọng của cán bộ giáo viên và công tác bảo đảm tiêu chuẩn, chế độ chính sách của nhà trường, thống nhất biện pháp giáo dục, động viên. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Tổ chức giáo dục, quán triệt cho đội ngũ giáo viên nhận thức sâu sắc các nghị quyết, chỉ thị, quy định về công tác giáo dục, đào tạo của nhà trường và những văn bản liên quan đến tiêu chuẩn, chế độ chính sách của quân đội; qua đó xác định nghĩa vụ, trách nhiệm trong giảng dạy và xây dựng nhà trường.
- Quan tâm bảo đảm tiêu chuẩn, chế độ chính sách, đời sống vật chất, tinh thần cho hậu phương gia đình cán bộ để gắn bó, yên tâm với nhiệm vụ.
- Thường xuyên làm tốt công tác tập huấn, bồi dưỡng nâng cao trình độ, phẩm chất, năng lực cho cán bộ, đáp ứng yêu cầu, nhiệm vụ xây dựng nhà trường trong điều kiện mới.
- Báo cáo cấp trên theo quy định.
Tình huống 61. Vợ của một cán bộ quản lý học viên đã lợi dụng thân quen giới thiệu cho giáo viên, học viên trong nhà trường mua hàng hóa kém chất lượng, gây dư luận không tốt
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình mua bán, trao đổi hàng hóa trong nhà trường có liên quan đến giáo viên của khoa, thống nhất biện pháp giải quyết. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ đồng chí giáo viên trao đổi, động viên, thuyết phục gia đình, vợ, con chấp hành nghiêm đường lối, chủ trương của Đảng, chính sách, pháp luật Nhà nước; thực hiện buôn bán, giao dịch hàng hóa đúng quy định của pháp luật và không làm ảnh hưởng đến xây dựng chính quy, sinh hoạt, hoạt động của nhà trường, an ninh, an toàn đơn vị.
- Phối hợp với cấp ủy, chính quyên địa phương tuyên truyền, phổ biến quy định của nhà trường đối với gia đình quân nhân khi ra vào doanh trại quân đội, không làm ảnh hưởng đến việc duy trì chế độ nền nếp xây dựng chính quy và hoạt động sinh hoạt của nhà trường, lợi dụng thân quen làm những việc quy định pháp luật Nhà nước.
- Duy trì quy định, quy chế ra vào doanh trại của nhà trường nghiêm túc, chặt chẽ, không để phần tử xâu móc nối, lôi kéo cán bộ, học viên tham gia hoạt động mua bán hàng hóa, trao đổi tài liệu, làm mất an ninh, an toàn đơn vị.
- Thường xuyên quản lý nắm chắc tình hình tư tưởng, kỷ luật và các mối quan hệ xã hội của cán bộ, giáo viên, nhân viên nhà trường, có biện pháp giáo dục, quản lý, chấn chỉnh kịp thời.
- Báo cáo cấp trên theo quy đinh.
Tình huông 62. Một học viên nghiên cứu sinh ở nước ngoài có ý đinh xin ra quân và định cư ở nước sở tại và nhà trường không cho phép, nảy sinh tư tưởng chán nản, thiếu yên tâm công tác
Gợi ý biện pháp xử lý
- Nắm chắc tình hình tư tưởng, kỷ luật và chất lượng học tập của học viên đang nghiên cứu sinh ở nước ngoài, nhất là những vần đề nảy sinh; đề xuất biện pháp giải quyết cho cáp ủy, chỉ huy đơn vị.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tâm tư, nguyện vọng của học viên đang học tập ở nước ngoài, thống nhất biện pháp xử lý. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Phối hợp với cơ quan chức năng của đơn vị giáo dục, động viên học viên nhận thức sâu sắc về sự quan tâm của quân đội và nhà trường cho đi học tập, nghiên cứu ở nước ngoài, tiếp thu khoa học hiện đại, nâng cao trình độ, kiến thức, năng lực, chuyên môn nghiệp vụ về phục vụ đất nước, quân đội; qua đó nâng cao ý thức tích cực học tập, cống hiến.
- Phối hợp với gia đình, địa phương, người thân, động viên học viên phát huy truyền thống quê hương, gia đình, hiểu rõ vinh dự, trách nhiệm của người cán bộ, đảng viên, tích cực học tập, rèn luyện cống hiến xây dựng quân đội, xây dựng nhà trường vững mạnh.
- Tổ chức sinh hoạt rút kinh nghiệm cho đội ngũ giáo viên, học viên trong nhà trường hiểu rõ vinh dự, trách nhiệm của cán bộ, đảng viên được Nhà nước quan tâm, tạo điều kiện cho học tập và phát triển lâu dài trong quân đội; qua đó nỗ lực cố gắng học tập, rèn luyện, hoàn thành chức trách, nhiệm vụ được giao.
- Thường xuyên quan tâm bảo đảm tiêu chuẩn chế độ, chính sách hậu phương gia đình để cán bộ yên tâm công tác, gắn bó với nhiệm vụ.
- Làm tốt công tác quy hoạch, đào tạo, bồi dưỡng cán bộ bảo đảm khách quan, chính xác, trọng dụng người tài, tạo môi trường thuận lợi để yên tâm, cống hiến xây dựng quân đội.
- Xử lý kỷ luật nghiêm túc, chặt chẽ đối với những đồng chí có tư tưởng thoái thác nhiệm vụ, chấp hành kỷ luật không nhiêm để răn đe, cảnh báo.
- Báo cáo cấp trên theo quy định.
Tình huống 63. Một giảng viên của trường sĩ quan hay tham gia chơi lô đề, cá độ, chơi hụi nợ tiền không có khả năng chi trả, đã ảnh hưởng tư tưởng và chất lượng công tác
Gợi ý biện pháp xử lý
- Năm chắc tình hình tư tưởng, kỷ luật, biểu hiện tham gia chơi hụi, vay tiền không có khả năng chi trả của đồng chí giảng viên; xác định số lượng tiền, hậu quả, nguyên nhân, dự kiến các biện pháp giải quyết cho cấp ủy, chỉ huy đơn vị.
- Hội ý cấp ủy, chỉ huy đơn vị rà soát tình hình, tư tưởng, kỷ luật của đồng chí giảng viên hay vay tiền, chơi hụi, thống nhât biện pháp giải quyết; phân công cán bộ phụ trách. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ đồng chí giảng viên hay chơi lô đề, chơi hụi giáo dục nhận rõ khuyết điểm, vị phạm kỷ luật quân đội, quy định đơn vị, ảnh hưởng đến uy tín, danh dự bản thân, gia đình, đơn vị bằng mọi biện pháp khắc phục hậu quả số tiền nợ; chỉ đạo đồng chí giảng viên viết bản tường trình, bản tự kiểm điểm, sinh hoạt đơn vị đề nghị hình thức kỷ luật phù hợp.
- Sinh hoạt đơn vị rút kinh nghiệm cho cán bộ, giáo viên nâng cao ý thức chấp hành nghiêm nghị quyết, chỉ thị của Đảng, pháp luật Nhà nước, kỷ luật quân đội, quy đinh xây dựng chính quy; đấu tranh phê phán với tệ nạn xã hội xâm nhập vào đơn vị, gây ảnh hưởng xấu trong nội bộ.
- Tăng cường quản lý tư tưởng, kỷ luật và các mối quan hệ xã hội của cán bộ giáo viên trong đơn vị, nhất là những quan hệ bất thường, chấp hành chế độ, thời gian giờ giấc không nghiêm, có biện pháp chấn chỉnh kịp thời.
- Định kỳ thông báo kết quả rèn luyện, chấp hành kỷ luật của giáo viên cho cấp ủy, chính quyền địa phương và gia đình biết cùng phối hợp giáo dục, động viên, nhắc nhở kịp thời.
- Tổng hợp kết quả báo cáo cấp trên theo quy định.
Tình huống 64. Một đồng chí giảng viên trong khoa được hiệu trưởng trường đại học ngoài quân đội mời đến làm việc với mức lương cao hơn, đã nảy sinh tư tưởng so bì, thiếu yên tâm công tác
Gợi ý biện pháp xử lý
- Nắm tình hình tâm tư, tình cảm, nguyện vọng, điều kiện hoàn cảnh gia đình của giáo viên trong khoa, đề xuất cấp ủy, chỉ huy biện pháp giải quyết.
- Hội ý cấp ủy, chỉ huy khoa đánh giá, rà soát tình hình tâm tư, nguyện vọng, điều kiện hoàn cảnh gia đình của cán bộ, giảng viên và công tác bảo đảm đời sống vật chất, tinh thần của đơn vị, thống nhất viện pháp xử lý.
- Gặp gỡ cán bộ, giảng viên trong khoa, động viên hiểu rõ vinh dự, trách nhiệm được Nhà nước, quân đội quan tâm tạo điều kiện cho học tập phát triển và phục vụ lâu dài, nâng cao ý thức trách nhiệm, đề cao kỷ luật, rèn luyện, tu dưỡng phẩm chất, đạo dức, yên tâm hoàn thành nhiệm vụ.
- Tổ chức sinh hoạt quán triệt các văn bản, chỉ thị, quy định và chế độ tiêu chuẩn chính sách của quân đội cho cán bộ giảng viên, xây dựng ý thức trách nhiệm, khắc phục khó khăn, hoàn thành tốt nhiệm vụ được giao.
- Làm tốt công tác đánh giá, đề bạt, bổ nhiệm cán bộ bảo đảm khách quan, chính xác, khuyến khích động viên giảng viên yên tâm học tập, rèn luyện phục vụ lâu dài trong quân đội.
- Quan tâm, chăm lo đời sống vật chất, tinh thần, chính sách hậu phương quân đội cho cán bộ, giảng viên yên tâm gắn bó với nhiệm vụ được giao.
- Quản lý chặt chẽ tình hình tư tưởng, kỷ luật và các mối quan hệ công tác của cán bộ, giảng viên trong nhà trường, nhất là quan hệ bất thường, phức tạp, kịp thời có biện pháp giải quyết.
- Tổng hợp tình hình báo cáo cấp trên theo quy định.
Tình huống 65. Một cán bộ ở đơn vị được điều động về khoa giáo viên công tác, do không đúng nguyện vọng đã nảy sinh tư tưởng buồn chán, thiếu yên tâm với nhiệm vụ
Gợi ý biện pháp xử lý
- Nắm tình hình tâm tư nguyện vọng, sở trường công tác của cán bộ giáo viên, đặc điểm yêu cầu, nhiệm vụ của nhà trường; đề xuất cho cấp ủy, chỉ huy khoa biện pháp giải quyết.
- Hội ý cấp ủy, chỉ huy khoa đánh giá tình hình tâm tư, nguyện vọng, khả năng công tác của cán bộ giáo viên trong nhà trường, thống nhất biện pháp giải quyết. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ cán bộ trao đổi, nhận rõ vinh dự, trách nhiệm, sự tin tưởng của cấp trên đối với trình độ, năng lực, kinh nghiệm thực tiễn của cán bộ đối với công tác giảng dạy và yêu cầu nhiệm vụ của nhà trường trong tình hình mới; qua đó nâng cao ý thức, chấp hành nghiêm điều động, phân công công tác của cấp trên, khắc phục khó khăn, cố gắng hoàn thành nhiệm vụ được giao.
- Phối hợp với cấp ủy, chính quyền địa phương và gia đình động viên cán bộ thực hiện nghiêm túc chủ trưởng luân chuyển phục vụ giảng dạy của nhà trường; qua đó khắc phục khó khăn hoàn thành nhiệm vụ được giao.
- Quan tâm chăm lo bảo đảm tiêu chuẩn, chế độ chính sách và sự phát triển trưởng thành để cán bộ gắn bó, yên tâm với nhiệm vụ.
- Tăng cường nắm, quản lý tư tưởng, kỷ luật và các mối quan hệ công tác của cán bộ, có biện pháp bồi dưỡng, giúp đở, động viên kịp thời.
- Tiếp tục quán triệt và thực hiện nghiêm các quy định về luân chuyển cán bộ từ đơn vị về nhà trường và từ nhà trường về đơn vị sát với thực tiễn nhiệm vụ huấn luyện, sẵn sàng chiến đấu ở đơn vị, đáp ứng yêu cầu, nhiệm vụ xây dựng quân đội, nâng cao chất lượng giáo dục, đào tạo.
- Đẩy mạnh phong trào thi đua dạy tốt, học tốt, nghiên cứu khoa học, phát huy kiến thức, kinh nghiệm thực tiễn của cán bộ vào giảng dạy, phục vụ tại nhà trường.
- Báo cáo cấp trên lãnh đạo, chỉ đạo


V. ĐỐI TƯỢNG HỌC VIÊN SĨ QUAN
Tình huống 66. Một số đồng chí học viên trong nhà trường có biểu hiện ngại học tập, ngại rèn luyện, hay xin điểm thi, điểm kiểm tra các môn học, gây bất bình trong đơn vị
Gợi ý biện pháp xử lý
- Nắm tình hình tư tưởng, kỷ luật, nhất là biểu hiện ngại học tập, ngại rèn luyện của học viên, đề xuất cấp ủy, chỉ huy có biện pháp xử lý.
- Hội ý lãnh đạo, chỉ huy đơn vị đánh giá tình hình, tư tưởng, kỷ luật, ý thức, trách nhiệm học tập, rèn luyện của học viên, thống nhất biện pháp khắc phục. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ học viên ngại học tập, hay xin điểm bài thi, kiểm tra, giáo dục nâng cao ý thức, trách nhiệm, tự giác học tập, tu dưỡng rèn luyện phẩm chất, đạo đức của người học viên, chấp hành nghiêm quy chế, quy định thi, kiểm tra các môn học, đáp ứng mục tiêu, yêu cầu đào tạo của nhà trường.
- Thường xuyên giáo dục, quán triệt quy chế, quy định thi, kiểm tra của nhà trường nghiêm túc, chặt chẽ để học viên nâng cao ý thức tự giác học tập, tu dưỡng, rèn luyện và chấp hành, nâng cao chất lượng giáo dục, đào tạo.
- Tăng cường kiểm tra, kiểm soát của cơ quan chức năng và cán bộ quản lý học viên đối với thực hiện quy chế, quy định thi, kiểm tra của nhà trường, bảo đảm đánh giá kết quả học tập của học viên khách quan, chính xác.
- Quản lý chặt chẽ tình hình tư tưởng, kỷ luật và các mối quan hệ của học viên, nhất là quan hệ giáo viên trong xin điểm, kịp thời phát hiện xử lý nghiêm túc những đồng chí vi phạm quy chế thi, kiểm tra.
Tình huống 67. Một số học viên sĩ quan chuẩn bị ra trường có biểu hiện băn khoăn lo lắng khi nhận nhiệm vụ không đúng nguyện vọng
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, nguyện vọng, hoàn cảnh gia đình của học viên, thống nhất biện pháp lãnh đạo, chỉ đạo. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ học viên nhận nhiệm vụ không đúng nguyện vọng, động viên hiểu rõ nhiệm vụ, mục tiêu, yêu cầu đào tạo của nhà trường, đặc điểm, nhiệm vụ đơn vị, quân đội, vinh dự, trách nhiệm của cán bộ, đảng viên khi được cấp trên giao nhiệm vụ đảm đương cương vị trọng trách mới; qua đó sẵn sàng chấp hành quyết định phân công của nhà trường.
- Phân công số học viên cùng về đơn vị mới, gặp gỡ trao đổi, động viên tạo điều kiện giúp đở lẫn nhau hoàn thành nhiệm vụ được phân công.
- Tổ chức sinh hoạt đơn vị, quán triệt các văn bản quy chế, quy định của trên về phân công công tác cho học viên mới tốt nghiệp ra trường, đặc điểm, yêu cầu, nhiệm vụ quân đội, nâng cao ý thức chấp hành nghiêm quyết định phân công công tác của nhà trường.
- Phối hợp chặt chẽ với địa phương, gia đình, bạn bè, động viên học viên xác định tinh thần, trách nhiệm của cán bộ, đảng viên được quân đội đào tạo cơ bản, có trình độ, năng lực đảm đương trọng trách mới, sẵn sàng nhận và hoàn thành nhiệm vụ được giao.
- Phối hợp với đơn vị tiếp nhận cán bộ làm tốt công tác tư tưởng, động viên xác định tốt nhiệm vụ được giao, tạo môi trường, điều kiện thuận lợi để cán bộ mới ra trường yên tâm cống hiến xây dựng đơn vị vững mạnh.
Tình hướng 68. Có một học viên sĩ quan không muốn học, nhưng gia đình vẫn bắt buộc phải học, dẫn đến có tư tưởng muốn bỏ học, trốn khỏi đơn vị
Gợi ý biện pháp xử lý
- Bằng mọi kênh thông tin thông báo, động viên học viên trở về trường tham gia học tập, công tác.
- Trao đổi trong cấp ủy, chỉ huy đơn vị, đánh giá tình hình tâm tư, nguyện vọng, khả năng học tập của học viên, nhất là vướng mắc về tư tưởng buồn chán dẫn đến không muốn học trở thành sĩ quan trong quân đội; thống nhất biện pháp giải quyết; báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ học viên có tư tưởng không muốn học, giáo dục, động viên nhận rõ mong muốn và niềm vinh dự tự hào của gia đình được quân đội đào tào phục vụ lâu dài phù hợp với bản thân học viên; qua đó nâng cao ý thức trách nhiệm, xác định tốt tư tưởng, khắc phục khó khăn, yên tâm trở lại trường học tập, rèn luyện.
- Thường xuyên phối hợp chặt chẽ giữa đơn vị, địa phương giáo dục, quan tâm thăm hỏi, động viên con em phát huy truyền thống quê hương, gia đình ra sức học tập, rèn luyện, hoàn thành tốt nhiệm vụ được giao.
- Quan tâm chăm lo đời sống vật chất, tinh thần và tạo mọi điều kiện thuận lợi cho học viên phấn đấu học tập, rèn luyện.
- Tổ chức thực hiện tốt cuộc vận động trong quân đội, phong trào thi đua của đơn vị với những mục tiêu, chỉ tiêu cụ thể, thiết thực để học viên phấn đấu rèn luyện; kịp thời biểu dương khen thưởng những cá nhân, tập thể có thành tích, phê bình, nhắc nhở kịp thời đối với những đồng chí thiếu ý thức có gắng phấn đấu, rèn luyện.
- Tổ chức ngày chính trị văn hóa tinh thần trong đơn vị, tạo mọi điều kiện thuận lợi cho học viên trình bày tâm tư, tình cảm, nguyện vọng để có biện pháp giải quyết những vướng mắc, bất cập kịp thời.
- Tổ chức thông báo kết quả học tập sau mỗi học kỳ nghĩ hè về cho gia đình biết để cùng phối hợp động viên con em học tập, rèn luyện.
Tình huống 69. Một số học viên được nhà trường biên chế vào chuyên ngành (khoa đào tạo) không đúng nguyện vọng, có tư tưởng băn khoăn, chán nản
Gợi ý biện pháp xử lý
- Xác minh tình hình tâm tư, nguyện vọng, khả năng công tác của học viên, đề xuất lãnh đạo, chỉ huy biện pháp giải quyết.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tâm tư, nguyện vọng, khả năng công tác, thống nhất biện pháp giải quyết; báo cáo cấp trên xin ý kiến chỉ đạo.
- Sinh hoạt đơn vị giáo dục, quán triệt các quy định, quy chế, mục tiêu, yêu cầu đào tạo của nhà trường và đối chiếu với điểm thi đầu vào, trình độ, năng lực của học viên để động viên xác định tư tưởng yên tâm học tập.
- Đẩy mạnh phong trào thi đua học tập tốt, rèn luyện tốt, tích cực nghiên cứu khoa học, động viên học viên phát huy trí tuệ, năng lực cống hiến xây dựng quân đội.
- Thường xuyên phối hợp giữa đơn vị, địa phương, gia đình quan tâm thăm hỏi, động viên học viên giải quyết những vướng mắc, bất cập trong tư tưởng, nhận thức về phân khoa đào tạo để học viên yên tâm, sẵn sàng nhận và hoàn thành nhiệm vụ.
- Quan tâm chăm lo đời sống vật chất, tinh thần, tạo mọi điều kiện thuận lợi về nơi ăn, ở, sinh hoạt cho học viên yên tâm công tác.
- Tham mưu phản ánh rà soát, rút kinh nghiệm quy trình lựa chọn học viên vào phân khoa đào tạo sát với quy chế, quy định và yêu cầu, nhiệm vụ của nhà trường.
- Báo cáo cấp trên theo quy định.
Tình huống 70. Một số học viên trong tiểu đoàn hình thành một nhóm sinh hoạt riêng, thường xuyên ký nợ hàng quán, ăn, uống, sinh hoạt tùy tiện, chấp hành chế độ không nghiêm, gây bức xúc trong đơn vị
Gợi ý biện pháp xử lý
- Nắm chắc tình hình tư tưởng, kỷ luật, việc ký nợ hàng quán và việc chấp hành chế độ, nền nếp xây dựng đơn vị chính quy; đề xuất các chủ trưởng, biện pháp tham mưu cho cấp ủy, chỉ huy giải quyết.
- Hội ý lãnh đạo, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật và các mối quan hệ của học viên, thống nhất biện pháp xử lý; báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ số học viên quán triệt nhận rõ khuyết điểm, hạn chế, qua đó, nâng cao ý thức chấp hành nghiêm kỷ luật quân đội, quy định của đơn vị, chi tiêu sinh hoạt cá nhân tiết kiệm, phù hợp với điều kiện kinh tế gia đình, bản thân.
- Căn cứ tính chất, mức độ vi phạm chế độ quy định, triển khai học viên viết bản tường trình, bản tự kiểm điểm, tổ chức sinh hoạt đơn vị đề nghị hình thức kỷ luật bảo đảm khách quan, chính xác.
- Phối hợp với cơ quan chức năng của đơn vị, giáo dục, tuyên truyền động viên học viên bằng mọi khả năng của bản thân và giúp đỡ của gia đình, bạn bè thanh toán số tiền nợ cho chủ quán không đề kéo dài.
- Cùng với địa phương, gia đình giáo dục, rèn luyện học viên, tổ chức sinh hoạt chi tiêu cá nhân, ăn uống phù hợp với điều kiện khả năng bản thân, hoàn cảnh gia đình, chấp hành nghiêm kỷ luật quân đội, quy định đơn vị, xây dựng nhà trường chính quy, vững mạnh.
- Rút kinh nghiệm cho cán bộ, học viên nâng cao ý thức chấp hành chi tiêu cá nhân có kế hoạch, phù hợp điều kiện hoàn cảnh gia đình, không làm ảnh hưởng đến đồng chí, đồng đội, xây dựng đơn vị có nền nếp chính quy.
- Quan tâm bảo đảm đời sống vật chất, tinh thần cho học viên học tập, công tác, yên tâm phục vụ lâu dài trong quân đội.
- Duy trì nhiêm chế độ nền nếp xây dựng đơn vị chính quy, nắm, quản lý chặt chẽ tình hình tư tưởng, kỷ luật và mối quan hệ của học viên, nhất là chi tiêu sinh hoạt trong ngày nghỉ, giờ nghỉ, có biện pháp giáo dục kịp thời.
Tình huống 71. Một đồng chí học viên trong nhà trường lo đổ vỡ trong tình yêu hôn nhân, biết người yêu đã yêu người khác, nảy sinh tư tưởng chán nản, không muốn tham gia học tập
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị nhận định, đánh giá tình hình tư tưởng, mối quan hệ yêu đương nam, nữ của học viên, thống nhất biện pháp giải quyết; phân công cán bộ động viên, giúp đỡ.
- Gặp gỡ trao đổi, chia sẽ, động viên học viên nâng cao ý thức hiểu biết về Luật Hôn nhân Gia đình, yêu đương nam, nữ, kết hôn là xuất phát tự nguyện của đôi bên và phải trải qua quá trình tìm hiểu tính cách và mức độ tình cảm của người mình yêu.
- Phối hợp với gia đình, đồng đội động viên học viên hiểu rõ tình yêu hôn nhân phải phù hợp mọi điều kiện của cả đôi bên, nếu không đồng cảm chia sẽ, thì xác định tư tưởng lựa chọn người phù hợp để yên tâm tư tưởng thực hiện tốt nhiệm vụ được giao.
- Tổ chức tốt các hoạt động giao lưu, tọa đàm, văn nghệ, tuyên truyền nâng cao kỹ năng sống, tình yêu hôn nhân và hạnh phúc gia đình cho học viên biết để có biện pháp ứng xử phù hợp.
- Phát huy hiệu quả tổ tư vấn tâm lý trong đơn vị gần gũi, động viên, giúp đỡ, chia sẽ khó khăn vướng mắc về tình yêu nam, nữ cho học viên, ổn định tư tưởng yên tâm tham gia học tập, công tác bình thường.
- Phân công cán bộ theo dõi, giúp đỡ học viên thiếu yên tâm công tác, ổn định tư tưởng, xác định tốt trách nhiệm, hoàn thành nhiệm vụ được giao.
- Tổng hợp tình hình báo cáo cấp trên theo quy định.
Tình huống 72. Một đồng chí học viên sĩ quan của nhà trường lợi dụng quan hệ thân thiết với người dân gần đơn vị đã mượn xe máy tham gia giao thông và bán lấy tiền tiêu xài, gây bất bình trong nhân dân và cán bộ, chiến sĩ đơn vị
Gợi ý biện pháp xử lý
- Phối hợp với cơ quan chức năng của đơn vị xác minh tình hình vụ việc và ý thức chấp hành kỷ luật của học viên, đề xuất cấp ủy, chỉ huy biện pháp xử lý.
- Họp cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật và công tác quản lý học viên của chỉ huy, nguyên nhân, đề xuất biện pháp xử lý; báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ học viên vi phạm quy định mượn tài sản, phương tiện của nhân dân, giáo dục nhận rõ việc làm sai trái; có biện pháp khắc phục sửa chữa, nâng cao ý thức chấp hành nghiêm kỷ luật quân đội, pháp luật Nhà nước, kỷ luật quan hệ quân dân. Chỉ đạo học viên vi phạm khuyết điểm viết bản trường trình, bản tự kiểm điểm, tổ chức sinh hoạt đơn vị đề nghị hình thức kỷ luật đúng quy trình, quy định.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho học viên quán triệt sâu sắc quy định sử dụng phương tiện tham gia giao thông của đơn vị; thực hiện tốt quy định mượn tài sản, hư hỏng phải sửa, mất phải đền, chấp hành nghiêm kỷ luật quân đội để mọi học viên tự giác chấp hành.
- Phối hợp với gia đình học viên khắc phục hậu quả hư hỏng phương tiện  và trả lại, trực tiếp xin lỗi người dân.
- Thông báo với chính quyền địa phương biết về quy định sử dụng phương tiện xe máy của học viên trong quân đội để phối hợp giáo dục và quản lý.
- Tăng cường quản lý chặt chẽ tình hình tư tưởng, kỷ luật và các mối quan hệ của học viện, nhất là quan hệ mượn phương tiện, tài sản của nhân dân, bảo đảm đúng hứa hẹn, giữ gìn phẩm chất đạo đức người học viên sĩ quan.
- Báo cáo cấp trên kết quả xử lý vụ việc
Tình huống 73. Trong đơn vị học viên có dư luận một số đồng chí lười học tập, ôn luyện, hay mang tài liệu vào phòng thi, vi phạm quy chế và gây bất bình trong nội bộ lớp
Gợi ý biện pháp xử lý
- Phối hợp với chỉ huy khoa và giáo viên giảng dạy xác minh tình hình tư tưởng kỷ luật và việc chấp hành quy chế thi, kiểm tra của học viên; kiến nghị các biện pháp xử lý.
- Hội ý cấp ủy, chỉ huy hệ và khoa giáo viên đánh giá tình hình học tập của học viên, việc chấp hành quy định, quy chế thi, kiểm tra của nhà trường, thống nhất biện pháp khắc phục, phân công cán bộ phụ trách.
- Phân loại đối tượng, gặp gỡ giáo dục, quán triệt cho những học viên nhận rõ khuyết điểm, nghiêm túc sửa chữa, nâng cao ý thức tự giác học tập, ôn bài chu đáo để thi, kiểm tra bảo đảm nghiêm túc, có chất lượng; khắc phục dứt điểm vi phạm quy chế thi.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho học viên nâng cao ý thức chấp hành nghiêm quy chế thi, kiểm tra của nhà trường, khắc phục biểu hiện quay cóp, đưa tài liệu vào phòng thi; đánh giá chính xác, khách quan kết quả học tập của học viên.
- Thường xuyên quán triệt cho học viên nhận thức sâu sắc quy chế, quy định thi, kiểm tra của nhà trường, nâng cao ý thức tự giác học tập, rèn luyện, chấp hành nghiêm kỷ luật quân đội, quy định trong thi kiểm tra. Kịp thời xử lý nghiêm kỷ luật đối với những đồng chí vi phạm quy chế thi, đánh giá chính xác, khách quan kết quả học tập.
- Đẩy mạnh phong trào thi đua học tập, rèn luyện cho học viên, nâng cao trình độ kiến thức, nghiệp vụ, đáp ứng mục tiêu, yêu cầu đào tạo của nhà trường.
Tình hướng 74. Trong thời gian diễn tập chiến thuật cuối khóa, một số học viên tự ý vào quán uống rượu, phát ngôn xử sự thiếu văn hóa với người dân, ảnh hưởng xấu đến hình ảnh Bộ đội Cụ Hồ
Gợi ý biện pháp xử lý
- Nắm chắc tình hình, tư tưởng của học viên và công tác quản lý kỷ luật của cán bộ khung, đề xuất các biện pháp ngăn ngừa vi phạm kỷ luật, lập biên bản sự việc (khi cần thiết).
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tính chất, hậu quả vi phạm kỷ luật của học viên, công tác quản lý duy trì nền nếp xây dựng đơn vị chính quy, xác định chủ trương, biện pháp xử lý. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ học viên vi phạm giáo dục, quán triệt nhận rõ khuyết điểm, khắc phục, sửa chữa lối sống sinh hoạt tùy tiện, phát ngôn thiếu văn hóa, nhất là khi quan hệ với nhân dân; nâng cao ý thức chấp hành kỷ luật quân đội, pháp luật Nhà nước, giữ gìn, phát huy phẩm chất Bộ đội Cụ Hồ.
- Chỉ đạo học viên vi phạm lễ tiết tác phong quân nhân viết bản tường trình, bản tự kiểm điểm, tổ chứ sinh hoạt đơn vị đề nghị hình thức kỷ luật đúng quy đinh của Điều lênh Quản lý bộ đội.
- Giáo dục quán triệt nghiêm túc điều lệnh, điều lệ, chỉ thị, quy định của quân đội cho mọi học viên trong đơn vị, nâng cao ý thức tự giác rèn luyện, ứng xử, phát ngôn có văn hóa khi tiếp xúc với nhân dân.
- Thường xuyên rà soát quản lý chặt chẽ tình hình tư tưởng, kỷ luật và các mối quan hệ của bộ đội trong mọi hoạt động của đơn vị, có biện pháp ngăn chặn kịp thời; kiên quyết xử lý nghiêm kỷ luật đối với quân nhân vi phạm, có kế hoạch gặp gỡ giáo dục riêng, giúp đở sửa chữa.
- Phối hợp cấp ủy, chính quyền, ban, ngành, đoàn thể địa phương tổ chức tọa đàm, văn hóa, thể thao, giao lưu, hiểu biết tin cậy, giúp đỡ lẫn nhau.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 75. Một số chiến sĩ trong đại đội cảnh vệ có biểu hiện nhận “quà” của học viên để cho ra, vào cổng nhà trường trong thời gian học tập, ôn luyện
Gợi ý biện pháp xử lý
- Phối hợp với đơn vị cảnh vệ nắm, thống nhất, đánh giá mối quan hệ của học viên, chiến sĩ làm cơ sở xử lý vụ việc.
- Hội ý cấp ủy, chỉ huy đơn vị nhận định, đánh giá tình hình tư tưởng, kỷ luật của học viên; các mối quan hệ chiến sĩ, thống nhất biện pháp giải quyết; phân công cán bộ phụ trách.
- Gặp gỡ riêng chiễn sĩ cảnh vệ và học viên giáo dục, quán triệt hiểu rõ việc làm ảnh hưởng đến phẩm chất, tư cách của người chiến sĩ, vi phạm điều lệnh, điều lệ, chế độ, quy định quân đội; đề cao ý thức tự giác chấp hành nghiêm quy định thời gian học tập, ôn luyện của nhà trường, góp phần xây dựng đơn vị chính quy, nghiêm túc.
- Căn cứ tính chất vụ việc để triển khai cho chiến sĩ vi phạm viết bản trường trình, bản tự kiểm điểm, tổ chức sinh hoạt đơn vị đề nghị hình thức kỷ luật nghiêm túc, có tính giáo dục cao.
- Tổ chức sinh hoạt rút kinh nghiệm về mối quan hệ của chiến sĩ với học viên trong nhà trường, quán triệt sâu sắc các quy định, quy chế ra vào cổng; thực hiện quan hệ trong sạch, lành mạnh, nghiêm túc, xây dựng đơn vị chính quy.
- Duy trì có chất lượng phong trào thi đua, khen thưởng đánh giá chính xác tập thể, cá nhân chấp hành nghiêm kỷ luật ra vào doanh trại, xử lý nghiêm túc những đồng chí vi phạm.
- Báo cáo cấp trên theo quy định.
Tình huống 76. Có một học viên nước ngoài nhận được tin chị ruột bị tai nạn giao thông đang cấp cứu tại bệnh viện, học viên đã báo cáo chỉ huy lớp học xin về thăm chị nhưng chưa được giải quyết, nên đã có biểu hiện buồn chán, muốn bỏ học
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy hệ nắm vững tư tưởng tình cảm của học viên đối với chị ruột, quy định của nhà trường, thống nhất biện pháp giải quyết. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Phân công cán bộ gửi thư (điện thoại) thăm hỏi, chia sẻ với gia đình, thông báo điều kiện học tập, công tác của học viên cho gia đình biết để thông cảm với điều kiện học tập công tác xa nhà và cùng động viên học viên, khắc phục khó khăn trong giải quyết mối quan hệ tình cảm, yên tâm học tập, công tác.
- Phân công cán bộ, bạn bè cùng quê hương thường xuyên quan tâm thăm hỏi, động viên học viên xác định tốt tư tưởng, yên tâm học tập, công tác.
- Xây dựng đơn vị học viên có tinh thần đoàn kết, giúp đỡ, thăm hỏi động viên lẫn nhau khi có hoàn cảnh đột xuất, yên tâm hoàn thành tốt nhiệm vụ được giao.
- Báo cáo cấp trên theo quy định.
VI. ĐỐI TƯỢNG DÂN QUÂN TỰ VỆ
Tình huống 77. Một đồng chí dân quân tự vệ trong thời gian huấn luyện đã sử dụng trang phục được cấp phát ra đường phạt những người phạm Luật Giao thông, vi phạm kỷ luật quân đội và kỷ luật dân vận
Gợi ý biện pháp xử lý
- Hội ý ban chỉ huy quân sự xã đánh giá tình hình sử dụng quân phục cấp phát dân quân tự vệ, thống nhất biện pháp xử lý. Phân công cán bộ phụ trách.
- Gặp gỡ đồng chí dân quân tự vệ giáo dục, quán triệt nhận rõ vi phạm kỷ luật quân đội, pháp luật Nhà nước, ảnh hưởng đến đơn vị; qua đó xây dựng ý thức tự giác chấp hành nghiêm quy chế, quy định sử dụng quân trang, quân phục khi thực hiện nhiệm vụ.
- Căn cứ tính chất, mức độ vi phạm triển khai cho chiến sĩ dân quân tự vệ viết bản tường trình, bản tự kiểm điểm, tổ chức sinh hoạt đơn vị đề nghị hình thức kỷ luật đúng mức.
- Tổ chức sinh hoạt rút kinh nghiệm trong đơn vị, quán triệt sâu sắc quy định về sử dụng trang phục của cán bộ, chiến sĩ dân quân tự vệ, chấp hành nghiêm kỷ luật quân đội, pháp luật Nhà nước, nâng cao ý thức tự giác chấp hành quy định sử dụng quân phục dân quân tự vệ trong khi làm nhiệm vụ.
- Nghiên cứu đề xuất sửa đổi quy định, quy chế sử dụng trang phục dân quân tự vệ trong khi làm nhiệm vụ nhằm khắc phục hạn chế, khuyết điểm vi phạm kỷ luật, pháp luật.
- Tăng cường quản lý tư tưởng, kỷ luật dân quân tự vệ trong thời gian huấn luyện của đơn vị, có biện pháp ngăn chặn kịp thời các vi phạm.
- Quản lý chặt chẽ việc sử dụng quân phục dân quân tự vệ về số lượng, chất lượng, nhất là những đồng chí hết thời hạn làm nhiệm vụ có kế hoạch thu hồi.
Tình huống 78. Một số đồng chí dân quân tự vệ của đơn vị lấy lý do mức chi trả tiền tham gia ngày công huấn luyện của Nhà nước thấp hơn lao động ngoài thị trường, do đó thiếu tích cực, tự giác trong học tập
Gợi ý biện pháp xử lý
- Hội ý chỉ đạo, chỉ huy đơn vị đánh giá tình hình tư tưởng dân quân tự về, phân loại đối tượng, thống nhất biện pháp xử lý.
- Tổ chức giáo dục, tuyên truyền cho chiến sĩ dân quân tự vệ nhận thức rõ Luật Dân quân tự vệ và các tiêu chuẩn, chế độ chính sách quân đội, địa phương chi trả trong thời gian huấn luyện; qua đó xác định vinh dự, trách nhiệm, nghĩa vụ, yên tâm hoàn thành nhiệm vụ được giao.
- Phối hợp với cấp ủy, chính quyền địa phương và gia đình giáo dục, tuyên truyền cho dân quân tự về nắm vững Luật Dân quân tự vệ, tiêu chuẩn, chế độ chính sách của Đảng, Nhà nước đối với nhiệm vụ huấn luyện, sẵn sàng chiến đấu và trách nhiệm, vinh dự của mỗi công dân.
- Làm tốt việc thông báo kết quả huấn luyện, rèn luyện của dân quân tự vệ cho chính quyền địa phương và gia đình biết; phối hợp động viên, cổ vũ, nâng cao ý thức trách nhiệm học tập công tác, rèn luyện.
- Quan tâm bảo đảm tiêu chuẩn, chế độ chính sách vật chất, tinh thần cho dân quân tự vệ trong thời gian huấn luyện để yên tâm gắn bó với nhiệm vụ.
- Tham mưu cho cấp ủy, chính quyền địa phương quan tâm tạo mọi điều kiện về cơ sở vật chất cho dân quân tự vệ, nâng cao chất lượng thực hiện nhiệm vụ huấn luyện.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 79. Một chiến sĩ dân quân tự vệ trong thời gian huấn luyện nhặt được chiếc ví có tiền và giấy tờ tùy thân của một người dân, chiễn sĩ đã nhắn tin cho người đánh mất, yêu cầu phải đưa lại tiền mới cho chuộc ví
Gợi ý biện pháp xử lý
- Nắm tình hình tư tưởng thái độ, trách nhiệm của đồng chí dân quân tự vệ nhặt được ví tiền của người dân và những diễn biến tư tưởng phát sinh, đề xuất biện pháp xử lý.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình diễn biến tư tưởng, kỷ luật của đồng chí dân quân tự vệ khi nhặt được ví tiền của người dân, thống nhất biện pháp giải quyết; báo cáo cấp trên xin ý kiến chỉ đạo.
- Tổ chức gặp gỡ đồng chí dân quân tự vệ nhặt được ví tiền của người dân giáo dục, quán triệt, nhận rõ quyền lợi, nghĩa vụ, trách nhiệm của người bị mất và người nhặt được của rơi; gương mẫu làm việc tốt và chấp hành nghiêm pháp luật Nhà nước, kỷ luật quân đội. Căn cứ tính chất, mức độ vi phạm, nhất là việc nhận khuyết điểm, chỉ đạo đồng chí dân quân tự vệ viết bản tường trình, tự kiểm điểm, tổ chức sinh hoạt đơn vị (đề nghị hình thức kỷ luật phù hợp với lỗi phạm).
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm chung về sự việc cho lực lượng dân quân tự vệ nêu cao ý thức chấp hành nghiêm pháp luật Nhà nước, kỷ luật quân đội, quy định đơn vị; qua đó rèn luyện phẩm chất, đạo đức của người quân nhân.
- Phát huy vai trò của các tổ chức, lực lượng trong đơn vị, tổ chức sinh hoạt, tọa đàm, giao lưu, giáo dục, tuyên truyền cho dân quân tự vệ nâng cao trách nhiệm, đồng cảm, chia sẻ mất mát đối với nhân dân, đồng chí, đồng đội, nhất là những người gặp hoàn cảnh đặc biệt khó khăn.
- Thường xuyên quản lý nắm chắc tình hình tư tưởng, kỷ luật và các mối quan hệ xã hội của dân quân tự vệ, chủ động phát hiện xử lý có hiệu quả các vấn đề nảy sinh. Báo cáo cấp trên theo quy định.
Tình huống 80. Một đồng chí dân quân tự về không nhận nhiệm vụ chữa cháy rừng với lý do chính sách chi trả tiền của Nhà nước quá thấp, không tương xứng công sức, gây dư luận không tốt trong nhân dân và lực lượng dân quân tự vệ
Gợi ý biện pháp xử lý
- Trao đổi trong ban chỉ huy quân sự xã nhận định tình hình tư tưởng, trách nhiệm của dân quân tự vệ trong thực hiện nhiệm vụ chữa cháy rừng, thống nhất biện pháp giải quyết. Báo cáo, xin ý kiến chỉ đạo của đảng ủy quân sự xã để bố trí người thay thế.
- Gặp gỡ số dân quân có biểu hiện không nhận nhiệm vụ chữa cháy rừng giáo dục, quán triệt hiểu rõ tác hại của sự chậm trễ trong phòng, chống cháy rừng, trách nhiệm, quyền lời, nghĩa vụ của mọi công dân; qua đó xây dựng trách nhiệm sẵn sàng nhận và hoàn thành nhiệm vụ, nâng cao ý thức chấp hành Luật Dân quân tự vệ, kỷ luật quân đội, quy định của địa phương.
- Phối hợp với gia đình, người thân và đồng chí, đồng đội, động viên số dân quân còn băn khoăn trong quá trình nhận nhiệm vụ, nâng cao ý thức, trách nhiệm của dân quân tự vệ sẵn sàng nhận nhiệm vụ chữa cháy rừng.
- Tham mưu cho ban chỉ huy quân sự xã tổ chức sinh hoạt rút kinh nghiệm công tác huy đông quân số chữa cháy rừng về ý thức thực hiện nhiệm vụ trong điều kiện khẩn trương, phức tạp và tác hại của sự chậm trễ; căn cứ tính chất vụ việc có thể đề nghị hình thức kỷ luật số dân quân chấp hành không nghiêm mệnh lệnh, đồng thời rà soát, lựa chọn những đồng chí có đủ phẩm chất chính trị, trách nhiệm trong công tác tham gia vào lực lượng dân quân của xã.
- Thường xuyên giáo dục, quán triệt các quy định, quy chế tổ chức hoạt động của dân quân tự vệ nâng cao ý thức trách nhiệm trong thực hiện nhiệm vụ.
- Làm tốt công tác đánh giá kết quả hoàn thành nhiệm vụ của lực lượng dân quân tự vệ, kịp thời biểu dương, khen thưởng tập thể, cá nhân có thành tích, kỷ luật nghiêm túc những đồng chí vi phạm.
- Báo cáo cấp trên theo quy định.
Tình huống 81. Một chiến sĩ dân quân tự vệ làm nhiệm vụ tuần tra trên địa bàn nhặt được tờ rơi của kẻ xấu đã cất giữ và đọc cho đồng đội nghe gây tâm lý hoan mang lo lắng
Gợi ý biện pháp xử lý
- Tổ chức thu gom tờ rơi nộp cho cơ quan chức năng xử lý.
- Nhận định về tính chất, mục đích của kẻ xấu, đặc điểm, tình hình an ninh chính trị, trật tự an toàn xã hội trên địa bàn; đề xuất biện pháp giải quyết với cấp ủy, ban chỉ huy quân sự xã.
- Hội ý cấp ủy, ban chỉ huy quân sự xã đánh giá về âm mưu, thủ đoạn hoạt động chống phá của các thế lực phản động, thù địch; tình hình an ninh chính trị, trật tự an toàn xã hội trên địa bàn, thống nhất biện pháp xử lý. Báo cáo cấp trên theo quy định.
- Gặp gỡ chiến sĩ dân quân tự vệ nhặt được tờ rơi của kẻ xấu giáo dục, quán triệt hiểu rõ âm mưu, thủ đoạn hoạt động chống phá của các thế lực thù địch, tuyên truyền, kích động, lôi kéo nhân dân làm mất an ninh chính trị, trật tự an toàn xã hội; căn cứ tính chất, thái độ nhận khuyết điểm của đồng chí dân quân tự vệ để xem xét xử lý phù hợp.
- Tổ chức sinh hoạt giáo dục, tuyên truyền, định hướng nhận thức, tư tưởng nâng cao ý thức cảnh giác cho dân quân tự vệ không nghe và tin theo tuyên truyền của các thế lực thù địch; vận động gia đình, người thân phát hiện tố giác những hành vi vi phạm.
- Tham mưu cho cấp ủy, chính quyền nhân dân địa phương tuyên truyền, vận động nhân dân chấp hành nghiêm đường lối, chủ trưởng của Đảng, pháp luật Nhà nước; nâng cao ý thức cảnh giác, không tin, không nghe kẻ xấu kích động, xúi giục làm mất an ninh chính trị, trật tự an toàn xã hội.
- Thường xuyên làm tốt công tác rà soát chất lượng chính trị nội bộ, lựa chọn dân quân tự về đủ tiêu chuẩn chính trị, phẩm chất đạo đức, năng lực công tác tham gia vào lực lượng thường trực đủ sức hoàn thành nhiệm vụ.
- Quản lý chặt chẽ tư tưởng, kỷ luật và các mối quan hệ xã hội của cán bộ, chiến sĩ dân quân tự vệ, chủ động thông tin, định hướng nhận thức, tư tưởng trước những vấn đề nhạy cảm, phức tạp.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 82. Trong thời gian huấn luyện một số dân quân đã tự ý bỏ đơn vị ra quán uống cà phê cùng với một số thanh niên địa phương, trong đó có người theo đạo; quá trình trò chuyện đã chế giễu giáo lý của người giáo dân xảy ra mâu thuẫn và gây mất đoàn kết quân dân, đoàn kết lương giáo
Gợi ý biện pháp xử lý
- Bằng mọi biện pháp ngăn chặn không để xảy ra vụ việc gây mâu thuẫn nghiêm trọng, nếu có thương tích đưa nạn nhân đi bệnh viện điều trị. Xác minh tình hình sự việc gây mất đoàn kết quân dân; đoàn kết lương giáo, đánh giá nguyên nhân, đề xuất biện pháp với cấp ủy, chỉ huy giải quyết.
- Trao đổi trong lãnh đạo, chỉ huy đơn vị đánh giá tình hình mâu thuẫn giữa chiến sĩ của đơn vị với thanh niên địa phương theo đạo và tình hình an ninh chính trị, trật tự an toàn xã hội trên địa bàn, thống nhất biện pháp xử lý; phân công cán bộ phụ trách.
- Gặp gỡ chiến sĩ dân quân tự vệ chỉ rõ khuyết điểm ảnh hưởng đến mối quan hệ đoàn kết quân dân, làm mất an ninh chính trị, trật tự an toàn xã hội trên địa bàn; định hướng cách thức xử lý, giải hòa mâu thuẫn với thanh niên địa phương, giáo dục, nâng cao ý thức chấp hành kỷ luật quân đội, quy định đơn vị.
- Chỉ đạo những quân nhân vi phạm khuyết điểm viết bản tường trình, bản tự kiểm điểm, tổ chức sinh hoạt đơn vị đề nghị hình thức kỷ luật quan hệ quân dân.
- Tổ chức sinh hoạt đơn vị, rút kinh nghiệm cho cán bộ, chiến sĩ nâng cao ý thức chấp hành pháp luật Nhà nước, kỷ luật quân đội, quy định của địa phương; xây dựng tinh thần đoàn kết lương giáo, đoàn kết quân dân.
- Thường xuyên duy trì chặt chẽ chế độ, nền nếp xây dựng đơn vị chính quy, quản lý kỷ luật bộ đội, nhất là trong ngày nghỉ, giờ nghỉ, hoạt động ngoài doanh trại, khu vực dân cư có người theo đạo để có biện pháp giáo dục, ngăn chặn kịp thời.
- Duy trì có chất lượng hoạt động giao lưu văn hóa văn nghệ vui tươi, lành mạnh, tăng cường hiểu biết, tôn trọng lẫn nhau, xây dựng mối đoàn kết gắn bó quân dân trên địa bàn.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 83. Một đồng chí nam dân quân tự vệ đã có gia đình nhưng vẫn còn quan hệ yêu đương với nữ chiến sĩ dân quân trong thời gian huấn luyện, gây dư luận không tốt trong cán bộ, chiến sĩ và nhân dân 
Gợi ý biện pháp xử lý
- Đánh giá tình hình tư tưởng, kỷ luật của dân quân tự vệ, nhất là mối quan hệ của nam, nữ chiến sĩ dân quân trong đơn vị; đề xuất với cấp ủy, chỉ huy biện pháp giải quyết.
- Hội ý ban chỉ huy đơn vị thống nhất nhận định, đánh giá tình hình chấp hành kỷ luật dân quân tự vệ, mối quan hệ giữa nam dân quân tự vệ đã có gia đình với nữ dân quân tự vệ, thống nhất biện pháp xử lý; báo cáo cấp trên, xin ý kiến chỉ đạo.
- Gặp gỡ nam và nữ chiến sĩ dân quân tự vệ giáo dục, quán triệt nhận rõ khuyết điểm, hạn chế trong mối quan hệ giữa người đã có gia đình còn yêu đương với nữ chiến sĩ chưa chồng là vi phạm Luật Hôn nhân và Gia đình, kỷ luật quân đội.
- Trường hợp đã gây ra hậu quả, phối hợp chặt chẽ với gia đình, địa phương cùng giải quyết phù hợp, tùy theo tính chất, mức độ triển khai đồng chí nam, nữ dân quân tự vệ viết bản tường trình, bản tự kiểm điểm; sinh hoạt đơn vị đề nghị hình thức kỷ luật đúng mức.
- Phối hợp với hội phụ nữ của địa phương gặp riêng giáo dục cho nữ dân quân nhận rõ sai phạm, khắc phục sửa chữa và tự giác chấp hành nghiêm Luật Hôn nhân và Gia đình, thực hiên quy định quan hệ một vợ một chồng lành mạnh.
- Thường xuyên làm tốt công tác, quản lý tư tưởng, kỷ luật và các mối quan hệ xã hội của dân quân tự vệ trong thời gian huấn luyện, nhất là quan hệ nam, nữ không lành mạnh, có biện pháp xử lý, phòng ngừa.
- Tổ chức sinh hoạt văn hóa tinh thần vui tươi, lành mạnh, xây dựng mối quan hệ nam, nữ trong sáng, lành mạnh trong đơn vị.
- Báo cáo kết quả xử lý lên cấp trên.
Tình huống 84. Một chiến sĩ dân quan có biểu hiện cục bộ địa phương, hay chia rẽ mất đoàn kết nội bộ, bắt nạt một số đồng chí yếu đuối hơn trong đơn vị, gây tâm lý lo lắng trong chiến sĩ dân quân
Gợi ý biện pháp xử lý
- Có biện pháp ngăn chặn kịp thời không để xảy ra hậu quả xấu trong mối quan hệ của chiến sĩ, xác minh tình hình, nguyên nhân, đề xuất biện pháp cấp ủy, chỉ huy đơn vị giải quyết.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật của dân quân tự vệ, nguyên nhân chia rẽ mất đoàn kết nội bộ, thống nhât biện pháp xử lý. Báo cáo cấp trên theo quy định.
- Triệu tập nhóm chiến sĩ dân quân tự vệ cục bộ, chia rẽ bè cánh, dọa nạt chiến sĩ yếu đuối trong đơn vị, giáo dục hiểu rõ việc làm sai trái ảnh hưởng đến đoàn kết nội bộ, bản chất truyền thống Bộ đội Cụ Hồ, nâng cao ý thức chấp hành kỷ luật quân đội, quy định của đơn vị. Căn cứ mức độ vi phạm triển khai cho số chiến sĩ có sai phạm viêt bản tường trình, bản tự kiểm điểm, sinh hoạt đơn vị đề nghị hình thức kỷ luật đúng quy định.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho cán bộ, chiến sĩ dân quân tự vệ nâng cao ý thức chấp hành kỷ luật quân đội, quy định đơn vị, tăng cường xây dựng mối quan hệ đoàn kết nội bộ, tăng cường giúp đỡ lẫn nhau cùng hoàn thành tốt nhiệm vụ.
- Tăng cường quản lý chặt chẽ tình hình tư tưởng, kỷ luật bộ đội trong mọi hoạt động thời gian tổ chức huấn luyện của đơn vị; chủ động phát hiện những vấn đề nảy sinh, có biện pháp giải quyết kịp thời.
- Xử lý nghiêm kỷ luật đối với những đồng chí hay gây mất đoàn kết nội bộ để chấn chỉnh, răn đe, giữ nghiêm kỷ luật trong đơn vị.
- Duy trì có chất lượng hoạt động văn hóa văn nghệ, thể dục thể thao, vui chơi giải trí trong đơn vị tăng cường hiểu biết, tôn trọng, giúp đỡ lẫn nhau cùng hoàn thành nhiệm vụ.
Tình huống 85. Khi điều động lực lượng dân quân tự vệ làm nhiệm vụ khắc phục sự cố môi trường trên địa bàn, một số chiến sĩ theo đạo không chấp hành mệnh lệnh chỉ huy mà còn đi theo, cổ vũ việc làm sai trái của phần tử xấu, làm lo lắng bất bình trong lực lượng và nhân dân
Gợi ý biện pháp xử lý
- Báo cáo tình hình sự việc chiến sĩ chấp hành không nghiêm mệnh lệnh người chỉ huy và xin ý kiến chỉ đạo của ban chỉ huy quân sự huyện.
- Hội ý ban chỉ huy quân sự xã đánh giá tình hình tư tưởng, kỷ luật dân quân tự vệ, trật tự an toàn xã hội trên địa bàn, đề xuất cấp ủy, ủy ban nhân dân xã biện pháp xử trí.
- Phân loại đối tượng, tổ chức gặp gỡ chiến sĩ theo đạo, giáo dục, tuyên truyền hiểu rõ đường lối, quan điểm của Đảng, pháp luật Nhà nước về tôn giáo, Luật Dân quân tự vệ, nâng cao ý thức cảnh giác, không nghe, không tin kẻ xấu tuyên truyền, xuyên tạc, kích động, làm mất an ninh chính trị, trật tự an toàn địa bàn. Căn cứ vào tính chất vi phạm, triển khai số dân quân tự vệ vi phạm viết bản tường trình, bản tự kiểm điểm, sinh hoạt đơn vị đề nghị hình thức kỷ luật.
- Phối hợp với cấp ủy, chính quyền địa phương tổ chức tuyên truyền, vận động nhân dân nói chung, lực lương dân quân tự vệ nói riêng chấp hành nghiêm đường lối, chủ trương của Đảng, pháp luật Nhà nước; không tin, không nghe kích động, dụ đỗ của phần tử xấu; nâng cao ý thức cảnh giác và vận động gia đình, người thân chấp hành nghiêm đường lối, chủ trương của Đảng, pháp luật Nhà nước, xây dựng địa bàn an toàn.
- Phát huy vai trò của các tổ chức, lực lượng trong xã, tổ chức tuyên truyền, giáo dục cho dân quân tự vệ là người theo đạo sống tốt đời đẹp đạo, kính chúa yêu nước, chấp hành nghiêm pháp luật Nhà nước.
- Tăng cường nắm, quản lý tư tưởng, kỷ luật dân quân tự vệ, nhất là những đồng chí có biểu hiện quan hệ bất thường với những đối tượng lạ mặt, có biện pháp xử lý kịp thời.
- Xử lý nghiêm kỷ luật đối với những đồng chí dân quân tự vệ chấp hành không nghiêm mệnh lệnh người chỉ huy, lôi kéo, móc nối với phần tử xấu, làm mất ổn định tình hình đơn vị.
- Thường xuyên chủ động nắm chắc tình hình địa bàn, những hoạt động lợi dụng tôn giáo kích động nhân dân biểu tình, chống đối làm mất an ninh chính trị, trật tự an toàn xã hội.
Tình huống 86. Gia đình một đồng chí dân quân cơ động nằm trong khu vực nguy hiểm bảo lũ buộc phải di dời theo quy định của xã, nhưng đồng chí không gương mẫu chấp hành mà còn có biểu hiện thách thức chính quyền, gây bất bình lo lắng trong nhân dân
Gợi ý biện pháp xử lý
- Báo cáo tình hình sự việc với ban chủ huy quân sự xã xin ý kiến chỉ đạo.
- Trực tiếp gặp gỡ chiến sĩ dân quân trao đổi, phân tích hiểu rõ sự quan tâm, chăm lo của Đảng, Nhà nước đối với cuộc sống của nhân dân, ý nghĩa của việc di dời nhân dân ra khỏi vùng nguy hiểm bảo lũ; đồng thời động viên gia đình chấp hành nghiêm quy định của chính quyền địa phương, bảo đảm an toàn về người và tài sản.
- Phối hợp cấp ủy, chính quyền địa phương tổ chức tuyên truyền, vận động nhân dân chấp hành nghiêm quy định phòng, chống, khắc phục hậu quả thiên tai của Nhà nước và địa phương.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho lực lượng dân quân tự vệ, giáo dục củng cố, nâng cao ý thức chấp hành nghiêm mệnh lệnh của người chỉ huy; gương mẫu vận động gia đình, người thân nhanh chóng di dời về nơi an toàn là trách nhiệm và quyền lợi của bản thân.
- Tăng cường nắm, quản lý giáo dục, định hướng nhận thức tư tưởng, kỷ luật chiến sĩ dân quân tự vệ, nhất là những đồng chí có biểu hiện thiếu yên tâm, chưa hiểu sâu sắc ý nghĩa việc làm.
- Thường xuyên bồi dưỡng, kiện toàn lực lượng dân quân đủ số lượng, có chấp lượng bổ sinh vào lực lượng dân quân tự vệ đáp ứng yêu cầu, nhiệm vụ.
Tình huống 87. Một đồng chí dân quân tự vệ nhặt và tập kết một số vật liệu nổ từ thời chiến tranh đã mang bán cho người dân gần đơn vị, gây tư tưởng hoang mang lo lắng cho nhân dân trên địa bàn
Gợi ý biện pháp xử lý
- Xác minh rõ sự việc và thái độ của dân quân tự vệ trong việc chấp hành quy định quản lý, tàng trữ, mua bán vật liệu nổ; đề xuất chủ trưởng, giải pháp cho cấp ủy, chỉ huy đơn vị xử lý.
- Hội ý cấp ủy, chỉ huy ban chỉ huy quân sự xã đánh giá tình hình công tác quản lý vật liệu nổ của chỉ huy đơn vị, tính chất vụ việc, xác định chủ trương, biện pháp lãnh đạo, chỉ đạo giải quyết. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Phối hợp với cơ quan chức năng bằng mọi biện pháp kịp thời ngăn chặn không để xảy ra mất an toàn. Lập biên bản thu hồi vật liệu nổ, thu gom sai quy định và báo cáo với chỉ huy các cấp theo quy định.
- Gặp gỡ chiến sĩ dân quân tự vệ giáo dục, tuyên truyền nâng cao ý thức hiểu biết về tác hại, hậu quả của mất an toàn vật liệu nổ, ảnh hưởng đến tính mạng, sức khỏe của người dân và những người có liên quan, làm mất an ninh chính trị, trật tự an toàn xã hội; qua đó chấp hành nghiêm quy định việc thu gom vật liêu nổ.
 	- Căn cứ tính chất, mức độ vị phạm quy định an toàn, triển khai cho đồng chí dân quân viết bản tường trình, bản tự kiểm điểm, sinh hoạt đơn vị để xem xét kỷ luật đúng mức.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho chiến sĩ dân quân tự vệ hiểu rõ về tác hại, hậu quả của mất an toàn thu gôm vật liệu nổ là rất lớn; nâng cao ý thức chấp hành quy tắc bảo đảm an toàn.
- Tăng cường quản lý chặt chẽ vật liệu nổ trôi nổi trên địa bàn, có biện pháp xử lý bảo đảm an toàn.
- Thường xuyên quán triệt, nhắc nhở, định hướng cho dân quân tự vệ chấp hành nghiêm quy định trong quản lý, thu gom vật liệu nổ.
Tình huống 88. Một đồng chí phó ban chỉ huy quân sự xã đã so sánh mức lương (phụ cấp) trong thực hiện nhiệm với đi làm tại các khu công nghiệp, nên nảy sinh tư tưởng thiếu yên tâm công tác, viết đơn xin nghỉ việc
Gợi ý biện pháp xử lý
- Nắm tình hình tâm tư, nguyện vọng của đồng chí phó ban chỉ huy quân sự xã trong thực hiện nhiệm vụ được giao, những vấn đề nảy sinh; đề xuất biện pháp xử lý, báo cáo với đảng ủy, ban chỉ huy quân sự huyện xin ý kiến chỉ đạo. 
- Hội ý cấp ủy, ban chỉ huy quân sự xã đánh giá tình hình tư tưởng, chất lượng hoàn thành nhiệm vụ của cán bộ, chiến sĩ dân quân và công tác bảo đảm tiêu chuẩn, chế độ chính sách theo quy định của Đảng, Nhà nước; thống nhất biện pháp giải quyết.
-  Gặp gỡ đồng chí phó ban chỉ huy quân sự xã tìm hiểu tâm tư, nguyện vọng, vinh dự, trách nhiệm, tín nhiệm của nhân dân, đảng ủy, ủy ban nhân dân xã đối với một cán bộ phó ban chỉ huy quân sự xã, cũng như tiêu chuẩn, chế độ đãi ngộ của Nhà nước đối với cán bộ; qua đó nhận thức đúng, đủ và xác định tốt trách nhiệm.
- Phối hợp với các tổ chức, lực lượng trong xã tuyên truyền, động viên đồng chí phó ban chỉ huy quân sự xã hiểu rõ nghĩa vụ, trách nhiệm của người cán bộ, đảng viên trong việc thực hiện nhiệm vụ quân sự, xác định tốt nhiệm vụ được giao.
- Bảo đảm tiêu chuẩn, chế độ, chính sách đúng quy định của Nhà nước, làm cho cán bộ yên tâm gắn bó với nhiệm vụ.
- Thường xuyên kiện toàn, bồi dưỡng đội ngũ cán bộ ban chỉ huy quân sự xã có đủ trình độ, phẩm chất năng lực, nhiệt tình, trách nhiệm đối với công tác được giao, đáp ứng yêu cầu, nhiệm vụ.
- Rà soát các quy định, quy chế quản lý cán bộ đúng với quy định của Nhà nước phù hợp với điều kiện tình hình, nhiệm vụ của địa phương.
Tình huống 89. Một đồng chí tự vệ công tác trong cơ quan ngân hàng nông nghiệp nông thôn huyện lấy lý do bận công việc chuyên môn, không nhận nhiệm vụ huấn luyện
Gợi ý biện pháp xử lý
- Nắm tình hình tư tưởng, trách nhiệm, điều kiện công việc của đồng chí tự về công tác trong cơ quan ngân hàng huyện, tham mưu ban chỉ huy quân sự biện pháp giải quyết.
- Hội ý ban chỉ huy quân sự đánh giá tình hình tư tưởng, trách nhiệm công tác của nhân viên ngân hàng  huyện, thống nhất biện pháp giải quyết. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Phối hợp với ban giám đốc ngân hàng huyện tuyên truyền, giáo dục, động viên, tạo mọi điều kiện thuân lợi cho nhân viên tham gia huấn luyện đúng, đủ quy đình, bảo đảm thời gian.
- Phối hợp với ban giám đốc ngân hàng gặp gỡ đồng chí tự vệ phổ biến quy chế, quy định của pháp luật về huấn luyện quân sự hàng năm; qua đó đề cao ý thức, trách nhiệm, tham gia đây đủ, đúng chương trình huấn luyện quân sự của ban chỉ huy quân sự huyện.
- Chủ động xây dựng kế hoạch, thông báo bổ sung thành phần, đối tượng tham gia huấn luyện quân sự để mọi cơ quan, đơn vị chủ đông sắp xếp công việc phân công dân quân tự vệ tham gia đầy đủ.
- Quan tâm bảo đảm đầy đủ đời sống vật chất, tinh thần, tạo mọi điều kiện thuận lợi cho dân quân tự vệ huấn luyện đạt kết quả tốt.
VII. ĐỐI TƯỢNG DỰ BỊ ĐỘNG VIÊN
Tình huống 90. Trong thời gian huấn luyện dự bị động viên, một số quân nhân dự bị mang xe máy gửi ở nhà dân để đi về nhà vào ngày nghỉ, giờ nghỉ, gây tâm lý so bì trong đơn vị
Gợi ý biện pháp xử lý
- Nắm tình hình chấp hành quy định sử dụng phương tiện cá nhân trong thời gian huấn luyện dự bị động viên về việc duy trì chế độ nền nếp xây dựng đơn vị chính quy; đề xuất cấp ủy, chỉ huy biện pháp giải quyết.
- Hội ý chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật quân nhân dự bị và việc duy trì chế độ, nền nếp xây dựng đơn vị chính quy, thống nhất biện pháp giải quyết.
- Gặp gỡ riêng những đồng chí quân nhân dự bị gửi phương tiện ở nhà dân đề đi về nhà vào ngày nghỉ, giờ nghỉ, giáo dục, quán triệt chấp hành nghiêm quy định của đơn vị trong thời gian huấn luyện, kỷ luật quân đội, Luật Giao thông đường bộ, không làm ảnh hưởng đến thời gian, chất lượng huấn luyện và chế độ nền nếp xây dựng chính quy của đơn vị.
- Tổ chức sinh hoạt đơn vị quán triệt cho quân nhân dự bị nhận thức sâu sắc kỷ luật quân đội, quy định đơn vị, đề cáo trách nhiệm tự giác chấp hành nghiêm quy định sử dụng phương tiện tham gia giao thông trong thời gian huấn luyện.
- Quản lý chặt chẽ tư tưởng, kỷ luật quân nhân dự bị, kịp thời phát hiện giải quyết tốt các vấn đề nảy sinh.
- Thường xuyên quán triệt quy chế, sử dụng phương tiện tham gia giao thông cho quân nhân dự bị trong thời gian tập trung huấn luyện, xây dựng ý thức tự giác chấp hành nghiêm túc quy định đơn vị.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 91. Một quân nhân dự bị đang làm việc tại công ty liên doanh với người nước ngoài nhận nhiệm vụ tham gia huấn luyện quân sự, nhưng ban quản lý công ty thông báo nếu sau này trở về cơ quan sẽ không nhận làm việc nữa, ảnh hưởng đến tư tưởng và kết quả thực hiện nhiệm vụ
Gợi ý biện pháp xử lý
- Xác minh tình hình tư tưởng, kỷ luật quân nhân dự bị, đặc điểm công ty liên doanh với nước ngoài, báo cáo cấp ủy, chỉ huy đơn vị giải quyết.
- Trao đổi trong đảng ủy, ban chỉ huy quân sự huyện nhận định, đánh giá tình hình, tư tưởng nảy sinh của quân nhân dự bị đang làm việc trong công ty có yếu tố nước ngoài, thống nhất biện pháp giải quyết; cử cán bộ trực tiếp phối hợp với công ty giải quyết sự việc.
- Phối hợp với cấp ủy, chính quyền địa phương chỉ đạo công ty nơi quân nhân dự bị làm việc, tạo điều kiện thuận lời để quân nhân tham gia huấn luyện quân sự đúng thành phần, thời gian quy định và thường xuyên quan tâm đến nhiệm vụ quân sự quốc phòng của địa phương.
- Phối hợp với cấp ủy, chính quyền và các ban, ngành, đoàn thể địa phương gặp gỡ, giáo dục, động viên quân nhân dự bị, nâng cao ý thức, trách nhiệm sắp xếp thời gian tham gia huấn luyện đúng thành phần quy định.
- Tham mưu với cấp ủy, chính quyền địa phương sửa đổi, bổ sung những quy định, quy chế về công tác phối hợp nhiệm vụ quân sự quốc phòng, an ninh với hoạt động sản xuất kinh doanh của công ty, xí nghiệp đóng trên địa bàn theo đúng quy định của pháp luật, thường xuyên quan tâm, tạo điều kiện cho công nhân tiếp tục về làm việc với công ty sau khi hoàn thành nhiệm vụ huấn luyện.
- Quan tâm bảo đảm tiêu chuẩn, chế độ chính sách trong quá trình huấn luyện đúng quy định của Nhà nước, quân đội để quân nhân dự bị yên tâm hoàn thành nhiệm vụ được giao.
- Làm tốt công tác nắm, quản lý tư tưởng, kỷ luật của lực lượng quân nhân dự bị, không để phát tán những thông tin tài liệu mật trong huấn luyện quân sự sau khi trở về doanh nghiệp tiếp tục công tác.
Tình huống 92. Một quân nhân dự bị tham gia huấn luyện, nhưng thường xuyên xin nghỉ đột xuất, ảnh hưởng chất lượng huấn luyện và tư tưởng của các đồng chí khác
Gợi ý biện pháp xử lý
- Hội ý chỉ huy đơn vị đánh giá tình hình chấp hành chế độ thời gian, hoàn cảnh gia đình của quân nhân dự bị tham gia huấn luyện, thống nhất biện pháp giải quyết.
- Gặp gỡ riêng đối với những quân nhân dự bị hay xin nghỉ đột xuất, giáo dục xác định rõ trách nhiệm, nghĩa vụ trong thực hiện nhiệm vụ, điều chỉnh công việc cá nhân cho phù hợp, tập trung cao độ cho nhiệm vụ huấn luyện quân sự của đơn vị.
- Tổ chức sinh hoạt giáo dục, quán triệt quân nhân dự vị thức hiện đúng nội dung, chương trình, thời gian huấn luyện, chấp hành nghiêm chế độ, nền nếp xây dựng chính quy, ý thức tự giác chấp hành nghiêm kỷ luật quân đội, quy định đơn vị trong thời gian huấn luyện.
- Quản lý, duy trì chặt chẽ quân nhân dự bị chấp hành đúng chương trình huấn luyện quân sự bảo đảm thời gian, chất lượng, hiệu quả, khắc phục biểu hiện nghỉ giữa giờ, nghỉ đột xuất.
- Quản lý chặt chẽ tư tưởng, kỷ luật và các mối quan hệ xã hội của quân nhân dự bị trong thời gian huấn luyện để có biện pháp giáo dục, giúp đỡ.
- Phối hợp với cấp ủy, chính quyền địa phương tuyên truyền, vận động gia đình, người thân tạo điều kiện thuận lợi về thời gian cho quân nhân dự bị tham gia huấn luyện đạt kết quả cao.
- Quan tâm bảo đảm đầy đủ tiêu chuẩn, chế độ chính sách, vật chất, tinh thần cho quân nhân dự bị yên tâm thực hiện nhiệm vụ.
- Tổng hợp tình hình báo cáo cấp trên theo quy định.
Tình huống 93. Một số quân nhân dự bị trong thời gian tập trung huấn luyện thường xuyên bỏ đơn vị ra quán uống rượu,bia, phát ngôn thiếu văn hóa, vi phạm kỷ luật quân đội và ảnh hưởng tư tưởng nhân dân
Gợi ý biện pháp xử lý
- Hội ý chỉ huy đại đội đánh giá tình hình tư tưởng quân nhân dự bị, thống nhất biện pháp giải quyết. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ quân nhân dự bị giáo dục, quán triệt, nhận rõ khuyết điểm, hạn chế vi phạm quy định sử dụng rượu, bia, nâng cao ý thức chấp hành kỷ luật quân đội, quy định của đơn vị và nền nếp xây dựng chính quy, rèn luyện kỷ luật.
- Phối hợp với cấp ủy, chính quyền địa phương tuyên truyền cho những hộ kinh doanh hàng hóa gần đơn vị chấp hành nghiêm quy định, không buôn bán hàng hóa quá thời gian quy định của địa phương, thời gian làm việc, sinh hoạt, học tập, công tác của quân nhân dự bị, bảo đảm an ninh chính trị, trật tự an toàn xã hội trên địa bàn.
- Quản lý chặt chẽ tình hình tư tưởng, kỷ luật quân nhân dự bị trong thời gian huấn luyện, nhất là hoạt động phân tán ngoài đơn vị có biện pháp nhắc nhở, khắc phục kịp thời.
- Thường xuyên quán triệt quy định, quy chế trong thời gian huấn luyện cho quân nhân dự bị nâng cao ý thức chấp hành nghiêm kỷ luật quân đội, quy định đơn vị hoàn thành tốt nhiệm vụ được giao.
- Quan tâm đời sống vật chất, tinh thần cho quân nhân dự vị, nâng cao chất lượng huấn luyện, rèn luyện, công tác.
- Tổng hợp tình hình xử lý báo cáo cấp trên theo phân cấp.
 Tình huống 94. Bố của một quân nhân dự bị ốm nặng đột xuất, khi thời gian huấn luyện còn hai tuần; chỉ huy đơn vị động viên đồng chí ở lại, nhưng vẫn có tư tưởng chưa yên tâm công tác
Gợi ý biện pháp xử lý
- Hội ý chỉ huy đại đội đánh giá tình hình, tư tưởng, nhu cầu nguyện vọng của quân nhân dự bị, thống nhất biện pháp giải quyết; báo cáo cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ đồng chí quân nhân dự bị giáo dục, động viên, chấp hành nghiêm các quy định của đơn vị trong thời gian huấn luyện; thông báo cho người thân, gia đình tạo mọi điều kiện thuận lợi và thời gian để hoàn thành nhiệm vụ theo kế hoạch.
- Phối hợp với cấp ủy, chính quyền và đoàn thể địa phương tổ chức thăm hỏi, động viên bố của chiến sĩ quân nhân dự bị ốm đau, yên tâm điều trị hồi phục sức khỏe, tạo điều kiện cho con hoàn thành nhiệm vụ.
- Căn cứ vào thực trạng sức khỏe bố của chiến sĩ quân nhân dự bị để nghiên cứu giải quyết đi tranh thủ cho phù hợp; trường hợp bệnh nặng khó qua khỏi thì báo cáo cấp trên tạo điều kiện để quân nhân dự bị về thăm bố.
- Thường xuyên quan tâm động viên, giúp đỡ, chia sẻ, tạo điều kiện thuận lợi cho quân nhân dự bị yên tâm hoàn thành nhiệm vụ
- Tổng hợp tình hình báo cáo cấp trên xin ý kiến chỉ đạo tiếp theo.
Tình huống 95. Có một số thanh niên địa phương thường xuyên gặp gỡ chiến sĩ quân nhân dự bị của đơn vị đang huấn luyện đã tuyên truyền, kích động gây mâu thuẫn trong nội bộ và mất đoàn kết quân dân
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình an nính chính trị, trật tự an toàn xã hội trên địa bàn; tư tưởng, kỷ luật của quân nhân dự bị trong thời gian huấn luyện của đơn vị, thống nhất biện pháp giải quyết.
- Gặp gỡ chiến sĩ quân nhân dự bị giáo dục, quán triệt nâng cao ý thức chấp hành nghiêm pháp luật Nhà nước, kỷ luật quân đội; cảnh giác với âm mưu kích động, xuyên tạc, gây chia rẽ mối quan hệ đoàn kết nội bộ, đoàn kết quân dân của một số thanh niên địa phương.
- Phối hợp với cấp ủy, chính quyền, đoàn thể, nhân dân địa phương và gia đình quân nhân dự bị giáo dục, tuyên truyền cho con em nâng cao ý thức chấp hành nghiêm quy định cảu quân đội, pháp luật Nhà nước, bảo đảm an ninh chính trị, trật tự an toàn xã hội trên địa bàn.
- Soát xét an ninh chính trị nội bộ, phân loại tư tưởng chính trị quân nhân dự bị, xây dựng đơn vị đoàn kết tin tưởng, giúp đỡ lẫn nhau, chấp hành nghiêm kỷ luật quân đội, pháp luật Nhà nước, hoàn thành tốt nhiệm vụ.
- Thường xuyên duy trì nghiêm chế dộ nền nếp xây dựng đơn vị chính quy, quản lý chặt chẽ quân số và các mối quan hệ của quân nhân dự bị trong thời gian huấn luyện, phòng ngừa kẻ xấu lôi kéo, móc nối mất an ninh chính trị, trật tự an toàn xã hội trên địa bàn.
- Thường xuyên nắm bắt tình hình tư tưởng, kỷ luật quân nhân dự bị, báo cáo cấp trên đứng quy định.
Tình huống 96. Một đồng chí sĩ quan dự bị trong thời gian huấn luyện lợi dụng danh nghĩa cán bộ trong quân đội tham gia cùng một số thanh niên quảng cáo, giao dịch, bán hang kém chất lượng trên mạng xã hội ảnh hưởng uy tín đơn vị.
Gợi ý biện pháp xử lý 
- Nắm chắc tình hình sĩ quan dự bị của đơn vị lợi dụng danh nghĩa cán bộ tham gia quảng cáo và bán hàng kém chất lượng trên mạng xã hội; đề xuất với lãnh đạo, chỉ huy biện pháp ngăn chặn, khắc phục.
- Gặp gỡ đồng chí sĩ quan dự bị, giáo dục nâng cao ý thức chấp hành nghiêm pháp luật Nhà nước, kỷ luật quân đội, rèn luyện  phẩm chất, đạo đức, tư cách nhười cán bộ, đảng viên, khắc phục hành vi lợi dụng danh nghĩa tham gia quảng cáo, bán hàng kém chất lượng ảnh hưởng đến uy tín đơn vị, quân đội. Căn cứ tính chất, mức độ vi phạm, triển khai đồng chí sĩ quan dự bị viết bản tường trình, bản tự kiểm điểm sinh hoạt xem xét lỗi phạm sĩ quan dự bị chấp hành nghiêm quy định pháp luật trong thời gian huấn luyện.
- Tổ chức sinh hoạt thông báo cho lực lượng quân nhân dự bị trong đơn vị và nhân dân địa phương biết hoạt động quảng cáo hàng kém chất lượng của sĩ quan dự bị, nâng cao ý thức cảnh giác với biểu hiện vi phạm kỷ luật, pháp luật, mất uy tín, danh dự bản thân, đơn vị.
- Quản lý chặt chẽ tình hình tư tưởng, kỷ luật và các mối quan hệ xã hội của quân nhân dự bị trong thời gian huấn luyện của đơn vị để có biện pháp ngăn chặn kịp thời.
- Phối hợp chặt chẽ với cấp ủy, chính quyền, nhân dân địa phương tuyên truyền, giáo dục cho nhân dân chấp hành nghiêm quy định của pháp luật trong hoạt động kinh doanh, giao dịch mua bán hang háo trên mạng xã hội, bảo đúng pháp luật, tăng cường an ninh chính trị, trật tự an toàn xã hội.
- Xử lý nghiêm kỷ luật đối với những trường hợp lợi dụng uy tín, danh nghĩa quân nhân dự bị, tham gia hoạt động, việc làm sai trái, ảnh hưởng uy tín quân đội, pháp luật Nhà nước.
- Báo cáo cấp trên theo quy định
Tình huống 97. Một đồng chí quan dự bị có lệnh tham gia huấn luyện bổ túc cấp đại đội, nhưng lấy lý do cừa mới cưới vộ, không tham gia.
Gợi ý biện pháp xử lý
- Hội ý chỉ huy đơn vị nhận định tình hình tư tưởng, kỷ luật của sĩ quan dự bị trong đơn vị, thống nhất biện pháp xử lý. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Phân công cán bộ gặp gỡ, động viên đồng chí sĩ quan dự bị hiểu rõ chức trách, nhiệm vụ được giao, giải quyết hài hòa công việc chung, riêng, gia đình, đơn vị, khắc phục khó khăn chấp hành nghiêm kế hoạch huấn luyện.
- Phối hợp cấp ủy, chính quyền địa phương và gia đinhg, gặp gỡ trao đổi, động viên đồng chí sĩ quan dự bị nhận rõ vinh dự, trách nhiệm của người cán bộ, đảng viên, nhiệm vụ được cấp ủy, chính quyền giao, nâng cao ý thức, trách nhiệm thực hiện tốt nhiệm vụ huấn luyện đúng quy định.
- Thường xuyên quán triệt quy chế, quy định nắm vững thành phần, thời gian, đị điểm, yêu cầu, nhiệm vụ huấn luyện của đơn vị, làm cho sĩ quan dự bị chủ động tham gia đầy đủ, nghiêm túc.
- Thường xuyên quán triệt quy chế, quy định nắm vững thành phần, thời gian, địa điểm, yêu cầu, nhiệm vụ huấn luyện của đơn vị,làm cho sĩ quan dự bị chủ động tham gia đầy đủ, nghiêm túc.
- Quan tâm bảo đảm tiêu chuẩn, chế độ chính sách đúng quy định của Nhà nước, phù hợp điều kiện của đơn vị và địa phương để sĩ quan dự bị tham gia đầy đủ, nghiêm túc. 
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 98. Một đồng chí quân nhân dự bị nhiễm viêm gan B nhưng vẫn đăng ký tham gia khóa huấn luyện, vì muốn vào quân đội để được điều trị bệnh, gây tâm lý lo lawngd cho cán bộ, chiến sĩ trong đơn vị.
Gợi ý biện pháp xử lý
- Phối hợp với các cơ quan có liên quan xác định tình hình sức khỏe của đồng chí quân nhân dự bị, nguyên nhân, đề xuất cấp ủy, chỉ huy biện pháp giải quyết.
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật, sức khỏe, nhất là những biểu hiện bất thường của quân nhân dự bị, thống nhất biện pháp giải quyết. Báo cáo lên cấp trên xin ý kiến chỉ đạo.
- Gặp gỡ quân nhân dự bị và gia đình tuyên truyền, giải thích, nắm vững tiêu chuẩn sức khỏe, phẩm chất chính trị, năng lực công tác đối với đói tượng tham gia huấn luyện quân sự, nâng cao ý thức trách nhiệm giáo dục, động viên, lựa chọn con em tham gia đúng tiêu chuẩn, thành phần, quy định.
- Phối hợp với cấp ủy, chính quyền và cơ quan quân sự địa phương tổ chức rút kinh nghiệm trong thực hiện nhiệm vụ phúc tra quân nhân dự bị về phẩm chất chính trị, sức khỏe, năng lực công tác trước khi triệu tập huấn luyện.
- Quản lý chặt chẽ chất lượng, số lượng quân nhân dự bị, không để sơ suất, sót lọt những đồng chí thiếu tiêu chuẩn vào huấn luyện trong đơn vị, nâng cao chất lượng huấn luyện của đơn vị.
- Thường xuyên phổ biến tuyên truyền quy chế, tiêu chuẩn chính trị, trình độ năng lực công tác của quân nhân dự bị khi tham gia  huấn luyện để mọi cơ quan, tổ chức, cá nhân chấp hành nghiêm túc.
- Tổng hợp tình hình báo cáo cấp trên.
  Tình huống 99. Một đồng chí quân nhân dự bị trong thời gian huấn luyện rủ nhau đánh bài ăn tiền, vi phạm quy định quân đội, ảnh hưởng tư tưởng trong đơn vị
Gợi ý biện pháp xử lý
- Lập biên bản sự việc, mức độ vi phạm của quân nhân dự bị và nắm tình hình duy trì chế độ nền nếp xây dựng chính quy của đơn vị; đề xuất biện pháp giải quyết cho lãnh đạo, chỉ huy đơn vị.
- Hội ý ban chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật quân nhân dự bị, nhất là thực hiện nền nấp, chế độ xây dựng chính quy, thống nhất biên pháp xử lý.
- Gặp gỡ quân nhân dự bị tham gia đánh bài ăn tiền trong thời gian huấn luyện, giáo dục nhận rõ khuyết điểm, vi phạm kỷ luật quân đội, quy định đơn vị, có biện pháp khắc phục sửa chữa. Căn cứ tính chất, mức độ vi phạm triển khai cho quân nhân dự bị viết bản tường trình, bản tự kiểm điểm, sinh hoạt đơn vị đề nghị hình thức kỷ luật.
- Tổ chức sinh hoạt rút kinh nghiệm trong toàn đơn vị, quán triệt các văn bản chỉ thị, quy định của quân đội, đơn vị, xây dựng cho quân nhân dự bị có ý thức chấp hành kỷ luật quân đội, pháp luật của Nhà nước.
- Duy trì chặt chẽ chế độ nền nếp xây dựng đơn vị chính quy, gắn với giáo dục động viên quân nhân dự bị tự giác chấp hành nghiêm kỷ luật quân đội, quy định của đơn vị, hoàn thành chức trách nhiệm vụ.
- Thường xuyên theo dõi, quản lý chặt chẽ quân nhân dự bị trong mọi hoạt động của đơn vị, nhất là thời gian ngoài giờ hành chính, biểu hiện bất thường, kịp thời phát hiện xử lý đúng quy chế, quy định.
- Phối hợp chặt chẽ với các tổ chức đoàn thể ở địa phương, duy trì hoạt động văn hóa văn nghệ, thể dục thể thao, xây dựng đơn vị có môi trường văn hóa trong sạch lành mạnh, làm cho quân nhân dự bị hoàn thành tốt nhiệm vụ.
Tình huống 100. Một sĩ quan dự bị được ban chỉ huy quân sự huyện cử tham gia huấn luyện, tham gia được một tuần đã lấy lý do có việc gia đình, xin về nhà không tham gia huấn luyện.
Gợi ý biện pháp xử lý
- Xác minh tình hình, tư tưởng kỷ luật, tâm tư, nguyện vọng và điều kiện hoàn cảnh gia đình của sĩ quan dự bị, đề xuất biện pháp cho lãnh đạo, chỉ huy đơn vị giải quyết.
- Hội ý ban chỉ huy quân sự địa phương đánh giá tình hình tư tưởng, kỷ luật, hoàn cảnh gia đình của sĩ quan dự bị, thống nhất biện pháp xử lý. Báo cáo cấp trên xin ý kiến chỉ đọa.
- Gặp gỡ sĩ quan dự bị trao đổi, động viên nhận nhiệm vụ huấn luyện trong thời gian không dài, đòi hỏi tập trung số cao, do đó nâng cao ý thức trách nhiệm, khắc phục khó khăn của gia đình, tham gia đầy đủ, nghiêm túc, bảo đảm nội dung, chương trình huấn luyện.
- Phối hợp ban chỉ huy quân sự địa phương, gia đình động viên đồng chí sĩ quan dự bị giải quyết hài hòa công việc chung, riêng giữa gia đình với nhiệm vụ huấn luyện của đơn vị, hoàn thành tốt nhiệm cụ được giáo.
- Quan tâm bảo đảm tiêu chuẩn, chế độ chính sách theo quy định của Nhà nước, quân đội cho sĩ quan dự bị yên tâm hoàn thành nhiệm vụ.
- Nắm, quản lý tình hình tư tưởng, kỷ luật và các mối quan hệ của sĩ quan dự bị trong thời gian huấn luyện, kịp thời động viên, giải quyết.
- Tổng hợp tình hình náo cáo cấp trên theo quy định.

TỔNG CỤC CHÍNH TRỊ
CỤC TUYÊN HUẤN
DẤU HIỆU NHẬN BIẾT HÀNH VI VI PHẠM KỶ LUẬT, MẤT AN TOÀN VÀ GỢI Ý BIỆN PHÁP XỬ LÝ CỦA CÁN BỘ CƠ SỞ ĐỐI VỚI NHỮNG TÌNH HUỐNG TƯ TƯỞNG CÓ THỂ NẢY SINH 

(Tài liệu tham khảo TẬP 3)

 

Lưu hành nội bộ


NHÀ XUẤT BẢN QUÂN ĐỘI NHÂN DÂN
HÀ NỘI - 2022

Ban biên soạn:
Thiếu tướng Nguyễn Văn Đức (chủ biên)
Đại tá Tạ Văn Thiện
Đại tá Nguyễn Hữu Tuyển
Đại tá TS Nguyễn Văn Luyện
Đại tá Bùi Lê Ninh
Đại tá TS Nguyễn Xuân Sinh
Thượng tá TS Nguyễn Văn Thi
Thượng tá Phạm Văn Quân









LỜI GIỚI THIỆU
Năm 2015 và 2018, Cục Tuyên huấn đã biên tập, phát hành tài liệu“100 tình huống tư tưởng có thể nảy sinh ở đơn vị và gợi ý biện pháp xử lý của cán bộ cơ sở”, đã được các cơ quan, đơn vị đón nhận và vận dụng với nhiều hình thức, biện pháp phong phú, sáng tạo vào xử lý, giải quyết tư tưởng quân nhân, ngăn ngừa vi phạm kỷ luật quân đội, pháp luật Nhà nước, góp phần xây dựng tổ chức đảng trong sạch vững mạnh, đơn vị vững mạnh toàn diện, hoàn thành tốt nhiệm vụ được giao. Tuy nhiên, vẫn còn một số cấp uỷ, chỉ huy và cán bộ cấp phân đội xử lý và giải quyết các vấn đề nảy sinh về tư tưởng quân nhân chưa kịp thời, dứt điểm, còn chủ quan, dập khuôn máy móc, thiếu tính khoa học và thuyết phục, có những vấn đề tư tưởng nảy sinh giải quyết không tốt dẫn đến từ vi phạm nhỏ thành vi phạm lớn, từ vấn đề đơn giản thành vấn đề phức tạp, ảnh hướng trực tiếp đến tư tưởng cán bộ, chiến sĩ và nhân dân; cá biệt có những vụ việc đã bị các phần tử xấu lợi dụng, xuyên tạc làm ảnh hưởng tới bản chất, truyền thống Quân đội và hình ảnh “Bộ đội Cụ Hồ”. Đồng thời, trong thực tiễn thực hiện nhiệm vụ phòng, chống thiên tai, dịch bệnh, huấn luyện, học tập, sinh hoạt và công tác ở đơn vị cơ sở đã phát sinh những vấn đề mới liên quan đến công tác quản lý tư tưởng quân nhân. 
Để khắc phục những tồn tại nêu trên, đồng thời kịp thời cập nhật, bổ sung những tình huống mới phát sinh, nhằm giúp cấp ủy, chỉ huy và đội ngũ cán bộ đơn vị cơ sở có thêm kiến thức, kỹ năng xử lý tình huống tư tưởng, kỷ luật, Cục Tuyên huấn phối hợp với các cơ quan, đơn vị tiếp tục biên soạn tài liệu “Dấu hiệu nhận biết hành vi vi phạm kỷ luật, mất an toàn và gợi ý biện pháp xử lý của cán bộ cơ sở đối với những tình huống tư tưởng có thể nảy sinh (tập 3)”. 
Nội dung tài liệu được kết cấu thành hai phần: 
Phần thứ nhất: Dấu hiệu nhận biết đối các nhóm hành vi vi phạm kỷ luật, mất an toàn (30 nhóm hành vi). 
Phần thứ hai:  Gợi ý biện pháp xử lý của cán bộ cơ sở đối với những tình huống tư tưởng có thể nảy sinh. Gồm 3 nhóm:
- Nhóm tình huống tư tưởng nảy sinh trong phòng, chống thiên tai, dịch bệnh (50 tình huống).
- Nhóm tình huống tư tưởng nảy sinh trong huấn luyện, sẵn sàng chiến đấu; xây dựng chính quy, rèn luyện kỷ luật (10 tình huống). 
- Nhóm tình huống tư tưởng nảy sinh trong giải quyết mối quan hệ đồng chí, đồng đội, gia đình, bạn bè, nam nữ, quan hệ quân dân (10 tình huống).
Đây là tập tài liệu tham khảo có tính thực tiễn, dùng để cán bộ cơ sở toàn quân nghiên cứu, vận dụng trong công tác quản lý tư tưởng quân nhân ở đơn vị cơ sở. Quá trình nghiên cứu, vận dụng, xử lý các tình huống cần thực hiện đúng nguyên tắc, quy trình, sáng tạo, linh hoạt, tránh dập khuôn máy móc; phát huy vai trò, trách nhiệm của người chỉ huy các cấp (tiểu đội, trung đội, đại đội, tiểu đoàn); của chính trị viên (chính trị viên phó) đại đội, tiểu đoàn và vai trò, trách nhiệm chỉ đạo, hướng dẫn của cấp ủy, chính ủy, chính trị viên (bí thư) và cơ quan cấp trên để đạt hiệu quả cao. 
Quá trình thực hiện rất mong nhận được ý kiến góp ý để chỉnh lý, bổ sung hoàn thiện tài liệu.

Xin trân trọng giới thiệu cùng các đồng chí!
  




























Phần thứ nhất
DẤU HIỆU NHẬN BIẾT VÀ BIỆN PHÁP PHÒNG NGỪA 
CÁC NHÓM HÀNH VI VI PHẠM KỶ LUẬT, MẤT AN TOÀN
1. Tự tử, tự sát
a) Dấu hiệu nhận biết
- Thông qua nhật ký, vở ghi chép, mạng xã hội (Zalo, Facebook…) nắm được quân nhân thường xuyên suy nghĩ ám ảnh một vấn đề nào đó có tính chất nghiêm trọng. Cảm thấy không còn một chút hy vọng nào, thấy cuộc sống trở nên vô nghĩa, hoặc không thể kiểm soát chúng, thường hay mơ hồ, hoặc không thể tập trung được.
- Có biểu hiện trầm cảm, buồn chán, giảm hứng thú với các thói quen cũ, mất ngủ kéo dài.
- Tâm trạng đột ngột thay đổi, thường hay bực bội, giận dữ cực độ. Thường xuyên căng thẳng, lo âu cùng cực, có cảm giác tội lỗi, buồn chán cuộc đời, hay xấu hổ, hoặc cảm thấy bản thân trở thành gánh nặng cho người khác. Thường hay cảm thấy cô đơn, biệt lập, thậm chí ngay cả khi đang ở cạnh nhiều người.
- Bị bệnh hiểm nghèo nhưng giấu bệnh, bi quan…
- Hay đề cập nhiều đến sự chết chóc biểu hiện qua các câu nói “Tôi lẽ ra không nên sinh ra trên đời này, tôi rất xin lỗi những người tôi làm sai, tôi chỉ mong một ngày tôi sẽ không ở trên đời này”, “Sống tới ngày bắn đạn thật”, “Cuộc đời này không đáng sống”, “Nó không còn quan trọng nữa rồi”, “Họ sẽ không thể nào làm tổn thương tôi được nữa”, “Họ sẽ nhớ về tôi khi tôi ra đi,” hoặc “Bạn sẽ thương tiếc khi tôi ra đi”, “Bạn/gia đình/bạn bè/bạn gái tôi sẽ sống tốt hơn nếu không có tôi”….
- Đột ngột có những hành vi bất thường: tắm rửa sạch sẽ, mặc quần áo đẹp dù không đi đâu, tự nhiên trò chuyện vui vẻ sau thời gian dài buồn bã. Cho đi tài sản có giá trị, nói lời tạm biệt với những người thân yêu, tìm kiếm hoặc tích trữ một dụng cụ có thể gây hại cho bản thân (thuốc ngủ, thuốc bảo vệ thực vật, dao, kéo, dây thừng, vũ khí…).
b) Biện pháp phòng ngừa
- Tăng cường giáo dục nâng cao nhận thức chính trị tư tưởng; coi trọng phát huy dân chủ gắn với hoàn thiện các quy chế, cơ chế để nắm, quản lý tình hình đơn vị, chất lượng các tổ chức, diễn biến tư tưởng của quân nhân; kết hợp chặt chẽ giáo dục nhận thức với các phong trào hành động để quản lý quân nhân.
- Chủ động, linh hoạt nắm thông tin từ vở học tập, sổ tay chiến sĩ, nhật ký, thiết bị nghe, nhìn cá nhân.
- Phân công cán bộ, đảng viên kèm cặp, giúp đỡ bộ đội. Phát huy vai trò của Chiến sĩ bảo vệ, dân vận, “Tổ 3 người”, “Tổ tư vấn tâm lý, pháp lý”, “Hòm thư góp ý”; khảo sát (điều tra xã hội học) để kịp thời nắm tình hình, tham mưu định hướng tư tưởng, giải quyết những vấn đề tư tưởng nảy sinh.
- Nghiên cứu, tìm hiểu, xác định nguyên nhân khách quan, chủ quan dẫn đến biểu hiện tư tưởng bất thường. Tư vấn về những vấn đề quân nhân gặp phải khó khăn, giải quyết nhanh chóng làm giảm căng thẳng, giải tỏa tâm lý, không để quân nhân bế tắc kéo dài, không lối thoát.
- Thường xuyên quan sát và triệt tiêu những nguy cơ có thể dẫn đến tự tử, tự sát. Tăng cường các biện pháp quản lý không để quân nhân sử dụng rượu, bia, chất kích thích, không để quân nhân có biểu hiện sang chấn tâm lý kéo dài. Tăng cường kiểm tra, quản lý chặt chẽ quân tư trang, vũ khí, cuốc, xẻng, dao, dây các loại, thuốc trừ sâu, thuốc diệt côn trùng, thuốc diệt cỏ…không để cán bộ, chiến sĩ lợi dụng những vật dụng đó nhằm thực hiện hành vi tiêu cực.
- Quân y đơn vị theo dõi chặt chẽ trường hợp quân nhân sau khi được điều trị các bệnh lý có rối loạn tâm thần, rối loạn cảm xúc, trầm cảm.
- Liên hệ địa phương, gia đình, bạn bè của quân nhân để nắm chắc mối quan hệ xã hội của quân nhân và phối hợp giải quyết những khó khăn, vướng mắc mà một mình quân nhân không giải quyết được.
- Duy trì thực chất nền nếp các khâu, các bước công tác quản lý tư tưởng quân nhân: Nắm, dự báo, quản lý, định hướng, giải quyết và đấu tranh tư tưởng;
- Tổ chức các hoạt động phong phú, đa dạng, phù hợp, lôi cuốn cán bộ, chiến sĩ tham gia vào các hoạt động của đơn vị.
- Tổ chức cho quân nhân (có ý định tự tử, tự sát) xem những phim, chương trình có những nhân vật vượt lên chính mình, vượt lên số phận để từng bước định hướng tư tưởng quân nhân.
- Thường xuyên đánh giá mức độ chuyển biến, dự báo xu hướng diễn biến tâm lý, tư tưởng của cán bộ, chiến sĩ để có biện pháp tác động kịp thời.
- Tổng hợp tình hình báo cáo cấp trên.
2. Cá độ bóng đá, bài bạc, lô đề
a) Dấu hiệu nhận biết:
- Có thói quen đánh bài, ham mê xem các nội dung liên quan đến cá cược, các trò chơi ăn tiền trên các trang mạng...
- Ham mê, theo dõi, bàn tán thắng thua các trận đấu của các giải bóng đá, bàn tán về khả năng thắng, thua những trận bóng đá sắp tới, kết quả xổ số, luận giải khả năng trúng vào các con số...
- Sau những trận bóng đá hoặc đánh đề tinh thần phấn chấn, vui vẻ khác thường, hào phóng, chi tiêu thoải mái hoặc buồn, ủ rũ, lo sợ.
- Có tính hiếu thắng, máu ăn thua, thích hưởng thụ, thích làm giàu nhanh mà không tốn công sức, đánh cược vào vận “đỏ đen”.
- Chất lượng, hiệu quả công việc giảm sút rõ rệt, ít quan tâm đến gia đình, bạn bè, đồng đội.
- Thường hay thu mình và lên mạng, ít giao tiếp, ít am hiểu những vấn đề được xã hội quan tâm, không quan tâm đến tình hình đơn vị.
- Tìm đủ cách vay mượn tiền, hay cầm cố đồ đạc, sử dụng các giấy tờ cá nhân thế chấp để vay tiền (thẻ đảng, giấy chứng minh thư sĩ quan, bằng tốt nghiệp…), nợ nần ngày càng nhiều không có khả năng chi trả.
b) Biện pháp phòng ngừa:
- Giáo dục cho quân nhân nhất là ý thức chấp hành Pháp luật Nhà nước, quy định của pháp luật hình sự về hành vi cá độ bóng đá, bài bạc, kỷ luật Quân đội, tác hại của việc tham gia cá độ bóng đá, đánh bạc, lô đề; những hình thức xử lý nghiêm minh của pháp luật khi tham gia cá độ, đánh bạc.
- Giáo dục, động viên, xây dựng cho cán bộ, chiến sĩ lối sống trong sạch, lành mạnh, trách nhiệm của bản thân đối với gia đình.
- Tăng cường các biện pháp nắm, quản lý của cán bộ các cấp, nhất là mối quan hệ xã hội của quân nhân.
- Kết hợp chặt chẽ công tác giáo dục, tuyên truyền giải thích, thuyết phục với việc duy trì nghiêm kỷ luật của Quân đội, quy định của đơn vị. Quản lý chặt chẽ quân nhân.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Định kỳ hoặc đột xuất kiểm tra thẻ đảng viên, chứng minh sĩ quan, QNCN, bằng tốt nghiệp…
- Tìm hiểu, nắm rõ nguồn tài sản có giá trị, việc chi tiêu quá thu nhập của quân nhân.
3. Vay mượn nợ không có khả năng chi trả
a) Dấu hiệu nhận biết:
- Muốn làm giàu nhanh chóng hoặc thích hưởng thụ, lười lao động, học tập, công tác.
- Đam mê cờ bạc, rượu chè bê tha, sống buông thả, xa hoa, lãng phí.
- Làm ăn thua lỗ, gia đình có người thân bệnh nặng.
- Suy tư, buồn bã, bi quan, chán nản, trầm cảm, thường xuyên hoang mang, lo sợ.
- Hay vay mượn tiền anh em trong đơn vị, bán, cầm cố tài sản có giá trị (xe, máy tính, điện thoại, đồ đạc trong gia đình…), hoặc cầm cố, thế chấp nhà cửa, đất đai.
- Giảm khả năng tập trung, chất lượng, hiệu quả công việc giảm sút rõ rệt, ít quan tâm đến gia đình, bạn bè, đồng đội.
- Ám ảnh và khó ngủ, né tránh các mối quan hệ. 
b) Biện pháp phòng ngừa:	
- Giáo dục pháp luật cho quân nhân nhất là ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, nguyên tắc chi tiêu hợp lý, phù hợp với khả năng tài chính của gia đình, những tác hại của việc vay nợ nặng lãi, hệ lụy khi không có khả năng chi trả.
- Tăng cường các biện pháp nắm, quản lý của cán bộ các cấp, nhất là mối quan hệ xã hội, việc chi tiêu của quân nhân.
- Kết hợp công tác giáo dục, tuyên truyền giải thích, thuyết phục với duy trì chặt chẽ, nghiêm túc kỷ luật của Quân đội, đơn vị.
- Làm tốt công tác hậu phương quân đội, thăm hỏi gia đình quân nhân, kết hợp gia đình nắm tình hình quân nhân.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
4. Mất đoàn kết giữa chiến sĩ cũ và chiến sĩ mới
a) Dấu hiệu nhận biết:
- Một số chiến sĩ nhập ngũ trước tỏ thái độ “thiếu thân thiện” với chiến sĩ mới hoặc ngược lại.
- Chiến sĩ cũ luôn thể hiện mình là đàn anh, tự cho mình cái “quyền” sai vặt những chiến sĩ khác. 
- Có những lời nói đe dọa chiến sĩ mới. 
- Một số chiến sĩ mới có tư tưởng bất an, lo âu, sợ sệt, ức chế.
- Chiến sĩ cũ và chiến sĩ mới không hòa đồng.
- Thời điểm dễ gây mất đoàn kết là mới điều chỉnh biên chế, chiến sĩ cũ chuẩn bị xuất ngũ.
- Trong đơn vị xuất hiện dư luận về mối quan hệ giữa chiến sĩ mới và chiến sĩ cũ.
b) Biện pháp phòng ngừa:
- Tăng cường giáo dục pháp luật cho quân nhân nhất là ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, chế độ, quy định, tinh thần đoàn kết, thương yêu giúp đỡ nhau, truyền thống quý báu của Quân đội ta.
- Phát huy trách nhiệm lãnh đạo, chỉ đạo của chi bộ, cán bộ các cấp, vai trò của các cơ quan và các tổ chức quần chúng trong giáo dục truyền thống.
- Tổ chức và duy trì  hiệu quả hoạt động giờ nghỉ, ngày nghỉ
- Chủ động nắm bắt tình hình để có biện pháp ngăn chặn, dự báo, phát hiện những dấu hiệu và hành vi vi phạm kỷ luật của quân nhân. 
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Phân công công tác phải có cán bộ phụ trách.
- Quan tâm chăm lo chu đáo đời sống vật chất tinh thần cho bộ đội.
- Tổ chức các hoạt động vui chơi, giải trí, huy động được nhiều người tham gia (thi đấu bóng đá, bóng chuyền…).
- Sinh hoạt dân chủ, phát huy tinh thần tương thân, tương trợ của chiến sĩ cũ với chiến sĩ mới.
5. Quân phiệt
a) Dấu hiệu nhận biết:
- Ít nói, khả năng thuyết phục kém, nói năng cộc cằn, cộc tính, thiếu kiên trì, thiếu kiềm chế.
- Tính tình hay nóng nảy, bộc trực, có biểu hiện độc đoán.
- Hay phàn nàn, bức xúc về lỗi vi phạm của quân nhân.
- Tâm sinh lý có biểu hiện ức chế, khó chịu do ảnh hưởng công việc, gia đình và tác động ngoài xã hội.
- Bệnh thành tích.
b) Biện pháp phòng ngừa:
- Giáo dục truyền thống, tinh thần đoàn kết, tình yêu thương đồng chí, đồng đội với khẩu hiệu hành động “Đơn vị là nhà, cán bộ, chiến sĩ là anh em”, xây dựng mối quan hệ đoàn kết cán-binh tốt đẹp.
- Giao nhiệm vụ cho cán bộ rèn luyện đức tính bình tĩnh, kiên nhẫn, đức độ, rộng lượng, xử lý các vụ việc trên cơ sở điều lệ quản lý bộ đội, điều lệnh Quân đội, pháp luật Nhà nước.
- Chỉ ra những hệ lụy cho cán bộ nếu có hành động quân phiệt.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Thường xuyên quan tâm theo dõi, nhất là trong thời điểm có dấu hiệu chuẩn bị xảy ra để ngăn chặn kịp thời.
- Khắc phục bệnh thành tích trong lãnh đạo, chỉ huy.
6. Vắng mặt trái phép
a) Biểu hiện nhận biết:
- Có thông tin người thân trong gia đình, bạn thân, người yêu…của quân nhân chết, bị bệnh nặng, tai nạn; đặc biệt là các trường hợp vợ đòi ly hôn, người yêu đòi chia tay…
- Tâm lý thay đổi khác thường, lo âu, bồn chồn, hay để ý, theo dõi chỉ huy, quan sát những vị trí thuận lợi có thể đi ra ngoài doanh trại.
- Thức khuya hoặc không ngủ trưa quan sát đồng chí, đồng đội tìm cơ hội thuận lợi để đi khỏi doanh trại. 
- Hay tìm lý do để vắng mặt trong sinh hoạt, học tập.
- Tập thể quân nhân, nhóm, bạn bè, đồng chí, đồng đội có những luồng dư luận xoay quanh vấn đề liên quan quân nhân có ý định vắng mặt trái phép.
- Chiến sĩ dân vận, chiến sĩ bảo vệ báo cáo.
 b) Biện pháp phòng ngừa:
- Tăng cường giáo dục pháp luật cho quân nhân nhất là ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, quy định của đơn vị, địa phương.
- Duy trì nghiêm nền nếp chính quy. 
- Chủ động nắm tình hình thực tế, dự báo kịp thời những dấu hiệu và hành vi vi phạm của quân nhân.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
7. Sử dụng trái phép chất ma túy, chất kích thích
a) Dấu hiệu nhận biết:
- Mắt đảo qua đảo lại, đồng tử nở rộng, đi vệ sinh, rửa tay, khát nước liên tục, rất thích nước ngọt, sụt cân và gầy đi rất nhanh, mồ hôi có mùi khai, xuất hiện quầng thâm mắt rõ rệt.
- Cánh tay hoặc chân có thể xuất hiện những vết như kim châm, trong đơn vị có thể có những dụng cụ để sử dụng ma túy (cất giấu những nơi khó phát hiện: khu vực nhà vệ sinh, kho vật chất, balô…). Quân nhân thường hay vào nhà vệ sinh giờ ngủ, nghỉ với thời gian lâu.
- Da nhăn nheo, nhiều mụn trứng cá lở loét trên cơ thể, men răng hỏng, miệng khô và hơi thở có mùi, hay bị chảy máu mũi.
- Cơ thể bị hội chứng “kiến bò dưới da”, ảo giác và sự thay đổi thất thường tâm trạng, thường có suy nghĩ hoang tưởng, nghi ngờ có người đi theo làm hại.
- Lơ là trong thực hiện nhiệm vụ, năng suất công việc giảm, luôn trong trạng thái tỉnh táo, có khi không cần ngủ tới cả tuần, giảm cân nhanh.
- Quân y lưu ý trường hợp quân nhân trẻ tuổi có các biểu hiện bất thường như: mạch nhanh, rối loạn nhịp tim, tăng huyết áp, nhịp thở nhanh.
- Vắng mặt trái phép theo quy luật, chu kỳ.
b) Biện pháp phòng ngừa:
- Tăng cường giáo dục pháp luật cho quân nhân nhất là ý thức chấp hành Luật phòng, chống ma túy, kỷ luật Quân đội, tác hại của việc tàng trữ, sử dụng chất kích thích nhất là các hợp chất ma túy...
- Kịp thời phát hiện sớm những quân nhân biểu hiện như mục a.
- Chủ động nắm bắt tình hình thực tế để có biện pháp ngăn chặn, dự báo kịp thời những dấu hiệu và hành vi vi phạm kỷ luật của quân nhân. 
- Tăng cường kiểm tra quân tư trang nhất là đối với các quân nhân vừa nghỉ phép, tranh thủ, ra ngoài doanh trại trở lại đơn vị. 
- Có biện pháp ngăn chặn đường xâm nhập của chất cấm vào đơn vị.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Tổ chức tốt các hoạt động trong giờ nghỉ, ngày nghỉ.
- Quan tâm chăm lo chu đáo đời sống vật chất tinh thần cho bộ đội.
8. Mất đoàn kết trong cấp ủy, chỉ huy cơ quan, đơn vị
a) Dấu hiệu nhận biết:
- Không thống nhất trong lãnh đạo, chỉ đạo, triển khai thực hiện nhiệm vụ của cơ quan, đơn vị.
- Lôi kéo, tạo bè phái trong cơ quan, đơn vị.
- Hay nói xấu, đổ lỗi cho nhau trước cấp trên và cấp dưới.
b) Biện pháp phòng ngừa:
- Tăng cường giáo dục xây dựng đoàn kết thống nhất trong cơ quan, đơn vị.
- Thực hiện tốt Quy chế dân chủ ở cơ sở; tăng cường đối thoại giữa cán bộ cấp trên với cấp dưới và chiến sỹ; cán bộ chủ trì phải có tinh thần cầu thị, lắng nghe, tiếp thu ý kiến đóng góp của tập thể.
- Công khai, minh bạch các hoạt động của cơ quan, đơn vị, nhất là tài chính, quỹ vốn; công tác cán bộ, chính sách, thi đua - khen thưởng.
- Thực hiện nghiêm nguyên tắc tổ chức sinh hoạt Đảng, nhất là nguyên tắc tập trung dân chủ, tập thể lãnh đạo, cá nhân phụ trách; quy chế làm việc của cấp ủy, chỉ huy, quy chế lãnh đạo các mặt trọng yếu.
- Cấp ủy, chỉ huy cấp trên phải thường xuyên sâu sát cơ quan, đơn vị trực thuộc, phân công cấp ủy viên dự sinh hoạt Đảng, sinh hoạt đối thoại dân chủ,... để kịp thời nắm tình hình, xử trí, không để kéo dài.
9. Gây mất đoàn kết quân dân
a) Dấu hiệu nhận biết:
- Quân nhân có biểu hiện lo lắng, bồn chồn, suy tư, trên người có thể có sây sát hoặc vết thương.
- Dư luận trong đơn vị có những biểu hiện khác thường, bàn tán, suy diễn xung quanh về sự việc, các quân nhân đang nói chuyện bàn tán thấy chỉ huy đơn vị thì lảng tránh.
- Chiến sĩ dân vận, bảo vệ của đơn vị báo cáo hoặc dư luận xung quanh khu vực đơn vị đóng quân có các thông tin liên quan đến vụ việc gây mất đoàn kết.
- Chính quyền và nhân dân địa phương thông báo.
b) Biện pháp phòng ngừa:
- Tăng cường giáo dục cho quân nhân về ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, nhất là 10 lời thề danh dự của quân nhân, 12 điều kỷ luật khi tiếp xúc với nhân dân, các quy định của đơn vị và địa phương.
- Thường xuyên giáo dục chính trị tư tưởng cho cán bộ, chiến sỹ nêu cao tinh thần trách nhiệm, ý thức tổ chức kỷ luật, phong tục tập quán của người dân địa bàn đóng quân và nơi công tác.
- Tích cực, chủ động nắm bắt tình hình để có biện pháp dự báo, ngăn chặn kịp thời những dấu hiệu và hành vi vi phạm kỷ luật của quân nhân.
- Tăng cường các biện pháp nắm, quản lý của cán bộ các cấp, tính chủ động của mỗi tổ chức đối với quản lý quân nhân thuộc quyền thường xuyên, liên tục ở mọi lúc, mọi nơi, chú ý những thời điểm nhạy cảm.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Duy trì nghiêm các chế độ ngày, tuần.
- Tổ chức giao lưu, kết nghĩa với chính quyền, đoàn thể địa phương.
10. Bị bệnh trầm cảm
a) Dấu hiệu nhận biết:
- Quân nhân thường xuyên có trạng thái trầm uất, giảm hứng thú trong tất cả hoặc đa số hoạt động, mất ngủ, chậm chạp hơn bình thường, ngồi trầm tư một mình.
- Suy giảm khí sắc, buồn bã, ủ rũ, ánh mắt đơn điệu, lờ đờ.
- Mất hưng phấn trong công việc và sở thích trước có.
- Mệt mỏi, giảm khả năng tập trung, giảm cân nặng cơ thể hoặc không quyết định được các vấn đề rất đơn giản, hay xa lánh mọi người.
- Trong sổ tay, nhất ký, vở ghi chép, mạng xã hội thường viết hoặc đăng tải nội dung tiêu cực, tâm trạng u buồn, phàn nàn, than trách thân phận, thậm chí đề cập về cái chết.
- Hoạt động trái quy luật về thời gian như: đêm thức ngày ngủ, sinh hoạt ăn nghỉ, làm việc không đúng thời gian quy định.
- Luôn bi quan trong mọi việc, cảm giác vô vọng, luôn tự ti về bản thân, có ý nghĩ tự tử, tự sát hoặc đã từng tự tử, tự sát không thành.
b) Biện pháp phòng ngừa: 
- Nắm chắc tình hình sức khỏe của quân nhân và lịch sử gia đình.
- Định kỳ hoặc đột xuất kiểm tra quân tư trang cá nhân toàn đơn vị (chú ý nhật ký, vở ghi chép, mạng xã hội…).
- Liên hệ địa phương và gia đình, bạn bè, người thân quân nhân, tìm hiểu nguyên nhân.
- Cán bộ gần gũi, giao tiếp thường xuyên, tổ chức các hoạt động về thể chất, thể dục thể thao, ăn uống, ngủ, nghỉ hợp lý, khoa học.
- Phối hợp chặt chẽ với địa phương, trong công tác tuyển chọn và gọi công dân nhập ngũ, tuyệt đối không tuyển chọn các công dân này vào Quân đội.
11. Nghiện chơi game và các trang mạng xã hội
a) Dấu hiệu nhận biết:
- Không điều khiển được bản thân rời khỏi game và mạng xã hội, thời gian chơi game nhiều hơn 03 giờ/ ngày, liên tục trong thời gian 01 tháng trở lên.
- Coi trọng việc chơi game và lên mạng hơn tất cả những công việc khác.
- Hay nói dối hoặc bỏ bê công việc để chơi game và lên mạng xã hội.
- Khi được giao nhiệm vụ hay quên, chất lượng, hiệu quả thực hiện các nhiệm vụ thấp, chậm tiến độ, không quan tâm, thờ ơ với những hoạt động của đơn vị...
- Có suy nghĩ mơ hồ, sống ảo, có biểu hiện giảm cân hoặc suy nhược cơ thể.
- Có xu hướng hành xử theo các mối quan hệ trong trò chơi online và trên mạng xã hội.
- Có dư luận tập thể quân nhân.
b) Biện pháp phòng ngừa:
- Phát huy vai trò lãnh đạo, chỉ đạo của cấp ủy, tổ chức đảng đối với công tác tuyên truyền, giáo dục pháp luật, kỷ luật, đạo đức, lối sống trong đơn vị nhất là kỹ năng sống, tác hại của nghiện chơi game, mạng xã hội.
- Sâu sát nắm chắc tình hình tư tưởng của quân nhân trong đơn vị. Duy trì chặt chẽ chế độ trong ngày, trong tuần của từng quân nhân.
- Tăng cường các biện pháp nắm, quản lý của cán bộ các cấp, tính chủ động của mỗi tổ chức đối với quản lý quân nhân ở mọi lúc, mọi nơi, nhưng cần chú ý những thời điểm nhạy cảm; đề cao vai trò giám sát của tập thể đơn vị.
Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi con người trong học tập, rèn luyện, công tác. 
- Tổ chức tốt hoạt động giờ nghỉ, ngày nghỉ.
- Quan tâm chăm lo chu đáo đời sống vật chất tinh thần cho bộ đội, thực hiện tốt chính sách quân đội và hậu phương quân đội.
12. Vi phạm pháp luật về giao thông đường bộ
a) Dấu hiệu nhận biết:
- Tính tình bốc đồng, thích thể hiện.
- Chuẩn bị tham gia giao thông có tâm trạng bất ổn, biểu hiện vội vã, luống cuống, mất tập trung.
- Nắm luật giao thông đường bộ không vững.
- Hay uống rượu bia, uống rượu bia say khi tham gia giao thông.
- Điều khiển phương tiện giao thông đường bộ thường phóng nhanh, giành đường, vượt ẩu, lạng lách, đánh võng.
- Có tiền sử bệnh tật (liên quan đến rối loạn tiền đình, bản lĩnh yếu, mắt kém, tay chân không vững...).
- Thích độ xe, thay đổi kết cấu, lắp thêm các thiết bị không đúng quy định.
- Phương tiện dùng để tham gia giao thông không đảm bảo các yếu tố kỹ thuật an toàn (phanh không ăn, đèn xe không đủ sáng, còi, xi nhan hỏng…), xe quá cũ hoặc hết hạn kiểm định.
b) Biện pháp phòng ngừa:
- Tăng cường giáo dục pháp luật cho quân nhân nhất là ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, nhất là Luật giao thông đường bộ.
- Phát huy trách nhiệm lãnh đạo, chỉ đạo của chi bộ, vai trò cán bộ các cấp, các tổ chức trong duy trì và giữ nghiêm kỷ luật quân đội, chú ý những thời điểm ngày nghỉ, giờ nghỉ, tiệc tùng....
- Phát huy vai trò trực ban nội vụ, trực nhật; đề cao vai trò giám sát của tập thể đơn vị; phối hợp tốt giữa cơ quan, đơn vị với chính quyền, nhân dân địa phương và gia đình trong việc quản lý, duy trì kỷ luật, xây dựng ý thức tự giác của từng người.
- Dự báo kịp thời những dấu hiệu và hành vi vi phạm kỷ luật của quân nhân.
- Giáo dục quân nhân ý thức tự giác chấp hành Luật giao thông đường bộ. Định kỳ kiểm tra phương tiện tham gia giao thông và điều kiện tham gia giao thông của quân nhân.
13. Mâu thuẫn trong quan hệ yêu đương nam, nữ
a) Dấu hiệu nhận biết:
- Đến những nơi không người khóc một mình, thời gian nói chuyện điện thoại lâu, lời nói cộc cằn, thô tục, nét mặt giận dữ, thù hận, cũng có thể tâm sự thuyết phục, cầu xin, năn nỉ, nét mặt buồn, não nề.
- Viết hồi ký, nhật ký chuyện tình cảm yêu đương, làm thơ tình buồn.
- Người yêu đột ngột không lên thăm, khi có người hỏi đến buồn bã hoặc cáu gắt.
- Buồn chán, căng thẳng tinh thần kéo dài, mất ngủ, mệt mỏi, trầm cảm, không còn động cơ làm việc, chất lượng hoàn thành nhiệm vụ đột nhiên giảm. 
- Bị mất tập trung, thậm chí không làm gì, ngồi thẫn thờ suy nghĩ về những kỷ niệm đã qua.
- Thông qua nhật ký, vở ghi chép, mạng xã hội thấy được quân nhân bộc lộ cảm xúc chán nản và tuyệt vọng, cho rằng không còn lý do nào để sống nếu thiếu tình yêu của người ấy.
b) Biện pháp phòng ngừa:
- Tăng cường giáo dục pháp luật cho quân nhân nhất là ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, nêu cao phẩm chất đạo đức, bản lĩnh chính trị của ngưới quân nhân cách mạng; giáo dục về tình yêu, hôn nhân và gia đình.
- Đề cao vai trò giám sát của tập thể quân nhân; phối hợp với địa phương, nhân dân và gia đình trong việc nắm, quản lý tư tưởng, quản lý quân nhân.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Quan tâm chăm lo chu đáo đời sống vật chất tinh thần cho bộ đội.
- Định kỳ, đột xuất kiểm tra quân tư trang cá nhân.
14. Quan hệ nam nữ bất chính, vi phạm Luật hôn nhân gia đình
a) Dấu hiệu nhận biết:
- Ít quan tâm đến gia đình, hay cáu gắt với vợ con, gia đình có những dấu hiệu rạn nứt, thường xuyên ngủ lại đơn vị kể cả ngày không trực.
- Tần suất sử dụng điện thoại (nghe, gọi, nhắn tin, zalo, facebook) nhiều hơn, giọng nói nhẹ nhàng, lãng mạn, nghe điện thoại thường né tránh đám đông hoặc chỉ huy. Sử dụng điện thoại riêng chỉ để trong đơn vị…
- Có những cuộc điện thoại bí mật, nói chuyện thường dùng từ không rõ nghĩa, lấp lửng.
- Thường xuyên vắng mặt tại nơi làm việc vào thời gian nghỉ hoặc ra ngoài không có lý do chính đáng, hay đi chơi về khuya. Ăn mặc trải chuốt, gọn gàng, xịt nước hoa, dầu thơm.
- Đối với nam, nữ cùng đơn vị có biểu hiện quan tâm đến mọi hoạt động của nhau vượt quá quan hệ giới hạn tình cảm thông thường. Thích được phân công công tác chung hoặc viện lý do để có thể gặp gỡ nhau trong khoảng thời gian nhất định, có thể có phương tiện liên lạc riêng với ký hiệu đặc biệt.
- Có người cùng đơn vị bắt gặp quân nhân nhiều lần đi cùng người khác giới và có dấu hiệu thân mật khác thường.
- Có dư luận hoặc phản ánh từ gia đình quân nhân. 
b) Biện pháp phòng ngừa:
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định của luật hôn nhân, gia đình, quan hệ 01 vợ, 01 chồng; quy định những điều đảng viên không được làm; Nghị quyết Trung ương 4 (khóa XII),…những thông tin liên quan đến việc xử lý cán bộ công chức quan hệ bất chính xảy ra trên địa bàn và cả nước để răn đe, hệ lụy của hôn nhân đổ vỡ.
- Thường xuyên nắm chắc các mối quan hệ xã hội của quân nhân.
- Duy trì nghiêm chế độ ngày, tuần, quản lý quân số và các mối quan hệ của quân nhân.
- Nắm bắt tâm tư, tình cảm, cuộc sống gia đình của quân nhân.
- Gặp gỡ, giáo dục, định hướng tư tưởng, nhận thức và hành động.
15. Yêu đương đồng giới
a) Dấu hiệu nhận biết:
- Dáng đi, giọng nói, cử chỉ, điệu bộ thường hay ẻo lả, nhẹ nhàng, khép nép, yểu điệu.
- Cảm thấy luống cuống, bối rối, hồi hộp khi đối diện với đồng chí điển trai khác, hoặc thường xuyên khen ngợi, thích trò chuyện, bàn luận về vẻ đẹp của nam giới. 
- Đứng trước người cùng giới có ngoại hình và khuôn mặt ưa nhìn, thường hướng ánh mắt và sự chú ý, hay có biểu hiện nhìn trộm, trìu mến. 
- Không có hứng thú với phụ nữ, xem phụ nữ dù là xinh đẹp đến đâu cũng chỉ là bạn.
- Hay chăm chút cho bản thân, hay sử dụng mỹ phẩm và luôn ước muốn mình trở nên đẹp hơn.
- Có lối sống, sinh hoạt cá nhân khác biệt mọi người như: thích tắm một mình, kín đáo.
- Thích (thầm yêu) một đồng chí nào đó trong đơn vị.
- Ít hòa đồng với đồng chí, đồng đội…
b) Biện pháp phòng ngừa: Phối hợp với địa phương trong sàng lọc, tuyển chọn quân nhân nhập ngũ.
16. Thu tiền sai quy định 
a) Dấu hiệu nhận biết
- Nhiều cán bộ, chiến sĩ bộc lộ tâm lý không thoải mái, có thái độ thiếu tôn trọng cấp trên, có những lời nói liên quan tới vấn đề tiền bạc, chi tiêu, thấy chỉ huy thì lảng tránh.
- Chiến sĩ bảo vệ, dân vận báo cáo; dư luận trong đơn vị bàn tán; cán bộ, chiến sĩ hoặc người nhà, người thân của cán bộ, chiến sĩ phản ánh…
- Có sự phân biệt, đối xử trong chỉ huy, quản lý.
b) Biện pháp phòng ngừa
- Cấp có thẩm quyền xây dựng quy chế, quy định về công tác quản lý tài chính, tổ chức quán triệt, triển khai thực hiện và phân công cán bộ kiểm tra chặt chẽ.
- Thường xuyên công khai tài chính.
- Thực hiện tốt Quy chế dân chủ cơ sở; tổ chức có hiệu quả Ngày Chính trị và văn hóa tinh thần, Ngày Pháp luật.
- Phát huy vai trò của Chiến sĩ bảo vệ, dân vận, “Tổ tư vấn tâm lý, pháp lý”, “Hòm thư góp ý”; khảo sát (điều tra xã hội học) để kịp thời nắm tình hình đơn vị.
17. Dựa dẫm vào mối quan hệ và người thân, thiếu rèn luyện phấn đấu
a) Dấu hiệu nhận biết
- Gia đình có điều kiện về kinh tế.
- Ham chơi, lười biếng, thích thể hiện, tính sĩ diện cao.
- Hay tụ tập, chấp hành kỷ luật không nghiêm.
- Khoe khoang có người thân là lãnh đạo làm ở chỗ này, chỗ kia...
b) Biện pháp phòng ngừa
-Tăng cường giáo dục cho quân nhân toàn đơn vị ý thức chấp hành pháp luật Nhà nước, kỷ luật Quân đội, quy định của đơn vị. Xây dựng ý thức tự rèn luyện phẩm chất đạo đức cách mạng của người quân nhân.
- Gặp gỡ quân nhân giáo dục nhận thức đúng, sai, tác hại của việc dựa dẫm ỷ lại, chấp hành kỷ luật không nghiêm.
- Phối hợp với gia đình, địa phương trong việc động viên quân nhân thực hiện chức trách, nhiệm vụ, ý thức chấp hành kỷ luật.
- Quản lý chặt chẽ quân nhân, dự báo những dấu hiệu vi phạm, kịp thời ngăn chặn.
- Duy trì nghiêm chế độ ngày, tuần.
- Báo cáo cấp trên xin ý kiến chỉ đạo.
18. Mất an toàn trong huấn luyện, công tác
- Chưa đảm bảo các biện pháp an toàn trong thực hiện nhiệm vụ.
- Quá trình thực hiện nhiệm vụ, trường hợp chỉ có một quân nhân thực hiện, dễ dẫn đến khó phát hiện các nguy hiểm có thể phát sinh và phòng ngừa như gãy cây, ngã thang, trượt chân, chập điện,….
- Phân công nhiệm vụ chưa xem xét sở trường, khả năng của quân nhân với yêu cầu thực hiện nhiệm vụ.
- Quân nhân thực hiện nhiệm vụ ngoài doanh trại, tại nhà riêng, không có sự theo dõi, giám sát của đơn vị.
b) Biện pháp phòng ngừa
- Tăng cường giáo dục, bồi dưỡng cho quân nhân kỹ năng, kinh nghiệm trong thực hiện nhiệm vụ; cách nhận biết các rủi ro, tình huống nguy hiểm có thể phát sinh khi thực hiện nhiệm vụ.
- Trước khi phân công phải xem xét tính chất, yêu cầu nhiệm vụ; căn cứ khả năng, kinh nghiệm của từng quân nhân để phân công cho phù hợp. 
- Hạn chế phân công quân nhân thực hiện nhiệm vụ độc lập, bố trí ít nhất từ 02 quân nhân trở lên để thực hiện nhiệm vụ, hỗ trợ lẫn nhau. Trường hợp cần thiết, phân công cán bộ hướng dẫn, theo dõi, giám sát lao động.
- Phải có nhân viên chuyên môn hướng dẫn các biện pháp bảo đảm an toàn trước khi lao động, học tập (sửa điện, các bài thể thao, bơi…).
- Trang bị bảo hộ và các biện pháp an toàn cần thiết cho quân nhân như mũ bảo vệ, dây an toàn, ngắt điện, thông báo và ngăn cách tạm thời khu vực lao động…
- Quán triệt quân nhân tuân thủ các quy định an toàn lao động cả khi lao động tại nhà riêng, ngoài doanh trại.
- Giáo dục cho mọi người cách xử trí khi xảy ra mất an toàn như: cháy, nổ, chập điện, đuối nước, ngã từ trên cao, rắn cắn…
19. Bạo lực gia đình (cha, mẹ, vợ, chồng, con)
a) Dấu hiệu nhận biết
- Biểu hiện cục cằn, thô lỗ với vợ con; thường xuyên chửi mắng, dọa nạt, đe dọa hành hung; chuẩn bị sẵn hung khí để ra tay; thường xuyên chửi mắng vợ con mỗi khi có hơi men…
- Nghe phản ánh của người dân, bạn bè, đồng nghiệp và chính vợ, con phản ánh về hành vi ngược đãi, đánh đập làm tổn thương tới sức khỏe, tính mạng của họ; quan sát thấy vợ, con có dấu hiệu bị đánh đập, tâm lý hoảng loạn, luôn lo sợ. 
- Có hành vi hành hạ, ngược đãi, đánh đập hoặc hành vi cố ý khác xâm hại đến sức khoẻ, tính mạng.
- Dùng lời nói, thái độ, hành vi làm tổn thương tới danh dự, nhân phẩm, tâm lý của thành viên gia đình.
- Cô lập, xua đuổi hoặc thường xuyên gây áp lực về tâm lý gây hậu quả nghiêm trọng.
- Ngăn cản việc thực hiện quyền, nghĩa vụ trong quan hệ gia đình giữa ông, bà và cháu; giữa cha, mẹ và con; giữa vợ và chồng; giữa anh, chị, em với nhau.
- Cưỡng ép quan hệ tình dục, cưỡng ép sinh con theo ý muốn, cấm vận về tình dục.
- Cưỡng ép tảo hôn; cưỡng ép kết hôn, ly hôn hoặc cản trở hôn nhân tự nguyện, tiến bộ của con cái.
- Chiếm đoạt, huỷ hoại, đập phá hoặc có hành vi khác cố ý làm hư hỏng tài sản riêng của thành viên khác trong gia đình hoặc tài sản chung của các thành viên gia đình.
- Cưỡng ép thành viên gia đình lao động quá sức, đóng góp tài chính quá khả năng của họ; kiểm soát quá khắt khe thu nhập của thành viên gia đình nhằm tạo ra tình trạng phụ thuộc về tài chính.
- Có hành vi trái pháp luật buộc thành viên gia đình ra khỏi chỗ ở.
b) Biện pháp phòng ngừa:
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định của Luật Phòng, chống bạo lực gia đình, Luật Bình đẳng giới; Luật hôn nhân, gia đình; Bộ luật hình sự; Nghị quyết Trung ương 4 (khóa XII); quy định những điều đảng viên không được làm; quy định nêu gương…, những thông tin liên quan đến việc xử lý bạo lực gia đình để răn đe, cảnh tỉnh.
- Tăng cường giáo dục cho quân nhân về ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, nhất là 10 lời thề danh dự của quân nhân, 12 điều kỷ luật khi tiếp xúc với nhân dân, các quy định của đơn vị và địa phương; giáo dục phát huy truyền thống tốt đẹp của đơn vị, gia đình; vai trò của họ hàng.
- Thường xuyên giáo dục chính trị tư tưởng cho cán bộ, chiến sỹ nêu cao tinh thần trách nhiệm trong xây dựng đơn vị, xây dựng gia đình trên cương vị là người chồng, người cha.
- Thường xuyên giữ mối liên hệ với gia đình quân nhân. Tổ chức các sự kiện gặp mặt gia đình quân nhân vào các dịp: 8/3; ngày gia đình Việt Nam 28/6; ngày 20/10; tất niên của đơn vị…
- Thường xuyên nắm chắc các mối quan hệ xã hội của quân nhân, nhất là quan hệ nam nữ.
- Yêu cầu kê khai đầy đủ các số điện thoại và các tài khoản mạng xã hội đang sử dụng.
- Chỉ huy đơn vị phải gần gũi, sâu sát, nắm bắt tâm tư, tình cảm, cuộc sống gia đình của quân nhân để có biện pháp dự báo, ngăn chặn kịp thời những dấu hiệu và hành vi vi phạm kỷ luật của quân nhân.
- Gặp gỡ, giáo dục, định hướng tư tưởng, nhận thức và hành động đối với các quân nhân có biểu hiện vi phạm.
- Tăng cường các biện pháp nắm, quản lý của cán bộ các cấp, tính chủ động của mỗi tổ chức đối với quản lý quân nhân thuộc quyền thường xuyên, liên tục ở mọi lúc, mọi nơi, chú ý những thời điểm nhạy cảm.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị; chăm lo đời sống vật chất, tinh thần, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Đưa nội dung phòng, chống bạo lực gia đình vào tiêu chí hoạt động thi đua, khen thưởng; phân loại các tổ chức, cá nhân hằng năm.

20. Uống rượu, bia say, bê tha, sai quy định
a) Dấu hiệu nhận biết
- Có lối sống thích ăn chơi, hưởng thụ; ngại huấn luyện, học tập, lao động, công tác, lười thể thao.
- Thường xuyên tụ tập, đàn đúm, tìm mọi lý do để gạ gẫm, lôi kéo, mời chào tổ chức ăn nhậu.
- Bị lệ thuộc vào rượu, luôn có quan điểm tiêu cực “làm việc trên bàn nhậu”.
- Sử dụng rượu, bia và đồ uống có cồn mọi lúc mọi nơi, ngay cả trong giờ làm việc. Thích uống rượu vào buổi sáng.
- Mất kiểm soát về lời nói và hành động khi sử dụng rượu, bia, như: Nói ngọng (nói lè nhè), nói quá to hoặc quá nhỏ, thích tâm sự, nói năng không chuẩn mực, vật lộn với từ ngữ khi nói, nói chậm hơn bình thường hoặc cứ lặp đi lặp lại lời đã nói, nói dai, nói dài; thích điện thoại cho người khác để tâm sự hoặc để thể hiện sự bức xúc về một vấn đề nào đó; thích đi đến những nơi sôi động: karaoke, vũ trường, quán bar; đi đến những nơi không lành mạnh: massa trá hình, karaoke ôm, khách sạn; chóng mặt, mất thăng bằng, đi lại loạng choạng hoặc tự ngã; nôn ọe, đi vệ sinh không kiểm soát; đi xe máy (ô tô) nhanh hơn bình thường, lạng lách; tính khí hung hăng, bốc đồng, khó kiểm soát hành vi và kiềm chế bản thân.
- Quần áo xộc xệch, mặt đỏ, hơi thở có mùi cồn; ánh mắt đờ đẫn, vằn đỏ, mí mắt rũ xuống, khó mở to mắt, ngủ li bì, ngủ ngáy to.
- Thích hút thuốc.
b) Biện pháp phòng ngừa:
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định về Luật phòng, chống tác hại của rượu bia 2019; quy định về những điều đảng viên không được làm (đặc biệt là Điều 18 trong Quy định 37 về hành vi vi phạm sử dụng rượu, bia không đúng quy định hoặc đến mức bê tha và các tệ nạn xã hội khác); quy định nêu gương; Nghị quyết Trung ương 4 (khóa XII),…những thông tin liên quan đến các vụ việc vi phạm kỷ luật liên quan đến sử dụng rượu, bia để răn đe, cảnh tỉnh.
- Tăng cường giáo dục cho quân nhân về ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, nhất là 10 lời thề danh dự của quân nhân, 12 điều kỷ luật khi tiếp xúc với nhân dân, các quy định của đơn vị và địa phương về việc không sử dụng rượu bia trong ngày làm việc, ngày trực, kể cả giờ nghỉ trưa.
- Thường xuyên giáo dục chính trị tư tưởng cho cán bộ, chiến sỹ nêu cao tinh thần trách nhiệm trong xây dựng đơn vị, xây dựng hình ảnh người quân nhân cách mạng. Tổ chức các buổi tọa đàm, sân khấu hóa trong các hội thi, hội diễn văn nghệ quần chúng để nâng cao nhận thức cho quân nhân về việc uống rượu, bia say, bê tha, sai quy định.
- Tăng cường công tác lãnh đạo, chỉ đạo, kiểm tra của cấp ủy, chỉ huy các cấp và cơ quan chức năng.
- Duy trì nghiêm chế độ ngày, tuần, quản lý chặt chẽ quân số mọi lúc, mọi nơi, nhất là trong ngày nghỉ, giờ nghỉ; thường xuyên kiểm tra lễ tiết, tác phong quân nhân.
- Phát huy trách nhiệm nêu gương của cán bộ, đảng viên mọi lúc, mọi nơi, nhất là người đứng đầu. Chỉ huy đơn vị phải gần gũi, sâu sát, nắm bắt tâm tư, tình cảm, cuộc sống gia đình của quân nhân để có biện pháp dự báo, ngăn chặn kịp thời những dấu hiệu và hành vi vi phạm kỷ luật của quân nhân.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị; chăm lo đời sống vật chất, tinh thần, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Khuyến khích nghiên cứu khoa học, phát triển công nghệ và ứng dụng công nghệ cao, công nghệ tiên tiến, công nghệ mới nhằm giảm tác hại của rượu, bia.
- Khen thưởng tập thể, cá nhân có thành tích trong phòng, chống tác hại của rượu, bia.
21. Nghiện ma túy
a) Dấu hiệu nhận biết
- Mắt đỏ ướt long lanh, đồng tử teo, sụp mi mắt; giọng nói khàn khàn, uống nhiều nước lạnh, tâm lý ở trạng thái hưng phấn cao, nói nhiều, cử chỉ và động tác thiếu chính xác. Nếu có tật thì tật thường xuất hiện ở mức cao như vuốt mũi, nhổ râu, nặn mụn, cắn móng tay, lấy ráy tai; ngồi tại chỗ mắt lim dim, gãi chân tay, vò đầu, bứt tóc; hay ngáp vặt, người lừ đừ, mệt mỏi, ngại lao động, bỏ vệ sinh cá nhân …
- Tìm chỗ yên tĩnh để thưởng thức cơn phê; nằm như ngủ nhưng không ngủ, lại hút nhiều thuốc lá, tàn thuốc vung vãi; quan sát nơi nghỉ thường thấy chăn màn thủng do tàn thuốc lá rơi vào, bề bộn đồ đạc, hôi hám.
- Tâm trạng thường lo lắng, bồn chồn, đôi khi nói nhiều, hay nói dối, hay có biểu hiện chống đối, cáu gắt hơn so với trước đây. 
- Giờ giấc sinh hoạt thay đổi thất thường: thức khuya, đêm ngủ ít, dậy muộn, ngày ngủ nhiều…; trong các hoạt động tập thể thường có mặt muộn hoặc vắng mặt (thường vào giờ nhất định). 
- Đi lại có quy luật: Mỗi ngày, cứ đến một giờ nhất định nào đó, dù đang bận việc gì cũng tìm cách, kiếm cớ để đi khỏi nhà, đơn vị.
- Thích ở một mình, ít hoặc ngại tiếp xúc với mọi người (kể cả người thân trong gia đình). Hay tụ tập, quan hệ với người có lối sống sinh hoạt buông thả, lười lao động, học tập, sinh hoạt… hoặc chơi thân với người sử dụng ma túy.
- Nhu cầu tiêu tiền ngày một nhiều, sử dụng tiền không có lý do chính đáng, thường xuyên xin tiền người thân và hay bán đồ đạt cá nhân, gia đình, nợ nần nhiều, ăn cắp vặt, hay lục túi người khác…
- Trong túi quần, áo, cặp, phòng ngủ thường có các thứ giấy bạc, thuốc lá, kẹo cao su, bật lửa ga, bơm kim tiêm, uống thuốc, thuốc phiện, gói nhỏ heroin.
- Có dấu kim trên mu bàn tay, cổ tay, mặt trong khuỷu tay, mặt trong mắt cá chân, ở bẹn, ở cổ…
b) Biện pháp phòng ngừa:
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định có liên quan đến phòng, chống việc sử dụng các chất ma túy, tác hại của việc sử dụng ma túy để răn đe, cảnh tỉnh.
- Tăng cường công tác lãnh đạo, chỉ đạo của cấp ủy, tổ chức đảng, cán bộ chủ trì các cấp trong phòng chống ma túy.
- Quản lý chặt chẽ quân nhân trong đơn vị, đặc biệt là quản lý các mối quan hệ quân nhân, chú ý các trường hợp cá biệt, có tiền sử nghiện thuốc lá và các chất kích thích khác. 
	- Khi phát hiện quân nhân trong đơn vị có biểu hiện sử dụng ma tuý cần báo ngay lãnh đạo, chỉ huy đơn vị và cơ quan chức năng để kịp thời xử lý.
	- Phối hợp với địa phương, đơn vị kết nghĩa xây dựng môi trường văn hóa đơn vị lành mạnh; tổ chức các buổi tọa đàm hoặc sân khấu hóa trong các hội thi, hội diễn văn nghệ quần chúng để nâng cao nhận thức cho quân nhân về tác hại ma túy và tham gia phòng, chống ma túy, góp phần tham gia đấu tranh phòng chống ma túy có hiệu quả.
22. Buôn bán, tàng trữ ma túy, chất cấm
a) Dấu hiệu nhận biết
- Nghiện ma túy; có mối quan hệ xã hội phức tạp cả ở đời thực và trên mạng xã hội.
- Sử dụng nhiều số điện thoại, nhiều tài khoản mạng xã hội một cách bất thường nhưng không báo cáo.
- Có quan hệ với các đối tượng nghiện ma túy hoặc sản xuất, mua bán, tàng trữ ma túy.
- Muốn làm giàu nhanh chóng hoặc thích hưởng thụ, lười lao động, học tập, công tác.
- Có những nguồn thu nhập bất chính, không chứng minh được nguồn gốc tài sản.
- Hay khoe khoang có mối quan hệ với lãnh đạo địa phương, cơ quan công an, các tập đoàn, doanh nghiệp…; có thể chạy việc…; khoe khoang cuộc sống sang chảnh, giàu sang, đi du lịch, đến các nơi sang trọng.
- Thường thuê nhà trọ, khách sạn để liên hệ mua bán ma túy hoặc đến các quán karaoke, quán bar,… để sử dụng ma túy.
- Nhà ở xây kín cổng cao tường, lắp đặt hệ thống an ninh, camera theo dõi từ xa hoặc có bảo vệ, cảnh giác với người lạ. Rất ít đi ra ngoài, ít tiếp xúc với người xung quanh.
- Thường xuyên vận chuyển các chất hóa học về nhà như: cồn công nghiệp, acid, photpho đỏ, thuốc tân dược,…
- Xin nghỉ phép hoặc tranh thủ không rõ lý do chính đáng, sau đó thuê nhà nghỉ, khách sạn trong thời gian dài, thường xuyên có nhiều người đến phòng tìm để giao dịch mua bán ma túy.
- Thường xuyên tụ tập, đi theo từng nhóm từ 3-4 người. Đa số mang theo ba lô, túi xách bên trong chứa laptop, máy nghe nhạc, loa, bình ga...
- Không tập trung chuyên môn và công việc ở đơn vị. Đi lại tự do, tùy tiện nhưng bí mật, thay đổi lịch trình thường xuyên, cảnh giác; thay đổi nhiều loại phương tiện, trang phục, nơi cư trú…
b) Biện pháp phòng ngừa:
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định có liên quan đến phòng, chống việc mua bán, tàng trữ ma túy, chất cấm.
- Tăng cường công tác lãnh đạo, chỉ đạo của cấp ủy, tổ chức đảng, cán bộ chủ trì các cấp trong phòng chống ma túy.
- Quản lý chặt chẽ quân nhân trong đơn vị, đặc biệt là quản lý các mối quan hệ quân nhân, chú ý các trường hợp có dấu hiệu mua bán, tàng trữ ma túy, chất cấm. Khi phát hiện hoặc nhận được thông tin tố cáo quân nhân trong đơn vị có biểu hiện mua bán, tàng trữ ma tuý, chất cấm cần báo ngay lãnh đạo, chỉ huy đơn vị và cơ quan chức năng để kịp thời xử lý.
	- Phối hợp với địa phương, đơn vị kết nghĩa xây dựng môi trường văn hóa đơn vị lành mạnh. Tổ chức các buổi tọa đàm hoặc sân khấu hóa trong các hội thi, hội diễn văn nghệ quần chúng để nâng cao nhận thức cho quân nhân về tác hại ma túy, chất cấm và tham gia phòng, chống ma túy, chất cấm, góp phần tham gia đấu tranh phòng chống ma túy, chất cấm có hiệu quả.
23. Sử dụng, buôn bán vũ khí quân dụng trái phép
a) Dấu hiệu nhận biết
- Muốn làm giàu nhanh chóng hoặc thích hưởng thụ, lười lao động, học tập, công tác.
- “Giàu” lên một cách bất thường và nhanh chóng, không chứng minh được khoản thu nhập tăng đột biến; tiêu tiền nhiều hơn một cách bất thường.
- Hay tìm hiểu về các loại vũ khí một cách bất thường, không sát với chức trách, nhiệm vụ, không phục vụ cho nhiệm vụ huấn luyện, sẵn sàng chiến đấu.
- Có mối quan hệ xã hội phức tạp, nhất là với các đối tượng có tiền án, tiền sự, tội phạm có liên quan đến các nhóm tội về chế tạo, tàng trữ, vận chuyển, sử dụng, mua bán trái phép hoặc chiếm đoạt vũ khí quân dụng, phương tiện kỹ thuật quân sự.
- Sử dụng nhiều số điện thoại, nhiều tài khoản mạng xã hội một cách bất thường nhưng không báo cáo. Điện thoại cho người khác một cách lén lút, bí mật, tâm lý cảnh giác, lo âu, luôn cảnh giác với người lạ.
- Có những mâu thuẫn căng thẳng với các quân nhân trong đơn vị hoặc người ngoài quân đội.
- Thường xuyên quan sát, để ý hành động, thói quen sinh hoạt của chỉ huy đơn vị, cán bộ quản lý vũ khí, trang bị nhằm tìm sơ hở để thực hiện hành vi lấy trộm vũ khí quân dụng.
- Quan tâm hơn tin tức trên tivi, báo chí về các vụ việc vi phạm.
- Đi lại bí ẩn, lịch trình không rõ ràng. 
- Cơ thể bị xây xát, bầm tím hoặc quần áo bị rách, có vết máu khi đi từ bên ngoài về nhà, đơn vị.
- Thích đi săn, đôi khi có chim, thú mang về…
- Nhà riêng lắp đặt hệ thống an ninh, camera theo dõi từ xa một cách bất thường. 
b) Biện pháp phòng ngừa:
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định của Bộ luật hình sự; quy định những điều đảng viên không được làm; Nghị quyết Trung ương 4 (khóa XII),…những thông tin liên quan đến các vụ việc sử dụng, buôn bán trái phép vũ khí quân dụng để răn đe, cảnh tỉnh.
- Tăng cường giáo dục cho quân nhân về ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, nhất là 10 lời thề danh dự của quân nhân, 12 điều kỷ luật khi tiếp xúc với nhân dân, các quy định của đơn vị và địa phương; giáo dụcphát huy truyền thống tốt đẹp của đơn vị, gia đình.
- Thường xuyên giáo dục chính trị tư tưởng cho cán bộ, chiến sỹ nêu cao tinh thần trách nhiệm trong xây dựng đơn vị.
- Chỉ huy đơn vị phải gần gũi, sâu sát, nắm bắt tâm tư, tình cảm, sức khỏe, cuộc sống gia đình của quân nhân. Phân công cán bộ theo phân cấp, đảng viên, chiến sĩ bảo vệ tăng cường các biện pháp nắm, quản lý quân nhân thuộc quyền thường xuyên, liên tục ở mọi lúc, mọi nơi, chú ý những thời điểm nhạy cảm; nắm chắc các mối quan hệ xã hội của quân nhân, nhất là với các thành phần phức tạp, kịp thời phát hiện những biểu hiện khác thường trong sinh hoạt của quân nhân.
- Thường xuyên kiểm tra quân tư trang toàn đơn vị… Tìm hiểu, nắm rõ nguồn tài sản có giá trị, việc chi tiêu quá thu nhập của quân nhân.
- Tăng cường lắp đặt hệ thống camera an ninh ở các khu vực công cộng, nhà ở…
- Quản lý chặt chẽ vũ khí, trang bị nhất là sau khi huấn luyện, diễn tập, bắn đạn thật, hành quân… có biện pháp bảo đảm an toàn đối với kho quân khí, các tủ súng của đơn vị.
- Yêu cầu kê khai đầy đủ các số điện thoại và các tài khoản mạng xã hội đang sử dụng.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị; chăm lo đời sống vật chất, tinh thần, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Tổ chức các buổi tọa đàm hoặc sân khấu hóa trong các hội thi, hội diễn văn nghệ quần chúng để nâng cao nhận thức cho quân nhân về sử dụng, buôn bán vũ khí, quân dụng trái phép.
24. Trộm, cướp tài sản
b) Dấu hiệu nhận biết
- Muốn làm giàu nhanh chóng hoặc thích hưởng thụ, lười lao động, học tập, công tác.
- “Giàu” lên một cách bất thường và nhanh chóng, không chứng minh được khoản thu nhập tăng đột biến; tiêu tiền nhiều hơn bình thường.
- Có các vật dụng mới như: điện thoại, máy tính, dây chuyền, ví da… không rõ nguồn gốc.
- Cho quà người khác một cách bí mật, riêng tư, tâm lý cảnh giác.
- Thường xuyên có những hành vi lấm lét để ý, quan sát rất kỹ càng tài sản, thói quen, lịch trình và giờ giấc sinh hoạt của người khác.
- Tâm lý luôn bất ổn, lo lắng. Đi lại không công khai, bí ẩn.
- Quan tâm quá mức bình thường các vụ trộm cắp tài sản trên trên tivi, báo chí, mạng xã hội, phim ảnh.
- Cơ thể bị xây xát, bầm tím hoặc quần áo bị rách, có vết máu; bị ướt khi đi từ bên ngoài về nhà, đơn vị.
b) Biện pháp phòng ngừa:
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định của Bộ luật hình sự; quy định những điều đảng viên không được làm; Nghị quyết Trung ương 4 (khóa XII),… những thông tin liên quan đến các vụ việc trộm, cướp tài sản để răn đe, cảnh tỉnh.
- Tăng cường giáo dục cho quân nhân về ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, nhất là 10 lời thề danh dự của quân nhân, 12 điều kỷ luật khi tiếp xúc với nhân dân, các quy định của đơn vị và địa phương; giáo dụcphát huy truyền thống tốt đẹp của đơn vị, gia đình.
- Thường xuyên giáo dục chính trị tư tưởng cho cán bộ, chiến sỹ nêu cao tinh thần trách nhiệm trong xây dựng đơn vị.
- Đẩy mạnh công tác tuyên truyền, vận động mọi quân dân nâng cao ý thức cảnh giác, tự bảo quản tài sản của mình và tích cực tham gia tố giác, lên án các hành vị trộm cắp tài sản.
- Phối hợp chặt chẽ giữa đơn vị, địa phương và gia đình làm tốt công tác quản lý, giáo dục quân nhân về đạo đức, lối sống, văn hóa trong sạch, lành mạnh và ý thức chấp hành kỷ luật, pháp luật, có trách nhiệm của bản thân đối với đơn vị, gia đình.
- Chỉ huy đơn vị phải gần gũi, sâu sát, nắm bắt tâm tư, tình cảm, sức khỏe, cuộc sống gia đình của quân nhân. Phân công cán bộ theo phân cấp, đảng viên, chiến sĩ bảo vệ tăng cường các biện pháp nắm, quản lý quân nhân thuộc quyền thường xuyên, liên tục ở mọi lúc, mọi nơi, chú ý những thời điểm nhạy cảm; nắm chắc các mối quan hệ xã hội của quân nhân, nhất là với các thành phần phức tạp, kịp thời phát hiện những biểu hiện khác thường trong sinh hoạt của quân nhân.
- Thường xuyên kiểm tra quân tư trang toàn đơn vị, quản lý chặt chẽ thiết bị nghe, nhìn… Tìm hiểu, nắm rõ nguồn tài sản có giá trị, việc chi tiêu quá thu nhập của quân nhân.
- Định kỳ hoặc đột xuất kiểm tra thẻ đảng viên, chứng minh sĩ quan, QNCN, bằng tốt nghiệp…
- Tăng cường lắp đặt hệ thống camera an ninh ở các khu vực công cộng, nhà ở…
- Không dừng, đậu xe nơi tối vắng, nếu phải qua khu vực này nên đi từ 2 người, cảnh giác khi có đối tượng nghi vấn.
- Không sử dụng điện thoại khi đi đường, trường hợp cần thì đậu xe trên lề và quan sát xung quanh.
- Nếu có nhu cầu vận chuyển tiền với số lượng lớn, cần phải dùng xe chuyên dụng hoặc ô tô, bố trí đủ người canh giữ bảo vệ khi đưa tiền lên xuống.
- Khi đi đường, người đeo dây chuyền vòng vàng cần cài kín nút áo cổ, không để lộ trang sức ra ngoài. Nếu mang túi xách nên bỏ vào cốp xe hoặc móc chặt vào xe ràng buộc kỹ càng.
- Khi rút tiền ở ngân hàng và điểm ATM nên có người đi cùng và quan sát cảnh giác.
- Trên đường đi nếu phát hiện có đối tượng nghi vấn bám theo thì chạy chậm sát lề đường hoặc tấp vào nơi có đông người.
- Khi bị cướp giật phải tri hô, đồng thời ghi nhớ nhận dạng, loại xe, biển số… và đến ngay cơ quan Công an gần nhất trình báo, đồng thời về báo cáo chỉ huy đơn vị.
25. Làm kinh tế sai quy định
a) Dấu hiệu nhận biết
- Biểu hiện muốn làm giàu nhanh chóng hoặc thích hưởng thụ, lười lao động, học tập, công tác.
- Có sự gia tăng đột biến về tài sản nhưng không thể chứng minh được nguồn gốc của lượng tài sản gia tăng đó.
- Có mối quan hệ xã hội phức tạp cả ở đời thực và trên mạng xã hội.
- Sử dụng nhiều số điện thoại, nhiều tài khoản mạng xã hội nhưng không báo cáo.
- Có mối quan hệ mật thiết với những đối tượng làm ăn phi pháp.
- Khoe khoang cuộc sống sang chảnh, giàu sang, hàng hiệu, đi du lịch, đến các nơi sang trọng. Thường xuyên tiếp khách, ăn nhậu, có những buổi tiệc tùng tốn kém.
- Hay khoe khoang có mối quan hệ với lãnh đạo địa phương, cơ quan công an, các tập đoàn, doanh nghiệp… và khả năng chạy việc làm.
- Đi lại tự do, tùy tiện; thường xuyên vắng mặt tại cơ quan, đơn vị không rõ lý do.
- Không tập trung thực hiện chức trách, kết quả hoàn thanh nhiệm vụ thấp.
- Nhà ở xây kín cổng cao tường, lắp đặt hệ thống an ninh, camera theo dõi từ xa hoặc có bảo vệ một cách bất thường.
- Tham gia vào các nhóm đa cấp trá hình, các nhóm cò mồi đất….
b) Biện pháp phòng ngừa:	
- Giáo dục pháp luật cho quân nhân nhất là ý thức chấp hành pháp luật Nhà nước, kỷ luật Quân đội, các quy định trong hoạt động kinh doanh; cảnh giác trước các phương thức lừa đảo; có kiến thức về tác hại của việc làm kinh tế sai quy định; sống có nguyên tắc chi tiêu hợp lý, phù hợp với khả năng tài chính của gia đình.
- Tuyên truyền, vận động, xây dựng cho quân nhân lối sống trong sạch, lành mạnh, có trách nhiệm đối với gia đình. Kết hợp công tác giáo dục, tuyên truyền giải thích, thuyết phục với duy trì chặt chẽ, nghiêm túc kỷ luật của Quân đội, đơn vị.
- Tăng cường các biện pháp nắm, quản lý của cán bộ các cấp, nhất là mối quan hệ xã hội, việc chi tiêu của quân nhân. Làm tốt công tác hậu phương quân đội, phối hợp chặt chẽ với gia đình để quản lý quân nhân.
- Thực hiện nghiêm túc việc kê khai tài sản hằng năm, phát huy vai trò nêu gương của người đứng đầu. Xác minh nguồn tài sản có giá trị không rõ nguồn gốc hoặc nghi ngờ, việc chi tiêu quá thu nhập của quân nhân.
- Thực hiện công tác kiểm tra, giám sát đúng quy định; xác định đối tượng kiểm tra, giám sát tập trung vào các lĩnh vực nhạy cảm, vị trí dễ xảy ra vi phạm; chú trọng công tác kiểm tra, giám sát việc thực hiện cam kết của cán bộ, đảng viên ở cơ quan, đơn vị và địa phương.
- Biểu dương những quân nhân, người lao động vừa hoàn thành tốt nhiệm vụ đơn vị, vừa phát triển kinh tế gia đình đúng quy định của pháp luật.
- Có chính sách, quy định chế độ khen thưởng cả về vật chất và tinh thần, bảo đảm công khai, dân chủ, công bằng. Có chế độ đãi ngộ để từng bước nâng cao đời sống vật chất, tinh thần và lợi ích thiết thực của quân nhân trong đơn vị.
26. Sử dụng tài chính, đất quốc phòng, tài sản công sai quy định
a) Dấu hiệu nhận biết
- “Giàu” lên một cách bất thường và nhanh chóng, có nhiều tài sản có giá trị như: bất động sản, xe ô tô, vàng, đồ gỗ có giá trị… không chứng minh được khoản thu nhập tăng đột biến.
- Cán bộ có thẩm quyền quản lý tài chính, đất quốc phòng, tài sản công sử dụng vào mục đích sản xuất, làm giàu cho cá nhân hoặc “nhóm lợi ích”.
- Có mối quan hệ xã hội phức tạp cả ở đời thực và trên mạng xã hội.
- Sử dụng nhiều số điện thoại, nhiều tài khoản mạng xã hội nhưng không báo cáo.
- Lập nhiều tài khoản ngân hàng; mua bán cổ phiếu, tiền ảo.
- Mua bán hóa đơn, chứng từ sai quy định. 
- Khoe khoang cuộc sống sang chảnh, giàu sang, đi du lịch, đến các nơi sang trọng.
- Hay khoe khoang có mối quan hệ với lãnh đạo địa phương, cơ quan công an, các tập đoàn, doanh nghiệp…có thể chạy việc….
- Thường xuyên có mối quan hệ làm ăn với các công ty xây dựng, khai thác khoáng sản, buôn bán bất động sản…
- Thường xuyên tiếp đãi, đưa phong bì các đoàn công tác, thanh tra, kiểm toán Nhà nước, lãnh đạo cấp trên…
- Biểu hiện lo lắng trước các thông tin khiếu nại, tố cáo, thanh tra, kiểm tra.
b) Biện pháp phòng ngừa
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định về quản lý, sử dụng tài chính, đất quốc phòng, tài sản công cho các đối tượng, nhất là các cá nhân, tổ chức có liên quan trực tiếp đến hoạt động quản lý, sử dụng.
- Làm tốt công tác lãnh đạo, chỉ đạo của cấp ủy, tổ chức đảng, cán bộ các cấp trong công tác quản lý, sử dụng tài chính, đất quốc phòng, tài sản công.
- Tăng cường kiểm tra, giám sát, kiểm toán các hoạt động liên quan đến công tác tài chính, sử dụng đất quốc phòng, tài sản công.
- Triển khai việc kê khai tài sản cá nhân chặt chẽ, minh bạch trong việc kê khai những tài sản của tập thể được giao cho cá nhân quản lý.
- Vận dụng chặt chẽ các văn bản quy phạm pháp luật và chỉ đạo của cấp trên trong công tác phân bổ kinh phí, vật chất, quy hoạch đất quốc phòng, xây dựng cơ bản… nhằm hạn chế thấp nhất các sơ hở, không để cá nhân lợi dụng trục lợi trái pháp luật.
- Thường xuyên nắm chắc các mối quan hệ xã hội của quân nhân, nhất là quan hệ làm ăn kinh tế bên ngoài đơn vị.
- Gặp gỡ, giáo dục, định hướng tư tưởng, nhận thức và hành động đối với các quân nhân có biểu hiện vi phạm.
- Thường xuyên giáo dục các phẩm chất đạo đức cách mạng, nhất là đức tính cần, kiệm, liêm, chính, chí công vô tư cho các đối tượng trong đơn vị.
- Xử lý kiên quyết, nghiêm minh các trường hợp chấp hành quy định về quản lý, sử dụng tài chính, đất quốc phòng, tài sản công sai quy định.
- Phối hợp chặt chẽ với cấp ủy, chính quyền địa phương nơi đóng quân tiếp tục rà soát, kiểm tra, bổ sung, hoàn thiện hồ sơ pháp lý, ranh giới, mốc giới, diện tích trên thực địa của từng điểm đất quốc phòng được giao quản lý.
27. Vi phạm nguyên tắc tập trung dân chủ, quy chế lãnh đạo, quy chế làm việc
a) Dấu hiệu nhận biết
- Không thực hiện nghiêm nguyên tắc thiểu số phục tùng đa số, cấp dưới phục tùng cấp trên, cá nhân phục tùng tổ chức. Không chấp hành quyết nghị của tập thể (về việc quy hoạch, bổ nhiệm, đề bạt, luân chuyển...), thậm chí cùng nhau viết, ký tên vào đơn phản ánh, tố cáo, kiến nghị, gây mất đoàn kết nội bộ. 
- Trong sinh hoạt (cấp ủy, tổ chức đảng, cơ quan, đơn vị…) không phát biểu ý kiến hoặc có thảo luận, tranh luận, đóng góp ý kiến nhưng khi ra ngoài thì phát biểu khác, nói khác với ý kiến phát biểu của mình hoặc khác với quyết nghị của tập thể.
- Lợi dụng quyền bảo lưu ý kiến của mình để có bài viết, bài nói, phát ngôn hoặc cung cấp cho báo chí đăng tin, bài trái với quan điểm, đường lối, nghị quyết của Đảng, của cấp ủy, tổ chức đảng, làm mất uy tín của tổ chức đảng và của cán bộ, đảng viên.
- Lợi dụng cơ chế, chế độ tập thể để hợp pháp hóa quyết định, ý đồ cá nhân của mình bằng việc phát biểu ý kiến dưới dạng “định hướng trước” hoặc gợi ý để các thành viên trong cấp ủy thảo luận, phát biểu ý kiến một cách xuôi chiều, miễn cưỡng theo gợi ý, định hướng, dẫn đến không khách quan, chính xác.
- Không thực hiện nghiêm quy chế làm việc của tổ chức mình, lạm quyền trong quyết định những vấn đề về công tác cán bộ thuộc trách nhiệm của tập thể (quyết định tiếp nhận, quy hoạch, bổ nhiệm, đề bạt, cử đi học, đào tạo, nâng lương, luân chuyển cán bộ; tài chính, xây dựng cơ bản, đất đai...), nhất là trong những thời điểm nhạy cảm như sắp hết nhiệm kỳ công tác, nghỉ hưu, chuyển công tác khác...; dẫn đến vi phạm nghiêm trọng nguyên tắc tập trung dân chủ, tập thể lãnh đạo, cá nhân phụ trách.
	b) Biện pháp phòng ngừa:
- Quán triệt sâu sắc các nghị quyết, chỉ thị, quy định, kết luận của Trung ương, xây dựng, bổ sung hoàn thiện các quy định để phát huy nguyên tắc tập trung dân chủ trong tổ chức và sinh hoạt đảng ở cấp ủy, tổ chức đảng ở đơn vị cho phù hợp. Cụ thể hóa nguyên tắc tập trung dân chủ bằng những văn bản hướng dẫn cụ thể, để mọi tổ chức đảng và đảng viên thực hiện.
- Đẩy mạnh học tập và làm theo tư tưởng đạo đức, phong cách Hồ Chí Minh gắn với thực hiện có hiệu quả nghị quyết, chỉ thị, kết luận của Trung ương về xây dựng đảng; kết hợp chặt chẽ công tác kiểm tra, giám sát của các cấp ủy, tổ chức đảng với việc thanh tra, kiểm tra của cơ quan chức năng, kịp thời phát hiện, ngăn chặn và xử lý nghiêm các biểu hiện vi phạm nguyên tắc tập trung dân chủ.
- Nâng cao nhận thức, trách nhiệm của mỗi cấp ủy, cán bộ, đảng viên về thực hiện nguyên tắc tập trung dân chủ, bảo đảm mọi vấn đề liên quan đến công tác lãnh đạo của Đảng đều được dân chủ bàn bạc, công khai, quyết định theo đa số trên cơ sở phân định rõ thẩm quyền và trách nhiệm tập thể, cá nhân. 
- Đẩy mạnh tự phê bình và phê bình, phát huy trách nhiệm tự soi, tự sửa của mỗi cấp ủy, tổ chức đảng và mỗi cán bộ, đảng viên; tăng cường kiểm tra, giám sát việc thực hiện nguyên tắc tập trung dân chủ, kỷ luật, kỷ cương, sự đoàn kết, thống nhất nội bộ; tránh dân chủ hình thức, khắc phục cách làm việc tắc trách, trì trệ, hoặc lạm dụng quyền lực xâm phạm nguyên tắc.
- Thực hiện tốt Quy chế dân chủ ở cơ sở, phát huy vai trò giám sát, phản biện của các tổ chức và cá nhân đối với việc thực hiện nguyên tắc của Đảng. 
- Đề cao vai trò của người đứng đầu, cán bộ chủ chốt trong giữ vững và phòng, chống tình trạng xa rời nguyên tắc tập trung dân chủ, nhất là bí thư cấp ủy; nỗ lực học tập, rèn luyện phong cách, phương pháp làm việc dân chủ, khoa học, tạo bầu không khí dân chủ trong tổ chức.
- Cầu thị lắng nghe ý kiến phản ánh về việc thực hiện nguyên tắc tập trung dân chủ ở đơn vị và định kỳ lấy phiếu tín nhiệm của cán bộ các cấp, nhất là người đứng đầu, cán bộ chủ trì, chủ chốt. Phát huy vai trò của tổ chức quần chúng, hội đồng quân nhân và tập thể quân nhân trong việc phản ánh những biểu hiện vi phạm nguyên tắc tập trung dân chủ.
- Xây dựng tốt tinh thần đoàn kết trên cơ sở nguyên tắc, quy định, kỷ luật của Đảng, pháp luật Nhà nước, kỷ luật quân đội. Chống mọi biểu hiện lợi ích nhóm, cục bộ, bè phái.
28. Sử dụng mạng xã hội phát ngôn, phát tán, truyền tải, chia sẻ thông tin, hình ảnh sai quy định

a) Dấu hiệu nhận biết	
- Biểu hiện “nghiện” Internet, mạng xã hội, thích “sống ảo”, bị lệ thuộc vào điện thoại di động, máy tính bảng....
- Thường xuyên sử dụng điện thoại di động, máy tính truy cập và bình luận vào các tài khoản mạng xã hội phản động, bạo lực, khiêu dâm,…
- Thường xuyên chia sẻ những hoạt động, công tác của cơ quan, đơn vị lên mạng xã hội.
- Tính cách bốc đồng, nóng nảy, dễ bị kích động và phát ngôn thiếu kiểm soát.
- Có tư tưởng lạc hậu, phong kiến, gia trưởng, cổ súy cho các hủ tục, mê tín, dị đoan, dâm ô, đồi trụy, không phù hợp với thuần phong, mỹ tục của dân tộc.
- Có mối quan hệ xã hội phức tạp cả ở đời thực và trên mạng xã hội.
- Sử dụng nhiều số điện thoại, nhiều tài khoản mạng xã hội nhưng không báo cáo.
- Thường xuyên chụp ảnh, quay clip và chia sẻ hình ảnh, hoạt động của đơn vị lên mạng xã hội.
- Chủ quan, mất cảnh giác, thiếu ý thức trách nhiệm, tùy tiện trong phát ngôn hoặc đưa lên mạng những thông tin, hình ảnh sai trái, gây phản cảm; tự ý trao đổi, cung cấp thông tin, tài liệu không đúng đối tượng và phạm vi phổ biến.
- Có biểu hiện bất mãn, tiêu cực với thực tế cuộc sống, cấp trên, đồng chí đồng đội…
b) Biện pháp phòng ngừa:
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định có liên quan về sử dụng mạng xã hội, quy định về phát ngôn, bảo vệ chính trị nội bộ; nâng cao nhận thức, trách nhiệm của quân nhân trong tham gia sử dụng mạng xã hội an toàn.
- Nắm tâm tư, tình cảm, nhất là những vấn đề bức xúc của quân nhân trước các vấn đề được đăng tải trên mạng xã hội có liên quan đến tình hình đất nước, Quân đội, đơn vị; kịp thời phát hiện, ngăn chặn, bóc gỡ những thông tin không chính thống, chưa được kiểm chứng, phản ánh sai sự thật hoặc làm lộ lọt bí mật quân sự.
- Chú trọng làm tốt công tác bảo vệ chính trị nội bộ, quản lý chặt chẽ đội ngũ cán bộ, nhân viên, chiến sĩ làm công tác cơ yếu, văn thư, bảo mật và làm việc trong các cơ quan tổ chức, cán bộ, thanh tra, kiểm tra, tư pháp…
- Quản lý chặt chẽ quân nhân trong đơn vị, nhất là các trường hợp có mối quan hệ phức tạp, thường xuyên sử dụng mạng xã hội để kinh doanh, buôn bán online và đăng bài chia sẻ cuộc sống cá nhân… 
- Phối hợp chặt chẽ, thường xuyên với các cá nhân, tổ chức, cơ quan, đơn vị chuyên môn có liên quan, kịp thời phát hiện, xử lý các vi phạm về quy định sử dụng mạng xã hội, bảo vệ chính trị nội bộ.
- Đẩy mạnh ứng dụng thành tựu khoa học công nghệ để làm tốt công tác bảo mật đường truyền mạng, bảo mật cổng thông tin, trang thông tin điện tử; tăng cường các giải pháp bảo đảm an ninh, an toàn thông tin mạng tại cơ quan, đơn vị.
29. Làm lộ, lọt bí mật quân sự
a) Dấu hiệu nhận biết
- Thường xuyên chụp ảnh, quay clip và chia sẻ hình ảnh, hoạt động của đơn vị lên mạng xã hội.
- Mượn các loại tài liệu của đơn vị để photo không đúng quy định. Thường để ý, dò hỏi thông tin về hoạt động, công tác của cơ quan, đơn vị.
- Truy cập internet mà không có sự kiểm soát.
- Sử dụng usb không an toàn, không đúng cách.
- Theo dõi và truy cập những tài khoản mạng xã hội có nội dung phản động, chống phá Đảng và Nhà nước.
- Có mối quan hệ xã hội phức tạp cả ở đời thực và trên mạng xã hội; quan hệ, kết nối với các đối tượng bất mãn, cá nhân hoặc tổ chức phản động trong và ngoài nước.
- Có giao dịch tiền tệ “mờ ám” từ nguồn trong nước hoặc nước ngoài gửi tới mà không thể chứng minh được nguồn gốc.
- Sử dụng nhiều số điện thoại, nhiều tài khoản mạng xã hội nhưng không báo cáo.
- Chủ quan, mất cảnh giác, thiếu ý thức trách nhiệm, tùy tiện trong phát ngôn hoặc đưa lên mạng những thông tin, hình ảnh sai trái, gây phản cảm; tự ý trao đổi, cung cấp thông tin, tài liệu không đúng đối tượng và phạm vi phổ biến.
- Chấp hành kỷ luật không nghiêm, đi lại tự do, tùy tiện.
b) Biện pháp phòng ngừa
- Tăng cường quán triệt các nghị quyết, chỉ thị của Đảng, Nhà nước, các quy định, hướng dẫn của Quân đội, đơn vị về công tác bảo vệ bí mật Nhà nước, bí mật quân sự. Chú trọng làm tốt công tác tuyên truyền, giáo dục, nâng cao nhận thức, trách nhiệm cho cán bộ, nhân viên và chiến sĩ về công tác bảo vệ bí mật quân sự trước yêu cầu mới; ý thức chấp hành pháp luật Nhà nước, kỷ luật Quân đội, kỷ luật phát ngôn; không tự ý trả lời phỏng vấn của các phương tiện truyền thông khi chưa được phép của cơ quan chức năng.
- Tổ chức tập huấn, bồi dưỡng kiến thức, kinh nghiệm, kỹ năng phòng gian, giữ bí mật Nhà nước, bí mật quân sự cho mọi quân nhân trong đơn vị.
- Làm tốt công tác bảo vệ chính trị nội bộ, nắm và quản lý chặt chẽ tình hình tư tưởng, kỷ luật và các mối quan hệ của cán bộ, chiến sĩ thuộc quyền.
- Yêu cầu kê khai đầy đủ các số điện thoại và các tài khoản mạng xã hội mà quân nhân đang sử dụng. Không để cán bộ, nhân viên, chiến sĩ truy cập vào các trang mạng có nội dung phản động, sai trái; đưa các thông tin, hình ảnh có nội dung liên quan đến bí mật quân sự hoặc “nhạy cảm” trên các phương tiện truyền thông, mạng xã hội.
- Duy trì chấp hành pháp luật Nhà nước, kỷ luật Quân đội, bảo đảm an ninh, an toàn cho các hoạt động của đơn vị. Quản lý chặt chẽ công văn, tài liệu, vũ khí, khí tài, trang bị, tài sản của Quân đội, không để lộ, lọt, mất mát. Tăng cường công tác quản lý bí mật quân sự trên các phương tiện thông tin và truyền thông, nhất là quản lý việc sử dụng dịch vụ internet và các thiết bị công nghệ thông tin. 
- Thường xuyên kiểm tra, giám sát việc chấp hành chỉ thị, quy định về phòng gian, giữ bí mật của cán bộ, chiến sĩ, nhất là các biện pháp phòng ngừa, không để lộ, lọt thông tin, tài liệu mật. 
- Thực hiện chặt chẽ quy trình xác minh, xét duyệt, tuyển chọn người vào cơ quan, đơn vị, vị trí trọng yếu, cơ mật; trong tuyển quân, tuyển sinh quân sự, đi học tập, công tác nước ngoài. Thường xuyên rà soát, đảm bảo tiêu chuẩn chính trị đối với cán bộ, nhân viên, chiến sĩ làm việc tại cơ quan, đơn vị, vị trí trọng yếu, cơ mật.
- Thực hiện nghiêm quy định trong quan hệ, tiếp xúc với các tổ chức, cá nhân nước ngoài.
- Phát huy vai trò của chiến sĩ bảo vệ, Cơ quan Bảo vệ an ninh thường xuyên nắm chắc tình hình, chủ động tham mưu đề xuất giúp cấp ủy, chỉ huy các cấp lãnh đạo, chỉ đạo và phối hợp chặt chẽ với các lực lượng, cơ quan chức năng kịp thời phát hiện, phòng ngừa, đấu tranh ngăn chặn, vô hiệu hóa các hoạt động phá hoại, đánh cắp thông tin, bí mật quân sự của các thế lực thù địch, phản động, bảo đảm an ninh, an toàn cho các hoạt động của đơn vị.
- Chủ động phát hiện, ngăn chặn kịp thời nhận thức và hành động không đúng, biểu hiện mơ hồ, mất cảnh giác, thiếu ý thức trách nhiệm, vô tình hay cố ý để lộ, lọt thông tin bí mật quân sự.
- Khi phát hiện thông tin, hình ảnh liên quan đến bí mật quân sự trên mạng xã hội, cần nhanh chóng báo cáo cấp trên và phối hợp chặt chẽ với cơ quan chức năng để có biện pháp xử lý.
30. Tự ý ra nước ngoài
a) Dấu hiệu nhận biết
- Tính cách thích ăn chơi, hưởng thụ, có điều kiện về kinh tế.
- Có người thân, bạn bè đang sinh sống và làm việc tại nước ngoài.
- Có mối quan hệ xã hội phức tạp cả ở đời thực và trên mạng xã hội, nhất là quan hệ với người nước ngoài và các trang mạng ngoài nước.
- Sử dụng nhiều số điện thoại, nhiều tài khoản mạng xã hội một cách bất thường nhưng không báo cáo.
- Tự ý làm một số giấy tờ: visa…
- Học thêm một số ngoại ngữ hoặc các ngôn ngữ nước ngoài một cách bất thường không phục vụ cho học tập, công tác và dạy dỗ con cái.
- Bán các loại tài sản có giá trị lớn như: bất động sản, cổ phiếu, vàng, xe ô tô…
- Thường xuyên tìm hiểu, bàn tán về địa lý, văn hóa,… của một hay một vài nước khác.
- Mua sắm quần áo, đồ dùng cần thiết để chuẩn bị cho một chuyến đi xa.
- Có những mối quan hệ với các đối tượng làm giả giấy tờ tùy thân, hộ chiếu; các đối tượng trong tổ chức phản động ở ngoài nước.
- Nghỉ phép, tranh thủ hoặc đi chữa bệnh dài ngày, vắng mặt tại cơ quan, đơn vị và không rõ lý do.
b) Biện pháp phòng ngừa
- Tăng cường làm tốt công tác giáo dục, quán triệt, thực hiện quy định trách nhiệm nêu gương và các quy định những điều đảng viên không được làm; xây dựng cho quân nhân có ý thức chấp hành pháp luật Nhà nước, điều lệnh, điều lệ, quy định của Quân đội, đơn vị.
- Thường xuyên giáo dục chính trị tư tưởng cho cán bộ, chiến sĩ phát huy truyền thống tốt đẹp của Quân đội, đơn vị, gia đình; nêu cao trách nhiệm xây dựng đơn vị.
- Thực hiện chặt chẽ công tác bảo vệ chính trị nội bộ, quản lý, nắm chắc tình hình tư tưởng, các mối quan hệ và ý thức chấp hành kỷ luật của quân nhân; chú trọng các mối quan hệ với các tổ chức, cá nhân người nước ngoài. Duy trì chấp hành nghiêm quy định trong quan hệ, tiếp xúc với các tổ chức, cá nhân nước ngoài.
- Tăng cường các biện pháp quản lý quân nhân thuộc quyền; gần gũi, sâu sát, nắm bắt tâm tư, tình cảm, sức khỏe, hoàn cảnh gia đình của quân nhân trong đơn vị, nhất là trường hợp có hoàn cảnh khó khăn, mắc bệnh hiểm nghèo... kịp thời quan tâm, động viên. Có biện pháp quản lý quân nhân trong nghỉ phép, nghỉ chữa bệnh dài ngày.
- Yêu cầu kê khai đầy đủ các số điện thoại và các tài khoản mạng xã hội mà quân nhân đang sử dụng.


Phần thứ hai
GỢI Ý BIỆN PHÁP XỬ LÝ CỦA CÁN BỘ CƠ SỞ ĐỐI VỚI NHỮNG TÌNH HUỐNG TƯ TƯỞNG CÓ THỂ NẢY SINH

	* NGUYÊN TẮC, QUY TRÌNH XỬ LÝ CƠ BẢN 
Tình huống tư tưởng có thể nảy sinh ở đơn vị cơ sở rất đa dạng, phức tạp với nhiều lý do khác nhau, đòi hỏi phải có các phương pháp xử lý phù hợp; quá trình xử lý thường theo một quy trình chung đó là:
Bước 1: Chuẩn bị xử lý
- Hội ý cấp uỷ, chỉ huy đơn vị, nhận định, đánh giá tính chất, tác hại, nguyên nhân, mức độ ảnh hưởng để trao đổi, thống nhất trong chỉ huy và báo cáo cấp trên xin ý kiến chỉ đạo;
- Lựa chọn chủ thể xử lý phù hợp với đối tượng xử lý (chính trị viên, chính trị viên phó, đại đội trưởng, đại đội phó, trung đội trưởng, tiểu (khẩu) đội trưởng, chiến sĩ bảo vệ, cũng có thể là người bạn thân hoặc gia đình…)
- Nhanh chóng thu thập, phân tích, kết luận thông tin bảo đảm chính xác;
- Xác định kế hoạch, nội dung xử lý, dự kiến tình huống, sử dụng các lực lượng tham gia xử lý (Hội đồng quân nhân, tổ tư vấn tâm lý, pháp lý, gia đình, địa phương …)
- Chuẩn bị môi trường, cơ sở vật chất cho việc xử lý.
Bước 2: Quá trình xử lý
- Gặp gỡ, tiếp xúc với đối tượng;
- Sử dụng các phương pháp xử lý cho phù hợp (phân tích thuyết phục; truyền đạt thông tin; hướng dẫn tư duy; ám thị gián tiếp; động viên, phê phán; tác động tình cảm; gợi nhớ);
- Quan sát, ghi nhận các biểu hiện, phản ứng của đối tượng;
- Nhận xét, đánh giá kết quả tác động;
- Điều chỉnh kế hoạch tác động cho phù hợp với thái độ, sự phản ứng của đối tượng.
Bước 3: Kết thúc xử lý: Tạm thời hay toàn bộ. Nếu đối tượng tác động có chuyển biến tư tưởng tốt, tích cực, hợp tác, quyết tâm khắc phục những biểu hiện tâm lý tư tưởng lệch lạc thì xem như kết thúc toàn bộ, còn kết thúc tạm thời là khi đối tượng có chuyển biến chậm phải tiếp tục thực hiện kế hoạch xử lý.
- Ổn định tình hình đơn vị;
- Tiếp tục theo dõi, tác động ổn định tư tưởng, củng cố lòng tin cho đối tượng;
- Đánh giá kết quả, rút ra bài học kinh nghiệm.
- Tổng hợp tình hình, báo cáo cấp trên, xin ý kiến chỉ đạo tiếp theo.

I. GỢI Ý BIỆN PHÁP XỬ LÝ NHÓM TÌNH HUỐNG TƯ TƯỞNG CÓ THỂ NẢY SINH TRONG THỰC HIỆN NHIỆM VỤ PHÒNG, CHỐNG THIÊN TAI, DỊCH BỆNH (50 tình huống).
	A. TÌNH HUỐNG TƯ TƯỞNG CÓ THỂ NẢY SINH TRONG THỰC HIỆN NHIỆM VỤ PHÒNG, CHỐNG DỊCH BỆNH
	Tình huống 01. Một chiến sĩ trong đơn vị có biểu hiện buồn chán khi bố (mẹ) ốm điều trị dài ngày ở bệnh viện (do bị nhiễm loại vi rút mới), nhưng đơn vị không giải quyết phép, vì đang trong giai đoạn dịch lây lan mạnh ngoài cộng đồng.
	Gợi ý biện pháp xử lý:
	- Hội ý chỉ huy đơn vị, đánh giá tình hình, thống nhất biện pháp xử lý.
	- Chỉ huy đơn vị triển khai quán triệt các văn bản của các cấp về các biện pháp phòng, chống đại dịch; gặp gỡ quân nhân có bố (mẹ) điều trị ở bệnh viện, chia sẻ, đồng cảm về điều kiện hoàn cảnh của gia đình; đồng thời nắm thêm về tình hình gia đình và tâm tư, nguyện vọng; động viên các quân nhân hiểu rõ yêu cầu cấp bách của nhiệm vụ phòng, chống đại dịch.
	- Báo cáo, đề xuất và xin ý kiến chỉ đạo của cấp trên: Nếu trường hợp bệnh viện ở gần nơi đơn vị đóng quân thì đề nghị cử cán bộ ra thăm hỏi, động viên gia đình. Nếu bệnh viện ở xa thì gọi điện cho người thân trong gia đình để hỏi thăm và nắm thêm tình hình.
	- Căn cứ vào tình trạng, mức độ bệnh tật của bố (mẹ) quân nhân để sinh hoạt thông báo với cán bộ, chiến sĩ trong đơn vị được biết để động viên, chia sẻ hoặc có thể quên góp ủng hộ về vật chất... giúp đỡ quân nhân yên tâm tư tưởng, xác định trách nhiệm và hoàn thành tốt nhiệm vụ.
- Phân công cán bộ, chiễn sĩ theo dõi, động viên, giúp đỡ quân nhân có bố (mẹ) đang nằm viện trong học tập, công tác, sinh hoạt, cùng gia đình khắc phục khó khăn, hoàn thành tốt nhiệm vụ nhiệm vụ được giao.
- Kết thúc thời gian giãn cách xã hội theo Chỉ thị 16, căn cứ tình hình nhiệm vụ của đơn vị đề nghị cấp trên giải quyết phép đặc biệt, hoặc phép về thăm gia đình cho quân nhân có bố (mẹ) ốm nằm viện.
Tình huống 02. Chỉ huy đơn vị nhận được thông tin, do căng thẳng, lo sợ trong thực hiện nhiệm vụ giúp nhân dân trong phòng, chống đại dịch tại tâm dịch tỉnh X, một số chiến sĩ có ý định đào ngũ.
Gợi ý biện pháp xử lý
- Hội ý chỉ huy đơn vị, đánh giá tình hình, thống nhất biện pháp xử lý.
- Tổ chức sinh hoạt đơn vị quán triệt, giáo dục cho cán bộ, chiến sĩ nhận thức sâu sắc về mục đích, ý nghĩa và yêu cầu của nhiệm vụ phòng, chống đại dịch; đây là vừa chức năng cơ bản (đội quân công tác), vừa là nhiệm vụ chiến đấu của quân đội trong thời bình; trên cơ sở đó xây dựng ý chí, quyết tâm và trách nhiệm trong thực hiện nhiệm vụ.
- Đánh giá, phân loại tư tưởng; phân công cán bộ gặp gỡ, động viên, giúp đỡ chiến sĩ có biểu hiện lo lắng, giao động tư tưởng; tập trung quản lý chặt chẽ quân số, tư tưởng, các mối quan hệ, chất lượng công tác của quân nhân.
- Đẩy mạnh đợt thi đua đặc biệt trong phòng, chống dịch, tập trung nâng cao nhận thức, trách nhiệm; chấp hành nghiêm pháp luật, kỷ luật; phát huy tốt vai trò tiền phong, gương mẫu của cán bộ đảng viên...; kịp thời biểu dương, nhân rộng những gương tập thể, cá nhân tiêu biểu trong thực hiện nhiệm vụ.
- Thường xuyên làm tốt công tác dự báo tình hình, nắm chắc tình hình tư tưởng để quản lý, không để bị động, bất ngờ. Phân công cán bộ thường xuyên gần gũi với chiến sĩ, tâm sự nắm chắc tâm tư tình cảm và chia sẻ những khó khăn vất vả với bộ đội, nhất là các quân nhân không yên tâm công tác.
- Kịp thời rút kinh nghiệm; tăng cường công tác quản lý, kiểm tra quân số (trong giờ nghỉ, ngày nghỉ, thời điểm nhạy cảm); phát huy hiệu quả hoạt động của các tổ chức, lực lượng, “tổ tư vấn tâm lý, pháp lý”, chiến sĩ dân vận, chiến sĩ bảo vệ; tổ chức  các hoạt động văn hóa tinh thần trong giờ nghỉ, ngày nghỉ thiết thực, hiệu quả. Quan tâm bảo đảm tốt đời sống vật chất, tinh thần cho bộ đội. 
Tình huống 03. Thời gian gần đây trong đơn vị xuất hiện nhiều thông tin sai sự thật về công tác phòng, chống đại dịch của Đảng, Nhà nước, Quân đội... gây hoang mang, lo lắng cho cán bộ, chiến sĩ.
Gợi ý biện pháp xử lý
- Hội ý chỉ huy đơn vị, đánh giá tình hình, thống nhất biện pháp xử lý.
- Tổ chức sinh hoạt đơn vị quán triệt, thông tin, tuyên truyền, giáo dục cán bộ, chiến sĩ nhận thức sâu sắc về quan điểm, chủ trương, chính sách của Đảng và Nhà nước ta về công tác phòng, chống dịch; trên cơ sở đó, định hướng nhận thức tư tưởng, xây dựng niềm tin, thái độ, trách nhiệm của mỗi quân nhân trước những tác động tiêu cực nảy sinh...
- Thường xuyên quán triệt sâu, kỹ về nhiệm vụ của quân đội và đơn vị; âm mưu “DBHB”, “phi chính trị hóa” Quân đội của các thế lực thù địch; kiên quyết đấu tranh phản bác những luận điệu phản ánh sai trái, bảo vệ nền tàng tư tưởng của Đảng; giữ vững niềm tin cho mọi cán bộ, chiến sĩ, yên tâm hoàn thành tốt mọi nhiệm vụ được giao. 
- Tăng cường tuyên truyền, giáo dục Lời kêu gọi của Đảng, Nhà nước, Chính phủ đối với công tác phòng, chống đại dịch; phát huy hiệu quả hoạt động tuyên truyền thông qua hệ thống thiết chế văn hóa, truyền thanh nội bộ, chế độ đọc báo, thông báo chính trị - thời sự, xem truyền hình. 
- Phối hợp chặt chẽ cấp ủy, chính quyền và các tổ chức đoàn thể địa phương trong công tác tuyên truyền, giáo dục; xây dựng đơn vị an toàn gắn với địa bàn an toàn.
- Kịp thời rút kinh nghiệm ở các cấp, thường xuyên giáo dục, tuyên truyền  nâng cao nhận thức, trách nhiệm cho bộ đội; coi trọng xây dựng ý chí quyết tâm, tinh thần khắc phục khó khăn, ý thức chấp hành pháp luật, kỷ luật; quan tâm  đảm bảo đời sống cho cán bộ, chiến sĩ; phát huy vai trò tiền phong của cán bộ, đảng viên trong thực hiện chức trách nhiệm vụ.
- Thường xuyên sâu sát, gần gũi bộ đội, kịp thời nắm bắt tâm tư, tình cảm, chia sẻ, tháo gỡ những vướng mắc, khó khăn của cán bộ, chiến sĩ. Thực hiện tốt công tác nắm, quản lý, dự báo, định hướng và giải quyết tình hình tư tưởng.
 Tình huống 04: Trong thời gian thực hiện Chỉ thị của Thủ tướng Chính phủ, do thời gian trực kéo dài, có quân nhân nảy sinh tư tưởng ngại khó khăn, xin nghỉ phép, nghỉ tranh thủ, lý do việc gia đình…
Gợi ý biện pháp xử lý:
- Tập trung phổ biến, quán triệt, tổ chức thực hiện nghiêm các văn bản của trên và đơn vị về công tác phòng, chống đại dịch.
- Tiến hành đồng bộ các tổ chức tuyên truyền, giáo dục về chức năng, nhiệm vụ của Quân đội.
-Tổ chức gặp gỡ trao đổi, động viên kịp thời, giải thích về những quy định phòng, chống đại dịch trong tình hình hiện nay.
- Thường xuyên nắm bắt tình hình tư tưởng, dư luận xã hội, mối quan hệ gia đình, địa phương, đồng chí, đồng đội của từng quân nhân; kết hợp nhiều biện pháp để giáo dục phù hợp với từng đối tượng, gần gũi nắm bắt tâm tư tình cảm.
- Tổ chức các hoạt động VHVN, TDTT tạo không khí vui tươi, lành mạnh trong đơn vị.
- Thường xuyên phối hợp với cấp ủy, chính quyền địa phương kịp thời nắm sự chỉ đạo của các cấp, sẵn sàng thực hiện các nhiệm vụ được giao trong phòng, chống dịch.
Tình huống 05: Đơn vị chuẩn bị nhận nhiệm vụ tăng cường cho tuyến đầu chống dịch, khu vực có nguy cơ lây nhiễm, tỷ lệ tử vong cao; có chiến sĩ lấy lý do sức khoẻ yếu, xin đi điều trị tại bệnh xá để không phải tham gia đợt công tác đặc biệt sắp tới, đã tác động xấu đến nhận thức nhiệm vụ của một số đồng chí khác.
Gợi ý biện pháp xử lý:
- Trao đổi thống nhất trong lãnh đạo, chỉ huy đơn vị về biện pháp xử lý; phân công cán bộ phụ trách, quan tâm, sâu sát động viên chăm sóc các đồng chí đó.
- Chỉ đạo quân y đơn vị phối hợp với quân y cấp trên kiểm tra sức khoẻ của chiến sĩ. Nếu ốm thật, đề nghị đánh giá đúng mức độ bệnh tình, chăm sóc điều trị chu đáo. Nếu không phải bị ốm mà là vì lý do ngại khó, ngại khổ, sợ lây dịch bệnh, có thể phải hy sinh trong khi thi hành nhiệm vụ thì phải xác định đây là trường hợp có biểu hiện bất thường về tư tưởng; trên cơ sở nhận định, đánh giá đúng tính chất sự việc như vậy để đưa ra biện pháp xử lý phù hợp.
- Trực tiếp gặp gỡ tìm hiểu rõ nguyên nhân; phương pháp phải khéo léo, mềm dẻo thông qua tâm sự, trò chuyện để nắm bắt tâm tư, tình cảm, vướng mắc của chiến sĩ.
- Giáo dục, động viên nâng cao nhận thức của chiến sĩ về trách nhiệm, nghĩa vụ của “Bộ đội Cụ Hồ” đối với Tổ quốc, với nhân dân; phân tích, quán triệt để chiến sĩ đó thấy được về tinh thần tương thân, tương ái, trong phóng, chống dịch, những tấm gương hy sinh quên mình nơi tuyến đầu chống dịch của đồng chí, đồng đội, các y bác sĩ và có cả những người dân thường... từ đó để nâng cao nhận thức, củng cố quyết tâm cho người chiến sĩ tự giác, tích cực tham gia thực hiện nhiệm vụ (nếu chiến sĩ đó vẫn không chuyển biến phải báo cáo với cấp trên để có biện pháp giáo dục, động viên xử lý phù hợp).
- Phát huy vai trò của các tổ chức, nhất là tổ 3 người, tiểu đội, trung đội, đoàn thanh niên, hội đồng quân nhân và các mối quan hệ bạn bè thân thiết, đồng hương, người thân, gia đình để giáo dục, động viên chiến sĩ có nhận thức tốt về nhiệm vụ, sẵn sàng tham gia thực hiện nhiệm vụ tăng cường cho tuyến đầu chống dịch. Tổ chức cho đơn vị xem, nghe các chương trình truyền hình, phát thanh đưa tin về những tấm lòng cao cả, tấm gương hy sinh quên mình trong phòng chống dịch.
- Hướng dẫn chỉ đạo tiểu đội, trung đội sinh hoạt rút kinh nghiệm về công tác quản lý tư tưởng bộ đội; xây dựng động cơ, trách nhiệm, bản lĩnh trong mọi tình huống và nhiệm vụ được giao.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 06: Trường hợp nhân viên nữ làm nhiệm vụ cấp dưỡng (nấu ăn) do thực hiện giãn cách lâu ngày không được về gia đình, đã nảy sinh tư tưởng buồn chán, trách nhiệm phục vụ không tốt trong quá trình phòng, chống dịch của đơn vị.
Gợi ý biện pháp xử lý:
- Nắm bắt tình hình diễn biến, gặp gỡ trao đổi, động viên quân nhân khắc phục tốt mọi khó khăn; tiếp tục quán triệt sâu rộng trong toàn đơn vị các văn bản của trên và đơn vị về nhiệm vụ phòng, chống dịch (đặc biệt là tầm quan trọng của việc thực hiện giãn cách xã hội).
- Các tổ chức trong đơn vị (nhất là Hội phụ nữ) kịp thời nắm bắt tâm tư, tình cảm, những khó khăn gia đình của quân nhân khi trực tại đơn vị; cùng bàn bạc, tìm biện pháp khắc phục để quân nhân yên tâm hoàn thành tốt nhiệm vụ.
- Căn cứ vào cấp độ dịch để có biện pháp nâng cao đời sống vật chất tinh thần cho cán bộ, chiến sĩ theo khả năng của đơn vị.
- Kết hợp đồng bộ công tác tuyên truyền gương người tốt, việc tốt trong phòng chống dịch.
Tình huống 07: Theo yêu cầu nhiệm vụ của trên giao đơn vị có nhiệm vụ tăng cường bảo đảm về quân số cơ động đến các địa phương có dịch để hỗ trợ trong công tác phòng chống đại dịch, thì có một số cán bộ, chiến sỹ còn băn khoăn, lo lắng không yên tâm công tác, vì phải xa nhà, xa đơn vị, thực hiện nhiệm vụ trong điều kiện khó khăn vất vả.
Gợi ý biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy đơn vị, đánh giá tình hình tư tưởng trong đơn vị, xác định các chủ trương, biện pháp khắc phục.
- Căn cứ nhiệm vụ cấp trên giao, giao cho đơn vị trực tiếp lựa chọn lực lượng nòng cốt thực hiện nhiệm vụ trước, để thực hiện công tác giáo dục, lan tỏa tư tưởng tốt trong cơ quan, đơn vị.
- Phân công các đồng chí trong cấp uỷ gặp gỡ số cán bộ, chiến sĩ không an tâm tư tưởng, giáo dục động viên làm rõ nghĩa vụ, trách nhiệm của quân nhân trong tham gia phòng chống đại dịch; giáo dục chức năng, nhiệm vụ của Quân đội; xác định đây là thời điểm nhân dân cần quân đội và các lực lượng liên quan giúp đỡ. 
- Tổ chức sinh hoạt đơn vị giáo dục, quán triệt định hướng tư tưởng cho bộ đội; giáo dục mức độ, thời gian ảnh hưởng của dịch bệnh; đơn vị tiếp tục thực hiện các nhiệm vụ khó khăn, phức tạp hơn; định hướng tư tưởng cho bộ đội an tâm, sẵn sàng nhận và thực hiện mọi nhiệm vụ được giao.
- Tổ chức diễn đàn, tọa đàm về phòng, chống dịch Covid-19, những tấm gương sáng trong thực hiện nhiệm vụ; phát động thi đua sẵn sàng nhận và hoàn thành mọi nhiệm vụ được giao, tổ chức đăng ký tự nguyện tham gia giúp đỡ nhân dân trong phòng chống đại dịch tại các địa phương
- Phân công cán bộ theo dõi, kèm cặp, giúp đỡ từng người, từng tổ; sử dụng các chiến sĩ bảo vệ của đơn vị nắm tình hình, chủ động dự kiến các vấn đề nảy sinh như đào ngũ, vắng mặt trái phép để có các biện pháp ngăn chặn và xử lý kịp thời.
Tình huống 08: Trong quá trình thực hiện nhiệm vụ giúp đỡ nhân dân phòng, chống đại dịch có chiến sỹ bị nhiễm bệnh tử vong, một số chiến sĩ có biểu hiện băn khoăn, lo lắng, dẫn đến kết quả hoàn thành nhiệm vụ thấp.
Gợi ý biện pháp xử lý:
- Người chỉ huy ra lệnh tạm dừng nhiệm vụ, phối hợp với các lực lượng, nhất là lực lượng quân y, có biện pháp khử khuẩn, bảo đảm an toàn; tổ chức bảo vệ hiện trường; sơ bộ nắm tình hình và báo cáo chỉ huy cấp trên.
- Họp cấp ủy, chỉ huy đơn vị đánh giá tình hình, xác định nguyên nhân ban đầu và biện pháp xử lý. Thực hiện các biện pháp phòng, chống dịch ở mức cao nhất.
- Xin ý kiến chỉ đạo của cấp trên; thông báo ngay cho gia đình thân nhân chiến sĩ tử vong.
- Phối hợp chặt chẽ với cấp ủy, chính quyền địa phương, cơ quan các cấp xác định nguyên nhân; thống nhất biện pháp giải quyết theo quy định.
- Cán bộ các cấp thường xuyên bám sát mọi hoạt động, động viên, nhắc nhở bộ đội ổn định tư tưởng, tâm lý; quán triệt thực hiện đúng công tác bảo đảm an toàn, giảm thiểu tối đa những hy sinh, mất mát tiếp theo.
- Tiến hành giải quyết hậu quả theo quy định, đúng chức năng, nhiệm vụ, quyền hạn và điều kiện thực tế của đơn vị.
- Động viên cán bộ, chiến sĩ đơn vị chia sẻ, giúp đỡ vật chất, tinh thần với gia đình quân nhân tử vong; phối hợp với gia đình tổ chức mai táng chu đáo.
- Kịp thời thông báo kết luận điều tra của cấp trên; kiểm điểm làm rõ trách nhiệm, rút ra bài học kinh nghiệm trong công tác lãnh đạo, chỉ đạo và tổ chức thực hiện; thực hiện tốt các chế độ, chính sách cho quân nhân.
Tình huống 09: Khi thực hiện nhiệm vụ tăng cường phòng, chống dịch, có một đồng chí sĩ quan không may nhiễm bệnh và tử vong đã gây ảnh hưởng lớn đến tâm lý, tư tưởng và kết quả thực hiện nhiệm vụ của cán bộ, chiến sĩ.
Gợi ý biện pháp xử lý:
- Nhanh chóng báo cáo cấp trên, đề nghị Quân y xử lý bước đầu đối với quân nhân nhiễm bệnh tử vong.
- Cùng với Quân y đưa thi thể quân nhân tử vong về nơi quy định để tiến hành lấy mẫu xét nghiệm vệ sinh dịch tễ để xác định chính xác nguyên nhân tử vong.
- Thực hiện các biện pháp khử khuẩn khu vực có quân nhân nhiễm bệnh và tử vong để không làm lây lan dịch bệnh ở nơi đơn vị đóng quân.
- Thông báo cho gia đình quân nhân tử vong biết về nguyên nhân ban đầu dẫn tới cái chết; động viên tư tưởng, phối hợp cùng gia đình chuẩn bị hậu sự cho quân nhân.
- Tiếp tục tổ sinh hoạt quán triệt chấp hành nghiêm quy định phòng, chống dịch bệnh của Bộ Y tế trong quá trình tăng cường phòng, chống dịch, đặc biệt là các biện pháp bảo đảm an toàn cho cá nhân; đồng thời giáo dục định hướng, ổn định tình hình tư tưởng, dư luận cho cán bộ, chiến sĩ, xây dựng quyết tâm hoàn thành tốt nhiệm vụ.
- Có thể cử một số cán bộ, chiến sĩ cùng với gia đình lo hậu sự cho quân nhân tử vong trong điều kiện phòng, chống dịch và phù hợp với nguyện vọng của gia đình, phong tục, tập quán của địa phương.
- Vận động cán bộ, chiến sĩ tham gia ủng hộ đối với gia đình quân nhân tử vong với tinh thần tương thân, tương ái.
- Phối hợp với cơ quan chức năng thực hiện tốt chế độ chính sách đối với quân nhân từ trần khi đang thực hiện nhiệm vụ.
- Tổng hợp kết quả giải quyết vụ việc, báo cáo cấp trên theo đúng quy định.
Tình huống 10: Trong thời điểm nhân dân cả nước đang tập trung phòng, chống dịch thì các thế lực thù địch lợi dụng mạng xã hội đăng tải, tuyên truyền sai sự thật về tình hình diễn biến của dịch trong đó có thông tin liên quan trực tiếp đến cán bộ, chiến sỹ trong đơn vị.
Gợi ý biện pháp xử lý:
- Chỉ đạo Lực lượng 47, các cơ quan, đơn vị liên quan nhanh chóng phối hợp với các đơn vị bạn, lực lượng địa phương, các cơ quan báo chí, truyền thông chính thống đăng tải nội dung tuyên truyền, định hướng dư luận
- Tổ chức lực lượng xây dựng nội dung tuyên truyền trên không gian mạng, đấu tranh phản bác, triệt phá, bóc gỡ các tin giả thông tin sai sự thật, xấu độc lợi dụng vụ việc để chống phá.
- Tổng hợp nhanh tình hình, thu thập tài liệu, kết quả xử lý sơ bộ báo cáo cấp trên.
Tình huống 11: Một cán bộ (trung đội trưởng) sử dụng điện thoại thông minh đăng tải không đúng tình hình phòng, chống đại dịch trong đơn vị và địa bàn đóng quân lên mạng xã hội, làm cho gia đình và bạn bè quân nhân khi truy cập, gây hoang mang, lo lắng.
* Gợi ý biện pháp xử lý
- Kiểm tra, nắm chắc tình hình vụ việc.
- Hội ý chỉ huy đơn vị đánh giá tình hình, nguyên nhân, hậu quả, thống nhất biện pháp giải quyết trong cấp ủy, chỉ huy.
- Gặp gỡ cán bộ đăng tin bài, phân tích rõ sự việc; chỉ đạo quân nhân cùng các cơ quan chức năng có liên quan tìm mọi biện pháp nhanh chóng gỡ bỏ thông tin sai trái trên mạng xã hội, thông tin định hướng tư tưởng cho gia đình. Tùy theo mức độ, hậu quả của vi phạm, triển khai cho cán bộ viết bản tường trình, bản kiểm điểm. 
- Tổ chức sinh hoạt rút kinh nghiệm trong cán bộ; xây dựng nhận thức đúng đắn quy định sử dụng mạng xã hội của đơn vị, kỷ luật quân đội; hiểu rõ tác hại, hậu quả của đăng tải thông tin sai trái, ảnh hưởng tư tưởng đồng chí, đồng đội, gây hoang mang trong đơn vị và gia đình.
- Thường xuyên giáo dục, quán triệt, nâng cao ý thức của quân nhân trong đơn vị đối với việc chấp hành pháp luật, kỷ luật quân đội và quy định của đơn vị trong bảo đảm an toàn thông tin, an ninh mạng. 
- Làm tốt công tác bảo vệ chính trị nội bộ; phát huy vai trò của BCĐ 35, lực lượng 47 trong đơn vị, không để xảy ra trường hợp cán bộ, QNCN sử dụng điện thoại đăng tải hình ảnh tin, bài sai trái làm ảnh hưởng đến an ninh, an toàn đơn vị, hình ảnh “Bộ đội Cụ Hồ”.
- Tổng hợp tình hình báo cáo cấp trên; tăng cường công tác thông tin định hướng tư tưởng dư luận và gia đình.
Tình huống 12: Một số sĩ quan, QNCN theo dõi trên mạng xã hội, nắm được thông tin Chính phủ cấp giấy chứng nhận sử dụng nhiều loại vắc xin, nảy sinh tư tưởng muốn lựa chọn vắc xin do nước ngoài sản xuất
* Biện pháp xử lý:
- Trao đổi thống nhất trong lãnh đạo, chỉ huy đơn vị về biện pháp xử lý.
- Nhanh chóng sinh hoạt quán triệt, giáo dục, tuyên truyền, nâng cao nhận thức của bộ đội về chủ trương của Đảng, Nhà nước, Chính phủ trong thực hiện Chiến lược tiêm vắc xin để thực hiện miễn dịch cộng đồng.
- Giáo dục cho bộ đội hiểu sâu sắc về chỉ đạo của Thủ tướng Chính phủ: “Phải tiếp cận bình đẳng tất cả các loại vắc xin, vắc xin tốt nhất là vắc xin được tiêm sớm nhất”; phản bác thông tin sai lệch trên mạng xã hội về vấn đề lựa chọn vắc xin.
- Tổng hợp các tập thể, đơn vị trong toàn quân, các địa bàn trên cả nước đã tiêm vắc xin trong nước hoặc các loại vắc xin thông qua con đường ngoại giao của nhà nước, viện trợ của quốc tế và các tổ chức vẫn đảm bảo an toàn, hiệu quả, tạo niềm tin cho bộ đội.
- Tổ chức rút kinh nghiệm nghiêm túc trong lãnh đạo, chỉ huy, đội ngũ cán bộ lãnh đạo, chỉ huy các cấp trong đơn vị và đối với toàn thể đơn vị về nhận thức và ý thức đối với chủ trương chung của Đảng, Nhà nước, Chính phủ.
Tình huống 13: Trong đơn vị có tin đồn sai sự thật về việc tiêm vắc xin ngừa Covid-19 sẽ ảnh hưởng đến sức khỏe sinh sản, thậm chí vô sinh đã gây hoang mang tư tưởng cho bộ đội.
Gợi ý biện pháp xử lý:
- Nắm tình hình, thông tin liên quan đến tin đồn sai sự thật trên.
- Hội ý cấp ủy, chỉ huy đơn vị nhận định tình hình, xác định nguồn gốc, mức độ ảnh hưởng của tin đồn và biện pháp giải quyết; báo cáo xin ý kiến chỉ đạo của cấp trên.
- Tìm hiểu xác định nguyên nhân của tin đồn sai sự thật (do quân nhân đơn vị nhận thức sai hay phần tử xấu ở bên ngoài bịa đặt) để ngăn chặn và có biện pháp xử lý kịp thời, không để lan rộng, kéo dài.
- Phân loại, nắm chắc và tiến hành tốt công tác tư tưởng đối với những đồng chí có biểu hiện hoang mang dao động.
- Tổ chức sinh hoạt đơn vị thông báo cho cán bộ, chiến sỹ biết về nguồn tin sai sự thật trên và nguồn tin chính thống về tác dụng của việc tiêm vắc xin ngừa Covid-19. Trên cơ sở đó định hướng tư tưởng, chỉ rõ sự cần thiết phải tiêm vắc xin ngừa Covid-19 cho bộ đội.
- Tăng cường công tác tuyên truyền, giáo dục nâng cao nhận thức cho bộ đội về mọi mặt; phát huy vai trò, trách nhiệm của chiến sĩ bảo vệ, Tổ ba người trong nắm tình hình chính trị nội bộ, chia sẻ, động viên lẫn nhau; kiên quyết phản bác những luận điệu sai trái, thù địch. 
 - Duy trì quản lý tốt tình hình chính trị nội bộ, giáo dục cho bộ đội nâng cao ý thức cảnh giác; chủ động phát hiện, ngăn chặn không để những thông tin xấu độc, những tư tưởng lệnh lạc xâm nhập vào trong đơn vị, giữ vững niềm tin cho bộ đội.
Tình huống 14: Một số chiến sĩ của đơn vị, khi huấn luyện gần khu cách ly có tâm lý lo sợ bị lây nhiễm, mất an toàn, không tích cực trong quá trình tham gia huấn luyện.
Gợi ý biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy đơn vị, thống nhất các biện pháp giải quyết (trong hội ý cán bộ đơn vị phản ánh, báo cáo tình hình tư tưởng, tâm trạng của số hạ sĩ quan, chiến sĩ có biểu hiện băn khoăn, lo lắng).
- Chỉ đạo sinh hoạt các tổ chức; tuyên truyền các tài liệu của cấp trên cho cán bộ, chiến sĩ nâng cao hiểu biết về loại vi rút và các biến thể của vi rút.
- Chỉ đạo lực lượng quân y đơn vị giải thích về khả năng lây nhiễm của vi rút trong từng điều kiện môi trường, khoảng cách để bộ đội yên tâm tham gia huấn luyện.
- Tiến hành tốt các biện pháp về công tác bảo đảm an toàn trong phòng, chống đại dịch.
- Phân công cán bộ theo dõi, động viên, ổn định tư tưởng, tâm lý cho  chiến sĩ trong quá trình huấn luyện.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 15: Chiến sĩ huấn luyện tại khu vực gần nơi cách ly có biểu hiện nóng, sốt và ngất xỉu gây hoang mang trong đơn vị; vì trước đó có tiếp xúc với người bị nhiễm bệnh (không có triệu trứng).
Gợi ý biện pháp xử lý:
- Kịp thời báo quân y về triệu trứng của chiến sĩ; đồng thời, có biện pháp cách ly, để bảo đảm an toàn cho đơn vị.
- Căn cứ vào hướng dẫn của các cơ quan truyền thông, kinh nghiệm xử lý các tình huống bị nhiễm bệnh trước đó, xử lý các tình huống ban đầu, nếu nhiễm bệnh nặng tiến hành ngay các biện pháp sơ cứu, chấp hành tốt công tác bảo đảm an toàn tránh lây lan dịch trong đơn vị.
- Kịp thời báo cáo Ban chỉ đạo phòng, chống dịch; xử lý, tập trung ổn định đội hình đơn vị, giải thích động viên tư tưởng bộ đội.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 16: Chiến sĩ trong Đại đội A có bố, mẹ và em phát hiện bị nhiễm loại vi rút mới, cả nhà phải đi cách ly, điều trị tập trung.
* Biện pháp xử lý:
- Hội ý, trao đổi trong cấp ủy, chỉ huy đại đội, thống nhất cách xử lý; phân công cán bộ đơn vị gặp gỡ, động viên chiến sĩ; báo cáo, xin ý kiến chỉ đạo của chỉ huy cấp trên.
- Chính trị viên đại đội, trung đội trưởng gặp gỡ quân nhân để nắm rõ hơn tình hình gia đình; ổn định tâm lý; giáo dục phân tích cho quân nhân thấy rõ các quy định phòng, chống dịch của đơn vị, địa phương; động viên quân nhân an tâm công tác.
- Cán bộ đại đội, tiểu đoàn gọi điện hỏi thăm, động viên gia đình chiến sỹ; chia sẻ các biện pháp tăng cường chăm sóc sức khỏe và điều trị bệnh. 
- Tạo điều kiện cho chiến sỹ thường xuyên gọi điện cho người thân trong gia đình, nhờ họ hàng, bạn bè... chăm lo, chia sẻ, hỗ trợ những khó khăn về vật chất, tinh thần cho người thân quân nhân thời gian điều trị.
- Các cấp xem xét, đề nghị trợ cấp khó khăn cho quân nhân trong điều kiện, khả năng của đơn vị.
- Phân công cán bộ, tiểu đội trưởng thường xuyên quan tâm nắm tâm tư, nguyện vọng và động viên quân nhân tích cực tham gia các hoạt động của đơn vị. Phát huy vai trò của chi đoàn, HĐQN, chiến sĩ dân vận, chiến sĩ bảo vệ, bạn bè, đồng đội thân thiết để gần gũi, chia sẻ, động viên tư tưởng tránh biểu hiện buồn chán, bi quan, ảnh hưởng đến công tác và chấp hành kỷ luật.
- Nắm chắc mọi diễn biến liên quan đến quân nhân và gia đình quân nhân để báo cáo cấp trên, xin ý kiến chỉ đạo giải quyết các vấn đề phát sinh theo quy định.
Tình huống 17: Trong thời gian thực hiện giãn cách xã hội theo Chỉ thị của Chính phủ. Quân nhân của đơn vị có thân nhân bị nhiễm bệnh tử vong, quân nhân lên báo cáo với chỉ huy đơn vị xin nghỉ phép để về viếng thân nhân.
- Hội ý cấp ủy, chỉ huy đại đội đánh giá tình hình, nắm chắc hoàn cảnh gia đình quân nhân, phân công cán bộ thường xuyên động viên tư tưởng, thống nhất biện pháp giúp đỡ quân nhân. Báo cáo lên chỉ huy cấp trên.
- Thống nhất trong chỉ huy đại đội: Phân công Chính trị viên đại đội gặp gỡ quân nhân để nắm rõ hơn tình hình, nguyện vọng của quân nhân và gia đình quân nhân.
- Thực hiện chỉ đạo của chỉ huy đơn vị: 
+ Chỉ huy cơ quan chính trị trực tiếp gặp gỡ, động viên chiến sĩ, nắm tình hình và động viên, thường xuyên chia sẻ với gia đình quân nhân; phân tích cho chiến sĩ và gia đình quân nhân những khó khăn, quy định của địa phương tổ chức tang lễ trong điều kiện diễn biến phức tạp; sự lây lan của dịch bệnh... (Địa phương sẽ tổ chức hỏa táng, không được tổ chức tang lễ đông người, mọi hoạt động đều phải chấp hành nghiêm quy định phòng dịch). Động viên chiến sĩ ở tại đơn vị, khi nào dịch bệnh ổn định, đơn vị sẽ tạo điều kiện để chiến sĩ về động viên gia đình và thắp nhang cho bố.
+ Chỉ huy cơ quan tham mưu liên lạc, phối hợp với ban chỉ huy quân sự quận, huyện (xã, phường) địa phương nơi gia đình quân nhân cư trú để giúp đỡ, hỗ trợ lo hậu sự cho bố quân nhân trong điều kiện cho phép.
- Tạo điều kiện cho chiến sĩ thường xuyên gọi điện cho người thân trong gia đình, nhờ họ hàng, bạn bè... gúp đỡ gia đình lo hậu sự trong điều kiện phòng chống dịch bệnh.
- Chỉ huy đơn vị; cán bộ, nhân viên, chiến sỹ trong đơn vị thăm hỏi, động viên, chia buồn mất mát với gia đình quân nhân và quân nhân bằng tình cảm chân thành nhất, thể hiện sâu đậm tình đồng chí đồng đội.
- Các cấp xét, đề nghị và trao trợ cấp khó khăn cho quân nhân.
- Báo cáo và đề xuất ý kiến chỉ đạo của cấp trên; lập bàn thờ bái vong tại đơn vị để các tổ chức, quân nhân đến thăm hỏi, chia buồn.
- Thông qua sinh hoạt, học tập, giao ban, hệ thống truyền thanh nội bộ... để kịp thời biểu dương việc khắc phục khó khăn, vượt qua sự mất mát người thân của chiến sĩ ở lại đơn vị, chấp hành nghiêm kỷ luật, phấn đấu hoàn thành tốt nhiệm vụ của quân nhân.
- Phân công cán bộ tiếp tục quan tâm nắm tâm tư, nguyện vọng và động viên quân nhân tích cực tham gia các hoạt động của đơn vị. Phát huy vai trò của chi đoàn, HĐQN, chiến sĩ dân vận, chiến sĩ bảo vệ, bạn bè, đồng đội thân thiết để gần gũi, chia sẻ, động viên tư tưởng tránh biểu hiện buồn chán, bi quan, ảnh hưởng đến công tác và chấp hành kỷ luật.
- Sau khi hết thực hiện giãn cách theo Chỉ thị của Chính phủ, căn cứ vào tình hình dịch và nhiệm vụ của đơn vị để đề nghị cấp trên giải quyết tranh thủ, hoặc chế độ phép cho quân nhân về thăm gia đình.
- Chỉ huy đại đội thường xuyên tổng hợp tình hình liên quan, báo cáo, xin ý chỉ huy cấp trên để kịp thời xử lý các vấn đề phát sinh.
Tình huống 18: Đơn vị lần đầu tiên nhận nhiệm vụ tham gia hỗ trợ nhân dân địa phương trong trong vùng dịch có nhiều ca nhiễm và nhiều người chết do nhiễm vi rút mới, một số chiến sĩ đã có biểu hiện băn khoăn, lo lắng
Gợi ý biện pháp xử lý: 
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng và việc chấp hành kỷ luật của chiến sĩ trong thời gian qua. Nắm vững tình hình tâm tư, nguyện vọng của chiến sĩ tham gia thực hiện nhiệm vụ để tham mưu cho cấp ủy, chỉ huy có biện pháp khắc phục.
- Gặp gỡ chiến sĩ có tâm lý lo lắng, giải thích rõ khi làm nhiệm vụ đơn vị đã có đủ các biện pháp bảo đảm an toàn (khẩu trang, tiêm vaccine, mặc quần áo bảo hộ, cách ly, theo dõi sức khỏe thường xuyên…) và khi thực hiện nhiệm vụ đã là quân nhân việc sẵn sàng hy sinh cho nhân dân, đất nước vừa là vinh dự vừa là trách nhiệm; xây dựng ý chí quyết tâm hoàn thành tốt nhiệm vụ được giao trong mọi hoàn cảnh.
- Thường xuyên giáo dục, tuyên truyền cho chiến sĩ nâng cao ý thức trách nhiệm, khắc phục khó khăn trong thực hiện nhiệm vụ, chấp hành nghiêm các biện pháp phòng, chống dịch.
- Chủ động bồi dưỡng kinh nghiệm, tổ chức luyện tập thường xuyên các phương án dập dịch cho quân nhân và phân đội, nhất là các quy tắc bảo đảm an toàn trong thực hiện nhiệm vụ
- Thường xuyên bổ sung các trang bị, vật dụng bảo đảm an toàn trong thực hiện nhiệm vụ (quần áo bảo hộ, khẩu trang…).
- Bảo đảm đúng, đủ tiêu chuẩn, chế độ chính sách cho chiến sĩ yên tâm trong thực hiện nhiệm vụ.
- Tổ chức sinh hoạt  rút kinh nghiệm sau mỗi lần thực hiện nhiệm vụ để chiến sĩ tự tin hơn trong quá trình thực hiện nhiệm vụ. Biểu dương, khen thưởng tập thể, cá nhân tham gia phòng, chống dịch.
- Thường xuyên nắm chắc tình hình đơn vị báo cáo trên theo quy định.
Tình huống 19: Khi nắm được thông tin đơn vị chuẩn bị nhận nhiệm vụ hành quân đến bệnh viện dã chiến để hỗ trợ các y, bác sĩ cứu chữa người bị dương tính với loại virut mới, một số cán bộ chiến sĩ có biểu hiện hoang mang, lo lắng, dao động về tư tưởng... 
Gợi ý biện pháp xử lý:
- Trao đổi thống nhất trong lãnh đạo, chỉ huy đơn vị về biện pháp xử lý. Nhanh chóng sinh hoạt quán triệt, giáo dục nâng cao nhận thức của cán bộ, chiến sĩ trong đơn vị hiểu sâu sắc về trách nhiệm của Quân đội nói chung, đơn vị nói riêng trong thực hiện chức năng đội quân công tác, phòng, chống dịch bệnh, giúp đỡ nhân dân; mục đích, ý nghĩa và tầm quan trọng của nhiệm vụ được giao.
- Đánh giá, phân loại tư tưởng cán bộ, chiến sĩ; phân công cán bộ gặp gỡ số chiến sĩ có biểu hiện tư tưởng dao động để nắm chắc tình hình và động viên bộ đội xác định rõ trách nhiệm được giao; khơi dậy tinh thần tham gia phòng, chống dịch vì cuộc sống của cộng đồng, của quê hương, của gia đình; kịp thời ngăn chặn những biểu hiện tư tưởng ngại khó, ngại khổ... chủ động định hướng, giải quyết, ổn định tình hình đơn vị.
- Đẩy mạnh công tác tuyên truyền, thông qua các phong trào thi đua của Chính phủ, Quân đội chung tay đẩy lùi dịch bệnh; các câu chuyện, video clip trực quan về các tấm gương sẵn sàng vì nhân dân không quản ngại khó khăn, gian khổ; những tình cảm yêu mến của nhân dân với “Bộ đội Cụ Hồ” và những việc làm ý nghĩa của các cơ quan, đơn vị toàn quân trong thời gian qua...
- Đề nghị cấp trên bồi dưỡng, tập huấn phương pháp phòng, chống dịch bệnh, bảo đảm an toàn; đơn vị tự bồi dưỡng cho cán bộ, chiến sĩ những kinh nghiệm qua thực tế, tạo niềm tin tưởng, yên tâm khi nhận nhiệm vụ.
- Tổ chức phát động đợt thi đua cao điểm, đột kích, để cán bộ, chiến sĩ hứa hẹn, ký kết giao ước thi đua, góp phần hoàn thành xuất sắc nhiệm vụ được giao.
- Quá trình thực hiện nhiệm vụ, tiếp tục đẩy mạnh các hoạt động thi đua, tuyên truyền; thường xuyên gần gũi với bộ đội, nhất là bộ phận khó khăn, phức tạp, thực hiện nhiệm vụ nhỏ lẻ, độc lập; nắm chắc tâm tư tình cảm và chia sẻ những khó khăn vất vả, khơi gợi niềm vinh dự tự hào khi được thực hiện nhiệm vụ.
Tình huống 20: Cán bộ, chiến sỹ thực hiện nhiệm vụ đặc thù (quân bưu, hậu cần...) buộc phải qua địa bàn có dịch diễn biến phức tạp, các địa phương thành lập chốt kiểm soát và duy trì, kiểm tra nghiêm ngặt người và phương tiện đi qua; nguy cơ nhiễm bệnh cao.
Gợi ý biện pháp xử lý:
- Chi ủy phải xác định các chủ trương, biện pháp lãnh đạo thực hiện nhiệm vụ sát thực tiễn, chỉ huy đơn vị đánh giá nguy cơ lây dịch bệnh, thống nhất biện pháp thực hiện nhiệm vụ, phân công cán bộ giáo dục, động viên tư tưởng; cán bộ huấn luyện bổ sung và chuẩn bị các vật chất để thực hiện nhiệm vụ; báo cáo cấp trên xin ý kiến chỉ đạo.
- Chính trị viên đại đội trực tiếp giáo dục, động viên cán bộ, chiến sỹ nhận thức sâu sắc nhiệm vụ; quyết tâm khắc phục khó khăn, bảo đảm tốt công tác phục vụ trong mọi tình huống. Trực tiếp gặp gỡ, đối thoại, tìm hiểu nắm tư tưởng, đặc biệt là biểu hiện lo sợ, do dự khi thực hiện nhiệm vụ hay không; giáo dục, động viên chiến sĩ có nhận thức đúng, không nên lo lắng, ngại khó khăn để thoái thác nhiệm vụ; động viên quân nhân tin tưởng và chấp hành các quy định trong phòng chống dịch.
- Tổ chức tốt hoạt động thi đua khắc phục khó khăn, quyết tâm hoàn thành nhiệm vụ trong toàn đơn vị. 
- Tổ chức chặt chẽ, nghiêm túc việc triển khai tổ chức thực hiện nhiệm vụ, thực hiện nghiêm các biện pháp phòng chống dịch (Bảo đảm cho 100% quân nhân thực hiện nhiệm vụ ngoài doanh trại đã được tiêm vaccine và tuân thủ đầy đủ các biện pháp bảo đảm phòng, chống dịch, hạn chế thấp nhất các nguy cơ lây nhiễm. Đồng thời, thực hiện các biện pháp phòng, chống dịch, khử khuẩn sau từng lượt, từng buổi công tác về đơn vị. Khi hoàn thành nhiệm vụ trở về đơn vị các phương tiện đều được phun khử khuẩn các phương tiện; bố trí ăn, nghỉ khu riêng cho cán bộ, chiến sĩ để hạn chế tiếp xúc, thực hiện phòng chống dịch ở mức cao hơn). 
- Tổ chức sinh hoạt đơn vị để giáo dục, tuyên truyền nâng cao hiểu biết, nhận thức về dịch bệnh và các biện pháp phòng, chống dịch; rút kinh nghiệm chung và động viên cán bộ, chiến sĩ xác định tư tưởng, trách nhiệm, khắc phục khó khăn, hoàn thành tốt nhiệm vụ được giao. 
- Phân công cán bộ theo dõi, giúp đỡ, động viên chiến sĩ trong quá trình thực hiện nhiệm vụ. Kịp thời nắm bắt và giải quyết tốt các tư tưởng nảy sinh trong quá trình thực hiện nhiệm vụ.
Tình huống 21: Trong điều kiện thực hiện giãn cách xã hội Chỉ thị của Thủ tưởng Chính phủ, đơn vị cấm trại dài ngày để phòng, chống dịch; có một số quân nhân trong đơn vị có biểu hiện nảy sinh tâm lý chủ quan, cho rằng đơn vị đã cấm trại lâu ngày, cách ly với bên ngoài nên buông lỏng, đơn giản trong thực hiện các quy định phòng, chống dịch.
Gợi ý biện pháp xử lý:
- Trao đổi trong cấp ủy, chỉ huy đơn vị, đánh giá tình hình tư tưởng của các quân nhân trong đơn vị, thống nhất biện pháp giải quyết, phân công cấp ủy viên phụ trách; báo cáo cấp trên xin ý kiến chỉ đạo.
- Tổ chức sinh hoạt đơn vị, trực tiếp đối thoại, tìm hiểu xác định rõ nguyên nhân, nắm tư tưởng của bộ đội, đặc biệt là các quân nhân có biểu hiện tâm lý chủ quan. Phân tích làm rõ tác hại của việc buông lỏng, thực hiện không nghiêm các quy định phòng dịch đối với từng quân nhân và toàn đơn vị để mọi quân nhân xác định lại trách nhiệm trong thực hiện.
- Tiếp tục tổ chức quán triệt lại các quy định của Chính phủ, cấp trên về phòng, chống dịch; các quy định tổ chức bảo đảm an toàn trong sẵn sàng chiến đấu, huấn luyện, sinh hoạt trong điều kiện thực hiện giãn cách xã hội để phòng, chống dịch theo Chỉ thị của Thủ tướng Chính phủ.
- Duy trì nghiêm nền nếp huấn luyện, sinh hoạt, chế độ chính quy phù hợp với trạng thái phòng, chống dịch đã được cấp trên quy định theo từng cấp độ. Xử lý nghiêm theo điều lệnh các quân nhân thực hiện không nghiêm các quy định phòng, chống dịch của đơn vị.
- Phát huy tác dụng của các thiết chế văn hóa, hệ thống website, truyền thanh nội bộ kịp thời lan tỏa những tấm gương tốt, những cách làm hay, mô hình hiệu quả trong phòng chống dịch bệnh; đồng thời phê bình, chấn chỉnh các biểu hiện tư tưởng lệch lạc, chủ quan trong phòng chống dịch.
- Giáo dục cho cán bộ, chiến sĩ tự rèn luyện, nâng cao sức khỏe, bảo đảm đời sống văn hóa, tinh thần lành mạnh, sẵn sàng thực hiện tốt các nhiệm vụ được giao.
- Phát huy vai trò các tổ chức thanh niên, HĐQN, chiến sĩ dân vận, chiến sĩ bảo vệ; phân công cán bộ để chia sẻ, động viên tư tưởng tránh biểu hiện buồn chán, bi quan; dẫn đến vi phạm kỷ luật, vi phạm quy định của đơn vị.
- Tổng hợp tình hình, báo cáo cấp trên theo quy định.
Tình huống 22: Một số cán bộ, chiến sĩ sau một thời gian dài thực hiện nhiệm vụ tại các chốt phòng, chống dịch Covid-19 trên biên giới có biểu hiện chủ quan, thiếu quyết tâm, lơ là trong thực hiện nhiệm vụ.
* Gợi ý biện pháp xử lý
- Cấp ủy, ban chỉ huy đơn vị rà soát nắm tình hình, kết quả thực hiện nhiệm vụ của cán bộ, chiến sĩ; tìm hiểu tâm lý, cũng như nguyên nhân tác động đến suy nghĩ của cán bộ, chiến sĩ dẫn đến có biểu hiện chủ quan thiếu quyết tâm trong quá trình thực hiện nhiệm vụ được giao, như: Điều kiện ăn, ở, sinh hoạt; hoàn cảnh gia đình; các mối quan hệ xã hội; đời sống tình cảm… 
- Phân công cấp ủy, ban chỉ huy đơn vị gặp gỡ, nắm tâm tư, nguyện vọng của cán bộ, chiến sĩ làm nhiệm vụ tại các chốt chống dịch để có biện pháp giáo dục, động viên, giúp đỡ chấn chỉnh kịp thời thái độ, tinh thần trong thực hiện chức trách, nhiệm vụ được giao.
- Dự kiến nội dung, biện pháp giải quyết những nảy sinh tư tưởng chủ quan, lơ là, thiếu quyết tâm; tổ chức sinh hoạt bộ phận và đơn vị quán triệt các văn bản của các cấp về công tác phòng, chống dịch Covid-19; tính chất nguy hiểm của dịch bệnh đối với sức khỏe và tính mạng con người; xác định nhiệm vụ phòng, chống dịch của lực lượng BĐBP là nhiệm vụ chính trị được Đảng, Nhà nước, Quân đội giao và vì Nhân dân phục vụ. Từ đó, xây dựng niềm tự hào ý thức trách nhiệm và tinh thần cảnh giác để quyết tâm khắc phục, khó khăn tiếp tục thực hiện nhiệm vụ được giao.
- Phân công nhiệm vụ cho các đồng chí chốt trưởng, bộ phận trưởng, cán bộ, đảng viên gần gũi, quan tâm, giúp đỡ, động viên các đồng chí trong quá trình thực hiện nhiệm vụ được giao; đồng thời thay mặt đơn vị, chỉ huy kết nối, động viên, thuyết phục như: Thăm hỏi gia đình, người thân quân nhân.
- Tăng cường giáo dục truyền thống Quân đội, lực lượng và đơn vị, đẩy mạnh thực hiện các phong trào thi đua trong đơn vị; tổ chức thực hiện tốt công tác tuyên truyền gương người tốt, việc tốt; nhân điển hình tiên tiến trong đơn vị.
- Duy trì nghiêm túc nền nếp, chế độ sinh hoạt, học tập, công tác theo quy định của cấp trên về từng trạng thái phòng, chống dịch bệnh; vận dụng linh hoạt trong giải quyết chế độ phép, nghỉ tranh thủ để cán bộ, chiến sĩ luân phiên được nghỉ tranh thủ, có điều kiện giải quyết công việc gia đình, bản thân. 
- Cấp ủy, chỉ huy đơn vị thường xuyên quan tâm động viên về vật chất và tinh thần cho cán bộ, chiến sĩ tại các chốt chống dịch; thực hiện tốt công tác chính sách, hậu phương Quân đội. 
- Xử lý nghiêm các trường hợp không hoàn thành nhiệm vụ, vi phạm các quy định trong quá trình thực hiện nhiệm vụ. 
Tình huống 23: Các quân nhân trong quá trình cách ly tập trung, sau khi xét nghiệm sáng lọc; thì phát hiện ra có 01 quân nhân dương tính với loại vi rút mới; làm cho cán bộ, chiến sĩ trong đơn vị nhiều đồng chí hoang mang, lo lắng.
Gợi ý biện pháp xử lý:
- Hội ý lãnh đạo, chỉ huy đơn vị báo cáo với cấp trên xin ý kiến chỉ đạo.
- Động viên tư tưởng quân nhân bị nhiễm và cán bộ, chiến sĩ trong đơn vị bình tĩnh, tự tin, tránh hoang mang dao động, tin tưởng vào công tác phòng, chống dịch tại khu cách ly và hiệu quả của vắcxin được tiêm.
- Kịp thời nắm bắt tư tưởng bộ đội, có những biện pháp xử lý phù hợp, ngăn chặn, xử lý các thông tin, dư luận gây hoang mang làm ảnh hưởng đến tư tưởng của cán bộ, chiến sĩ trong đơn vị.
- Lãnh đạo, chỉ huy đơn vị thường xuyên quan tâm, động viên thăm hỏi, chia sẻ những khó khăn, vướng mắc của quân nhân, đồng thời tạo điều kiện để quân nhân mắc loại vi rút mới có tinh thần tốt nhất trong điều trị bệnh. 
- Tổ chức bình xét khen thưởng các quân nhân đã hoàn thành nhiệm vụ tham gia trực tiếp trên tuyến đầu phòng, chống dịch.
Tình huống 24: Đơn vị nằm trong khu vực phải thực hiện giãn cách xã hội theo Chỉ thị của Chính phủ; đơn vị thực hiện nhiệm vụ sản xuất kinh doanh có hiện tượng sản xuất cầm chừng, xuất hiện luồng tư tưởng lo lắng vì thu nhập thấp.
Gợi ý biện pháp xử lý:
- Quán triệt sâu kỹ các văn bản, chỉ thị, hướng dẫn các cấp; triển khai tăng cường công tác tuyên truyền, giáo dục phòng, chống đại dịch. Qua đó giúp cán bộ, người lao động hiểu rõ về dịch bệnh và các biện pháp phòng, chống. Đẩy mạnh công tác tuyên truyền phòng, chống dịch trên hệ thống truyền thanh nội bộ, panô, băng zôn, khẩu hiệu; lồng ghép vào các buổi sinh hoạt, học tập, huấn luyện; thường xuyên cập nhật thông tin, diễn biến tình hình dịch bệnh kết hợp với định hướng tư tưởng cho người lao động.
- Ra nghị quyết chuyên đề của cấp ủy lãnh đạo thực hiện nhiệm vụ phòng,  chống dịch; cùng với những xây dựng kế hoạch, phương án được chủ động xây dựng, sẵn sàng xử trí mọi tình huống giúp cán bộ, người lao động trong quá trình sản xuất kinh doanh; không hoang mang, lo lắng trong phòng, chống dịch. 
- Các cấp ủy, tổ chức đảng, cơ quan, đơn vị trong các đơn vị sản xuất kinh doanh làm tốt công tác giáo dục chính trị, giáo dục truyền thống cho người lao động; chủ động, sáng tạo thực hiện các biện pháp phòng, chống dịch bệnh.
- Làm tốt công tác dự báo, chủ động xây dựng các phương án, kế hoạch sản xuất kinh doanh, hoạt động CTĐ, CTCT phù hợp với tình hình thực tế của từng cấp độ dịch; nắm chắc tình hình địa bàn, chủ động triển khai hoạt động sản xuất, kinh doanh bảo đảm phù hợp với quy định phòng, chống dịch; tích cực tham gia sản xuất, bảo đảm an sinh xã hội, đời sống của cán bộ, nhân viên người lao động phục vụ công cuộc, góp phần ổn định chính trị, phát triển kinh tế, văn hóa, xã hội của đất nước.
- Đẩy mạnh thực hiện tốt các phong trào thi đua, hướng vào khắc phục khâu yếu, việc khó, vươn lên hoàn thành xuất sắc nhiệm vụ phòng chống dịch; các cơ quan, đơn vị đề cao tinh thần trách nhiệm, tích cực hưởng ứng Lời kêu gọi Đảng, Nhà nước phát động. Các cơ quan, đơn vị đẩy mạnh thực hành tiết kiệm góp phần tạo nguồn lực để tập trung chống dịch, bảo đảm an sinh xã hội, chăm lo sức khỏe và đời sống cho người lao động, đặc biệt là đối tượng hoàn cảnh khó khăn. Các cấp ủy, tổ chức đảng trong đơn vị SXKD quán triệt và tổ chức triển khai thực hiện nghiêm túc, quyết liệt, sáng tạo hiệu quả những nội dung thi đua của Chính phủ và các cấp phát động.
Tình huống 25: Đồng chí B là Học viên tăng cường cho đồn Biên phòng X, đang thực hiện nhiệm vụ tại chốt phòng, chống dịch trên biên giới. Tuy nhiên, đồng chí thường xuyên có biểu hiện trầm tư; qua tìm hiểu, một số cán bộ, chiến sĩ cùng chốt cho biết, đồng chí B thường sử dụng điện thoại để lên facebook chia sẻ về những khó khăn vất vả trong thực hiện nhiệm vụ phòng, chống dịch và đã nhận được nhiều bình luận trái chiều khác nhau liên quan đến việc thực hiện nhiệm vụ phòng, chống dịch.
Gợi ý Biện pháp xử lý:
- Hội ý chỉ huy đơn vị để thống nhất biện pháp giải quyết; phân công cán bộ phụ trách.
- Kiểm tra, nắm lại số chiến sĩ sử dụng điện thoại không đúng quy định trong đơn vị, xác định nguyên nhân và trách nhiệm của cán bộ quản lý trong việc thực hiện quy định về việc Hạ sĩ quan, chiến sĩ không được sử dụng điện thoại di động trong thời gian tại ngũ.
- Tiến hành gặp gỡ đồng chí B để nắm tình hình cụ thể. Phân tích để đồng chí thấy được việc chiến sĩ tự ý sử dụng điện thoại di động trong thời gian thực hiện nhiệm vụ là sai với quy định của đơn vị, việc chia sẻ hoạt động quân sự trên facebook là vi phạm quy định, làm lộ lọt bí mật quân sự (facebook là diễn đàn tự do, ý kiến bình luận khác nhau, trong đó có nhiều ý kiến tiêu cực, tác động xấu đến nhận thức tư tưởng của chiến sĩ); động viên chiến sĩ cần nghiêm túc rút kinh nghiệm; yêu cầu đồng chí B gỡ bỏ ngay những nội dung đã đăng tải có liên quan đến Quân đội, BĐBP và đơn vị, chấm dứt ngay việc làm trên; yêu cầu chiến sĩ B gửi điện thoại về nhà hoặc gửi cho chỉ huy đơn vị giữ hộ.
- Chỉ đạo đơn vị tổ chức cho chiến sĩ vi phạm quy định về sử dụng điện thoại di động viết tường trình, kiểm điểm; tiến hành sinh hoạt đơn vị kiểm điểm theo phân cấp (căn cứ vào tính chất, mức độ để nhắc nhở, giải quyết phù hợp); đồng thời yêu cầu mọi quân nhân trong đơn vị rút kinh nghiệm, tự giác chấp hành nghiêm quy định của đơn vị. 
- Cấp uỷ, chỉ huy đơn vị sinh hoạt rút kinh nghiệm, tăng cường công tác bảo vệ chính trị nội bộ; phân công đảng viên theo dõi, giúp đỡ học viên an tâm công tác, hoàn thành tốt nhiệm vụ. 
Tình huống 26: Một số quân nhân đang làm nhiệm vụ trên tàu chưa yên tâm trong thực hiện nhiệm tuần tra, kiểm tra, kiểm soát ngăn chặn người xuất, nhập cảnh trái phép bằng đường biển trong phòng, chống đại dịch.
Gợi ý biện pháp xử lý:
- Chỉ huy tàu phải kịp thời tìm hiểu, nắm thực chất tư tưởng của số quân nhân chưa yên tâm trong thực hiện nhiệm vụ phòng, chống đại dịch.
- Trao đổi với cấp ủy, tranh thủ ý kiến của các ngành (bộ phận) để phân tích, thống nhất nhận định, đánh giá, phân loại tư tưởng, xác định rõ nguyên nhân của số quân nhân chưa yên tâm thực hiện nhiệm vụ phòng, chống dịch (sợ bị lây nhiễm dịch từ những người xuất, nhập cảnh trái phép, sợ khó khăn vất vả, do tác động của mặt trái cơ chế thị trường…). Sơ bộ báo cáo cấp trên, đề xuất biện pháp tiến hành công tác tư tưởng. 
- Gặp gỡ, giáo dục, động viên nâng cao nhận thức, trách nhiệm cho cán bộ, chiến sĩ trên tàu, đặc biệt tập trung vào số quân nhân chưa yên tâm thực hiện nhiệm vụ. Trong đó chủ yếu, trọng tâm là giáo dục động cơ, mục tiêu lý tưởng phấn đấu, các quy định, biện pháp bảo đảm an toàn trong phòng, chống dịch; trình độ và khả năng cứu chữa của đội ngũ y, bác sỹ…, giáo dục truyền thống, nhiệm vụ quân đội, lực lượng; các gương điển hình tiên tiến trong tham gia phòng, chống dịch của đơn vị, lực lượng và toàn quân.
- Giải quyết thoả đáng kịp thời những khó khăn, vướng mắc trong điều kiện khả năng cho phép của tàu.
- Tăng cường đối thoại trực tiếp, xây dựng môi trường lành mạnh, bầu không khí dân chủ, đoàn kết thống nhất, thương yêu, giúp đỡ nhau. Tạo điều kiện để các đồng chí đó tích cực tham gia vào các hoạt động chung của tàu.
- Phát huy vai trò của tổ chức đoàn, hội đồng quân nhân để động viên, thuyết phục giúp đỡ các quân nhân yên tâm công tác.
- Phối hợp, cùng với gia đình, người thân, bạn bè, đồng hương để tác động giải quyết các vướng mắc trong nhận thức và tư tưởng.
- Phân công các đồng chí trưởng ngành (trưởng bộ phận) thường xuyên theo dõi, giúp đỡ cảm hoá, động viên, nắm diễn biến tư tưởng, hành động của quân nhân chưa yên tâm công tác, kịp thời báo cáo chỉ huy tàu.
- Chỉ huy tàu thường xuyên sâu sát, quản lý tốt tình hình tư tưởng bộ đội, kịp thời có biện pháp sát, đúng, trúng giải quyết dứt điểm các vấn đề nảy sinh về tư tưởng trong quá trình thực hiện nhiệm vụ, đồng thời động viên, khích lệ khi các đồng chí đó có chuyển biến tiến bộ.
- Kết thúc nhiệm vụ, kịp thời ổn định mọi mặt, sẵn sàng nhận nhiệm vụ tiếp theo khi có lệnh; tổng hợp tình hình báo cáo chỉ huy hải đội theo quy định.
Tình huống 27: Cán bộ trẻ, có gia đình riêng ở Hà Nội, bố mẹ hai bên (bên chồng và bên vợ) đều ở quê (xa Hà Nội từ 120-300km), vợ mới sinh con được 3 tháng (phải mổ đẻ), con thứ nhất còn nhỏ mới được 3 tuổi, hiện chồng là người chăm sóc, lo toan chính các công việc trong nhà; nhận nhiệm vụ đi miền Nam tham gia phòng chống dịch.
Gợi ý biện pháp xử lý:
- Trước khi lập danh sách cử cán bộ đó đi công tác miền Nam; lãnh đạo, chỉ huy đã tiến hành rà soát toàn bộ cán bộ trong cơ quan để lập danh sách cán bộ tham gia chỉ thị của cấp trên.
- Khi cán bộ có tình huống trên được cử đi công tác, đã được lãnh đạo, chỉ huy gặp riêng, thăm dò nắm bắt nguyện vọng; đồng chí đã nhất trí nhận nhiệm vụ, nhưng có báo cáo tình hình hiện tại của gia đình.
- Lãnh đạo, chỉ huy cơ quan đã đưa ra những gợi ý, phương án giải quyết; đồng chí cán bộ đã đưa ra được phương án nhờ gia đình bên ngoại ra giúp đỡ gia đình khi đi công tác xa nhà.
- Kết quả đồng chí cán bộ đã nhận nhiệm vụ, lên đường và hiện đang công tác tại một tổ quân y lưu động tại một quận ở thành phố Hồ Chí Minh.
- Chỉ huy cơ quan có phương án thăm hỏi, động viên cán bộ và gia đình cán bộ.
- Kết thúc đợt công tác, thông qua kết quả hoàn thành nhiệm vụ của cá nhân, triển khai bình xét, khen thưởng, biểu dương thành tích trước cơ quan, đơn vị.
- Tiến hành rút kinh nghiệm chung những vấn đề đạt được và chưa đạt được của các đội công tác.
Tình huống 28: Đơn vị tiếp nhận công dân từ nước ngoài về cách ly y tế tập trung. Do điều kiện sống ở nước ngoài đầy đủ tiện nghi, nhưng khi về đến đơn vị, một số công dân không thích nghi được với điều kiện cơ sở vật chất trong khu cách ly và đòi hỏi quá mức, không tôn trọng tập thể. Khi đơn vị không đáp ứng được những yêu cầu thì đã có những hành vi gây rối mất trật tự trong khu cách ly.
Gợi ý biện pháp xử lý:
- Nắm chắc tình hình đơn vị, hội ý lãnh đạo, chỉ huy bàn biện pháp giải quyết; báo cáo lên cấp trên; thông báo tình hình cho cấp ủy, chính quyền và lực lượng làm nhiệm vụ bảo đảm an ninh, trật tự trên địa bàn.
- Rà soát phân loại đối tượng, xác định người lôi kéo và người bị lôi kéo. Phân công cán bộ tiếp xúc với những người lôi kéo, cầm đầu, người có uy tín, giải thích tính ưu việt của Đảng, Nhà nước Việt Nam trong việc tạo điều kiện cho công dân đang học tập, công tác và định cư ở nước ngoài về nước phòng, chống dịch bệnh; phân tích rõ những thuận lợi, khó khăn và kết quả các lần tiếp nhận, cách ly công dân của đơn vị.
- Lắng nghe, tiếp thu ý kiến của công dân; đáp ứng các nhu cầu chính đáng của công dân trong điều kiện cho phép của đơn vị; động viên bộ phận phục vụ tăng cường chế biến món ăn bảo đảm vệ sinh, hợp khẩu vị theo chế độ, quy định hiện hành. Tạo điều kiện để công dân tham gia giám sát việc bảo đảm chế độ tiêu chuẩn và tiếp cận lực lượng phục vụ để công dân tận mắt chứng kiến việc cán bộ, chiến sĩ đơn vị khắc phục khó khăn, hết lòng vì nhân dân phục vụ.
- Phổ biến và quán triệt lại toàn bộ các tiêu chuẩn, chế độ cũng như điều kiện của đơn vị trong phục vụ cách ly công dân; để mọi người nắm được và chấp hành nghiêm các quy định của đơn vị, không làm ảnh hưởng đến lực lượng phục vụ cũng như các công dân khác.
- Chỉ đạo lực lượng quân y làm tốt công tác thăm, khám, lấy mẫu xét nghiệm; gắn quá trình thực hiện nhiệm vụ với việc trò chuyện cùng công dân, lắng nghe, tiếp thu ý kiến để trao đổi, báo cáo lại với chỉ huy đơn vị; thường xuyên nắm chắc diễn biến về tâm lý, tư tưởng của công dân.
- Phát huy vai trò của các thiết chế văn hóa, mạng truyền thanh nội bộ và các trang, nhóm Facebook của đơn vị trong việc tuyên truyền thường xuyên về tình hình dịch bệnh, ý thức trách nhiệm của cán bộ, chiến sĩ, tính ưu việt của chế độ XHCN, chế độ được hưởng…(có thể mời các công dân có uy tín, năng khiếu cùng tham gia tuyên truyền)
- Những trường hợp cố tình chống đối, có hành vi phá hoại tài sản của đơn vị, tiến hành lập biên bản sự việc, (ghi lại hình ảnh) kịp thời báo cáo cấp trên, báo cáo với các cơ quan pháp luật và lực lượng bảo đảm an ninh trật tự để có biện pháp chấn áp kịp thời.
- Thường xuyên duy trì nghiêm nền nếp, chế độ giao ban, hội ý và chế độ báo cáo theo quy định.       
Tình huống 29: Sau khi bình xét đề nghị khen thưởng thành tích đợt tham gia phòng chống thiên tai, dịch bệnh tại địa phương, có dư luận trong đơn vị cho rằng: Việc bình xét khen thưởng chưa đúng người, đúng thành tích; có quân nhân được đề nghị khen thưởng do chỉ huy ưu ái. 
Gợi ý biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy đánh giá mức độ ảnh hưởng dư luận; phân công cán bộ xác minh làm rõ.
- Kiểm tra nắm lại các quy trình, thủ tục xét đề nghị khen thưởng của đơn vị; 
- Gặp gỡ trao đổi với cán bộ, chiến sĩ đơn vị có luận để nắm tình hình xét khen thưởng và đề nghị khen thưởng. 
- Gặp gỡ ban chỉ huy đơn vị có dư luận để trao đổi, nghe phản ánh tình hình.
- Nếu phát hiện có sai sót trong quy trình, thủ tục, tiêu chuẩn đề nghị khen thưởng thì yêu cầu cấp ủy cấp dưới tổ chức xét, đề nghị khen thưởng lại. Lãnh đạo, chỉ huy cấp trên trực tiếp dự họp để nắm, chỉ đạo trực tiếp. Có biện pháp chấn chỉnh, phê bình nghiêm túc đối với lãnh đạo, chỉ huy, cán bộ đơn vị làm không đúng quy định.
- Nếu phát hiện sai sót sau khi đã đề nghị lên cấp trên thì họp cấp ủy, thống nhất đề nghị lên cấp trên xem xét lại kết quả khen thưởng, hoặc đề nghị khen thưởng bổ sung, nhưng phải bảo đảm đúng tiêu chuẩn, tỷ lệ quy định.
- Tổ chức rút kinh nghiệm nghiêm túc ở các tổ chức, các cơ quan, đơn vị có liên quan.
Tình huống 30: Đơn vị có một đồng chí quân nhân viết đơn tình nguyện lên đường tham gia phòng, chống dịch ở địa phương xa đơn vị, thời gian dài. Trong đơn vị có dư luận cho rằng đồng chí đó làm như vậy là cơ hội. Mục đích chính là để đánh bóng bản thân và để được khen thưởng cuối năm vì đồng chí đó sắp đến hạn nâng lương, thăng quân hàm.
- Nắm nguồn dư luận trong đơn vị, gặp gỡ những quân nhân có suy nghĩ lệch lạc, tìm hiểu nguyên nhân vì sao lại có suy nghĩ về việc viết đơn của đồng chí đó như vậy.
- Hội ý chỉ huy đơn vị đánh giá tính chất, mức độ của dư luận là do mâu thuẫn cá nhân hay do thiếu hiểu biết để có biện pháp xử lý phù hợp. Báo cáo cấp trên về tình hình đơn vị.
- Gặp gỡ, động viên, khích lệ quân nhân tình nguyện lên đường tham gia phòng chống dịch.
- Thông qua sinh hoạt đơn vị quán triệt cho mọi cán bộ, chiến sĩ thấy được tình hình và sự nguy hiểm của dịch, quan điểm của Đảng, Nhà nước, Quân đội, những tấm gương sáng trong phòng chống dịch bệnh. Trước tập thể đơn vị biểu dương tinh thần, hành động cao đẹp của đồng đội, đồng thời nghiêm túc phê bình những suy nghĩ lệch lạc trong đơn vị.
- Tiến hành tuyên truyền trên hệ thống loa truyền thanh, bảng tin của đơn vị về gương của đồng chí tình nguyện lên đường tham gia phòng chống dịch.
- Sau khi đồng chí thực hiện nhiệm vụ xong trở về đơn vị, tiến hành xem xét, đánh giá chất lượng hoàn thành nhiệm vụ của quân nhân đó để thông báo cho đơn vị và đề nghị biểu dương, khen thưởng.
- Tiếp tục theo dõi, nắm tình hình tư tưởng của quân nhân tham gia phòng chống dịch sau khi thực hiện nhiệm vụ và dư luận trong đơn vị.
- Tổng hợp tình hình, báo cáo cấp trên.
Tình huống 31: Hiện tượng một số sĩ quan trong đơn vị có biểu hiện chạy thành tích, che dấu khuyết điểm vi phạm trong quá trình thực hiện nhiệm vụ phòng, chống dịch, gây dư luận xấu trong nội bộ 
Gợi ý biện pháp xử lý:
- Chính ủy, chính trị viên nắm chắc tình hình tư tưởng, chấp hành kỷ luật của cán bộ và những biểu hiện che dấu khuyết điểm, chạy theo thành tích của cán bộ trong quá trình thực hiện nhiệm vụ phòng, chống dịch, thống nhất với chỉ huy đơn vị biện pháp lãnh đạo, chỉ đạo khắc phục.
 - Họp cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, chấp hành kỷ luật, dư luận của sĩ quan, quân nhân chuyên nghiệp, nguyên nhân che dấu khuyết điểm, chạy theo thành tích, thống nhất biện pháp khắc phục.
- Gặp gỡ giáo dục, tuyên truyền cho sĩ quan, quân nhân chuyên nghiệp hiểu rõ tác hại, hậu quả của biểu hiện che dấu khuyết điểm, chạy theo thành tích là vi phạm quy định của Quân đội về chế độ báo cáo; vi phạm chế độ trách nhiệm của người chỉ huy, ảnh hưởng đến việc hoàn thành nhiệm vụ phòng, chống dịch, kết quả xây dựng chi bộ TSVM, đơn vị VMTD mẫu mực tiêu biểu. 
- Tổ chức sinh hoạt đơn vị giáo dục, tuyên truyền cho sĩ quan, quân nhân chuyên nghiệp trong đơn vị nhận thức sâu sắc nhiệm vụ phòng, chống dịch và xác định đây cũng là nhiệm vụ chính trị của đơn vị để xây dựng chi bộ TSVM, đơn vị VMTD mẫu mực tiêu biểu; kiên quyết đấu tranh với những quan điểm, tư tưởng báo cáo không trung thực, che dấu khuyết điểm, chạy theo thành tích của sĩ quan, quân nhân chuyên nghiệp trong đơn vị.
- Duy trì nghiêm chế độ báo cáo, phản ánh tình hình về tư tưởng, chấp hành kỷ luật và các mối quan hệ của sĩ quan, quân nhân chuyên nghiệp trong thực hiện nhiệm vụ phòng, chống dịch. 
- Xử lý kỷ luật nghiêm minh đối với những trường hợp vi phạm.
Tình huống 32: Ban CHQS huyện H đảm nhiệm chuẩn bị và duy trì khu cách ly phòng, chống dịch; phân công cho đồng chí A (QNCN) làm công tác bảo đảm hậu cần, tuy nhiên quá trình thực hiện có dư luận cho rằng đồng chí A thực hiện thu - chi chưa rõ ràng, thiếu tính minh bạch, tác động tư tưởng của quân nhân A.
Gợi ý biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy thống nhất đánh giá tình hình quản lý tài chính trong công tác phòng chống dịch bệnh thời gian qua, dư luận của cán bộ đơn vị, thống nhất biện pháp giải quyết, khắc phục. 
- Tổ chức lực lượng chuyên môn xác minh thông tin, nắm chắc tình hình, kiểm tra công tác chi tiêu tài chính; đề xuất Đảng ủy, Ban chỉ huy giải quyết.
- Tùy theo tính chất mức độ để tổng hợp báo cáo cấp trên xin ý kiến chỉ đạo; có thể xảy ra một trong hai trường hợp sau:
Khi có biểu hiện sai phạm:
- Gặp gỡ, phân tích quân nhân A nhận rõ sai sót, khuyết điểm, thực hiện công khai, minh bạch, không làm ảnh hưởng đến uy tín của bản thân và đơn vị; yêu cầu có biện pháp khắc phục, đền bù thâm hụt (nếu có). 
- Tổ chức kiểm điểm, kỷ luật đúng với tính chất, mức độ sai phạm
- Thông qua các hình thức thông báo cho công dân đang thực hiện cách ly và cán bộ, chiến sĩ về kết quả kiểm tra, xác minh, xử lý; rút ra bài học trong công tác lãnh đạo, chỉ đạo, quản lý tài chính đảm bảo đúng nguyên tắc, công khai, minh bạch, tạo sự thống nhất cao.
- Trường hợp đồng chí A còn yếu về chuyên môn, tổ chức bồi dưỡng, tập huấn để đáp ứng yêu cầu nhiệm vụ.
- Tổng hợp kết quả xử lý, báo cáo cấp trên. 
Khi thông tin dư luận không đúng sự thật:
- Thông qua các hình thức thông báo cho công dân đang thực hiện cách ly và cán bộ, chiến sĩ về kết quả kiểm tra, xác minh, xử lý; tuyên truyền về bản chất, truyền thống tốt đẹp của “Bộ đội Cụ Hồ”, theo dõi, định hướng dư luận.
- Gặp gỡ đồng chí A để phân tích, động viên tiếp tục thực hiện nhiệm vụ
- Thông báo rõ các chế độ, tiêu chuẩn của các đối tượng tại khu cách ly y tế; thường xuyên đối thoại, giải quyết các thắc mắc của công dân và cán bộ, chiến sĩ. 
- Báo cáo đề nghị cấp trên chỉ đạo các lực lượng phối hợp, theo dõi không gian mạng, có biện pháp đấu tranh, pha loãng, gỡ bỏ những thông tin lợi dụng sai phạm để chống phá Đảng, Nhà nước và nhiệm vụ phòng, chống dịch, gây ảnh hưởng xấu đến bản chất, truyền thống của Quân đội, đơn vị.
- Trường hợp dư luận có ảnh hưởng lớn đến uy tín Quân đội, đơn vị thì tiến hành điều tra, xử lý nghiêm trường hợp thông tin sai sự thật.
- Tổng hợp kết quả xử lý, báo cáo cấp trên. 
Tình huống 33: Qua dư luận đơn vị nắm được, một đồng chí cán bộ đã vận động tiền của người dân trong khu vực cách ly để hỗ trợ cán bộ, chiến sĩ phục vụ người dân tại khu cách ly đã gây dư luận không tốt trong đơn vị.
Gợi ý biện pháp xử lý:
- Xác định đây là sự việc nhạy cảm, liên quan đến phẩm chất, uy tín của Quân đội nói chung của cán bộ nói riêng. Vì vậy, khi tiến hành cần phải thận trọng, khách quan, kiểm tra xác minh chặt chẽ, khoa học.
- Chính ủy, chính trị viên cần xác minh lại nguồn dư luận về cán bộ thực hiện nhiệm vụ trong khu cách ly, nếu đúng sự thật thì tiến hành trao đổi thẳng thắn, chân tình với đồng chí cán bộ đó; thông báo về dư luận trong khu cách ly, kết quả kiểm tra xác minh; phân tích về sự việc trên đã ảnh hưởng không tốt đến tình hình của đơn vị và uy tín của cán bộ, hình ảnh “Bộ đội Cụ Hồ”; đề nghị đồng chí chấm dứt việc làm trên.
- Trường hợp đồng chí cán bộ không nhận lỗi thì chính ủy, chính trị viên phải báo cáo cấp trên xin ý kiến chỉ đạo, cùng với cấp trên có biện pháp xác minh, chứng minh sự phản ánh của dư luận là đúng sự thật.
- Ủy ban kiểm tra cấp trên có biện pháp kiểm tra đảng viên có dấu hiệu vi phạm kỷ luật.
- Tổ chức sinh hoạt đơn vị, ổn định tình hình tư tưởng của cán bộ, chiến sĩ nhắc nhở cán bộ, chiến sĩ, nhất là các đồng chí tham gia thực hiện nhiệm vụ trong khu cách ly nêu cao ý thức tu dưỡng, rèn luyện đạo đức, lối sống, chấp hành nghiêm các quy định trong phòng, chống dịch, các quy định khi tiếp xúc với nhân dân.
- Báo cáo kết quả giải quyết vụ việc lên cấp trên.
Tình huống 34: Một số HSQ-CS trong quá trình tham gia phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh, do tính chất nhiệm vụ khó khăn, vất vả đã thể hiện thái độ không ân cần, hòa nhã với nhân dân. 
Gợi ý biện pháp xử lý:
- Cử cán bộ đơn vị gặp gỡ nhân dân nắm lại tình hình vụ việc.
- Phân công cán bộ gặp gỡ HSQ-CS trong đơn vị cùng tham gia thực hiện nhiệm vụ với bộ phận vi phạm để đối chiếu thông tin, để có cơ sở đánh giá chính xác tình hình vụ việc.
- Hội ý cấp ủy, đánh giá tính chất, mức độ, nguyên nhân biểu hiện thái độ, hành vi thiếu ân cần, hòa nhã của HSQ-CS. Thống nhất biện pháp giáo dục, khắc phục.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm sự việc xảy ra; kết hợp giáo dục cho cán bộ, chiến sĩ nhận thức sâu sắc về ý nghĩa của nhiệm vụ tham gia phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh; chức năng, nhiệm vụ của Quân đội; phẩm chất “Bộ đội Cụ Hồ”, truyền thống đoàn kết quân dân để củng cố ý thức, trách nhiệm cho bộ đội.
- Phân công cấp ủy viên phụ trách công tác dân vận, phối hợp với cấp ủy, chính quyền, đoàn thể địa phương gặp gỡ, trao đổi, nhận khuyết điểm trước nhân dân về thái độ, hành vi của HSQ-CS trong đơn vị.
- Tùy tình hình điều kiện phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh, nếu điều kiện cho phép có thể phối hợp tổ chức tốt các hoạt động VHVN, thể thao giữa đơn vị với đoàn viên thanh niên và nhân dân địa phương để tăng cường hiểu biết, tạo lập, củng cố mối quan hệ đoàn kết, gắn bó giữa đơn vị và nhân dân trên địa bàn.
- Tăng cường quản lý tư tưởng, ý thức kỷ luật của bộ đội trong mọi hoạt động của đơn vị trong đó có nhiệm vụ cứu hộ, cứu nạn, phòng, chống thiên tai, dịch bệnh.
Tình huống 35: Một số đồng chí dân quân tự vệ không nhận nhiệm vụ tham gia phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh với lý do chính sách chi trả tiền quá thấp, không tương xứng với công sức bỏ ra, gây dư luận không tốt trong nhân dân và lực lượng dân quân tự vệ
Gợi ý biện pháp xử lý:
- Trao đổi trong Ban chỉ huy quân sự xã nhận định tình hình tư tưởng, trách nhiệm của dân quân tự vệ trong thực hiện nhiệm vụ phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh, thống nhất biện pháp giải quyết; báo cáo xin ý kiến chỉ đạo của cấp trên để bố trí người thay thế.
- Tổ chức gặp gỡ số dân quân không nhận nhiệm vụ tham gia phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh; giáo dục, quán triệt hiểu rõ sự cần thiết phải tham gia giúp nhân dân khắc phục hậu quả thiên tai, dịch bệnh, trách nhiệm, quyền lợi, nghĩa vụ của một người dân quân; qua đó xây dựng trách nhiệm sẵn sàng nhận và hoàn thành nhiệm vụ, nâng cao ý thức chấp hành Luật Dân quân tự vệ, kỷ luật Quân đội, quy định của địa phương.
- Phối hợp với gia đình, người thân, đồng chí đồng đội, động viên số dân quân còn băn khoăn trong quá trình nhận nhiệm vụ, nâng cao ý thức, trách nhiệm của dân quân tự vệ sẵn sàng nhận và hoàn thành tốt nhiệm vụ được giao.
- Định hướng để Ban chỉ huy quân sự xã tổ chức sinh hoạt rút kinh nghiệm công tác huy động quân số tham gia thực hiện nhiệm vụ phòng, chống, khắc phục sự cố thiên tai, dịch bệnh về ý thức nhận vụ trong điều kiện khó khăn, vất vả; căn cứ tính chất vụ việc có thể đề nghị hình thức kỷ luật số dân quân chấp hành không nghiêm mệnh lệnh, đồng thời rà soát, lựa chọn những đồng chí có đủ phẩm chất chính trị, trách nhiệm trong công tác tham gia vào lực lượng dân quân của xã.
- Làm tốt công tác đánh giá kết quả hoàn thành nhiệm vụ của lực lượng tham gia phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh; kịp thời khen thưởng tập thể, cá nhân có thành tích; xử lý nghiêm minh  những đồng chí vi phạm.
- Báo cáo cấp trên theo quy định.


	B. TÌNH HUỐNG TƯ TƯỞNG CÓ THỂ NẢY SINH TRONG THỰC HIỆN NHIỆM VỤ PHÒNG, CHỐNG THIÊN TAI
Tình huống 1. Một đồng chí chiến sĩ trong đơn vị có biểu hiện rất buồn và lo lắng vì khi đang tham gia phòng chống thiên tai, cứu hộ cứu nạn ở địa phương khác thì nhận được tin gia đình mình ở quê bị lũ quét cuốn trôi một số tài sản, vật dụng trong nhà, cũng như thiệt hại về hoa màu của gia đình.
Gợi ý biện pháp xử lý:
- Hội ý cán bộ đơn vị đang thực hiện nhiệm vụ phòng, chống thiên tai để nhận định tình hình, bàn cách xử trí, phân công cán bộ theo dõi, giúp đỡ chiến sĩ.
- Liên hệ với chính quyền địa phương của gia đình đồng chí đang sinh sống để nắm bắt tình hình thiệt hại do bão lũ gây ra ở đó và cụ thể thiệt hại mà gia đình của đồng chí chiến sĩ đang phải gánh chịu và nhanh chóng báo cáo với chỉ huy các cấp.
- Gặp gỡ đồng chí chiến sĩ để kịp thời động viên tư tưởng nhằm giảm bớt đi sự lo lắng, đồng thời để đồng chí hiểu được vị trí quan trọng của nhiệm vụ, từ đó cảm thấy rõ vinh dự, trách nhiệm để khắc phục khó khăn xây dựng ý chí quyết tâm và hoàn thành tốt nhiệm vụ được giao.
- Tổ chức sinh hoạt đơn vị để thông báo về tình hình nhiệm vụ, đồng thời biểu dương tinh thần khắc phục khó khăn để tiếp tục thực hiện nhiệm vụ của đồng chí chiến sĩ để mọi người cùng nhau động viên, san sẻ.
- Tạo điều kiện để đồng chí được liên hệ về gia đình thăm hỏi và động viên người thân của mình.
- Thường xuyên làm tốt công tác tuyên truyền, giáo dục cho chiến sĩ nhận thức rõ nhiệm vụ, nâng cao trách nhiệm, khắc phục mọi khó khăn trong thực hiện nhiệm vụ phòng chống thiên tai, cứu hộ cứu nạn.
- Phân công đồng chí, đồng đội thường xuyên nắm bắt, quan tâm và thường xuyên động viên đối với đồng chí đó.
- Quan tâm bảo đảm đầy đủ về tiêu chuẩn, đề nghị giải quyết tốt các chế độ, chính sách theo quy định cho chiến sĩ gặp hoàn cảnh khó khăn yên tâm công tác, xác định tốt nhiệm vụ.
- Tổ chức sinh hoạt rút kinh nghiệm sau mỗi lần thực hiện nhiệm vụ để kịp thời khắc phục những vấn đề còn tồn tại và đề ra phương hướng cho những đợt thực hiện nhiệm vụ tiếp theo. 
Tình huống 2: Trong đơn vị quân nhân A có biểu hiện buồn chán, tiêu cực khi có thân nhân (bố, mẹ, vợ, con) điều trị ở bệnh viện nhưng đơn vị chưa giải quyết phép vì phải trực phòng chống thiên tai, sẵn sàng cứu hộ, cứu nạn.
Gợi ý biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy và tiến hành gặp gỡ quân nhân A, nắm thêm các nội dung: tình hình sức khỏe và mức độ của bệnh; tình hình người chăm sóc trong gia đình; công việc của vợ và độ tuổi của các con có ảnh hưởng đến chăm sóc người bệnh không; hoàn cảnh kinh tế gia đình. Động viên quân nhân hiểu rõ yêu cầu của nhiệm vụ trực phòng chống thiên tai, sẵn sàng cứu hộ, cứu nạn, yên tâm hoàn thành tốt nhiệm vụ.
- Liên lạc với thân nhân trong gia đình đồng chí A, nắm thêm tình hình của gia đình. 
- Căn cứ vào tình trạng sức khỏe, mức độ bệnh tật của thân nhân quân nhân A để sinh hoạt thông báo với cán bộ, chiến sĩ trong đơn vị được biết để gần gũi, động viên, hoặc thăm hỏi về vật chất.
- Thường xuyên nắm tình hình tư tưởng, đánh giá đúng kết quả thực hiện nhiệm vụ và chấp hành kỷ luật của quân nhân có thân nhân nằm viện; có biện pháp khắc phục kịp thời nếu chất lượng công việc bị ảnh hưởng, hoặc biểu dương, nhân rộng trong toàn đơn vị nếu quân nhân đó hoàn thành tốt nhiệm vụ.
- Phát huy vai trò của tổ chức công đoàn, làm tốt công tác giáo dục, định hướng và quản lý chặt chẽ tình hình tư tưởng. Tránh trường hợp quân nhân vì tư tưởng không thông suốt mà có thái độ tiêu cực, trốn ra ngoài đơn vị.
- Trong trường hợp thân nhân bị bệnh rất nặng, khả năng không qua khỏi thì báo cáo cấp trên giải quyết cho quân nhân về thăm gia đình. (Lưu ý: Trước khi về cần quán triệt cụ thể, tỉ mỉ để quân nhân chấp hành nghiêm kỷ luật, bảo đảm an toàn, gửi lời hỏi thăm của đơn vị đến gia đình).
Tình huống 03: Trong đơn vị có gia đình một đồng chí hạ sĩ quan (chiến sĩ) gặp mưa bão, nhà cửa bị đất đá sạt lở vùi lấp, không bị thiệt hại về người, có biểu hiện hoang mang, lo lắng
Gợi ý biện pháp xử lý:
- Nắm chắc tâm tư, hoàn cảnh cụ thể gia đình quân nhân thông qua các nguồn tin các mối quan hệ của quân đó (các cấp báo cáo) từ đó xác định biện pháp cách thức giải quyết.
- Tiến hành gặp gỡ, trò chuyện, nắm tâm tư, nguyện vọng, những vướng mắc của quân nhân có hoàn cảnh khó khăn; từ đó động viên, chia sẻ, giúp đỡ quân nhân đó vượt qua khó khăn, yên tâm công tác xác định rõ nhiệm vụ.
- Báo cáo chỉ huy cấp trên để cùng theo dõi động viên xác định biện pháp giải quyết.
- Chỉ đạo trung đội (đại đội) có quân nhân gặp hoàn cảnh khó khăn phân công cán bộ, đảng viên, đoàn viên ưu tú theo dõi, động viên giúp đỡ quân nhân có gia đình gặp khó khăn hoàn thành nhiệm vụ.
- Chỉ đạo đơn vị có biện pháp tác động với những quân nhân khác là bạn bè thân thiết, đồng hương… với chiến sĩ gặp khó khăn để cùng chia sẻ, động viên, an ủi.
- Trường hợp (xét thấy cần thiết) đề nghị cấp có thẩm quyền giải quyết cho quân nhân đi phép về giải quyết việc gia đình.
- Đề nghị tập thể đơn vị và chỉ huy cấp trên quan tâm động viên giúp đỡ chiến sĩ gặp khó khăn về vật chất và tinh thần để góp phần giải quyết khó khăn (đề nghị trợ cấp khó khăn cho quân nhân đó theo quy định).
- Nếu có điều kiện đề nghị chỉ huy cấp trên cử cán bộ về thăm hỏi, động viên gia đình quân nhân đó.
Tình huống 04: Đơn vị nhận được nhiệm vụ tăng cường lực lượng đi giúp dân phòng chống bão lụt nhưng qua các vụ việc mất an toàn của quân đội trong giúp dân phòng chống bão lụt một số cán bộ, quân nhân chuyên nghiệp, HSQ-CS có biểu hiện lo lắng, dao động tư tưởng, tìm các lý do để trốn tránh nhiệm vụ.
Gợi ý biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy đơn vị nhận định, đánh giá tình hình tác động đến tư tưởng của bộ đội, thống nhất biện pháp giải quyết, phân công cán bộ tích cực nắm, quản lý tư tưởng bộ đội, kịp thời xử lý các tình huống có thể xảy ra.
- Nhanh chóng tổ chức sinh hoạt, quán triệt, giáo dục nâng cao nhận thức cho cán bộ, quân nhân chuyên nghiệp, HSQ-CS trong đơn vị hiểu sâu sắc về mục đích, ý nghĩa, yêu cầu và tầm quan trọng của nhiệm vụ giúp dân phòng chống bão lụt, kết quả hoàn thành nhiệm vụ của đơn vị trong thời gian qua; thấy rõ niềm vinh dự tự hào khi được chỉ huy cấp trên tin tưởng giao nhiệm vụ cho đơn vị; trên cơ sở đó xây dựng niềm tin động cơ trách nhiệm và ý chí quyết tâm hoàn thành tốt nhiệm vụ được giao.
- Đánh giá, phân loại tư tưởng cán bộ, chiến sĩ, phân công cán bộ gặp gỡ để nắm chắc tình hình và động viên bộ đội hiểu rõ nhiệm vụ; kịp thời ngăn chặn những biểu hiện tư tưởng ngại khó, ngại khổ; chủ động định hướng giải quyết ổn định tình hình đơn vị; tổng hợp báo cáo xin ý kiến chỉ đạo của cấp trên.
- Phân công những cán bộ có trình độ năng lực, phẩm chất đạo đức, tinh thần trách nhiệm tốt chỉ huy phụ trách những nhiệm vụ khó khăn phức tạp để làm gương cho cán bộ chiến sĩ yên tâm noi theo.
- Phát huy tốt hoạt động của chiến sĩ dân vận, chiến sĩ bảo vệ, duy trì sinh hoạt tổ, tiểu đội thông qua đó tìm hiểu sâu kỹ về nguyên nhân trốn tránh nhiệm vụ.
- Tổ chức phát động đợt thi đua cao điểm, đột kích, tập trung làm rõ ý nghĩa tầm quan trọng và yêu cầu của nhiệm vụ, lòng tự hào và trách nhiệm được trên giao; xác định mục tiêu, nội dung, biện pháp xác thực nhằm nâng cao nhận thức trách nhiệm, xây dựng ý chí quyết tâm chủ động khắc phục khó khăn, ý thức chấp hành kỷ luật; quan tâm đảm bảo đời sống cho cán bộ, chiến sỹ phát huy vai trò tiền phong của cán bộ, đảng viên, số chiến sĩ có thành tích trong thực hiện chức trách nhiệm vụ, tổ chức cho cán bộ chiến sĩ viết đăng ký quyết tâm thực hiện nhiệm vụ.
- Đẩy mạnh các hoạt động tuyên truyền cổ động thực hiện nhiệm vụ, thường xuyên gần gũi bộ đội, nắm chắc tâm tư tình cảm và chia sẻ những khó khăn vất vả cũng như là vinh dự tự hào khi được thực hiện nhiệm vụ giúp dân phòng chống bão lụt.
- Duy trì chặt chẽ nghiêm túc các chế độ nề nếp, sinh hoạt đơn vị rút kinh nghiệm để biểu dương khen thưởng và chấn chỉnh những sai phạm kịp thời, chủ động làm tốt công tác tư tưởng, quản lý chặt chẽ tình hình mọi mặt của đơn vị, không để dư luận xấu xảy ra trong đơn vị.
Tình huống 05: Sau siêu bão, các đợt mưa lớn kéo dài, gây ngập lụt cục bộ, làm ách tắc giao thông nghiêm trọng; một số cán bộ, CNVC, lao động không đến đơn vị làm việc được, ảnh hưởng đến dây chuyền sản xuất, chất lượng sản phẩm và công tác an toàn. Mưa bão gây thiệt hại về tài sản, tài nguyên; sân công nghiệp một số đơn vị khai thác than hầm lò bị ngập sâu, nước và đất đá có nguy cơ tràn vào trong lò, gây sập lò và hư hỏng các trang thiết bị
Gợi ý biện pháp xử lý:
- Cấp ủy, chỉ huy, cơ quan chính trị tiếp tục quán triệt, thực hiện nghiêm túc các văn bản lãnh đạo, chỉ đạo của Trung ương, QUTW-BQP và của đơn vị về phòng, chống khắc phục hậu quả thiên tai, thảm họa, dịch bệnh, cứu hộ - cứu nạn. Hội ý nhanh cấp ủy, chỉ huy bàn các giải pháp ứng phó, phòng, chống, giảm nhẹ và khắc phục thiệt hại do mưa bão gây ra, như: Phương án sản xuất kinh doanh, bảo vệ tài nguyên trong mưa bão; huy động con người, trang thiết bị; công tác bảo đảm hậu cần đời sống (xe đưa đón công nhân, nơi ở, cung ứng thực phẩm, nhu yếu phẩm, ..); công tác phòng, chống dịch bệnh (thuốc men, vật tư y tế...).
- Tăng cường lãnh đạo, chỉ đạo công tác tuyên tuyền, giáo dục chính trị, tư tưởng làm cho cấp ủy, chỉ huy các cấp, cán bộ, đảng viên, CNVC, lao động trong đơn vị thấy được những diễn biến phức tạp, khó lường của khí hậu, thời tiết, hậu quả do thiên tai gây ra, nhất là thảm họa của bão mạnh, siêu bão; những khó khăn, hạn chế trong ứng phó siêu bão và tìm kiếm cứu nạn.
- Xây dựng, nâng cao nhận thức, trách nhiệm, ý chí quyết tâm cho cán bộ, CNVC, lao động sẵn sàng nhận và hoàn thành xuất sắc mọi nhiệm vụ được giao, chống tư tưởng ngại khó khăn gian khổ, thoái thác nhiệm vụ, tích cực tham gia khắc phục hậu quả thiên tai tại đơn vị và phối hợp với cấp ủy, chính quyền địa phương trên địa bàn đứng chân tham gia cứu trợ thảm họa, giúp đỡ nhân dân khắc phục hậu quả siêu bão theo phương châm “4 tại chỗ” và “Tích cực, chủ động, ứng phó nhanh, có hiệu quả, giảm thiểu thiệt hại thấp nhất về người và tài sản”, bảo đảm an toàn tuyệt đối về người, trang thiết bị, hệ thống kho tàng, cơ sở vật chất phục vụ sản xuất kinh doanh, doanh trại, công trình phòng, chống mưa bão của đơn vị. 
- Lãnh đạo, chỉ đạo thực hiện nghiêm kỷ luật dân vận, mệnh lệnh của cấp trên, quy tắc về bảo đảm an toàn trong thực hiện nhiệm vụ; làm tốt công tác bảo vệ chính trị nội bộ, bảo vệ bí mật, bảo đảm an ninh, an toàn; quản lý chặt chẽ quân số, vũ khí, trang bị, phương tiện, vật liệu nổ...chăm lo bảo đảm tốt đời sống vật chất, tinh thần và thực hiện đúng các chế độ, chính sách đối với cán bộ, CNVC, lao động trong đơn vị, nhất là cán bộ, người lao động bị thương, hy sinh trong khi làm nhiệm vụ phòng, chống, khắc phục hậu quả thiên tai, thảm họa, dịch bệnh, cứu hộ - cứu nạn. 
- Chỉ đạo tổ chức tốt việc sơ, tổng kết rút kinh nghiệm ở các cấp trong phòng, chống, khắc phục hậu quả thiên tai, thảm họa, dịch bệnh, cứu hộ - cứu nạn; bổ sung giải pháp thực hiện nhiệm vụ tốt hơn trong thời gian tới. Kịp thời biểu dương, khen thưởng những tập thể, cá nhân có thành tích tốt; xử lý nghiêm những trường hợp vi phạm (nếu có).
Tình huống 06: Trong quá trình thực hiện nhiệm vụ giúp đỡ Nhân dân địa phương khắc phục hậu quả thiên tai gây ra, có hai chiến sĩ trong đại đội tổ chức uống rượu sau đó gây gổ mất đoàn kết với một số thanh niên địa phương và bị thương phải đưa đi điều trị tại bệnh viện.
Gợi ý biện pháp xử lý:
- Trao đổi nhanh trong chỉ huy đại đội, thống nhất biện pháp xử lý và phân công cán bộ phụ trách giải quyết vụ việc, đưa chiến sĩ đi bệnh viện điều trị.
- Báo cáo cấp trên xin ý kiến chỉ đạo và đề nghị cử cán bộ và cơ quan chức năng phối hợp với đơn vị để giải quyết vụ việc.
- Gặp gỡ các nhân chứng của vụ việc để nắm lại tình hình vụ việc cụ thể.
- Cùng với cấp trên và cơ quan chức năng làm việc với chính quyền và cơ quan chức năng địa phương để tiến hành các biện pháp giáo dục số thanh niên có liên quan đến vụ việc xảy ra.
- Cử cán bộ thăm hỏi, động viên chiến sĩ nằm viện, nắm bắt tình hình tư tưởng, tâm trạng của bộ đội.
- Tiến hành xem xét, kiểm điểm và xử lý kỷ luật đối với các chiến sĩ vi phạm và cán bộ liên đới trách nhiệm theo đúng quy định của Bộ Quốc phòng sau khi chiến sĩ ra viện.
- Tổ chức sinh hoạt đơn vị để giáo dục, định hướng tư tưởng, dư luận, kịp thời rút kinh nghiệm chung trong toàn đơn vị về các yêu cầu khi thực hiện nhiệm vụ phòng, chống, khắc phục thiên tai và việc chấp hành kỷ luật dân vận, giữ gìn phẩm chất “Bộ đội Cụ Hồ”.
- Tổng hợp báo cáo cấp trên về kết quả giải quyết và xử lý vụ việc theo quy định.
Tình huống 07: Ban CHQS huyện giao nhiệm vụ cho một quân nhân phụ trách xã cùng một số quân nhân khác trong đơn vị phối hợp với Ban CHQS xã hỗ trợ nhân dân ven đê đang bị sạt lở và có nguy cơ vỡ bối đê do mưa lớn kéo dài, nước trên thượng nguồn xả lớn đã có biểu hiện băn khoăn, lo lắng và sợ nguy hiểm muốn thoái thác nhiệm vụ.
Gợi ý biện pháp xử lý:
- Trao đổi chỉ huy, thống nhất biện pháp, đánh giá cụ thể tư tưởng, những khó khăn, lo lắng của quân nhân khi được phân công phụ trách xã và tham gia phòng, chống thiên tai, tìm kiếm cứu nạn nơi khó khăn để thống nhất biện pháp giải quyết và phân công cán bộ phụ trách, theo dõi.
- Gặp gỡ trực tiếp động viên, giải thích cho quân nhân hiểu rõ vị trí, vai trò, chức năng, nhiệm vụ của quân đội (là đội quân công tác); tinh thần đoàn kết, kết quả thực hiện nhiệm vụ của cơ quan, đơn vị và của Đảng, nhà nước, nhân dân ta trong những năm qua; tính nguy hiểm của thiên tai bão lụt, nếu không được khắc phục, phòng chống kịp thời đối với nhân dân địa phương và chính cơ quan, đơn vị mình công tác.
- Sinh hoạt đơn vị, tổ chức giáo dục, quán triệt cho cán bộ, nhân viên những văn bản chỉ đạo của Trung ương và địa phương quyết tâm đoàn kết, chung sức, đồng lòng thi đua phòng, chống lụt bão, giảm nhẹ thiên tai, tìm kiếm cứu nạn, góp phần nâng cao ý thức trách nhiệm của mỗi quân nhân; nhất là tinh thần tự giác noi gương quyết tâm bảo vệ tính mạng, tài sản hoa màu của nhà nước và nhân dân trước nguy cơ lũ lụt.
- Quan tâm chăm lo, bảo đảm tốt chế độ chính sách, tiêu chuẩn cho quân nhân yên tâm, gắn bó với cơ quan với nhiệm vụ được phân công.
- Tổ chức sinh hoạt rút kinh nghiệm kịp thời sau mỗi lần cử cán bộ, nhân viên tham gia thực hiện những nhiệm vụ khó khăn, phức tạp nhất là tham gia nhiệm vụ phòng chống thiên tai, cứu hộ, cứu nạn.
Tình huống 08: Khi đơn vị có lệnh dự báo của cấp trên chuẩn bị lực lượng, phương tiện tham gia cứu hộ, cứu nạn một số chiến sĩ có biểu hiện lo sợ khi nhìn thấy hình ảnh các cán bộ, chiến sĩ hi sinh trong thực hiện nhiệm vụ cứu hộ, cứu nạn nên đã lấy lý do sức khỏe yếu, xin đi điều trị khám bệnh để không phải tham gia đã tác động xấu đến nhận thức về nhiệm vụ của một số đồng chí khác.
Gợi ý biện pháp xử lý:
- Nhanh chóng hội ý trao đổi, thống nhất trong chỉ huy về phương án giải quyết.
- Báo cáo cấp trên xin ý kiến chỉ đạo.
- Tiến hành kiểm tra sức khỏe của chiến sĩ. Nếu ốm thật, đề nghị quân y kiểm tra mức độ bệnh tình chăm sóc điều trị chu đáo, thay thế đồng chí khác tham gia.
- Nắm lại tình hình tư tưởng của số hạ sĩ quan, chiến sĩ sau sự việc hi sinh của một số cán bộ, chiến sĩ trong thực hiện nhiệm vụ tìm kiếm cứu hộ cứu, cứu nạn. Trường hợp một số đồng chí có tư tưởng trốn tránh nhiệm vụ thì trực tiếp gặp gỡ, nắm nguyên nhân tại sao đồng chí đó lo sợ. Chú ý: phương pháp nắm bắt phải khéo léo, mềm dẻo thông qua tâm sự, trò chuyện để nắm bắt tâm tư, tình cảm, vướng mắc của chiến sĩ.
- Hội ý cấp ủy, chỉ huy đơn vị, thống nhất các biện pháp giải quyết (trong hội ý cán bộ đơn vị phản ánh, báo cáo tình hình tư tưởng, tâm trạng của số hạ sĩ quan, chiến sĩ có biểu hiện băn khoăn, lo lắng).
- Trực tiếp gặp gỡ số hạ sĩ quan, chiến sĩ có biểu hiện băn khoăn, lo lắng phân tích cho bộ đội hiểu được nguyên nhân vụ việc là rất hiếm, động viên bộ đội an tâm thực hiện nhiệm vụ.
- Tổ chức cho bộ đội xem phim tư liệu về công tác tham gia cứu hộ cứu nạn của Quân đội nói chung và của đơn vị nói riêng trong những năm gần đây để bộ đội yên tâm, tin tưởng vào khả năng lãnh đạo, chỉ đạo thực hiện nhiệm vụ tìm kiếm, cứu hộ, cứu nạn của đơn vị.
- Tổ chức sinh hoạt đơn vị, giáo dục định hướng tư tưởng cho bộ đội, xác định vinh dự và trách nhiệm của người quân nhân cách mạng, phát huy phẩm chất “Bộ đội cụ Hồ”, khi được phân công nhiệm vụ ở những nơi nguy hiểm, vất vả, thậm chí phải hi sinh vì tính mạng, tài sản của nhân dân trước thiên tai, bão lũ. Xây dựng niềm tin vào trang bị, phương tiện cứu hộ, cứu nạn, bản lĩnh, ý chí, trình độ, kỹ năng xử lý của cán bộ, chiến sĩ đơn vị trong thực hiện nhiệm vụ cứu hộ cứu nạn. 
- Chỉ đạo chi đoàn tổ chức các hoạt động diễn đàn, tọa đàm về ý nghĩa, trách nhiệm của quân đội trong tham gia tìm kiếm, cứu hộ, cứu nạn...
- Sau khi hoàn thành nhiệm vụ hướng dẫn chỉ đạo tiểu đội, trung đội sinh hoạt rút kinh nghiệm về công tác quản lý tư tưởng bộ đội; xây dựng động cơ, trách nhiệm trong sẵn sàng thực nhiệm vụ cứu hộ, cứu nạn; biểu dương, khen thưởng kịp thời những tập thể, cá nhân có thành tích xuất sắc và phê bình, nhắc nhở những đồng chí thoái thác, ngại khó, ngại khổ… từ đó động viên chiến sĩ phát huy truyền thống của đơn vị dũng cảm, tích cực tham gia thực hiện nhiệm vụ.
- Tổ chức phân công cán bộ đơn vị tiếp tục theo dõi, kèm cặp, giúp đỡ, ổn định tư tưởng, tâm lý cho quân nhân.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 09: Phòng chống cháy rừng trong điều kiện thời tiết khắc nghiệt, vất vả, một số đồng chí có biểu hiện lo lắng, mệt mỏi, chán nản muốn thoái thác nhiệm vụ.
Gợi ý biện pháp xử lý:
	- Nắm vững tình hình tâm tư, nguyện vọng của chiến sĩ làm việc trong điều kiện khó khăn, vất vả tham mưu cho cấp ủy, chỉ huy có biện pháp khắc phục.
	- Hội ý cấp ủy, chỉ huy đánh giá tình hình tư tưởng, kỷ luật trong đơn vị đặc biệt là những đồng chí được giao nhiệm vụ phòng, chống cháy rừng. Thống nhất biện pháp giải quyết và phân công cán bộ phụ trách.
	- Gặp gỡ, động viên và giáo dục cho chiến sĩ được giao nhiệm vụ hiểu rõ về nhiệm vụ “Chiến đấu trong thời bình” vinh dự, trách nhiệm của chiến sĩ khi được giao nhiệm vụ và xây dựng quyết tâm, ý thức trách nhiệm khắc phục mọi khó khăn để thực hiện nhiệm vụ. Làm tốt công tác tuyên truyền về truyền thống cách mạng, chức năng, nhiệm vụ Quân đội, gương người tốt, việc tốt.
	- Tổ chức bồi dưỡng thêm một số kinh nghiệm, kỹ năng cho chiến sĩ khi thực hiện nhiệm vụ phòng chống, cháy rừng nhằm đảm bảo an toàn và hoàn thành tốt nhiệm vụ.
	- Làm tốt công tác chuẩn bị mọi mặt cho thực hiện nhiệm vụ và quan tâm đảm bảo chế độ tiêu chuẩn cho chiến sĩ yên tâm thực hiện nhiệm vụ.
	- Chỉ đạo Chi đoàn tổ chức diễn đàn Thanh niên với nhiệm vụ “Chiến đấu trong thời bình”.
	- Tổng hợp tình hình tư tưởng chiến sĩ trước khi thực hiện nhiệm vụ báo cáo cấp trên. 
Tình huống 10: Đơn vị chuẩn bị thực hiện nhiệm vụ cứu nạn do bão gây sạt lở ở địa bàn khó khăn, phức tạp, phân tán lực lượng; cán bộ, chiến sĩ có biểu hiện dao động về tư tưởng và xuất hiện tình trạng báo ốm.
Gợi ý biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy đơn vị nhận định tình hình, xác định chủ trương, biện pháp giải quyết.
- Triển khai cho quân y khám sàng lọc bệnh tình của các quân nhân báo ốm đau để xác định rõ nguyên nhân. 
- Nhanh chóng tổ chức sinh hoạt quán triệt, giáo dục nâng cao nhận thức cho cán bộ, chiến sĩ trong đơn vị hiểu sâu sắc về mục đích, ý nghĩa, yêu cầu và tầm quan trọng của nhiệm vụ cứu hộ cứu nạn; kết quả hoàn thành nhiệm vụ của đơn vị thời gian qua; thấy rõ niềm vinh dự, tự hào khi được chỉ huy cấp trên tin tưởng giao nhiệm vụ cho đơn vị.
- Đánh giá, phân loại tư tưởng cán bộ, chiến sĩ; phân công cán bộ gặp gỡ để nắm chắc tình hình và động viên bộ đội hiểu rõ nhiệm vụ; kịp thời ngăn chặn những biểu hiện tư tưởng ngại khó, ngại khổ… chủ động định hướng, giải quyết, ổn định tình hình đơn vị.
- Phân công cán bộ có trình độ, năng lực, phẩm chất đạo đức, tình thần trách nhiệm tốt chỉ huy, phụ trách những nhiệm vụ khó khăn, phức tạp để làm gương cho cán bộ, chiến sĩ yên tâm và noi theo.
- Phát huy tốt hoạt động của chiến sĩ bảo vệ, duy trì sinh hoạt tổ, tiểu đội, thông qua đó tìm hiểu sâu về nguyên nhân báo ốm của quân nhân.
- Phối hợp với gia đình, người thân cùng với đơn vị tăng cường các biện pháp giáo dục, quản lý bộ đội, chống hiện tượng giả bệnh trốn tránh nhiệm vụ.
- Đẩy mạnh các hoạt động tuyên truyền cổ động trong thực hiện nhiệm vụ; thường xuyên gần gũi bộ đội, nắm chắc tâm tư tình cảm và chia sẻ những khó khăn vất vả, nhưng cũng là vinh dự tự hào khi được thực hiện nhiệm vụ.
- Duy trì chặt chẽ nền nếp sinh hoạt đơn vị (rút kinh nghiệm, chấn chỉnh những sai phạm; chủ động làm công tác tư tưởng; quản lý chặt chẽ tình hình mọi mặt của đơn vị không để dư luận xấu xảy ra trong đơn vị).
- Biểu dương các cá nhân, tập thể nhân rộng điển hình tiên tiến hoàn thành tốt nhiệm vụ trong thời gian qua.
Tình huống 11: Trong đơn vị có chiến sỹ lái xe sau khi nhận nhiệm vụ đi vận chuyển hàng cứu trợ do mưa bão, sạt lở đất ở các tỉnh Miền trung đã nảy sinh tư tưởng không muốn thực hiện nhiệm vụ, tác động xấu đến nhận thức về nhiệm vụ của một số chiến sỹ lái xe khác.
¬Gợi ý biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy đơn vị nhận định tình hình, đánh giá tính chất, tác hại, nguyên nhân, mức độ ảnh hưởng để trao đổi thống nhất trong chỉ huy và báo cáo cấp trên xin ý kiến chỉ đạo.
- Phân công cán bộ động viên đồng chí đó; thu thập thông tin, phân tích, kết luận nguyên nhân đồng chí đó không muốn thực hiện nhiệm vụ vận chuyển.
- Tiến hành gặp gỡ quân nhân đó nắm thực chất lý do, nguyên nhân; nếu trường hợp quân nhân đó đang có việc gia đình quan trọng cần về để giải quyết thì cắt cử đồng chí khác thực hiện nhiệm vụ thay thế; nếu do phân công cắt cử chưa khoa học, hoặc do cường độ vận chuyển quá mức, hoặc do sức khỏe không đáp ứng được thì phải điều chỉnh lại cho phù hợp.
- Trường hợp quân nhân ngại đi vận chuyển thì trực tiếp gặp gỡ, nắm nguyên nhân, đồng thời giáo dục cho bộ đội nhận thức sâu sắc trách nhiệm, vinh dự tự hào khi được đơn vị lựa chọn đi thực hiện nhiệm vụ.
- Nếu quân nhân nảy sinh tư tưởng do ngại khó, ngại khổ, sợ vất vả nguy hiểm nên không muốn thực hiện nhiệm vụ vận chuyển mà chỉ huy các cấp đã quán triệt, giáo dục, động viên thì chỉ định dừng thực hiện nhiệm vụ, cử người khác thay thế và tổ chức sinh hoạt kiểm điểm xử lý kỷ luật theo điều lệnh, quy định của quân đội và pháp luật Nhà nước.
- Phát huy vai trò của Chi đoàn, HĐQN và các mối quan hệ bạn bè, đồng hương, người thân, gia đình để giáo dục, động viên chiến sỹ có nhận thức tốt về nhiệm vụ, tích cực tham gia các nhiệm vụ vận chuyển.
- Hướng dẫn chỉ đạo đơn vị sinh hoạt rút kinh nghiệm về công tác quản lý tư tưởng và chấp hành kỷ luật; xây dựng động cơ, trách nhiệm trong nhiệm vụ vận chuyển; phát động thi đua trong vận chuyển .…Động viên chiến sỹ tích cực tham gia.
- Tiếp tục theo dõi, quan tâm, động viên, củng cố lòng tin đối với các quân nhân thực hiện nhiệm vụ và nhất là đồng chí có biểu hiện nảy sinh tư tưởng không muốn thực hiện nhiệm vụ nơi khó khăn, vất vả.
- Kịp thời biểu dương tập thể, cá nhân có thành tích trong vận chuyển, làm tốt công tác nhân rộng điển hình tiên tiến; tổ chức rút kinh nghiệm đối với đội ngũ cán bộ về quá trình xử lý.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 12: Đơn vị nhận được lệnh đi cứu hộ, cứu nạn tàu ngư dân gặp nạn trên biển do áp thấp nhiệt đới gần bờ, một số cán bộ, chiến sĩ hoang mang, lo lắng?
Gợi ý biện pháp xử lý:
- Cấp ủy, chỉ huy đơn vị trực tiếp nắm tình hình tâm tư, nguyện vọng của cán bộ, chiến sĩ trực tiếp tham gia thực hiện nhiệm vụ cứu hộ, cứu nạn. 
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật của cán bộ, chiến sĩ trong thực hiện nhiệm cứu hộ, cứu nạn tàu ngư dân gặp nạn trên biển. Thống nhất biện pháp giải quyết, phân công cán bộ phụ trách.
- Gặp gỡ giáo dục, động viên những cán bộ, chiến sĩ có tâm lý lo lắng trong thực hiện nhiệm vụ khó khăn phức tạp hiểu rõ vinh dự, trách nhiệm, quyền lợi, nghĩa vụ, xây dựng ý chí quyết tâm hoàn thành tốt nhiệm vụđược giao.
- Thường xuyên làm tốt công tác quán triệt, giáo dục về tính chất, đặc điểm của nhiệm vụ cho cán bộ, chiến sĩ nâng cao ý thức trách nhiệm, khắc phục khó khăn trong thực hiện nhiệm vụ.
- Tổ chức bồi dưỡng kinh nghiệm cho những cán bộ, chiến sĩ mới tham gia thực hiện nhiệm vụ lần đầu, xây dựng niềm tin vào khả năng bản thân, đơn vị và tình trạng kỹ thuật phương tiện tàu thuyền của đơn vị có đủ khả năng hoàn thành tốt nhiệm vụcứu hộ, cứu nạn trên biển.
- Thường xuyên bảo đảmcác trang thiết bị có độ an toàn cao phục vụ cho công tác cứu hộ, cứu nạn; thực hiện đúng nguyên tắc bảo đảm an toàn trong suốt quá trình thực hiện nhiệm vụ.
- Quan tâm bảo đảm tiêu chuẩn, chế độ chính sách cho cán bộ, chiến sĩ yên tâm, gắn bó với nhiệm vụ.
- Kết thúc nhiệm vụ làm tốt công tác rút kinh nghiệm, kịp thời biểu dương khen thưởng những tập thể, cá nhân hoàn thành tốt nhiệm vụ. Thẳng thắn chỉ ra những hạn chế tồn tại.
- Tổ chức sinh hoạt rút kinh nghiệm sau mỗi lần thực hiện nhiệm vụ cứu hộ, cứu nạn để cho cán bộ, chiến sĩ tự tin với nhiệm vụ.
Tình huống 13: Do mưa bão lâu dài nên Điểm cao sau nhà ở đơn vị bị sụt lở và có nhiều đường nứt, có thể gây nguy hiểm nên một số cán bộ, chiến sĩ có biểu hiện tư tưởng băn khoăn, lo lắng.
Gợi ý biện pháp xử lý: 
- Thông báo ngay cho các đơn vị nhanh chóng cơ động về về tạm trú tại vị trí an toàn.
- Báo cáo tình hình về Thủ trưởng cấp trên (thông qua trực ban tác chiến, trực ban cơ quan cấp trên); đồng thời, xin ý kiến chỉ đạo của Thủ trưởng cấp trên.
- Triển khai cho đơn vị làm tốt công tác giáo dục chính trị tư tưởng, giáo dục quán triệt tác hại của sự sụt lỡ và những thuận lợi, khó khăn trong công tác phòng, chống thiên tai, bão lụt, tìm kiếm cứu nạn; xây dựng ý chí quyết tâm cho cán bộ, chiến sỹ tích cực chủ động làm tốt công tác chuẩn bị sẵn sàng nhận và hoàn thành mọi nhiệm vụ được giao.
- Thường xuyên nắm tình hình đơn vị mình, nhất là những đơn vị bị ảnh hưởng; kịp thời động viên CB,CS an tâm tư tưởng, bình tĩnh, không giao động, lo sợ; Tập trung triển khai làm tốt công tác chuẩn bị, theo phương châm 4 tại chỗ, trước hết là chuẩn bị lực lượng, cơ sở vật chất, phương tiện, trang bị…
- Tiến hành kiểm tra, khảo sát khu vực, nhất là các vị trí trọng điểm về chất đất, những nơi có biểu hiện nứt, dễ sụt lỡ ….đề xuất biện khắc phục
- Dự kiến khu vực sơ tán người, tài sản đơn vị, cá nhân và xác định bãi đỗ phương tiện tham gia cứu hộ cứu nạn…
- Thông báo cho cấp ủy và chính quyền địa phương trên địa bàn để phối hợp trong xử lý tình hình; đồng thời tuyên truyền đưa tin hoạt động của cán bộ, chiến sỹ tham gia khắc phục sạt lỡ 
- Sau khi hoàn thành nhiệm vụ:
+ Nhanh chóng tổng hợp tình hình báo cáo nhanh cấp trên theo phân cấp; 
+ Hướng dẫn, chỉ đạo các cơ quan, đơn vị nắm diễn biến tình hình tư tưởng CB, CS, tổ chức hội nghị rút kinh nghiệm kịp thời biểu dương, khen thưởng những tập thể cá nhân có thành tích xuất sắc trong tham gia khắc phục hậu quả thiên tai, đồng thời phê bình, nhắc nhỡ những tập thể cá nhân có biểu hiện hoang mang, lo sợ không hoàn thành nhiệm vụ khi được phân công.
+ Bám sát diễn biến tình hình, phát hiện giải quyết kịp thời những biểu hiện ngại khó khăn, gian khổ, giảm sút ý chí, tư tưởng giao động; tổ chức tốt phong trào thi đua và thực hiện tốt công tác chính sách đối với cán bộ, chiến sỹ trong đơn vị.
+ Bổ sung hoàn thiện kế hoạch CTĐ, CTCT trong phòng chống thiên tai, cứu hộ cứu nạn.
Tình huống 14: Trong đơn vị có gia đình một đồng chí hạ sĩ quan (chiến sĩ) gặp mưa bão, nhà cửa bị đất đá sạt lở vùi lấp, không bị thiệt hại về người, có biểu hiện hoang mang, lo lắng
Gợi ý biện pháp xử lý:
- Nắm chắc tâm tư, hoàn cảnh cụ thể gia đình quân nhân thông qua các nguồn tin các mối quan hệ của quân đó (các cấp báo cáo) từ đó xác định biện pháp cách thức giải quyết.
- Tiến hành gặp gỡ, trò chuyện, nắm tâm tư, nguyện vọng, những vướng mắc của quân nhân có hoàn cảnh khó khăn; từ đó động viên, chia sẻ, giúp đỡ quân nhân đó vượt qua khó khăn, yên tâm công tác xác định rõ nhiệm vụ.
- Báo cáo chỉ huy cấp trên để cùng theo dõi động viên xác định biện pháp giải quyết.
- Chỉ đạo trung đội (đại đội) có quân nhân gặp hoàn cảnh khó khăn phân công cán bộ, đảng viên, đoàn viên ưu tú theo dõi, động viên giúp đỡ quân nhân có gia đình gặp khó khăn hoàn thành nhiệm vụ.
- Chỉ đạo đơn vị có biện pháp tác động với những quân nhân khác là bạn bè thân thiết, đồng hương… với chiến sĩ gặp khó khăn để cùng chia sẻ, động viên, an ủi.
- Trường hợp (xét thấy cần thiết) đề nghị cấp có thẩm quyền giải quyết cho quân nhân đi phép về giải quyết việc gia đình.
- Đề nghị tập thể đơn vị và chỉ huy cấp trên quan tâm động viên giúp đỡ chiến sĩ gặp khó khăn về vật chất và tinh thần để góp phần giải quyết khó khăn (đề nghị trợ cấp khó khăn cho quân nhân đó theo quy định).
- Nếu có điều kiện đề nghị chỉ huy cấp trên cử cán bộ về thăm hỏi, động viên gia đình quân nhân đó.
Tình huống 15: Khi đơn vị thực hiện nhiệm vụ giúp Nhân dân chữa cháy rừng do điều kiện gió to, không may một chiến sĩ bị bỏng nặng gây tâm lý hoang mang, lo lắng đối với cán bộ, chiến sĩ trong đơn vị.
Gợi ý các biện pháp xử lý:
- Nhanh chóng bằng mọi biện pháp tiến hành sơ cứu cho chiến sĩ bị bỏng (đúng quy trình sơ cứu ban đầu, không để nặng thêm) và đưa đến bệnh viện gần nhất để kịp thời cứu chữa.
- Trao đổi, thống nhất nhanh trong chỉ huy đơn vị, phân công cán bộ phụ trách trên từng vị trí.
- Tổng hợp tình hình báo cáo cấp trên đúng quy định.
- Động viên cán bộ, chiến sĩ bình tĩnh, thực hiện tốt các quy định về công tác bảo đảm an toàn, tiếp tục thực hiện nhiệm vụ chữa cháy rừng.
- Tập trung lực lượng, phương tiện tạo ranh giới lửa để đám cháy không lan rộng xung quanh, nếu cần thiết đề nghị hỗ trợ thêm lực lượng, phương tiện để dập tắt đám cháy.
- Khi đám cháy được dập tắt, tổ chức thu quân, kiểm tra lại tình hình mọi mặt, cơ động về đơn vị tiến hành sinh hoạt rút kinh nghiệm về tổ chức thực hiện nhiệm vụ và công tác bảo đảm an toàn.
- Vận động cán bộ, chiến sĩ thực hiện tinh thần tương thân, tương ái giúp đỡ đồng đội bị bỏng, cử cán bộ thăm hỏi động viên chiến sĩ nằm viện.
- Phối hợp với cơ quan chức năng của địa phương, đơn vị thực hiện tốt công tác chính sách đối với quân nhân gặp nạn trong quá trình thực hiện nhiệm vụ.
- Tổng hợp tình hình mọi mặt báo cáo cấp trên.
Tình huống 16: Trong quá trình thực hiện nhiệm vụ giúp đỡ Nhân dân phòng, chống lụt bão, không may một chiến sĩ bị hy sinh gây hoang mang, lo lắng trong đơn vị 
Gợi ý biện pháp xử lý:
- Cán bộ trực tiếp chỉ huy nhanh chóng tổ chức cứu chữa cho chiến sĩ bị hy sinh (nếu còn cơ hội), đưa chiến sĩ bị hy sinh lên vị trí an toàn, nắm tình hình báo cáo chỉ huy cấp trên.
- Nhanh chóng hội ý, thống nhất trong cấp ủy, chỉ huy đơn vị đánh giá tình hình, xác định nguyên nhân ban đầu và biện pháp xử lý.
- Tiến hành thông báo ngay cho gia đình (thân nhân) chiến sĩ hy sinh.
- Phối hợp chặt chẽ với các cấp tiến hành điều tra, kết luận và làm rõ nguyên nhân xảy ra mất an toàn khi thực hiện nhiệm vụ; thống nhất biện pháp giải quyết hậu quả.
- Đội ngũ cán bộ các cấp tiếp tục bám sát quá trình thực hiện nhiệm vụ của đơn vị, động viên, nhắc nhở bộ đội ổn định tư tưởng, tâm lý; không để bộ đội hoảng loạn, lo lắng, gây xáo trộn trong các bộ phận.
- Phối hợp với địa phương tiến hành giải quyết hậu quả theo đúng quy định, đúng chức năng, nhiệm vụ, quyền hạn và điều kiện thực tế của đơn vị.
- Động viên cán bộ, chiến sĩ trong đơn vị bằng vật chất, tinh thần chia sẻ, giúp đỡ với gia đình chiến sĩ hy sinh; phối hợp cùng gia đình tổ chức lễ mai táng chu đáo, đúng phong tục, tập quán của địa phương.
- Tổ chức sinh hoạt cấp ủy, chi bộ, đội ngũ cán bộ và đơn vị để thông báo kết luận điều tra của cấp trên; kiểm điểm làm rõ trách nhiệm, rút ra bài học kinh nghiệm trong công tác lãnh đạo, chỉ đạo và tổ chức thực hiện nhiệm vụ của đơn vị trong thời gian tiếp theo để bảo đảm an toàn tuyệt đối; xem xét trách nhiệm và tiến hành xử lý kỷ luật đối với cán bộ chỉ huy trực tiếp và liên đới trách nhiệm.
- Thực hiện tốt các chế độ, chính sách đối với quân nhân hy sinh khi thực hiện nhiệm vụ.
- Tổng hợp tình hình giải quyết vụ việc báo cáo cấp trên theo quy định.
II. NHÓM TÌNH HUỐNG TƯ TƯỞNG CÓ THỂ NẢY SINH TRONG THỰC HIỆN NHIỆM VỤ HUẤN LUYỆN, SẴN SÀNG CHIẾN ĐẤU, XÂY DỰNG CHÍNH QUY, RÈN LUYỆN KỶ LUẬT (10 tình huống)
Tình huống 1. Từ một số vụ việc HSQ-BS (học viên) bị tai nạn trong quá trình đơn vị tổ chức bắn đạn thật, cá biệt đã có quân nhân dùng súng tự sát ngay trong quá trình thực hành bắn, đã gây tâm lý băn khoăn, lo lắng cho một số sĩ quan được giao nhiệm vụ chỉ huy bắn (TH3; QĐ3, TrSQLQ1 2022).
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình, chất lượng huấn luyện và kết quả bắn súng, xác định nguyên nhân, thống nhất biện pháp bồi dưỡng. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Rà soát, phân loại tâm lý, khả năng bắn súng của từng quân nhân; giáo dục, quán triệt làm cho quân nhân nắm vững mục tiêu, yêu cầu, chức trách, nhiệm vụ, qua đó nâng cao ý thức học tập, rèn luyện kỹ năng bắn súng. 
- Phân công cán bộ có kinh nghiệm kèm cặp, giúp đỡ, kỹ năng, phương pháp bắn súng, giúp quân nhân tin tưởng vào khả năng của bản thân, kiên trì luyện tập.
-  Duy trì nghiêm nền nếp chế độ huấn luyện quân sự, kiểm tra bắn súng theo quy định. Thực hiện nghiêm quy trình huấn luyện, tổ chức bắn súng chặt chẽ; chú trọng làm tốt công tác kiểm tra, rà soát, đánh giá toàn diện các yếu tố, có phương án bảo đảm an toàn trong suốt quá trình trước, trong và sau khi thực hành bắn. 
- Bồi dưỡng nâng cao bản lĩnh, kỹ năng tổ chức thực hành bắn cho đội ngũ cán bộ phân đội; luyện tập thuần thục phương án xử trí các tình huống bất chắc, mất an toàn có thể xảy ra.
Tình huống 2. Một số cán bộ (có cả cán bộ chủ trì) trong đơn vị có biểu hiện che giấu khuyết điểm, chạy theo thành tích, thiếu công tâm, khách quan trong giải quyết công việc, gây dư luận không tốt trong đơn vị.
Gợi ý biện pháp xử lý
- Kịp thời rà soát, nắm tình hình tư tưởng của quân nhân trong đơn vị; kịp thời phát hiện những biểu hiện che giấu khuyết điểm, chạy theo thành tích, thiếu công tâm, khách quan trong giải quyết công việc.
- Họp cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật, dư luận của quân nhân; xác định đối tượng, hành vi, hậu quả, nguyên nhân dẫn đến hành vi che giấu khuyết điểm, chạy theo thành tích; thống nhất biện pháp khắc phục.
- Gặp gỡ giáo dục, chấn chỉnh những cá nhân có biểu hiện, hành vi vi phạm; phân tích rõ tác hại, hậu quả của biểu hiện che giấu khuyết điểm, chạy theo thành tích, thiếu công tâm, khách quan là vi phạm quy định của quân đội về chế độ báo cáo, xin ý kiến chỉ thị, vi phạm chế độ trách nhiệm của người chỉ huy, ảnh hưởng chất lượng, kết quả, xây dựng chi bộ TSVM, đơn vị VMTD. 
- Tổ chức sinh hoạt đơn vị giáo dục, tuyên truyền cho SQ, QNCN nhận thức sâu sắc vị trí, ý nghĩa của đánh giá đúng thực chất tình hình đơn vị để xây dựng chi bộ TSVM, đơn vị VMTD; qua đó có biện pháp đấu tranh quan điểm, tư tưởng báo cáo không trung thực, che dấu khuyết điểm, chạy theo thành tích, thiếu công tâm, khách quan trong đơn vị.
- Thực hiện tốt nền nếp tự phê bình và phê bình; phát huy trách nhiệm tự soi, tự sửa của mỗi cấp ủy, tổ chức đảng và mỗi cán bộ, đảng viên; tăng cường kiểm tra, giám sát việc thực hiện nguyên tắc tập trung dân chủ, kỷ luật, kỷ cương, sự đoàn kết, thống nhất nội bộ; tránh dân chủ hình thức, khắc phục cách làm việc tắc trách, trì trệ, hoặc lạm dụng quyền lực xâm phạm nguyên tắc.
- Thực hiện tốt Quy chế dân chủ ở cơ sở, phát huy vai trò giám sát, phản biện của các tổ chức và cá nhân đối với việc thực hiện nguyên tắc của Đảng. 
- Đề cao vai trò của người đứng đầu, cán bộ chủ chốt trong giữ vững và phòng, chống tình trạng xa rời nguyên tắc tập trung dân chủ, nhất là bí thư cấp ủy; nỗ lực học tập, rèn luyện phong cách, phương pháp làm việc dân chủ, khoa học, tạo bầu không khí dân chủ trong tổ chức.
- Cầu thị lắng nghe ý kiến phản ánh về việc thực hiện nguyên tắc tập trung dân chủ ở đơn vị và định kỳ lấy phiếu tín nhiệm của cán bộ các cấp, nhất là người đứng đầu, cán bộ chủ trì, chủ chốt. Phát huy vai trò của tổ chức quần chúng, hội đồng quân nhân và tập thể quân nhân trong việc phản ánh những biểu hiện vi phạm nguyên tắc tập trung dân chủ.
- Tham mưu đề xuất rà soát bổ sung, sửa đổi các quy định, quy chế báo cáo, xin chỉ thị của các tổ chức; khắc, phục biểu hiện che giấu khuyết điểm, chạy theo thành tích, đáp ứng yêu cầu, nhiệm vụ xây dựng đơn vị trong tình hình mới.
- Xây dựng tốt tinh thần đoàn kết trên cơ sở nguyên tắc, quy định, kỷ luật của Đảng, pháp luật Nhà nước, kỷ luật quân đội. Chống mọi biểu hiện lợi ích nhóm, cục bộ, bè phái.
- Duy trì nghiêm chế độ báo cáo, phản ánh tình hình về tư tưởng, kỷ luật bộ đội trong đơn vị, nhất là những khó khăn vướng mắc, có biện pháp giúp đỡ kịp thời; phê bình thẳng thắn đối với cá nhân báo cáo không trung thực, chạy theo thành tích, giải quyết kịp thời mọi tình huống phát sinh và xử lý nghiêm kỷ luật đối với những trường hợp vi phạm.
Tình huống 3. Thực hiện lộ trình thực hiện tổ chức Quân đội nhân dân Việt Nam giai đoạn 2021 - 2030 và những năm tiếp theo, theo đó một số cán bộ có tâm lý băn khoăn về vị trí, đơn vị công tác khi có sự điều chỉnh tổ chức.
Gợi ý biện pháp xử lý
- Tuyên truyền, phổ biến làm cho quân nhân nhận thức sâu sắc chủ trương của Đảng, của QUTW về tổ chức Quân đội nhân dân Việt Nam giai đoạn 2021 - 2030 và những năm tiếp theo; nắm rõ lộ trình, đối tượng, chế độ chính sách..., đồng thuận với đường lối, chủ trương, quan điểm của Đảng, pháp luật Nhà nước, xác định tinh thần, trách nhiệm, sẵn sàng nhận và hoàn thành tốt nhiệm vụ.
- Nắm bắt tâm tư, nguyện vọng, hoàn cảnh, điều kiện gia đình của quân nhân, nhất là đối tượng trong diện điều chỉnh; kịp thời tham mưu, đề xuất biện pháp giải quyết phù hợp với từng đối tượng, đáp ứng yêu cầu nhiệm vụ.
- Bảo đảm đầy đủ tiêu chuẩn, chế độ, chính sách theo đúng quy định của Bộ Quốc phòng, giúp cho các đối tượng trong diện điều chỉnh ổn định cuộc sống gia đình, yên tâm nhận nhiệm vụ.
- Tổng hợp tình hình và báo cáo cấp trên.
Tình huống 4. Một số cán bộ chưa được bố trí công việc phù hợp với nguyện vọng và chuyên môn đào tạo đã phát sinh tâm lý băn khoăn, hoài nghi từ phía gia đình, nên nảy sinh tư tưởng, thiếu yên tâm công tác, chất lượng hoàn thành nhiệm vụ không cao.
Gợi ý biện pháp xử lý
 - Rà soát tình hình tổ chức, biên chế của đơn vị, công tác bố trí sử dụng nguồn nhân lực, nắm chắc số, chất lượng của từng đối tượng, nhất là các vị trí trọng yếu, chuyên ngành chuyên sâu, đào tạo dài hạn…
- Nắm tình hình, tìm hiểu nguyên nhân của việc bố trí lực lượng trái với chuyên ngành đào tạo; tâm tư, nguyện vọng của quân nhân. 
 - Hội ý lãnh đạo, chỉ huy đánh giá thực trạng tình hình biên chế, tổ chức và những vấn đề tư tưởng trong đơn vị, thống nhất biện pháp giải quyết; báo cáo cấp trên xin ý kiến chỉ đạo.
 - Gặp gỡ giáo dục, động viên các quân nhân trong diện bố trí công việc trái với chuyên ngành đào tạo, giúp quân nhân nắm vững tình hình, đặc điểm, yêu cầu, nhiệm vụ, cơ cấu tổ chức biên chế đơn vị và việc sắp xếp một số chức danh chưa phù hợp, qua đó xác định tư tưởng, trách nhiệm, khắc phục khó khăn, hoàn thành tốt nhiệm vụ được phân công.
- Tổ chức sinh hoạt quán triệt, rút kinh nghiệm cho quân nhân nhận thức đúng về yêu cầu tổ chức biên chế của đơn vị, trình độ chuyên môn đào tạo, nâng cao ý thức chấp hành sự phân công công tác của cấp ủy đảng, chỉ huy.
- Tổ chức tập huấn, bồi dưỡng kiến thức, kỹ năng, kinh nghiệm, phương pháp công tác giúp các quân nhân trong diện bố trí công việc trái với chuyên ngành đào tạo có đủ năng lực, đáp ứng yêu cầu nhiệm vụ, yên tâm công tác. 
- Chấp hành nghiêm các quy định về tổ chức biên chế, sử dụng lực lượng; bảo đảm dân chủ, công khai, công bằng, phát huy trình độ năng lực công tác.
- Quan tâm chăm lo đời sống vật, chất tinh thần, chính sách hậu phương quân đội cho QNCN phấn khởi, yêu tâm gắn bó xây dựng đơn vị.
Tình huống 5. Một số cán bộ, nhất là cán bộ trẻ có biểu hiện dựa dẫm vào mối quan hệ với cấp trên và người thân, thiếu rèn luyện phấn đấu, giải quyết mối quan hệ cấp trên, cấp dưới, đồng chí, đồng đội không chuẩn mực, gây bất bình trong đơn vị.
Gợi ý biện pháp xử lý
-Tăng cường giáo dục cho quân nhân toàn đơn vị ý thức chấp hành pháp luật Nhà nước, kỷ luật Quân đội, quy định của đơn vị. Xây dựng ý thức tự rèn luyện phẩm chất đạo đức cách mạng của người quân nhân.
- Gặp gỡ quân nhân giáo dục nhận thức đúng, sai, tác hại của việc dựa dẫm ỷ lại, chấp hành kỷ luật không nghiêm.
- Phối hợp với gia đình, địa phương trong việc động viên quân nhân thực hiện chức trách, nhiệm vụ, ý thức chấp hành kỷ luật.
- Quản lý chặt chẽ quân nhân, dự báo những dấu hiệu vi phạm, kịp thời ngăn chặn.
- Duy trì nghiêm chế độ ngày, tuần.
- Báo cáo cấp trên xin ý kiến chỉ đạo.
Tình huống 6. Từ một số vụ việc cháy, nổ vũ khí, đạn xảy ra ở một số đơn vị, một số cán bộ làm nhiệm vụ quản lý, bảo quản, vũ khí, súng đạn; nhiệm vụ sản xuất thuốc phóng, thuốc nổ, nhất là tại các kho chứa vũ khí, đạn có niên hạn sản xuất lâu năm, đã nảy sinh tư tương băn khoăn, lo lắng.
 Gợi ý biện pháp xử lý
- Nắm chắc tình hình tư tưởng, kỷ luật QNCN, thực trạng trang bị, vũ khí, kỹ thuật, công tác bảo đảm an toàn kho tàng của đơn vị, tham mưu cho cấp ủy, chỉ huy giải quyết. 
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình, tư tưởng QNCN làm công tác bảo quản, bảo dưỡng vũ khí trang bị kỹ thuật và những yếu tố tác động bảo đảm an toàn kho tàng, thống nhất biện pháp khắc phục.
- Gặp gỡ số QNCN làm công tác bảo quản vũ khí trang bị kỹ thuật, động viên ổn định tư tưởng, tâm lý, tự tin vào khả năng chuyên môn nghiệp vụ, quy trình, nguyên tắc bảo quản, bảo dưỡng, sử dụng súng đạn đã được học tập trang bị.
- Tổ chức tập huấn cho SQ, QNCN về quy trình, quy tắc, phương pháp bảo quản, bảo dưỡng, vũ khí súng đạn, nắm vững tính năng, niên hạn sử dụng các loại vũ khí, tạo tâm lý thoải mái, yên tâm thực hiện nhiệm vụ được giao.
- Làm tốt công tác rà soát phân loại đạn dược theo phân cấp, quá niên hạn sử dụng, báo cáo cấp trên xử lý.
- Thường xuyên tổ chức kiểm tra bổ sung, củng cố trang thiết bị phục vụ cho công tác bảo quản vũ khí, khí tài bảo đảm an toàn.
- Quan tâm chăm lo bảo đảm chế độ, tiêu chuẩn đời sống vật chất, tinh thần theo quy định của quân đội, để cho QNCN yên tâm, gắn bó với nhiệm vụ.
 Tình huống 7. Khi cán bộ kiểm tra gác phát hiện chiến sĩ làm nhiệm vụ gác chấp hành không nghiêm quy định đã có lời nói, hành vi chấn chỉnh thái quá, xúc phạm đến bản thân và gia đình quân nhân, làm cho quân nhân bức xúc hành hung lại cán bộ.
Gợi ý biện pháp xử lý
- Nhanh chóng ngăn chặn chiến sỹ có biểu hiện quấy rối do say rượu, sử dụng lực lượng khống chế, bố trí quân y kiểm tra chăm sóc sức khỏe; triển khai các biện pháp cần thiết ổn định tình hình đơn vị; bố trí chiến sỹ thay thế gác.
- Hội ý chỉ huy đơn vị đánh giá, nhận định tình hình tư tưởng, kỷ luật chiến sỹ và phương pháp quản lý, chỉ huy của đồng chí trung đội trưởng, thống nhất biện pháp giải quyết.
- Triển khai cho cán bộ trung đội trưởng và chiến sỹ viết bản tường trình, bản tự kiểm điểm, sinh hoạt đơn vị phân tích hiểu rõ hạn chế khuyết điểm, hậu quả, tác hại của vi phạm quy định canh phòng, phương pháp quản lý bộ đội của cán bộ, đề nghị hình thức kỷ luật bảo đảm khách quan, chính xác.

- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho cán bộ, chiến sỹ nâng cao ý thức chấp hành nghiêm điều lệnh canh phòng, quy định về uống rượu, bia trong khi thực hiện nhiệm vụ, phương pháp giáo dục, quản lý, chỉ huy bộ đội của đội ngũ cán bộ các cấp.
- Duy trì nghiêm chế độ, nền nếp xây dựng đơn vị chính quy, quản lý chặt chẽ tư tưởng, kỷ luật và các mối quan hệ xã hội của bộ đội để có biện pháp giáo dục khắc phục kịp thời.
- Gặp gỡ đồng chí trung đội trưởng giáo dục, nhận rõ việc làm sai trái, có biện pháp khắc phục, sửa chữa; nâng cao kỹ năng, phương pháp giáo dục, quản lý chỉ huy bộ đội theo đúng quy định quân đội, đơn vị, khắc phục cách xử phạt vi phạm nhân cách quân nhân. 
- Thường xuyên giáo dục cho chiến sỹ nâng cao ý thức, trách nhiệm chấp hành nghiêm kỷ luật quân đội, quy định canh phòng bảo đảm đúng tư thế tác phong quân nhân, bảo đảm an toàn đơn vị và địa bàn đóng quân. 
- Quan tâm chăm lo đời sống vật chất, tinh thần cho chiến sỹ, yên tâm, gắn bó với nhiệm vụ.
 - Báo cáo cấp trên theo quy định.
Tình huống 8. Một chiến sĩ có biểu hiện tự do, phát ngôn thiếu chuẩn mực, chấp hành không nghiêm quy định của đơn vị, bị kiểm điểm, kỷ luật... ảnh hưởng đến tập thể khi phải sinh hoạt nhiều lần; một số chiến sĩ đã bức xúc, hành hung đồng đội.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị nhận định, đánh giá tình hình tư tưởng quân nhân và dư luận trong đơn vị, phân tích làm rõ thực trạng, xác định đối tượng, nguyên nhân vi phạm kỷ luật của hạ sĩ quan - chiến sĩ; thống nhất chủ trương, biện pháp giải quyết.
- Phân công cán bộ gặp gỡ chiến sĩ hay vi phạm kỷ luật để nắm bắt tâm tư, nguyện vọng, nguyên nhân vi phạm khuyết điểm và tác hại của việc mất đoàn kết trong nội bộ; qua đó giáo dục, thuyết phục, nâng cao ý thức tự giác chấp hành kỷ luật quân đội, quy định đơn vị, tích cực tham gia xây dựng đơn vị. Với các quân nhân vi phạm, triển khai viết bản tường trình, kiểm điểm, sinh hoạt đơn vị kiểm điểm và đề nghị hình thức kỷ luật, nghiêm túc, chặt chẽ (nếu đến mức phải xử lý kỷ luật).
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho chiến sỹ nâng cao ý thức chấp hành kỷ luật quân đội, quy định đơn vị, tích cực học tập, rèn luyện nâng cao phẩm chất, đạo đức tư cách người quân nhân cách mạng, giữ gìn phẩm chất tốt đẹp "Bộ đội Cụ Hồ”, tình thần đoàn kết giúp đỡ lẫn nhau, xây dựng đơn vị vững mạnh.
- Duy trì nghiêm chế độ nền nếp xây dựng đơn vị chính quy, quản lý chặt chẽ tình hình tư tưởng, kỷ luật và các mối quan hệ xã hội của bộ đội, nhất là trong ngày nghỉ, giờ nghỉ, hoạt động ngoài doanh trại để có biện pháp giáo dục kịp thời.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị; tổ chức tốt hoạt động văn hóa tinh thần, tạo không khí vui tươi, lành mạnh; quan tâm chăm lo đời sống vật chất, tinh thần, kịp thời động viên cán bộ, chiến sĩ yên tâm, gắn bó xây dựng đơn vị. 
	Tình huống 9. Trong đơn vị có một số HSQ-BS chấp hành không nghiêm quy định sử dụng điện thoại của đơn vị, cá biệt có quân nhân khi uống rượu say đã hành hung cán bộ khi bị ngăn cấm sử dụng điện thoại di động.
Gợi ý biện pháp xử lý
- Nhanh chóng bố trí chiến sĩ thay thế làm nhiệm vụ gác; sử dụng lực lượng khống chế, ngăn chặn chiến sĩ có biểu hiện quấy rối do say rượu; chỉ đạo quân y kiểm tra, chăm sóc sức khỏe; triển khai các biện pháp cần thiết ổn định tình hình đơn vị.
- Hội ý chỉ huy đơn vị đánh giá, nhận định tình hình tư tưởng, kỷ luật chiến sỹ và phương pháp quản lý, chỉ huy của đồng chí trung đội trưởng, thống nhất biện pháp giải quyết.
- Triển khai cho cán bộ, chiến sĩ có liên quan viết bản tường trình, kiểm điểm; tổ chức sinh hoạt đơn vị, phân tích làm rõ khuyết điểm, lỗi phạm, tác hại, hậu quả của hành vi hành hung cán bộ và việc sử dụng rượu bia, điện thoại sai quy định; phương pháp, tác phong công tác của của cán bộ; xem xét, đề nghị hình thức kỷ luật bảo đảm khách quan, chính xác.
- Nắm tình hình tư tưởng, việc chấp hành quy định sử dụng rượu bia, điện thoại di động, Internet, mạng xã hội của hạ sĩ quan - binh sĩ, đề xuất các biện pháp giải quyết cho cấp ủy, chỉ huy đơn vị. 
- Thường xuyên giáo dục, quán triệt, tuyên truyền phổ biến nâng cao nhận  thức của cán bộ, chiến sĩ, tự giác chấp hành nghiêm Luật phòng, chống tác hại của rượu, bia và các chỉ thị, quy định, hướng dẫn sử dụng điện thoại di động, Internet, mạng xã hội, nhất là quy định về việc sử dụng điện thoại di động đối với hạ sĩ quan - binh sĩ. Tổ chức các buổi tọa đàm, sân khấu hóa trong các hội thi, hội diễn văn nghệ quần chúng để nâng cao nhận thức cho quân nhân về việc uống rượu, bia say, bê tha và sử dụng điện thoại sai quy định.
- Duy trì nghiêm chế độ, nền nếp xây dựng đơn vị chính quy, quản lý chặt chẽ tư tưởng, kỷ luật và các mối quan hệ xã hội của bộ đội để có biện pháp giáo dục khắc phục kịp thời.
- Phối hợp với địa phương và gia đình hạ sĩ quan - binh sĩ làm tốt công tác quản lý, giáo dục làm cho quân nhân nhận thức đúng và chấp hành quy định của đơn vị về sử dụng điện thoại di động.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị; quan tâm chăm lo đời sống vật chất, tinh thần, kịp thời động viên cán bộ, chiến sĩ yên tâm, gắn bó xây dựng đơn vị; có biện pháp đáp ứng nhu cầu thông tin chính đáng cho hạ sĩ quan - binh sĩ.
- Tổng hợp tình hình, báo cáo cấp trên.
Tình huống 10. Trong đơn vị xảy ra 01 trường hợp chiến sĩ tử vong trong trạng thái treo cổ; đơn vị đã tiến hành các bước giải quyết vụ việc; song do công tác cung cấp thông tin, phối hợp giải quyết chưa chu đáo, chặt chẽ, nên gia đình đã nảy sinh hoài nghi về nguyên nhân, phát tán thông tin, hình ảnh trên mạng xã hội, tạo kẽ hở để các thế lực phản động lợi dụng xuyên tạc chống phá, gây bức xúc dư luận, ảnh hưởng an ninh chính trị, trật tự an toàn xã hội.
Gợi ý biện pháp xử lý
	- Phân công cán bộ có uy tín, kinh nghiệm thay mặt chỉ huy đơn vị, đón tiếp và nắm nguyện vọng của gia đình chiến sĩ.
	- Báo cáo cấp trên xin ý kiến chỉ đạo, mời cơ quan chức năng xuống đơn vị phối hợp giải quyết vụ việc.
	- Trao đổi thống nhất trong cấp uỷ, chỉ huy đơn vị, phân công cán bộ phụ trách giải quyết vụ việc và ổn định tình hình đơn vị 
	- Mời một số cán bộ, chiến sĩ trực tiếp chứng kiến vụ việc và một số chiến sĩ cùng quê với gia đình lên cùng với chỉ huy đơn vị làm việc với gia đình chiến sĩ.
	- Cung cấp cho gia đình một số thông tin về kết quả làm việc của cơ quan chức năng như: Biên bản vụ việc, kết quả giám định pháp y, các chế độ chính sách đơn vị đã chi trả với chiến sĩ và các hoạt động hỗ trợ của cán bộ chiến sĩ đơn vị đối với gia đình (nếu có); trao đổi, chia sẻ cùng gia đình về những đau thương mất mát; cùng với các thành phần trong buổi làm việc, phân tích để gia đình hiểu rõ bản chất sự việc, động viên gia đình tin tưởng vào quy trình giải quyết của đơn vị và các cơ quan chức năng, không nghe theo luận điệu xuyên tạc; phối hợp chặt chẽ với đơn vị để lo hậu sự cho quân nhân theo phong tục, để giảm bớt nỗi khổ đau cho gia đình... (chú ý trong khi làm việc với gia đình cần có biên bản, ghi lại diễn biến, kết quả làm việc và ý kiến của gia đình, tránh về sau gia đình tiếp tục có ý kiến với đơn vị).
	- Phân công cán bộ kịp thời báo cáo xin ý kiến chỉ đạo của cấp trên và cung cấp thông tin, định hướng dư luận; phối hợp chặt chẽ với cấp ủy, chính quyền, các đoàn thể, cơ quan quân sự và những người có uy tín ở địa phương tập trung mọi nỗ lực cao nhất, tiến hành đồng bộ công tác tuyên truyền vận động với các biện pháp khác nhằm ổn định tình hình, giữ vững an ninh chính trị, trật tự an toàn xã hội; giải quyết hậu quả bảo đảm nhanh gọn, đúng nguyên tắc, quy trình, chặt chẽ, chu đáo.
- Tổ chức sinh hoạt đơn vị, thông báo cho cán bộ, chiến sĩ kết quả làm việc của các cơ quan chức năng và gia đình, ổn định tình hình tư tưởng trong đơn vị; rút kinh nghiệm từ vụ giáo dục quân nhân nêu cao ý thức chấp hành kỷ luật, quán triệt và thực hiện nghiêm túc các quy định về bảo đảm an toàn trong thực hiện nhiệm vụ; nắm, hiểu và thực hiện đúng quy trình các bước xử lý các vấn đề tư tưởng nảy sinh, nhất là các vụ việc nghiêm trọng, có tính chất phức tạp, nhạy cảm, dễ bị lợi dụng xuyên tạc, kích động, chống phá.
	
- Chỉ đạo Lực lượng 47 tăng cường nắm tình hình trên không gian mạng để kịp thời phát hiện, đề xuất xử lý các nội dung có liên quan đến vụ việc. Kiên quyết xử lý với những biểu hiện tuyên truyền, xuyên tạc gây hoang mang trong đơn vị.
- Cán bộ các cấp tăng cường công tác kiểm tra nắm chắc tình hình đơn vị, nhất là những nơi có biểu hiện hoang mang, dao động. Phát huy vai trò tổ chức hội đồng quân nhân, chi đoàn thanh niên, chiến sĩ bảo vệ trong việc phân tích, dự báo, đánh giá diễn biến tình hình tư tưởng để động viên giải quyết kịp thời.
- Đề nghị giải quyết các chế độ chính sách đối với quân nhân.
- Tổng hợp tình hình, báo cáo kết quả xử lý lên cấp trên. 
III. NHÓM TÌNH HUỐNG TƯ TƯỞNG CÓ THỂ NẢY SINH TRONG GIẢI QUYẾT MỐI QUAN HỆ ĐỒNG CHÍ ĐỒNG ĐỘI, QUÂN DÂN, GIA ĐÌNH, BẠN BÈ, NAM NỮ (10 tình huống)
Tình huống 1. Trong đơn vị có biểu hiện thiếu thống nhất trong cấp ủy, chỉ huy, gây khó khăn trong công tác lãnh đạo, chỉ đạo triển khai thực hiện nhiệm vụ và xây dựng mối đoàn kết nội bộ, gây dư luận không tốt.
Gợi ý biện pháp xử lý
- Cấp ủy, chỉ huy cấp trên nhận định, đánh giá tình hình, phân công cán bộ dự theo dõi, chỉ đạo các buổi sinh hoạt của cơ quan, đơn vị cấp dưới xảy ra mất đoàn kết nội bộ để nắm tình hình.
- Tiến hành gặp gỡ, trao đổi với cấp ủy, chỉ huy cơ quan, đơn vị để xảy ra mất đoàn kết nội bộ.
- Chỉ đạo tổ chức kiểm tra đột xuất đối với tập thể cấp ủy, cán bộ chủ trì nơi để xảy ra mất đoàn kết nội bộ, làm rõ nguyên nhân, trách nhiệm của tập thể, cá nhân.
+ Nếu mất đoàn kết do bất đồng quan điểm cá nhân thì cấp trên phân tích, định hướng để cấp ủy, chỉ huy cấp dưới thống nhất trong lãnh đạo, chỉ đạo, tổ chức thực hiện nhiệm vụ của cơ quan, đơn vị.
+ Nếu mất đoàn kết do vi phạm nguyên tắc, quy chế làm việc, quy chế lãnh đạo, chỉ huy thì phải chỉ đạo kiểm điểm, kỷ luật theo quy định (tùy theo tính chất sự việc) bảo đảm nghiêm minh, chính xác, kịp thời. 
- Nghiên cứu, đề xuất điều chuyển công tác (Nếu cần thiết).
- Tổ chức hội nghị cơ quan, đơn vị để rút kinh nghiệm, thông báo tình hình và định hướng, thống nhất tư tưởng, nhận thức cho cán bộ, chiến sĩ.
- Tổng hợp tình hình kết quả báo cáo cấp trên.
Tình huống 2. Một số chiến sĩ, nhất là chiến sĩ mới có biểu hiện ngại học, ngại rèn, bộc lộ tâm tư buồn chán qua lời nói, nhật ký (vở học tập,...) những nội dung bất thường: “Tôi lẽ ra không nên sinh ra trên đời này, tôi rất xin lỗi những người tôi làm sai, tôi chỉ mong một ngày tôi sẽ không ở trên đời này”, “Sống tới ngày bắn đạn thật”, “Cuộc đời này không đáng sống”, “Nó không còn quan trọng nữa rồi”, “Họ sẽ không thể nào làm tổn thương tôi được nữa”, “Họ sẽ nhớ về tôi khi tôi ra đi,” hoặc “Bạn sẽ thương tiếc khi tôi ra đi”, “Bạn/gia đình/bạn bè/bạn gái tôi sẽ sống tốt hơn nếu không có tôi”….
Gợi ý biện pháp xử lý
- Tăng cường giáo dục nâng cao nhận thức chính trị tư tưởng; coi trọng phát huy dân chủ gắn với hoàn thiện các quy chế, cơ chế để nắm, quản lý tình hình đơn vị, chất lượng các tổ chức, diễn biến tư tưởng của quân nhân; kết hợp chặt chẽ giáo dục nhận thức với các phong trào hành động để quản lý quân nhân.
- Chủ động, linh hoạt nắm thông tin từ vở học tập, sổ tay chiến sĩ, nhật ký, thiết bị nghe, nhìn cá nhân.
- Phân công cán bộ, đảng viên kèm cặp, giúp đỡ bộ đội. Phát huy vai trò của Chiến sĩ bảo vệ, dân vận, “Tổ 3 người”, “Tổ tư vấn tâm lý, pháp lý”, “Hòm thư góp ý”; khảo sát (điều tra xã hội học) để kịp thời nắm tình hình, tham mưu định hướng tư tưởng, giải quyết những vấn đề tư tưởng nảy sinh.
- Nghiên cứu, tìm hiểu, xác định nguyên nhân khách quan, chủ quan dẫn đến biểu hiện tư tưởng bất thường. Tư vấn về những vấn đề quân nhân gặp phải khó khăn, giải quyết nhanh chóng làm giảm căng thẳng, giải tỏa tâm lý, không để quân nhân bế tắc kéo dài, không lối thoát.
- Thường xuyên quan sát và triệt tiêu những nguy cơ có thể dẫn đến tự tử, tự sát. Tăng cường các biện pháp quản lý không để quân nhân sử dụng rượu, bia, chất kích thích, không để quân nhân có biểu hiện sang chấn tâm lý kéo dài. Tăng cường kiểm tra, quản lý chặt chẽ quân tư trang, vũ khí, cuốc, xẻng, dao, dây các loại, thuốc trừ sâu, thuốc diệt côn trùng, thuốc diệt cỏ…không để cán bộ, chiến sĩ lợi dụng những vật dụng đó nhằm thực hiện hành vi tiêu cực.
- Quân y đơn vị theo dõi chặt chẽ trường hợp quân nhân sau khi được điều trị các bệnh lý có rối loạn tâm thần, rối loạn cảm xúc, trầm cảm.
- Liên hệ địa phương, gia đình, bạn bè của quân nhân để nắm chắc mối quan hệ xã hội của quân nhân và phối hợp giải quyết những khó khăn, vướng mắc mà một mình quân nhân không giải quyết được.
- Duy trì thực chất nền nếp các khâu, các bước công tác quản lý tư tưởng quân nhân: Nắm, dự báo, quản lý, định hướng, giải quyết và đấu tranh tư tưởng;
- Tổ chức các hoạt động phong phú, đa dạng, phù hợp, lôi cuốn cán bộ, chiến sĩ tham gia vào các hoạt động của đơn vị.
- Tổ chức cho quân nhân (có ý định tự tử, tự sát) xem những phim, chương trình có những nhân vật vượt lên chính mình, vượt lên số phận để từng bước định hướng tư tưởng quân nhân.
- Thường xuyên đánh giá mức độ chuyển biến, dự báo xu hướng diễn biến tâm lý, tư tưởng của cán bộ, chiến sĩ để có biện pháp tác động kịp thời.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 3. Trong đơn vị có dư luận về việc quân nhân yêu đồng giới, gây tâm lý băn khoăn trong một bộ phận cán bộ, chiến sĩ.
Gợi ý biện pháp xử lý
- Rà soát, đánh giá tình hình đơn vị; xác minh thông tin, đối tượng có biểu hiện yêu đồng giới. Chỉ đạo quân y đơn vị nắm và theo dõi. Tham khảo để hiểu rõ hơn về nguyên nhân và biểu hiện của những người có quan hệ đồng giới.
- Khi đã xác minh được đối tượng, chủ động phối hợp với địa phương và gia đình tìm hiểu nắm rõ điều kiện, hoàn cảnh gia đình mối quan hệ và các biểu hiện tâm sinh lý của quân nhân khi ở gia đình; kết quả sàng lọc, tuyển chọn quân nhân nhập ngũ. 
- Hội ý cấp ủy, nhận định, đánh giá tình hình, xác định chủ trương, biện pháp lãnh đạo làm chuyển biến tình hình, giữ vững ổn định đơn vị. 
- Phân công cán bộ chủ động có biện pháp khéo léo gặp gỡ, trao đổi, nắm bắt tâm tư, nguyện vọng của quân nhân, tìm hiểu bản chất, nguyên nhân; tâm sự, chia sẻ giúp quân nhân hiểu rõ bản chất, tác hại của hành vi. Động viên tích cực tham gia các hoạt động phù hợp với khả năng của cá nhân, đơn vị, giữ gìn phẩm chất, đạo đức, chuẩn mực người quân nhân.
- Phân công cán bộ, đảng viên, tổ tư vấn tâm lý, pháp lý và quần chúng nòng cốt gần gũi, động viên, từng bước giúp quân nhân nhận thức được hành vi không đúng của bản thân. Trong thực hiện nhiệm vụ thường xuyên phân công đồng đội kèm cặp, giúp đỡ; không được gây căng thẳng, kỳ thị tạo sức ép cho quân nhân.
- Không chọc ghẹo để quân nhân mặc cảm.
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định của luật hôn nhân, gia đình, quan hệ 01 vợ, 01 chồng; thuần phong mỹ tục của dân tộc… những thông tin liên quan đến tác hại và dư luận lên tiếng về yêu đồng giới để cảnh tỉnh quân nhân, tránh để xảy ra những hệ lụy của hôn nhân. Tổ chức các buổi tọa đàm, sân khấu hóa trong các hội thi, hội diễn văn nghệ quần chúng để nâng cao nhận thức cho quân nhân về hạnh phúc, hôn nhân.
- Ngăn chặn không để lây lan.
- Duy trì nghiêm chế độ ngày, tuần, quản lý quân số và các mối quan hệ của quân nhân. 
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị; quan tâm chăm lo đời sống vật chất, tinh thần, kịp thời động viên cán bộ, chiến sĩ yên tâm, gắn bó xây dựng đơn vị.
- Tổng hợp tình hình báo cáo cấp trên.
	
Tình huống 4: Trong đơn vị có dư luận về việc cán bộ của đơn vị quan hệ nam nữ bất chính với phụ nữ địa phương nơi đóng quân.
- Tiến hành hội ý chỉ huy thống nhất biện pháp giải quyết.
- Điều tra, xác minh cụ thể mối quan hệ bất hợp pháp của quân nhân.
- Gặp gỡ quân nhân nghe trình bày rõ sự việc, giáo dục, động viên nhận rõ khuyết điểm.
- Gặp gỡ người thân, vợ con để tìm cách giải quyết.
- Tổ chức sinh hoạt rút kinh nghiệm, kiểm điểm, kỷ luật theo quy định (tùy theo tính chất sự việc).
- Nghiên cứu, đề xuất điều chuyển công tác (Nếu quân nhân không khắc phục, sửa chữa khuyết điểm).
- Tăng cường làm tốt công tác giáo dục, quán triệt các quy định của luật hôn nhân, gia đình, quan hệ 01 vợ, 01 chồng; quy định những điều đảng viên không được làm; Nghị quyết Trung ương 4 (khóa XII),… những thông tin liên quan đến việc xử lý cán bộ công chức quan hệ bất chính xảy ra trên địa bàn và cả nước để răn đe, hệ lụy của hôn nhân đổ vỡ.
- Tổng hợp tình hình báo cáo cấp trên.
	Tình huống 5. Trong đơn vị có dư luận về trường hợp một chiến sĩ mới nhập ngũ, do nhận được lời chia tay của người yêu nên đã có biểu hiện buồn chán, phát ngôn không chuẩn xác, thiếu tích cực tham gia các hoạt động tập thể, chất lượng hoàn thành nhiệm vụ thấp.
	Gợi ý biện pháp xử lý
- Nắm tình hình, xác minh quan hệ yêu đương của quân nhân qua các bạn đồng khóa đang công tác ở đơn vị, gia đình và bạn gái. Rà soát, nắm bắt những thông tin cá nhân trên mạng xã hội, trang facebook, zalo...
- Hội ý cấp ủy, chỉ huy, thống nhất biện pháp giáo dục, giải quyết.
- Phân công cán bộ,  “Tổ 3 người”, “Tổ tư vấn tâm lý, pháp lý”… gặp gỡ, động viên, tâm sự để quân nhân giãi bày, giải tỏa tâm lý; đồng thời giúp quân nhân có nhận thức đầy đủ, bình tĩnh, từng bước động viên người yêu để cùng nhau vượt qua khó khăn ban đầu, giữ được hạnh phúc lứa đôi. 
- Trao đổi với gia đình quân nhân về tình hình của quân nhân tại đơn vị, để gia đình nắm và phối hợp động viên, chia sẻ.
- Thông qua mối quan hệ bạn bè thân thiết, đồng chí, đồng đội khuyên nhủ, động viên.
- Duy trì nghiêm chế độ nền nếp xây dựng đơn vị chính quy, quản lý chặt chẽ tình hình tư tưởng, kỷ luật và các mối quan hệ xã hội của bộ đội, nhất là trong ngày nghỉ, giờ nghỉ, hoạt động ngoài doanh trại để có biện pháp giáo dục kịp thời.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị; tổ chức tốt hoạt động văn hóa tinh thần, tạo không khí vui tươi, lành mạnh; quan tâm chăm lo đời sống vật chất, tinh thần, kịp thời động viên cán bộ, chiến sĩ yên tâm, gắn bó xây dựng đơn vị. 
- Thường xuyên nắm chắc tình hình, báo cáo cấp trên.
	Tình huống 6. Trong đơn vị có cán bộ biểu hiện tư tưởng buồn chán, tiêu cực… vì vợ chồng bất hòa, anh em trong gia đình mất đoàn kết từ việc bố mẹ phân chia đất đai, nhà ở không công bằng, nên thiếu tập trung vào công việc, chất lượng hoàn thành nhiệm vụ thấp.
Gợi ý biện pháp xử lý 
- Hội ý chỉ huy đơn vị thống nhất đánh giá tình hình, phân công cán bộ phụ trách giải quyết tư tưởng. Lưu ý, đây là việc riêng, nhạy cảm của gia đình quân nhân; do đó chủ yếu tác động làm cho quân nhân thuộc quyền hiểu thực chất sự việc, ý kiến đề xuất gia đình "thấu tình, đạt lý ", giữ vững mối quan hệ ruột thịt trong gia đình.
- Gặp quân nhân tìm hiểu, nắm chắc hoàn cảnh gia đình, trước hết là tôn trọng quyết định của bố, mẹ; tổ tư vấn tâm lý pháp luật tuyên truyền cho quân nhân nắm chắc luật thừa kế, luật sở hữu tài sản. Chấp hành nghiêm túc luật thừa kế tài sản theo quy định của pháp luật; động viên quân nhân: vật chất, tài sản là quan trọng nhưng tình cảm gia đình còn quý giá hơn, có tiền cũng không thể mua được; tài sản có thể làm ra nhưng tình cảm gia đình mà mất đi thì rất khó lấy lại được, tình cảm, danh dự là tài sản quý nhất của con người, không bao giờ có thể đánh đổi bằng tiền bạc. Lấy ví dụ, dẫn chứng xác thực để quân nhân nhìn nhận vấn đề, tránh mắc phải khuyết điểm nóng vội, duy ý chí, chỉ thấy cái lợi trước mắt, tức thời mà bỏ quên cái lợi lâu dài... quyết định sai lầm từ vấn đề tranh chấp tài sản có thể dẫn đến mất đoàn kết gia đình khiến quân nhân phải hối hận (nếu đơn vị chưa thành lập tổ tư vấn tâm lý, pháp luật thì chính trị viên tiến hành nội dung này);
- Liên hệ, thông báo với gia đình biết về tư tưởng, tình cảm, nguyện vọng của quân nhân trước việc gia đình phân chia tài sản; đề nghị gia đình phối hợp động viên quân nhân hiểu rõ sự việc, yên tâm thực hiện nhiệm vụ.
- Cử cán bộ theo dõi, động viên quân nhân yên tâm, tư tưởng, tôn trọng bố mẹ (gia đình), chấp hành nghiêm pháp luật, đề cao trách nhiệm, hoàn thành mọi nhiệm vụ được giao.
 	Tình huống 7. Trong đơn vị có trường hợp quân nhân A vay mượn tiền của quân nhân B nhưng thiếu trách nhiệm thực hiện nghĩa vụ trả nợ, giải quyết mối quan hệ không tốt dẫn đến mâu thuẫn, ảnh hưởng không tốt đến đơn vị.
	- Hội ý chỉ huy đánh giá tình hình, báo cáo cấp trên.
	- Cán bộ gặp gỡ quân nhân, nghe quân nhân trình bày hoàn cảnh kinh tế gia đình của quân nhân, mục đích vay tiền và ý định, khả năng trả nợ; quán triệt, giáo dục làm cho quân nhân nhận thức rõ về trách nhiệm của bản thân đối với gia đình và việc trả nợ cho đồng đội; hệ lụy của việc sử dụng tiền không đúng mục đích, không hiệu quả và sự ảnh hưởng đến uy tín cá nhân, tình đồng chí, đồng đội…; bàn biện pháp khắc phục trước mắt, động viên tư tưởng cho quân nhân.
	- Gặp gỡ những người cho quân nhân vay tiền để nắm số tiền vay, gặp gỡ gia đình, nói rõ quan điểm của chỉ huy đơn vị trong việc quản lý, giáo dục quân nhân, đồng thời phối hợp cùng gia đình nắm chắc tình hình tư tưởng, động viên gia đình, khắc phục khó khăn, cùng với quân nhân có trách nhiệm trả nợ và giải quyết tốt mối quan hệ với người cho vay, tránh gây mất đoàn kết.
	- Chỉ huy đơn vị thường xuyên theo dõi diễn biến tư tưởng, hướng trả nợ của quân nhân; đồng thời giáo dục mọi cán bộ, chiến sĩ trong đơn vị rút kinh nghiệm chung, sống có trách nhiệm với hành vi của bản thân, tránh việc vay nợ để tham gia các tệ nạn xã hội với bất kỳ hình thức nào.
	- Nếu mất khả năng chi trả, xử lý kỷ luật đề nghị cho phục viên, thôi việc hoặc xử lý theo pháp luật.
	- Sinh hoạt đơn vị rút kinh nghiệm.
	- Tổng hợp tình hình báo cáo cấp trên.
	Tình huống 8. Trong quá trình nghỉ phép, một cán bộ tham gia giao lưu với một số thanh niên địa phương, do bất đồng nhận thức, quan điểm và tác phong sinh hoạt đã nảy sinh mâu thuẫn, một số người dân địa phương chứng kiến đã quay video và phát tán trên mạng xã hội; đồng chí cán bộ lo lắng vì thông tin trên mạng xã hội sẽ ảnh hưởng tới uy tín Quân đội, đã báo cáo xin ý kiến của chỉ huy đơn vị.
Gợi ý biện pháp xử lý 
- Trao đổi nhanh trong chỉ huy đơn vị, thống nhất biện pháp xử lý và phân công cán bộ phụ trách giải quyết vụ việc 
- Báo cáo cấp trên xin ý kiến chỉ đạo và đề nghị cử cán bộ và cơ quan chức năng phối hợp với đơn vị để giải quyết vụ việc, trước hết là bóc gỡ thông tin nói trên.
- Gặp gỡ đồng chí cán bộ để nắm lại tình hình, yêu cầu báo cáo cụ thể về sự việc và số thanh niên địa phương cùng giao lưu và nguyên nhân mâu thuẫn.
- Cùng với cấp trên và cơ quan chức năng làm việc với chính quyền và cơ quan chức năng địa phương để tiến hành các biện pháp giáo dục số thanh niên có liên quan
- Tùy theo lỗi phạm, tiến hành kiểm điểm, xử lý nghiêm túc đối với đồng chí cán bộ.
- Tổ chức sinh hoạt đơn vị để giáo dục, định hướng, rút kinh nghiệm chung trong toàn đơn vị về các yêu cầu khi thực hiện nhiệm vụ dân vận và việc nêu cao ý thức giữ gìn phẩm chất, tư cách “Bộ đội Cụ Hồ”  
- Tổng hợp báo cáo với cấp trên về kết quả giải quyết và xử lý vụ việc theo quy định. 
 	Tình huống 9. Trong đơn vị có một số quân nhân có biểu hiện nghiện chơi game và đam mê các trang mạng xã hội, làm ảnh hưởng đến sinh hoạt của đơn vị và kết quả hoàn thành chức trách, nhiệm vụ cá nhân.
Gợi ý biện pháp xử lý:
- Trao đổi thống nhất trong cấp ủy, chỉ huy đánh giá tình hình, báo cáo xin ý kiến chỉ đạo của cấp trên.
- Tiến hành gặp gỡ, đối thoại tìm hiểu rõ nguyên nhân, nghe tâm tư, nguyện vọng. Định hướng tư tưởng, phân tích làm rõ những tác động tiêu cực của việc nghiện game và các trang mạng xã hội đối với hệ thần kinh, và mức độ ảnh hưởng đến công việc của bản thân và đơn vị; làm cho quân nhân nhận thức đúng thực chất của sự việc. 
- Sinh hoạt toàn đơn vị quán triệt các quy định của cấp trên về việc sử dụng thiết bị thông minh trong học tập, công tác. Nhắc nhở quân nhân toàn đơn vị, chấp hành nghiêm quy định.
- Thường xuyên giao nhiệm vụ cụ thể, đưa quân nhân vào các hoạt động của đơn vị.
- Báo cáo kết quả phấn đấu, khắc phục của quân nhân nghiện game lên cấp trên và xin ý kiến chỉ đạo.
- Nếu nghiện nặng đề xuất cho quân nhân đi điều trị.
- Tổng hợp báo cáo với cấp trên về kết quả giải quyết và xử lý vụ việc theo quy định. 
Tình huống 10. Trong đơn vị có dư luận về quân nhân vay tiền của dân, quá khả năng chi trả, do túng quẫn nên đã có ý định đào ngũ, xin ra quân…
Gợi ý biện pháp xử lý:
- Hội ý cấp uỷ, chỉ huy đơn vị, nhận định, đánh giá tình hình vay nợ của quân nhân trong đơn vị đơn vị, xác định số lượng, đối tượng, mục đích vay nợ và khả năng trả nợ của quân nhân. Dự báo một số trường hợp có thể nảy sinh ý định đào bỏ ngũ nhằm “chạy nợ”; những hậu quả tiếp theo của sự việc trên có thể xảy ra như: mất an toàn giao thông, trộm cắp..., qua đó trao đổi, thống nhất biện pháp giải quyết và báo cáo cấp trên xin ý kiến chỉ đạo;
- Triển khai các biện pháp quản lý chặt số quân nhân nói trên
	- Yêu cầu các quân nhân trong đơn vị tự giác báo cáo bằng văn bản số nợ..., phương hướng sử dụng nguồn tiền để trả nợ (tiền phụ cấp, tiền thanh toán chế độ xuất ngũ, tiền gia đình hỗ trợ...)
	- Phân công cán bộ nắm tình hình vay nợ của quân nhân, đối chiếu với phần tự khai để có biện pháp giải quyết...
- Gặp gỡ số quân nhân vay nợ (nhất là số nợ xấu), nắm tình hình, phương hướng giải quyết; động viên quân nhân cùng với gia đình có biện pháp khắc phục kịp thời số nợ, không để trở thành nợ xấu; đồng thời chấp hành nghiêm kỷ luật, cần có thái độ tích cực hợp tác với các bên để giải quyết, nghiêm cấm đào ngũ và các hành vi tiêu cực khác.
	- Liên lạc với gia đình để trao đổi thống nhất các biện pháp phối hợp giải quyết (khi làm việc với gia đình quân nhân cần có văn bản ghi chép chặt chẽ).
	- Tổ chức sinh hoạt đơn vị quán triệt nhiệm vụ, định hướng tư tưởng cho quân nhân; biểu dương các đồng chí tiết kiệm trong chi tiêu giúp đỡ gia đình, người thân; phê bình nhắc nhở hành vi vay nợ quá khả năng thanh toán làm ảnh hưởng đến bản thân, gia đình và đơn vị; nêu cao ý thức chấp hành nghiêm kỷ luật đơn vị, ý thức tiết kiệm trong chi tiêu, tích cực hợp tác chặt chẽ với đơn vị và gia đình để khắc phục số nợ.
- Sau khi giải quyết xong, cần tổ chức sinh hoạt rút kinh nghiệm, kiểm điểm làm rõ trách nhiệm những cán bộ thiếu trách nhiệm trong công tác quản lý, giáo dục bộ đội.
	- Phân công cán bộ kèm cặp giáo dục, giúp đỡ quân nhân thuộc quyền không để tái diễn tình trạng trên.
- Tổng hợp báo cáo với cấp trên về kết quả giải quyết theo quy định./. 


TỔNG CỤC CHÍNH TRỊ
CỤC TUYÊN HUẤN
DẤU HIỆU NHẬN BIẾT HÀNH VI VI PHẠM KỶ LUẬT, MẤT AN TOÀN VÀ GỢI Ý BIỆN PHÁP XỬ LÝ CỦA CÁN BỘ CƠ SỞ ĐỐI VỚI NHỮNG TÌNH HUỐNG TƯ TƯỞNG CÓ THỂ NẢY SINH 

(Tài liệu tham khảo TẬP 3)

 

Lưu hành nội bộ


NHÀ XUẤT BẢN QUÂN ĐỘI NHÂN DÂN
HÀ NỘI - 2022

Ban biên soạn:
Thiếu tướng Nguyễn Văn Đức (chủ biên)
Đại tá Tạ Văn Thiện
Đại tá Nguyễn Hữu Tuyển
Đại tá TS Nguyễn Văn Luyện
Đại tá Bùi Lê Ninh
Đại tá TS Nguyễn Xuân Sinh
Thượng tá TS Nguyễn Văn Thi
Thượng tá Phạm Văn Quân









LỜI GIỚI THIỆU
Năm 2015 và 2018, Cục Tuyên huấn đã biên tập, phát hành tài liệu“100 tình huống tư tưởng có thể nảy sinh ở đơn vị và gợi ý biện pháp xử lý của cán bộ cơ sở”, đã được các cơ quan, đơn vị đón nhận và vận dụng với nhiều hình thức, biện pháp phong phú, sáng tạo vào xử lý, giải quyết tư tưởng quân nhân, ngăn ngừa vi phạm kỷ luật quân đội, pháp luật Nhà nước, góp phần xây dựng tổ chức đảng trong sạch vững mạnh, đơn vị vững mạnh toàn diện, hoàn thành tốt nhiệm vụ được giao. Tuy nhiên, vẫn còn một số cấp uỷ, chỉ huy và cán bộ cấp phân đội xử lý và giải quyết các vấn đề nảy sinh về tư tưởng quân nhân chưa kịp thời, dứt điểm, còn chủ quan, dập khuôn máy móc, thiếu tính khoa học và thuyết phục, có những vấn đề tư tưởng nảy sinh giải quyết không tốt dẫn đến từ vi phạm nhỏ thành vi phạm lớn, từ vấn đề đơn giản thành vấn đề phức tạp, ảnh hướng trực tiếp đến tư tưởng cán bộ, chiến sĩ và nhân dân; cá biệt có những vụ việc đã bị các phần tử xấu lợi dụng, xuyên tạc làm ảnh hưởng tới bản chất, truyền thống Quân đội và hình ảnh “Bộ đội Cụ Hồ”. Đồng thời, trong thực tiễn thực hiện nhiệm vụ phòng, chống thiên tai, dịch bệnh, huấn luyện, học tập, sinh hoạt và công tác ở đơn vị cơ sở đã phát sinh những vấn đề mới liên quan đến công tác quản lý tư tưởng quân nhân. 
Để khắc phục những tồn tại nêu trên, đồng thời kịp thời cập nhật, bổ sung những tình huống mới phát sinh, nhằm giúp cấp ủy, chỉ huy và đội ngũ cán bộ đơn vị cơ sở có thêm kiến thức, kỹ năng xử lý tình huống tư tưởng, kỷ luật, Cục Tuyên huấn phối hợp với các cơ quan, đơn vị tiếp tục biên soạn tài liệu “Dấu hiệu nhận biết hành vi vi phạm kỷ luật, mất an toàn và gợi ý biện pháp xử lý của cán bộ cơ sở đối với những tình huống tư tưởng có thể nảy sinh (tập 3)”. 
Nội dung tài liệu được kết cấu thành hai phần: 
Phần thứ nhất: Dấu hiệu nhận biết đối các nhóm hành vi vi phạm kỷ luật, mất an toàn (30 nhóm hành vi). 
Phần thứ hai:  Gợi ý biện pháp xử lý của cán bộ cơ sở đối với những tình huống tư tưởng có thể nảy sinh. Gồm 3 nhóm:
- Nhóm tình huống tư tưởng nảy sinh trong phòng, chống thiên tai, dịch bệnh (50 tình huống).
- Nhóm tình huống tư tưởng nảy sinh trong huấn luyện, sẵn sàng chiến đấu; xây dựng chính quy, rèn luyện kỷ luật (10 tình huống). 
- Nhóm tình huống tư tưởng nảy sinh trong giải quyết mối quan hệ đồng chí, đồng đội, gia đình, bạn bè, nam nữ, quan hệ quân dân (10 tình huống).
Đây là tập tài liệu tham khảo có tính thực tiễn, dùng để cán bộ cơ sở toàn quân nghiên cứu, vận dụng trong công tác quản lý tư tưởng quân nhân ở đơn vị cơ sở. Quá trình nghiên cứu, vận dụng, xử lý các tình huống cần thực hiện đúng nguyên tắc, quy trình, sáng tạo, linh hoạt, tránh dập khuôn máy móc; phát huy vai trò, trách nhiệm của người chỉ huy các cấp (tiểu đội, trung đội, đại đội, tiểu đoàn); của chính trị viên (chính trị viên phó) đại đội, tiểu đoàn và vai trò, trách nhiệm chỉ đạo, hướng dẫn của cấp ủy, chính ủy, chính trị viên (bí thư) và cơ quan cấp trên để đạt hiệu quả cao. 
Quá trình thực hiện rất mong nhận được ý kiến góp ý để chỉnh lý, bổ sung hoàn thiện tài liệu.

Xin trân trọng giới thiệu cùng các đồng chí!
  




























Phần thứ nhất
DẤU HIỆU NHẬN BIẾT VÀ BIỆN PHÁP PHÒNG NGỪA 
CÁC NHÓM HÀNH VI VI PHẠM KỶ LUẬT, MẤT AN TOÀN
1. Tự tử, tự sát
a) Dấu hiệu nhận biết
- Thông qua nhật ký, vở ghi chép, mạng xã hội (Zalo, Facebook…) nắm được quân nhân thường xuyên suy nghĩ ám ảnh một vấn đề nào đó có tính chất nghiêm trọng. Cảm thấy không còn một chút hy vọng nào, thấy cuộc sống trở nên vô nghĩa, hoặc không thể kiểm soát chúng, thường hay mơ hồ, hoặc không thể tập trung được.
- Có biểu hiện trầm cảm, buồn chán, giảm hứng thú với các thói quen cũ, mất ngủ kéo dài.
- Tâm trạng đột ngột thay đổi, thường hay bực bội, giận dữ cực độ. Thường xuyên căng thẳng, lo âu cùng cực, có cảm giác tội lỗi, buồn chán cuộc đời, hay xấu hổ, hoặc cảm thấy bản thân trở thành gánh nặng cho người khác. Thường hay cảm thấy cô đơn, biệt lập, thậm chí ngay cả khi đang ở cạnh nhiều người.
- Bị bệnh hiểm nghèo nhưng giấu bệnh, bi quan…
- Hay đề cập nhiều đến sự chết chóc biểu hiện qua các câu nói “Tôi lẽ ra không nên sinh ra trên đời này, tôi rất xin lỗi những người tôi làm sai, tôi chỉ mong một ngày tôi sẽ không ở trên đời này”, “Sống tới ngày bắn đạn thật”, “Cuộc đời này không đáng sống”, “Nó không còn quan trọng nữa rồi”, “Họ sẽ không thể nào làm tổn thương tôi được nữa”, “Họ sẽ nhớ về tôi khi tôi ra đi,” hoặc “Bạn sẽ thương tiếc khi tôi ra đi”, “Bạn/gia đình/bạn bè/bạn gái tôi sẽ sống tốt hơn nếu không có tôi”….
- Đột ngột có những hành vi bất thường: tắm rửa sạch sẽ, mặc quần áo đẹp dù không đi đâu, tự nhiên trò chuyện vui vẻ sau thời gian dài buồn bã. Cho đi tài sản có giá trị, nói lời tạm biệt với những người thân yêu, tìm kiếm hoặc tích trữ một dụng cụ có thể gây hại cho bản thân (thuốc ngủ, thuốc bảo vệ thực vật, dao, kéo, dây thừng, vũ khí…).
b) Biện pháp phòng ngừa
- Tăng cường giáo dục nâng cao nhận thức chính trị tư tưởng; coi trọng phát huy dân chủ gắn với hoàn thiện các quy chế, cơ chế để nắm, quản lý tình hình đơn vị, chất lượng các tổ chức, diễn biến tư tưởng của quân nhân; kết hợp chặt chẽ giáo dục nhận thức với các phong trào hành động để quản lý quân nhân.
- Chủ động, linh hoạt nắm thông tin từ vở học tập, sổ tay chiến sĩ, nhật ký, thiết bị nghe, nhìn cá nhân.
- Phân công cán bộ, đảng viên kèm cặp, giúp đỡ bộ đội. Phát huy vai trò của Chiến sĩ bảo vệ, dân vận, “Tổ 3 người”, “Tổ tư vấn tâm lý, pháp lý”, “Hòm thư góp ý”; khảo sát (điều tra xã hội học) để kịp thời nắm tình hình, tham mưu định hướng tư tưởng, giải quyết những vấn đề tư tưởng nảy sinh.
- Nghiên cứu, tìm hiểu, xác định nguyên nhân khách quan, chủ quan dẫn đến biểu hiện tư tưởng bất thường. Tư vấn về những vấn đề quân nhân gặp phải khó khăn, giải quyết nhanh chóng làm giảm căng thẳng, giải tỏa tâm lý, không để quân nhân bế tắc kéo dài, không lối thoát.
- Thường xuyên quan sát và triệt tiêu những nguy cơ có thể dẫn đến tự tử, tự sát. Tăng cường các biện pháp quản lý không để quân nhân sử dụng rượu, bia, chất kích thích, không để quân nhân có biểu hiện sang chấn tâm lý kéo dài. Tăng cường kiểm tra, quản lý chặt chẽ quân tư trang, vũ khí, cuốc, xẻng, dao, dây các loại, thuốc trừ sâu, thuốc diệt côn trùng, thuốc diệt cỏ…không để cán bộ, chiến sĩ lợi dụng những vật dụng đó nhằm thực hiện hành vi tiêu cực.
- Quân y đơn vị theo dõi chặt chẽ trường hợp quân nhân sau khi được điều trị các bệnh lý có rối loạn tâm thần, rối loạn cảm xúc, trầm cảm.
- Liên hệ địa phương, gia đình, bạn bè của quân nhân để nắm chắc mối quan hệ xã hội của quân nhân và phối hợp giải quyết những khó khăn, vướng mắc mà một mình quân nhân không giải quyết được.
- Duy trì thực chất nền nếp các khâu, các bước công tác quản lý tư tưởng quân nhân: Nắm, dự báo, quản lý, định hướng, giải quyết và đấu tranh tư tưởng;
- Tổ chức các hoạt động phong phú, đa dạng, phù hợp, lôi cuốn cán bộ, chiến sĩ tham gia vào các hoạt động của đơn vị.
- Tổ chức cho quân nhân (có ý định tự tử, tự sát) xem những phim, chương trình có những nhân vật vượt lên chính mình, vượt lên số phận để từng bước định hướng tư tưởng quân nhân.
- Thường xuyên đánh giá mức độ chuyển biến, dự báo xu hướng diễn biến tâm lý, tư tưởng của cán bộ, chiến sĩ để có biện pháp tác động kịp thời.
- Tổng hợp tình hình báo cáo cấp trên.
2. Cá độ bóng đá, bài bạc, lô đề
a) Dấu hiệu nhận biết:
- Có thói quen đánh bài, ham mê xem các nội dung liên quan đến cá cược, các trò chơi ăn tiền trên các trang mạng...
- Ham mê, theo dõi, bàn tán thắng thua các trận đấu của các giải bóng đá, bàn tán về khả năng thắng, thua những trận bóng đá sắp tới, kết quả xổ số, luận giải khả năng trúng vào các con số...
- Sau những trận bóng đá hoặc đánh đề tinh thần phấn chấn, vui vẻ khác thường, hào phóng, chi tiêu thoải mái hoặc buồn, ủ rũ, lo sợ.
- Có tính hiếu thắng, máu ăn thua, thích hưởng thụ, thích làm giàu nhanh mà không tốn công sức, đánh cược vào vận “đỏ đen”.
- Chất lượng, hiệu quả công việc giảm sút rõ rệt, ít quan tâm đến gia đình, bạn bè, đồng đội.
- Thường hay thu mình và lên mạng, ít giao tiếp, ít am hiểu những vấn đề được xã hội quan tâm, không quan tâm đến tình hình đơn vị.
- Tìm đủ cách vay mượn tiền, hay cầm cố đồ đạc, sử dụng các giấy tờ cá nhân thế chấp để vay tiền (thẻ đảng, giấy chứng minh thư sĩ quan, bằng tốt nghiệp…), nợ nần ngày càng nhiều không có khả năng chi trả.
b) Biện pháp phòng ngừa:
- Giáo dục cho quân nhân nhất là ý thức chấp hành Pháp luật Nhà nước, quy định của pháp luật hình sự về hành vi cá độ bóng đá, bài bạc, kỷ luật Quân đội, tác hại của việc tham gia cá độ bóng đá, đánh bạc, lô đề; những hình thức xử lý nghiêm minh của pháp luật khi tham gia cá độ, đánh bạc.
- Giáo dục, động viên, xây dựng cho cán bộ, chiến sĩ lối sống trong sạch, lành mạnh, trách nhiệm của bản thân đối với gia đình.
- Tăng cường các biện pháp nắm, quản lý của cán bộ các cấp, nhất là mối quan hệ xã hội của quân nhân.
- Kết hợp chặt chẽ công tác giáo dục, tuyên truyền giải thích, thuyết phục với việc duy trì nghiêm kỷ luật của Quân đội, quy định của đơn vị. Quản lý chặt chẽ quân nhân.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Định kỳ hoặc đột xuất kiểm tra thẻ đảng viên, chứng minh sĩ quan, QNCN, bằng tốt nghiệp…
- Tìm hiểu, nắm rõ nguồn tài sản có giá trị, việc chi tiêu quá thu nhập của quân nhân.
3. Vay mượn nợ không có khả năng chi trả
a) Dấu hiệu nhận biết:
- Muốn làm giàu nhanh chóng hoặc thích hưởng thụ, lười lao động, học tập, công tác.
- Đam mê cờ bạc, rượu chè bê tha, sống buông thả, xa hoa, lãng phí.
- Làm ăn thua lỗ, gia đình có người thân bệnh nặng.
- Suy tư, buồn bã, bi quan, chán nản, trầm cảm, thường xuyên hoang mang, lo sợ.
- Hay vay mượn tiền anh em trong đơn vị, bán, cầm cố tài sản có giá trị (xe, máy tính, điện thoại, đồ đạc trong gia đình…), hoặc cầm cố, thế chấp nhà cửa, đất đai.
- Giảm khả năng tập trung, chất lượng, hiệu quả công việc giảm sút rõ rệt, ít quan tâm đến gia đình, bạn bè, đồng đội.
- Ám ảnh và khó ngủ, né tránh các mối quan hệ. 
b) Biện pháp phòng ngừa:	
- Giáo dục pháp luật cho quân nhân nhất là ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, nguyên tắc chi tiêu hợp lý, phù hợp với khả năng tài chính của gia đình, những tác hại của việc vay nợ nặng lãi, hệ lụy khi không có khả năng chi trả.
- Tăng cường các biện pháp nắm, quản lý của cán bộ các cấp, nhất là mối quan hệ xã hội, việc chi tiêu của quân nhân.
- Kết hợp công tác giáo dục, tuyên truyền giải thích, thuyết phục với duy trì chặt chẽ, nghiêm túc kỷ luật của Quân đội, đơn vị.
- Làm tốt công tác hậu phương quân đội, thăm hỏi gia đình quân nhân, kết hợp gia đình nắm tình hình quân nhân.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
4. Mất đoàn kết giữa chiến sĩ cũ và chiến sĩ mới
a) Dấu hiệu nhận biết:
- Một số chiến sĩ nhập ngũ trước tỏ thái độ “thiếu thân thiện” với chiến sĩ mới hoặc ngược lại.
- Chiến sĩ cũ luôn thể hiện mình là đàn anh, tự cho mình cái “quyền” sai vặt những chiến sĩ khác. 
- Có những lời nói đe dọa chiến sĩ mới. 
- Một số chiến sĩ mới có tư tưởng bất an, lo âu, sợ sệt, ức chế.
- Chiến sĩ cũ và chiến sĩ mới không hòa đồng.
- Thời điểm dễ gây mất đoàn kết là mới điều chỉnh biên chế, chiến sĩ cũ chuẩn bị xuất ngũ.
- Trong đơn vị xuất hiện dư luận về mối quan hệ giữa chiến sĩ mới và chiến sĩ cũ.
b) Biện pháp phòng ngừa:
- Tăng cường giáo dục pháp luật cho quân nhân nhất là ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, chế độ, quy định, tinh thần đoàn kết, thương yêu giúp đỡ nhau, truyền thống quý báu của Quân đội ta.
- Phát huy trách nhiệm lãnh đạo, chỉ đạo của chi bộ, cán bộ các cấp, vai trò của các cơ quan và các tổ chức quần chúng trong giáo dục truyền thống.
- Tổ chức và duy trì  hiệu quả hoạt động giờ nghỉ, ngày nghỉ
- Chủ động nắm bắt tình hình để có biện pháp ngăn chặn, dự báo, phát hiện những dấu hiệu và hành vi vi phạm kỷ luật của quân nhân. 
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Phân công công tác phải có cán bộ phụ trách.
- Quan tâm chăm lo chu đáo đời sống vật chất tinh thần cho bộ đội.
- Tổ chức các hoạt động vui chơi, giải trí, huy động được nhiều người tham gia (thi đấu bóng đá, bóng chuyền…).
- Sinh hoạt dân chủ, phát huy tinh thần tương thân, tương trợ của chiến sĩ cũ với chiến sĩ mới.
5. Quân phiệt
a) Dấu hiệu nhận biết:
- Ít nói, khả năng thuyết phục kém, nói năng cộc cằn, cộc tính, thiếu kiên trì, thiếu kiềm chế.
- Tính tình hay nóng nảy, bộc trực, có biểu hiện độc đoán.
- Hay phàn nàn, bức xúc về lỗi vi phạm của quân nhân.
- Tâm sinh lý có biểu hiện ức chế, khó chịu do ảnh hưởng công việc, gia đình và tác động ngoài xã hội.
- Bệnh thành tích.
b) Biện pháp phòng ngừa:
- Giáo dục truyền thống, tinh thần đoàn kết, tình yêu thương đồng chí, đồng đội với khẩu hiệu hành động “Đơn vị là nhà, cán bộ, chiến sĩ là anh em”, xây dựng mối quan hệ đoàn kết cán-binh tốt đẹp.
- Giao nhiệm vụ cho cán bộ rèn luyện đức tính bình tĩnh, kiên nhẫn, đức độ, rộng lượng, xử lý các vụ việc trên cơ sở điều lệ quản lý bộ đội, điều lệnh Quân đội, pháp luật Nhà nước.
- Chỉ ra những hệ lụy cho cán bộ nếu có hành động quân phiệt.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Thường xuyên quan tâm theo dõi, nhất là trong thời điểm có dấu hiệu chuẩn bị xảy ra để ngăn chặn kịp thời.
- Khắc phục bệnh thành tích trong lãnh đạo, chỉ huy.
6. Vắng mặt trái phép
a) Biểu hiện nhận biết:
- Có thông tin người thân trong gia đình, bạn thân, người yêu…của quân nhân chết, bị bệnh nặng, tai nạn; đặc biệt là các trường hợp vợ đòi ly hôn, người yêu đòi chia tay…
- Tâm lý thay đổi khác thường, lo âu, bồn chồn, hay để ý, theo dõi chỉ huy, quan sát những vị trí thuận lợi có thể đi ra ngoài doanh trại.
- Thức khuya hoặc không ngủ trưa quan sát đồng chí, đồng đội tìm cơ hội thuận lợi để đi khỏi doanh trại. 
- Hay tìm lý do để vắng mặt trong sinh hoạt, học tập.
- Tập thể quân nhân, nhóm, bạn bè, đồng chí, đồng đội có những luồng dư luận xoay quanh vấn đề liên quan quân nhân có ý định vắng mặt trái phép.
- Chiến sĩ dân vận, chiến sĩ bảo vệ báo cáo.
 b) Biện pháp phòng ngừa:
- Tăng cường giáo dục pháp luật cho quân nhân nhất là ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, quy định của đơn vị, địa phương.
- Duy trì nghiêm nền nếp chính quy. 
- Chủ động nắm tình hình thực tế, dự báo kịp thời những dấu hiệu và hành vi vi phạm của quân nhân.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
7. Sử dụng trái phép chất ma túy, chất kích thích
a) Dấu hiệu nhận biết:
- Mắt đảo qua đảo lại, đồng tử nở rộng, đi vệ sinh, rửa tay, khát nước liên tục, rất thích nước ngọt, sụt cân và gầy đi rất nhanh, mồ hôi có mùi khai, xuất hiện quầng thâm mắt rõ rệt.
- Cánh tay hoặc chân có thể xuất hiện những vết như kim châm, trong đơn vị có thể có những dụng cụ để sử dụng ma túy (cất giấu những nơi khó phát hiện: khu vực nhà vệ sinh, kho vật chất, balô…). Quân nhân thường hay vào nhà vệ sinh giờ ngủ, nghỉ với thời gian lâu.
- Da nhăn nheo, nhiều mụn trứng cá lở loét trên cơ thể, men răng hỏng, miệng khô và hơi thở có mùi, hay bị chảy máu mũi.
- Cơ thể bị hội chứng “kiến bò dưới da”, ảo giác và sự thay đổi thất thường tâm trạng, thường có suy nghĩ hoang tưởng, nghi ngờ có người đi theo làm hại.
- Lơ là trong thực hiện nhiệm vụ, năng suất công việc giảm, luôn trong trạng thái tỉnh táo, có khi không cần ngủ tới cả tuần, giảm cân nhanh.
- Quân y lưu ý trường hợp quân nhân trẻ tuổi có các biểu hiện bất thường như: mạch nhanh, rối loạn nhịp tim, tăng huyết áp, nhịp thở nhanh.
- Vắng mặt trái phép theo quy luật, chu kỳ.
b) Biện pháp phòng ngừa:
- Tăng cường giáo dục pháp luật cho quân nhân nhất là ý thức chấp hành Luật phòng, chống ma túy, kỷ luật Quân đội, tác hại của việc tàng trữ, sử dụng chất kích thích nhất là các hợp chất ma túy...
- Kịp thời phát hiện sớm những quân nhân biểu hiện như mục a.
- Chủ động nắm bắt tình hình thực tế để có biện pháp ngăn chặn, dự báo kịp thời những dấu hiệu và hành vi vi phạm kỷ luật của quân nhân. 
- Tăng cường kiểm tra quân tư trang nhất là đối với các quân nhân vừa nghỉ phép, tranh thủ, ra ngoài doanh trại trở lại đơn vị. 
- Có biện pháp ngăn chặn đường xâm nhập của chất cấm vào đơn vị.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Tổ chức tốt các hoạt động trong giờ nghỉ, ngày nghỉ.
- Quan tâm chăm lo chu đáo đời sống vật chất tinh thần cho bộ đội.
8. Mất đoàn kết trong cấp ủy, chỉ huy cơ quan, đơn vị
a) Dấu hiệu nhận biết:
- Không thống nhất trong lãnh đạo, chỉ đạo, triển khai thực hiện nhiệm vụ của cơ quan, đơn vị.
- Lôi kéo, tạo bè phái trong cơ quan, đơn vị.
- Hay nói xấu, đổ lỗi cho nhau trước cấp trên và cấp dưới.
b) Biện pháp phòng ngừa:
- Tăng cường giáo dục xây dựng đoàn kết thống nhất trong cơ quan, đơn vị.
- Thực hiện tốt Quy chế dân chủ ở cơ sở; tăng cường đối thoại giữa cán bộ cấp trên với cấp dưới và chiến sỹ; cán bộ chủ trì phải có tinh thần cầu thị, lắng nghe, tiếp thu ý kiến đóng góp của tập thể.
- Công khai, minh bạch các hoạt động của cơ quan, đơn vị, nhất là tài chính, quỹ vốn; công tác cán bộ, chính sách, thi đua - khen thưởng.
- Thực hiện nghiêm nguyên tắc tổ chức sinh hoạt Đảng, nhất là nguyên tắc tập trung dân chủ, tập thể lãnh đạo, cá nhân phụ trách; quy chế làm việc của cấp ủy, chỉ huy, quy chế lãnh đạo các mặt trọng yếu.
- Cấp ủy, chỉ huy cấp trên phải thường xuyên sâu sát cơ quan, đơn vị trực thuộc, phân công cấp ủy viên dự sinh hoạt Đảng, sinh hoạt đối thoại dân chủ,... để kịp thời nắm tình hình, xử trí, không để kéo dài.
9. Gây mất đoàn kết quân dân
a) Dấu hiệu nhận biết:
- Quân nhân có biểu hiện lo lắng, bồn chồn, suy tư, trên người có thể có sây sát hoặc vết thương.
- Dư luận trong đơn vị có những biểu hiện khác thường, bàn tán, suy diễn xung quanh về sự việc, các quân nhân đang nói chuyện bàn tán thấy chỉ huy đơn vị thì lảng tránh.
- Chiến sĩ dân vận, bảo vệ của đơn vị báo cáo hoặc dư luận xung quanh khu vực đơn vị đóng quân có các thông tin liên quan đến vụ việc gây mất đoàn kết.
- Chính quyền và nhân dân địa phương thông báo.
b) Biện pháp phòng ngừa:
- Tăng cường giáo dục cho quân nhân về ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, nhất là 10 lời thề danh dự của quân nhân, 12 điều kỷ luật khi tiếp xúc với nhân dân, các quy định của đơn vị và địa phương.
- Thường xuyên giáo dục chính trị tư tưởng cho cán bộ, chiến sỹ nêu cao tinh thần trách nhiệm, ý thức tổ chức kỷ luật, phong tục tập quán của người dân địa bàn đóng quân và nơi công tác.
- Tích cực, chủ động nắm bắt tình hình để có biện pháp dự báo, ngăn chặn kịp thời những dấu hiệu và hành vi vi phạm kỷ luật của quân nhân.
- Tăng cường các biện pháp nắm, quản lý của cán bộ các cấp, tính chủ động của mỗi tổ chức đối với quản lý quân nhân thuộc quyền thường xuyên, liên tục ở mọi lúc, mọi nơi, chú ý những thời điểm nhạy cảm.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Duy trì nghiêm các chế độ ngày, tuần.
- Tổ chức giao lưu, kết nghĩa với chính quyền, đoàn thể địa phương.
10. Bị bệnh trầm cảm
a) Dấu hiệu nhận biết:
- Quân nhân thường xuyên có trạng thái trầm uất, giảm hứng thú trong tất cả hoặc đa số hoạt động, mất ngủ, chậm chạp hơn bình thường, ngồi trầm tư một mình.
- Suy giảm khí sắc, buồn bã, ủ rũ, ánh mắt đơn điệu, lờ đờ.
- Mất hưng phấn trong công việc và sở thích trước có.
- Mệt mỏi, giảm khả năng tập trung, giảm cân nặng cơ thể hoặc không quyết định được các vấn đề rất đơn giản, hay xa lánh mọi người.
- Trong sổ tay, nhất ký, vở ghi chép, mạng xã hội thường viết hoặc đăng tải nội dung tiêu cực, tâm trạng u buồn, phàn nàn, than trách thân phận, thậm chí đề cập về cái chết.
- Hoạt động trái quy luật về thời gian như: đêm thức ngày ngủ, sinh hoạt ăn nghỉ, làm việc không đúng thời gian quy định.
- Luôn bi quan trong mọi việc, cảm giác vô vọng, luôn tự ti về bản thân, có ý nghĩ tự tử, tự sát hoặc đã từng tự tử, tự sát không thành.
b) Biện pháp phòng ngừa: 
- Nắm chắc tình hình sức khỏe của quân nhân và lịch sử gia đình.
- Định kỳ hoặc đột xuất kiểm tra quân tư trang cá nhân toàn đơn vị (chú ý nhật ký, vở ghi chép, mạng xã hội…).
- Liên hệ địa phương và gia đình, bạn bè, người thân quân nhân, tìm hiểu nguyên nhân.
- Cán bộ gần gũi, giao tiếp thường xuyên, tổ chức các hoạt động về thể chất, thể dục thể thao, ăn uống, ngủ, nghỉ hợp lý, khoa học.
- Phối hợp chặt chẽ với địa phương, trong công tác tuyển chọn và gọi công dân nhập ngũ, tuyệt đối không tuyển chọn các công dân này vào Quân đội.
11. Nghiện chơi game và các trang mạng xã hội
a) Dấu hiệu nhận biết:
- Không điều khiển được bản thân rời khỏi game và mạng xã hội, thời gian chơi game nhiều hơn 03 giờ/ ngày, liên tục trong thời gian 01 tháng trở lên.
- Coi trọng việc chơi game và lên mạng hơn tất cả những công việc khác.
- Hay nói dối hoặc bỏ bê công việc để chơi game và lên mạng xã hội.
- Khi được giao nhiệm vụ hay quên, chất lượng, hiệu quả thực hiện các nhiệm vụ thấp, chậm tiến độ, không quan tâm, thờ ơ với những hoạt động của đơn vị...
- Có suy nghĩ mơ hồ, sống ảo, có biểu hiện giảm cân hoặc suy nhược cơ thể.
- Có xu hướng hành xử theo các mối quan hệ trong trò chơi online và trên mạng xã hội.
- Có dư luận tập thể quân nhân.
b) Biện pháp phòng ngừa:
- Phát huy vai trò lãnh đạo, chỉ đạo của cấp ủy, tổ chức đảng đối với công tác tuyên truyền, giáo dục pháp luật, kỷ luật, đạo đức, lối sống trong đơn vị nhất là kỹ năng sống, tác hại của nghiện chơi game, mạng xã hội.
- Sâu sát nắm chắc tình hình tư tưởng của quân nhân trong đơn vị. Duy trì chặt chẽ chế độ trong ngày, trong tuần của từng quân nhân.
- Tăng cường các biện pháp nắm, quản lý của cán bộ các cấp, tính chủ động của mỗi tổ chức đối với quản lý quân nhân ở mọi lúc, mọi nơi, nhưng cần chú ý những thời điểm nhạy cảm; đề cao vai trò giám sát của tập thể đơn vị.
Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi con người trong học tập, rèn luyện, công tác. 
- Tổ chức tốt hoạt động giờ nghỉ, ngày nghỉ.
- Quan tâm chăm lo chu đáo đời sống vật chất tinh thần cho bộ đội, thực hiện tốt chính sách quân đội và hậu phương quân đội.
12. Vi phạm pháp luật về giao thông đường bộ
a) Dấu hiệu nhận biết:
- Tính tình bốc đồng, thích thể hiện.
- Chuẩn bị tham gia giao thông có tâm trạng bất ổn, biểu hiện vội vã, luống cuống, mất tập trung.
- Nắm luật giao thông đường bộ không vững.
- Hay uống rượu bia, uống rượu bia say khi tham gia giao thông.
- Điều khiển phương tiện giao thông đường bộ thường phóng nhanh, giành đường, vượt ẩu, lạng lách, đánh võng.
- Có tiền sử bệnh tật (liên quan đến rối loạn tiền đình, bản lĩnh yếu, mắt kém, tay chân không vững...).
- Thích độ xe, thay đổi kết cấu, lắp thêm các thiết bị không đúng quy định.
- Phương tiện dùng để tham gia giao thông không đảm bảo các yếu tố kỹ thuật an toàn (phanh không ăn, đèn xe không đủ sáng, còi, xi nhan hỏng…), xe quá cũ hoặc hết hạn kiểm định.
b) Biện pháp phòng ngừa:
- Tăng cường giáo dục pháp luật cho quân nhân nhất là ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, nhất là Luật giao thông đường bộ.
- Phát huy trách nhiệm lãnh đạo, chỉ đạo của chi bộ, vai trò cán bộ các cấp, các tổ chức trong duy trì và giữ nghiêm kỷ luật quân đội, chú ý những thời điểm ngày nghỉ, giờ nghỉ, tiệc tùng....
- Phát huy vai trò trực ban nội vụ, trực nhật; đề cao vai trò giám sát của tập thể đơn vị; phối hợp tốt giữa cơ quan, đơn vị với chính quyền, nhân dân địa phương và gia đình trong việc quản lý, duy trì kỷ luật, xây dựng ý thức tự giác của từng người.
- Dự báo kịp thời những dấu hiệu và hành vi vi phạm kỷ luật của quân nhân.
- Giáo dục quân nhân ý thức tự giác chấp hành Luật giao thông đường bộ. Định kỳ kiểm tra phương tiện tham gia giao thông và điều kiện tham gia giao thông của quân nhân.
13. Mâu thuẫn trong quan hệ yêu đương nam, nữ
a) Dấu hiệu nhận biết:
- Đến những nơi không người khóc một mình, thời gian nói chuyện điện thoại lâu, lời nói cộc cằn, thô tục, nét mặt giận dữ, thù hận, cũng có thể tâm sự thuyết phục, cầu xin, năn nỉ, nét mặt buồn, não nề.
- Viết hồi ký, nhật ký chuyện tình cảm yêu đương, làm thơ tình buồn.
- Người yêu đột ngột không lên thăm, khi có người hỏi đến buồn bã hoặc cáu gắt.
- Buồn chán, căng thẳng tinh thần kéo dài, mất ngủ, mệt mỏi, trầm cảm, không còn động cơ làm việc, chất lượng hoàn thành nhiệm vụ đột nhiên giảm. 
- Bị mất tập trung, thậm chí không làm gì, ngồi thẫn thờ suy nghĩ về những kỷ niệm đã qua.
- Thông qua nhật ký, vở ghi chép, mạng xã hội thấy được quân nhân bộc lộ cảm xúc chán nản và tuyệt vọng, cho rằng không còn lý do nào để sống nếu thiếu tình yêu của người ấy.
b) Biện pháp phòng ngừa:
- Tăng cường giáo dục pháp luật cho quân nhân nhất là ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, nêu cao phẩm chất đạo đức, bản lĩnh chính trị của ngưới quân nhân cách mạng; giáo dục về tình yêu, hôn nhân và gia đình.
- Đề cao vai trò giám sát của tập thể quân nhân; phối hợp với địa phương, nhân dân và gia đình trong việc nắm, quản lý tư tưởng, quản lý quân nhân.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Quan tâm chăm lo chu đáo đời sống vật chất tinh thần cho bộ đội.
- Định kỳ, đột xuất kiểm tra quân tư trang cá nhân.
14. Quan hệ nam nữ bất chính, vi phạm Luật hôn nhân gia đình
a) Dấu hiệu nhận biết:
- Ít quan tâm đến gia đình, hay cáu gắt với vợ con, gia đình có những dấu hiệu rạn nứt, thường xuyên ngủ lại đơn vị kể cả ngày không trực.
- Tần suất sử dụng điện thoại (nghe, gọi, nhắn tin, zalo, facebook) nhiều hơn, giọng nói nhẹ nhàng, lãng mạn, nghe điện thoại thường né tránh đám đông hoặc chỉ huy. Sử dụng điện thoại riêng chỉ để trong đơn vị…
- Có những cuộc điện thoại bí mật, nói chuyện thường dùng từ không rõ nghĩa, lấp lửng.
- Thường xuyên vắng mặt tại nơi làm việc vào thời gian nghỉ hoặc ra ngoài không có lý do chính đáng, hay đi chơi về khuya. Ăn mặc trải chuốt, gọn gàng, xịt nước hoa, dầu thơm.
- Đối với nam, nữ cùng đơn vị có biểu hiện quan tâm đến mọi hoạt động của nhau vượt quá quan hệ giới hạn tình cảm thông thường. Thích được phân công công tác chung hoặc viện lý do để có thể gặp gỡ nhau trong khoảng thời gian nhất định, có thể có phương tiện liên lạc riêng với ký hiệu đặc biệt.
- Có người cùng đơn vị bắt gặp quân nhân nhiều lần đi cùng người khác giới và có dấu hiệu thân mật khác thường.
- Có dư luận hoặc phản ánh từ gia đình quân nhân. 
b) Biện pháp phòng ngừa:
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định của luật hôn nhân, gia đình, quan hệ 01 vợ, 01 chồng; quy định những điều đảng viên không được làm; Nghị quyết Trung ương 4 (khóa XII),…những thông tin liên quan đến việc xử lý cán bộ công chức quan hệ bất chính xảy ra trên địa bàn và cả nước để răn đe, hệ lụy của hôn nhân đổ vỡ.
- Thường xuyên nắm chắc các mối quan hệ xã hội của quân nhân.
- Duy trì nghiêm chế độ ngày, tuần, quản lý quân số và các mối quan hệ của quân nhân.
- Nắm bắt tâm tư, tình cảm, cuộc sống gia đình của quân nhân.
- Gặp gỡ, giáo dục, định hướng tư tưởng, nhận thức và hành động.
15. Yêu đương đồng giới
a) Dấu hiệu nhận biết:
- Dáng đi, giọng nói, cử chỉ, điệu bộ thường hay ẻo lả, nhẹ nhàng, khép nép, yểu điệu.
- Cảm thấy luống cuống, bối rối, hồi hộp khi đối diện với đồng chí điển trai khác, hoặc thường xuyên khen ngợi, thích trò chuyện, bàn luận về vẻ đẹp của nam giới. 
- Đứng trước người cùng giới có ngoại hình và khuôn mặt ưa nhìn, thường hướng ánh mắt và sự chú ý, hay có biểu hiện nhìn trộm, trìu mến. 
- Không có hứng thú với phụ nữ, xem phụ nữ dù là xinh đẹp đến đâu cũng chỉ là bạn.
- Hay chăm chút cho bản thân, hay sử dụng mỹ phẩm và luôn ước muốn mình trở nên đẹp hơn.
- Có lối sống, sinh hoạt cá nhân khác biệt mọi người như: thích tắm một mình, kín đáo.
- Thích (thầm yêu) một đồng chí nào đó trong đơn vị.
- Ít hòa đồng với đồng chí, đồng đội…
b) Biện pháp phòng ngừa: Phối hợp với địa phương trong sàng lọc, tuyển chọn quân nhân nhập ngũ.
16. Thu tiền sai quy định 
a) Dấu hiệu nhận biết
- Nhiều cán bộ, chiến sĩ bộc lộ tâm lý không thoải mái, có thái độ thiếu tôn trọng cấp trên, có những lời nói liên quan tới vấn đề tiền bạc, chi tiêu, thấy chỉ huy thì lảng tránh.
- Chiến sĩ bảo vệ, dân vận báo cáo; dư luận trong đơn vị bàn tán; cán bộ, chiến sĩ hoặc người nhà, người thân của cán bộ, chiến sĩ phản ánh…
- Có sự phân biệt, đối xử trong chỉ huy, quản lý.
b) Biện pháp phòng ngừa
- Cấp có thẩm quyền xây dựng quy chế, quy định về công tác quản lý tài chính, tổ chức quán triệt, triển khai thực hiện và phân công cán bộ kiểm tra chặt chẽ.
- Thường xuyên công khai tài chính.
- Thực hiện tốt Quy chế dân chủ cơ sở; tổ chức có hiệu quả Ngày Chính trị và văn hóa tinh thần, Ngày Pháp luật.
- Phát huy vai trò của Chiến sĩ bảo vệ, dân vận, “Tổ tư vấn tâm lý, pháp lý”, “Hòm thư góp ý”; khảo sát (điều tra xã hội học) để kịp thời nắm tình hình đơn vị.
17. Dựa dẫm vào mối quan hệ và người thân, thiếu rèn luyện phấn đấu
a) Dấu hiệu nhận biết
- Gia đình có điều kiện về kinh tế.
- Ham chơi, lười biếng, thích thể hiện, tính sĩ diện cao.
- Hay tụ tập, chấp hành kỷ luật không nghiêm.
- Khoe khoang có người thân là lãnh đạo làm ở chỗ này, chỗ kia...
b) Biện pháp phòng ngừa
-Tăng cường giáo dục cho quân nhân toàn đơn vị ý thức chấp hành pháp luật Nhà nước, kỷ luật Quân đội, quy định của đơn vị. Xây dựng ý thức tự rèn luyện phẩm chất đạo đức cách mạng của người quân nhân.
- Gặp gỡ quân nhân giáo dục nhận thức đúng, sai, tác hại của việc dựa dẫm ỷ lại, chấp hành kỷ luật không nghiêm.
- Phối hợp với gia đình, địa phương trong việc động viên quân nhân thực hiện chức trách, nhiệm vụ, ý thức chấp hành kỷ luật.
- Quản lý chặt chẽ quân nhân, dự báo những dấu hiệu vi phạm, kịp thời ngăn chặn.
- Duy trì nghiêm chế độ ngày, tuần.
- Báo cáo cấp trên xin ý kiến chỉ đạo.
18. Mất an toàn trong huấn luyện, công tác
- Chưa đảm bảo các biện pháp an toàn trong thực hiện nhiệm vụ.
- Quá trình thực hiện nhiệm vụ, trường hợp chỉ có một quân nhân thực hiện, dễ dẫn đến khó phát hiện các nguy hiểm có thể phát sinh và phòng ngừa như gãy cây, ngã thang, trượt chân, chập điện,….
- Phân công nhiệm vụ chưa xem xét sở trường, khả năng của quân nhân với yêu cầu thực hiện nhiệm vụ.
- Quân nhân thực hiện nhiệm vụ ngoài doanh trại, tại nhà riêng, không có sự theo dõi, giám sát của đơn vị.
b) Biện pháp phòng ngừa
- Tăng cường giáo dục, bồi dưỡng cho quân nhân kỹ năng, kinh nghiệm trong thực hiện nhiệm vụ; cách nhận biết các rủi ro, tình huống nguy hiểm có thể phát sinh khi thực hiện nhiệm vụ.
- Trước khi phân công phải xem xét tính chất, yêu cầu nhiệm vụ; căn cứ khả năng, kinh nghiệm của từng quân nhân để phân công cho phù hợp. 
- Hạn chế phân công quân nhân thực hiện nhiệm vụ độc lập, bố trí ít nhất từ 02 quân nhân trở lên để thực hiện nhiệm vụ, hỗ trợ lẫn nhau. Trường hợp cần thiết, phân công cán bộ hướng dẫn, theo dõi, giám sát lao động.
- Phải có nhân viên chuyên môn hướng dẫn các biện pháp bảo đảm an toàn trước khi lao động, học tập (sửa điện, các bài thể thao, bơi…).
- Trang bị bảo hộ và các biện pháp an toàn cần thiết cho quân nhân như mũ bảo vệ, dây an toàn, ngắt điện, thông báo và ngăn cách tạm thời khu vực lao động…
- Quán triệt quân nhân tuân thủ các quy định an toàn lao động cả khi lao động tại nhà riêng, ngoài doanh trại.
- Giáo dục cho mọi người cách xử trí khi xảy ra mất an toàn như: cháy, nổ, chập điện, đuối nước, ngã từ trên cao, rắn cắn…
19. Bạo lực gia đình (cha, mẹ, vợ, chồng, con)
a) Dấu hiệu nhận biết
- Biểu hiện cục cằn, thô lỗ với vợ con; thường xuyên chửi mắng, dọa nạt, đe dọa hành hung; chuẩn bị sẵn hung khí để ra tay; thường xuyên chửi mắng vợ con mỗi khi có hơi men…
- Nghe phản ánh của người dân, bạn bè, đồng nghiệp và chính vợ, con phản ánh về hành vi ngược đãi, đánh đập làm tổn thương tới sức khỏe, tính mạng của họ; quan sát thấy vợ, con có dấu hiệu bị đánh đập, tâm lý hoảng loạn, luôn lo sợ. 
- Có hành vi hành hạ, ngược đãi, đánh đập hoặc hành vi cố ý khác xâm hại đến sức khoẻ, tính mạng.
- Dùng lời nói, thái độ, hành vi làm tổn thương tới danh dự, nhân phẩm, tâm lý của thành viên gia đình.
- Cô lập, xua đuổi hoặc thường xuyên gây áp lực về tâm lý gây hậu quả nghiêm trọng.
- Ngăn cản việc thực hiện quyền, nghĩa vụ trong quan hệ gia đình giữa ông, bà và cháu; giữa cha, mẹ và con; giữa vợ và chồng; giữa anh, chị, em với nhau.
- Cưỡng ép quan hệ tình dục, cưỡng ép sinh con theo ý muốn, cấm vận về tình dục.
- Cưỡng ép tảo hôn; cưỡng ép kết hôn, ly hôn hoặc cản trở hôn nhân tự nguyện, tiến bộ của con cái.
- Chiếm đoạt, huỷ hoại, đập phá hoặc có hành vi khác cố ý làm hư hỏng tài sản riêng của thành viên khác trong gia đình hoặc tài sản chung của các thành viên gia đình.
- Cưỡng ép thành viên gia đình lao động quá sức, đóng góp tài chính quá khả năng của họ; kiểm soát quá khắt khe thu nhập của thành viên gia đình nhằm tạo ra tình trạng phụ thuộc về tài chính.
- Có hành vi trái pháp luật buộc thành viên gia đình ra khỏi chỗ ở.
b) Biện pháp phòng ngừa:
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định của Luật Phòng, chống bạo lực gia đình, Luật Bình đẳng giới; Luật hôn nhân, gia đình; Bộ luật hình sự; Nghị quyết Trung ương 4 (khóa XII); quy định những điều đảng viên không được làm; quy định nêu gương…, những thông tin liên quan đến việc xử lý bạo lực gia đình để răn đe, cảnh tỉnh.
- Tăng cường giáo dục cho quân nhân về ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, nhất là 10 lời thề danh dự của quân nhân, 12 điều kỷ luật khi tiếp xúc với nhân dân, các quy định của đơn vị và địa phương; giáo dục phát huy truyền thống tốt đẹp của đơn vị, gia đình; vai trò của họ hàng.
- Thường xuyên giáo dục chính trị tư tưởng cho cán bộ, chiến sỹ nêu cao tinh thần trách nhiệm trong xây dựng đơn vị, xây dựng gia đình trên cương vị là người chồng, người cha.
- Thường xuyên giữ mối liên hệ với gia đình quân nhân. Tổ chức các sự kiện gặp mặt gia đình quân nhân vào các dịp: 8/3; ngày gia đình Việt Nam 28/6; ngày 20/10; tất niên của đơn vị…
- Thường xuyên nắm chắc các mối quan hệ xã hội của quân nhân, nhất là quan hệ nam nữ.
- Yêu cầu kê khai đầy đủ các số điện thoại và các tài khoản mạng xã hội đang sử dụng.
- Chỉ huy đơn vị phải gần gũi, sâu sát, nắm bắt tâm tư, tình cảm, cuộc sống gia đình của quân nhân để có biện pháp dự báo, ngăn chặn kịp thời những dấu hiệu và hành vi vi phạm kỷ luật của quân nhân.
- Gặp gỡ, giáo dục, định hướng tư tưởng, nhận thức và hành động đối với các quân nhân có biểu hiện vi phạm.
- Tăng cường các biện pháp nắm, quản lý của cán bộ các cấp, tính chủ động của mỗi tổ chức đối với quản lý quân nhân thuộc quyền thường xuyên, liên tục ở mọi lúc, mọi nơi, chú ý những thời điểm nhạy cảm.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị; chăm lo đời sống vật chất, tinh thần, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Đưa nội dung phòng, chống bạo lực gia đình vào tiêu chí hoạt động thi đua, khen thưởng; phân loại các tổ chức, cá nhân hằng năm.

20. Uống rượu, bia say, bê tha, sai quy định
a) Dấu hiệu nhận biết
- Có lối sống thích ăn chơi, hưởng thụ; ngại huấn luyện, học tập, lao động, công tác, lười thể thao.
- Thường xuyên tụ tập, đàn đúm, tìm mọi lý do để gạ gẫm, lôi kéo, mời chào tổ chức ăn nhậu.
- Bị lệ thuộc vào rượu, luôn có quan điểm tiêu cực “làm việc trên bàn nhậu”.
- Sử dụng rượu, bia và đồ uống có cồn mọi lúc mọi nơi, ngay cả trong giờ làm việc. Thích uống rượu vào buổi sáng.
- Mất kiểm soát về lời nói và hành động khi sử dụng rượu, bia, như: Nói ngọng (nói lè nhè), nói quá to hoặc quá nhỏ, thích tâm sự, nói năng không chuẩn mực, vật lộn với từ ngữ khi nói, nói chậm hơn bình thường hoặc cứ lặp đi lặp lại lời đã nói, nói dai, nói dài; thích điện thoại cho người khác để tâm sự hoặc để thể hiện sự bức xúc về một vấn đề nào đó; thích đi đến những nơi sôi động: karaoke, vũ trường, quán bar; đi đến những nơi không lành mạnh: massa trá hình, karaoke ôm, khách sạn; chóng mặt, mất thăng bằng, đi lại loạng choạng hoặc tự ngã; nôn ọe, đi vệ sinh không kiểm soát; đi xe máy (ô tô) nhanh hơn bình thường, lạng lách; tính khí hung hăng, bốc đồng, khó kiểm soát hành vi và kiềm chế bản thân.
- Quần áo xộc xệch, mặt đỏ, hơi thở có mùi cồn; ánh mắt đờ đẫn, vằn đỏ, mí mắt rũ xuống, khó mở to mắt, ngủ li bì, ngủ ngáy to.
- Thích hút thuốc.
b) Biện pháp phòng ngừa:
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định về Luật phòng, chống tác hại của rượu bia 2019; quy định về những điều đảng viên không được làm (đặc biệt là Điều 18 trong Quy định 37 về hành vi vi phạm sử dụng rượu, bia không đúng quy định hoặc đến mức bê tha và các tệ nạn xã hội khác); quy định nêu gương; Nghị quyết Trung ương 4 (khóa XII),…những thông tin liên quan đến các vụ việc vi phạm kỷ luật liên quan đến sử dụng rượu, bia để răn đe, cảnh tỉnh.
- Tăng cường giáo dục cho quân nhân về ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, nhất là 10 lời thề danh dự của quân nhân, 12 điều kỷ luật khi tiếp xúc với nhân dân, các quy định của đơn vị và địa phương về việc không sử dụng rượu bia trong ngày làm việc, ngày trực, kể cả giờ nghỉ trưa.
- Thường xuyên giáo dục chính trị tư tưởng cho cán bộ, chiến sỹ nêu cao tinh thần trách nhiệm trong xây dựng đơn vị, xây dựng hình ảnh người quân nhân cách mạng. Tổ chức các buổi tọa đàm, sân khấu hóa trong các hội thi, hội diễn văn nghệ quần chúng để nâng cao nhận thức cho quân nhân về việc uống rượu, bia say, bê tha, sai quy định.
- Tăng cường công tác lãnh đạo, chỉ đạo, kiểm tra của cấp ủy, chỉ huy các cấp và cơ quan chức năng.
- Duy trì nghiêm chế độ ngày, tuần, quản lý chặt chẽ quân số mọi lúc, mọi nơi, nhất là trong ngày nghỉ, giờ nghỉ; thường xuyên kiểm tra lễ tiết, tác phong quân nhân.
- Phát huy trách nhiệm nêu gương của cán bộ, đảng viên mọi lúc, mọi nơi, nhất là người đứng đầu. Chỉ huy đơn vị phải gần gũi, sâu sát, nắm bắt tâm tư, tình cảm, cuộc sống gia đình của quân nhân để có biện pháp dự báo, ngăn chặn kịp thời những dấu hiệu và hành vi vi phạm kỷ luật của quân nhân.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị; chăm lo đời sống vật chất, tinh thần, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Khuyến khích nghiên cứu khoa học, phát triển công nghệ và ứng dụng công nghệ cao, công nghệ tiên tiến, công nghệ mới nhằm giảm tác hại của rượu, bia.
- Khen thưởng tập thể, cá nhân có thành tích trong phòng, chống tác hại của rượu, bia.
21. Nghiện ma túy
a) Dấu hiệu nhận biết
- Mắt đỏ ướt long lanh, đồng tử teo, sụp mi mắt; giọng nói khàn khàn, uống nhiều nước lạnh, tâm lý ở trạng thái hưng phấn cao, nói nhiều, cử chỉ và động tác thiếu chính xác. Nếu có tật thì tật thường xuất hiện ở mức cao như vuốt mũi, nhổ râu, nặn mụn, cắn móng tay, lấy ráy tai; ngồi tại chỗ mắt lim dim, gãi chân tay, vò đầu, bứt tóc; hay ngáp vặt, người lừ đừ, mệt mỏi, ngại lao động, bỏ vệ sinh cá nhân …
- Tìm chỗ yên tĩnh để thưởng thức cơn phê; nằm như ngủ nhưng không ngủ, lại hút nhiều thuốc lá, tàn thuốc vung vãi; quan sát nơi nghỉ thường thấy chăn màn thủng do tàn thuốc lá rơi vào, bề bộn đồ đạc, hôi hám.
- Tâm trạng thường lo lắng, bồn chồn, đôi khi nói nhiều, hay nói dối, hay có biểu hiện chống đối, cáu gắt hơn so với trước đây. 
- Giờ giấc sinh hoạt thay đổi thất thường: thức khuya, đêm ngủ ít, dậy muộn, ngày ngủ nhiều…; trong các hoạt động tập thể thường có mặt muộn hoặc vắng mặt (thường vào giờ nhất định). 
- Đi lại có quy luật: Mỗi ngày, cứ đến một giờ nhất định nào đó, dù đang bận việc gì cũng tìm cách, kiếm cớ để đi khỏi nhà, đơn vị.
- Thích ở một mình, ít hoặc ngại tiếp xúc với mọi người (kể cả người thân trong gia đình). Hay tụ tập, quan hệ với người có lối sống sinh hoạt buông thả, lười lao động, học tập, sinh hoạt… hoặc chơi thân với người sử dụng ma túy.
- Nhu cầu tiêu tiền ngày một nhiều, sử dụng tiền không có lý do chính đáng, thường xuyên xin tiền người thân và hay bán đồ đạt cá nhân, gia đình, nợ nần nhiều, ăn cắp vặt, hay lục túi người khác…
- Trong túi quần, áo, cặp, phòng ngủ thường có các thứ giấy bạc, thuốc lá, kẹo cao su, bật lửa ga, bơm kim tiêm, uống thuốc, thuốc phiện, gói nhỏ heroin.
- Có dấu kim trên mu bàn tay, cổ tay, mặt trong khuỷu tay, mặt trong mắt cá chân, ở bẹn, ở cổ…
b) Biện pháp phòng ngừa:
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định có liên quan đến phòng, chống việc sử dụng các chất ma túy, tác hại của việc sử dụng ma túy để răn đe, cảnh tỉnh.
- Tăng cường công tác lãnh đạo, chỉ đạo của cấp ủy, tổ chức đảng, cán bộ chủ trì các cấp trong phòng chống ma túy.
- Quản lý chặt chẽ quân nhân trong đơn vị, đặc biệt là quản lý các mối quan hệ quân nhân, chú ý các trường hợp cá biệt, có tiền sử nghiện thuốc lá và các chất kích thích khác. 
	- Khi phát hiện quân nhân trong đơn vị có biểu hiện sử dụng ma tuý cần báo ngay lãnh đạo, chỉ huy đơn vị và cơ quan chức năng để kịp thời xử lý.
	- Phối hợp với địa phương, đơn vị kết nghĩa xây dựng môi trường văn hóa đơn vị lành mạnh; tổ chức các buổi tọa đàm hoặc sân khấu hóa trong các hội thi, hội diễn văn nghệ quần chúng để nâng cao nhận thức cho quân nhân về tác hại ma túy và tham gia phòng, chống ma túy, góp phần tham gia đấu tranh phòng chống ma túy có hiệu quả.
22. Buôn bán, tàng trữ ma túy, chất cấm
a) Dấu hiệu nhận biết
- Nghiện ma túy; có mối quan hệ xã hội phức tạp cả ở đời thực và trên mạng xã hội.
- Sử dụng nhiều số điện thoại, nhiều tài khoản mạng xã hội một cách bất thường nhưng không báo cáo.
- Có quan hệ với các đối tượng nghiện ma túy hoặc sản xuất, mua bán, tàng trữ ma túy.
- Muốn làm giàu nhanh chóng hoặc thích hưởng thụ, lười lao động, học tập, công tác.
- Có những nguồn thu nhập bất chính, không chứng minh được nguồn gốc tài sản.
- Hay khoe khoang có mối quan hệ với lãnh đạo địa phương, cơ quan công an, các tập đoàn, doanh nghiệp…; có thể chạy việc…; khoe khoang cuộc sống sang chảnh, giàu sang, đi du lịch, đến các nơi sang trọng.
- Thường thuê nhà trọ, khách sạn để liên hệ mua bán ma túy hoặc đến các quán karaoke, quán bar,… để sử dụng ma túy.
- Nhà ở xây kín cổng cao tường, lắp đặt hệ thống an ninh, camera theo dõi từ xa hoặc có bảo vệ, cảnh giác với người lạ. Rất ít đi ra ngoài, ít tiếp xúc với người xung quanh.
- Thường xuyên vận chuyển các chất hóa học về nhà như: cồn công nghiệp, acid, photpho đỏ, thuốc tân dược,…
- Xin nghỉ phép hoặc tranh thủ không rõ lý do chính đáng, sau đó thuê nhà nghỉ, khách sạn trong thời gian dài, thường xuyên có nhiều người đến phòng tìm để giao dịch mua bán ma túy.
- Thường xuyên tụ tập, đi theo từng nhóm từ 3-4 người. Đa số mang theo ba lô, túi xách bên trong chứa laptop, máy nghe nhạc, loa, bình ga...
- Không tập trung chuyên môn và công việc ở đơn vị. Đi lại tự do, tùy tiện nhưng bí mật, thay đổi lịch trình thường xuyên, cảnh giác; thay đổi nhiều loại phương tiện, trang phục, nơi cư trú…
b) Biện pháp phòng ngừa:
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định có liên quan đến phòng, chống việc mua bán, tàng trữ ma túy, chất cấm.
- Tăng cường công tác lãnh đạo, chỉ đạo của cấp ủy, tổ chức đảng, cán bộ chủ trì các cấp trong phòng chống ma túy.
- Quản lý chặt chẽ quân nhân trong đơn vị, đặc biệt là quản lý các mối quan hệ quân nhân, chú ý các trường hợp có dấu hiệu mua bán, tàng trữ ma túy, chất cấm. Khi phát hiện hoặc nhận được thông tin tố cáo quân nhân trong đơn vị có biểu hiện mua bán, tàng trữ ma tuý, chất cấm cần báo ngay lãnh đạo, chỉ huy đơn vị và cơ quan chức năng để kịp thời xử lý.
	- Phối hợp với địa phương, đơn vị kết nghĩa xây dựng môi trường văn hóa đơn vị lành mạnh. Tổ chức các buổi tọa đàm hoặc sân khấu hóa trong các hội thi, hội diễn văn nghệ quần chúng để nâng cao nhận thức cho quân nhân về tác hại ma túy, chất cấm và tham gia phòng, chống ma túy, chất cấm, góp phần tham gia đấu tranh phòng chống ma túy, chất cấm có hiệu quả.
23. Sử dụng, buôn bán vũ khí quân dụng trái phép
a) Dấu hiệu nhận biết
- Muốn làm giàu nhanh chóng hoặc thích hưởng thụ, lười lao động, học tập, công tác.
- “Giàu” lên một cách bất thường và nhanh chóng, không chứng minh được khoản thu nhập tăng đột biến; tiêu tiền nhiều hơn một cách bất thường.
- Hay tìm hiểu về các loại vũ khí một cách bất thường, không sát với chức trách, nhiệm vụ, không phục vụ cho nhiệm vụ huấn luyện, sẵn sàng chiến đấu.
- Có mối quan hệ xã hội phức tạp, nhất là với các đối tượng có tiền án, tiền sự, tội phạm có liên quan đến các nhóm tội về chế tạo, tàng trữ, vận chuyển, sử dụng, mua bán trái phép hoặc chiếm đoạt vũ khí quân dụng, phương tiện kỹ thuật quân sự.
- Sử dụng nhiều số điện thoại, nhiều tài khoản mạng xã hội một cách bất thường nhưng không báo cáo. Điện thoại cho người khác một cách lén lút, bí mật, tâm lý cảnh giác, lo âu, luôn cảnh giác với người lạ.
- Có những mâu thuẫn căng thẳng với các quân nhân trong đơn vị hoặc người ngoài quân đội.
- Thường xuyên quan sát, để ý hành động, thói quen sinh hoạt của chỉ huy đơn vị, cán bộ quản lý vũ khí, trang bị nhằm tìm sơ hở để thực hiện hành vi lấy trộm vũ khí quân dụng.
- Quan tâm hơn tin tức trên tivi, báo chí về các vụ việc vi phạm.
- Đi lại bí ẩn, lịch trình không rõ ràng. 
- Cơ thể bị xây xát, bầm tím hoặc quần áo bị rách, có vết máu khi đi từ bên ngoài về nhà, đơn vị.
- Thích đi săn, đôi khi có chim, thú mang về…
- Nhà riêng lắp đặt hệ thống an ninh, camera theo dõi từ xa một cách bất thường. 
b) Biện pháp phòng ngừa:
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định của Bộ luật hình sự; quy định những điều đảng viên không được làm; Nghị quyết Trung ương 4 (khóa XII),…những thông tin liên quan đến các vụ việc sử dụng, buôn bán trái phép vũ khí quân dụng để răn đe, cảnh tỉnh.
- Tăng cường giáo dục cho quân nhân về ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, nhất là 10 lời thề danh dự của quân nhân, 12 điều kỷ luật khi tiếp xúc với nhân dân, các quy định của đơn vị và địa phương; giáo dụcphát huy truyền thống tốt đẹp của đơn vị, gia đình.
- Thường xuyên giáo dục chính trị tư tưởng cho cán bộ, chiến sỹ nêu cao tinh thần trách nhiệm trong xây dựng đơn vị.
- Chỉ huy đơn vị phải gần gũi, sâu sát, nắm bắt tâm tư, tình cảm, sức khỏe, cuộc sống gia đình của quân nhân. Phân công cán bộ theo phân cấp, đảng viên, chiến sĩ bảo vệ tăng cường các biện pháp nắm, quản lý quân nhân thuộc quyền thường xuyên, liên tục ở mọi lúc, mọi nơi, chú ý những thời điểm nhạy cảm; nắm chắc các mối quan hệ xã hội của quân nhân, nhất là với các thành phần phức tạp, kịp thời phát hiện những biểu hiện khác thường trong sinh hoạt của quân nhân.
- Thường xuyên kiểm tra quân tư trang toàn đơn vị… Tìm hiểu, nắm rõ nguồn tài sản có giá trị, việc chi tiêu quá thu nhập của quân nhân.
- Tăng cường lắp đặt hệ thống camera an ninh ở các khu vực công cộng, nhà ở…
- Quản lý chặt chẽ vũ khí, trang bị nhất là sau khi huấn luyện, diễn tập, bắn đạn thật, hành quân… có biện pháp bảo đảm an toàn đối với kho quân khí, các tủ súng của đơn vị.
- Yêu cầu kê khai đầy đủ các số điện thoại và các tài khoản mạng xã hội đang sử dụng.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị; chăm lo đời sống vật chất, tinh thần, tạo điều kiện thuận lợi cho mỗi quân nhân trong học tập, rèn luyện, công tác. 
- Tổ chức các buổi tọa đàm hoặc sân khấu hóa trong các hội thi, hội diễn văn nghệ quần chúng để nâng cao nhận thức cho quân nhân về sử dụng, buôn bán vũ khí, quân dụng trái phép.
24. Trộm, cướp tài sản
b) Dấu hiệu nhận biết
- Muốn làm giàu nhanh chóng hoặc thích hưởng thụ, lười lao động, học tập, công tác.
- “Giàu” lên một cách bất thường và nhanh chóng, không chứng minh được khoản thu nhập tăng đột biến; tiêu tiền nhiều hơn bình thường.
- Có các vật dụng mới như: điện thoại, máy tính, dây chuyền, ví da… không rõ nguồn gốc.
- Cho quà người khác một cách bí mật, riêng tư, tâm lý cảnh giác.
- Thường xuyên có những hành vi lấm lét để ý, quan sát rất kỹ càng tài sản, thói quen, lịch trình và giờ giấc sinh hoạt của người khác.
- Tâm lý luôn bất ổn, lo lắng. Đi lại không công khai, bí ẩn.
- Quan tâm quá mức bình thường các vụ trộm cắp tài sản trên trên tivi, báo chí, mạng xã hội, phim ảnh.
- Cơ thể bị xây xát, bầm tím hoặc quần áo bị rách, có vết máu; bị ướt khi đi từ bên ngoài về nhà, đơn vị.
b) Biện pháp phòng ngừa:
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định của Bộ luật hình sự; quy định những điều đảng viên không được làm; Nghị quyết Trung ương 4 (khóa XII),… những thông tin liên quan đến các vụ việc trộm, cướp tài sản để răn đe, cảnh tỉnh.
- Tăng cường giáo dục cho quân nhân về ý thức chấp hành Pháp luật Nhà nước, kỷ luật Quân đội, nhất là 10 lời thề danh dự của quân nhân, 12 điều kỷ luật khi tiếp xúc với nhân dân, các quy định của đơn vị và địa phương; giáo dụcphát huy truyền thống tốt đẹp của đơn vị, gia đình.
- Thường xuyên giáo dục chính trị tư tưởng cho cán bộ, chiến sỹ nêu cao tinh thần trách nhiệm trong xây dựng đơn vị.
- Đẩy mạnh công tác tuyên truyền, vận động mọi quân dân nâng cao ý thức cảnh giác, tự bảo quản tài sản của mình và tích cực tham gia tố giác, lên án các hành vị trộm cắp tài sản.
- Phối hợp chặt chẽ giữa đơn vị, địa phương và gia đình làm tốt công tác quản lý, giáo dục quân nhân về đạo đức, lối sống, văn hóa trong sạch, lành mạnh và ý thức chấp hành kỷ luật, pháp luật, có trách nhiệm của bản thân đối với đơn vị, gia đình.
- Chỉ huy đơn vị phải gần gũi, sâu sát, nắm bắt tâm tư, tình cảm, sức khỏe, cuộc sống gia đình của quân nhân. Phân công cán bộ theo phân cấp, đảng viên, chiến sĩ bảo vệ tăng cường các biện pháp nắm, quản lý quân nhân thuộc quyền thường xuyên, liên tục ở mọi lúc, mọi nơi, chú ý những thời điểm nhạy cảm; nắm chắc các mối quan hệ xã hội của quân nhân, nhất là với các thành phần phức tạp, kịp thời phát hiện những biểu hiện khác thường trong sinh hoạt của quân nhân.
- Thường xuyên kiểm tra quân tư trang toàn đơn vị, quản lý chặt chẽ thiết bị nghe, nhìn… Tìm hiểu, nắm rõ nguồn tài sản có giá trị, việc chi tiêu quá thu nhập của quân nhân.
- Định kỳ hoặc đột xuất kiểm tra thẻ đảng viên, chứng minh sĩ quan, QNCN, bằng tốt nghiệp…
- Tăng cường lắp đặt hệ thống camera an ninh ở các khu vực công cộng, nhà ở…
- Không dừng, đậu xe nơi tối vắng, nếu phải qua khu vực này nên đi từ 2 người, cảnh giác khi có đối tượng nghi vấn.
- Không sử dụng điện thoại khi đi đường, trường hợp cần thì đậu xe trên lề và quan sát xung quanh.
- Nếu có nhu cầu vận chuyển tiền với số lượng lớn, cần phải dùng xe chuyên dụng hoặc ô tô, bố trí đủ người canh giữ bảo vệ khi đưa tiền lên xuống.
- Khi đi đường, người đeo dây chuyền vòng vàng cần cài kín nút áo cổ, không để lộ trang sức ra ngoài. Nếu mang túi xách nên bỏ vào cốp xe hoặc móc chặt vào xe ràng buộc kỹ càng.
- Khi rút tiền ở ngân hàng và điểm ATM nên có người đi cùng và quan sát cảnh giác.
- Trên đường đi nếu phát hiện có đối tượng nghi vấn bám theo thì chạy chậm sát lề đường hoặc tấp vào nơi có đông người.
- Khi bị cướp giật phải tri hô, đồng thời ghi nhớ nhận dạng, loại xe, biển số… và đến ngay cơ quan Công an gần nhất trình báo, đồng thời về báo cáo chỉ huy đơn vị.
25. Làm kinh tế sai quy định
a) Dấu hiệu nhận biết
- Biểu hiện muốn làm giàu nhanh chóng hoặc thích hưởng thụ, lười lao động, học tập, công tác.
- Có sự gia tăng đột biến về tài sản nhưng không thể chứng minh được nguồn gốc của lượng tài sản gia tăng đó.
- Có mối quan hệ xã hội phức tạp cả ở đời thực và trên mạng xã hội.
- Sử dụng nhiều số điện thoại, nhiều tài khoản mạng xã hội nhưng không báo cáo.
- Có mối quan hệ mật thiết với những đối tượng làm ăn phi pháp.
- Khoe khoang cuộc sống sang chảnh, giàu sang, hàng hiệu, đi du lịch, đến các nơi sang trọng. Thường xuyên tiếp khách, ăn nhậu, có những buổi tiệc tùng tốn kém.
- Hay khoe khoang có mối quan hệ với lãnh đạo địa phương, cơ quan công an, các tập đoàn, doanh nghiệp… và khả năng chạy việc làm.
- Đi lại tự do, tùy tiện; thường xuyên vắng mặt tại cơ quan, đơn vị không rõ lý do.
- Không tập trung thực hiện chức trách, kết quả hoàn thanh nhiệm vụ thấp.
- Nhà ở xây kín cổng cao tường, lắp đặt hệ thống an ninh, camera theo dõi từ xa hoặc có bảo vệ một cách bất thường.
- Tham gia vào các nhóm đa cấp trá hình, các nhóm cò mồi đất….
b) Biện pháp phòng ngừa:	
- Giáo dục pháp luật cho quân nhân nhất là ý thức chấp hành pháp luật Nhà nước, kỷ luật Quân đội, các quy định trong hoạt động kinh doanh; cảnh giác trước các phương thức lừa đảo; có kiến thức về tác hại của việc làm kinh tế sai quy định; sống có nguyên tắc chi tiêu hợp lý, phù hợp với khả năng tài chính của gia đình.
- Tuyên truyền, vận động, xây dựng cho quân nhân lối sống trong sạch, lành mạnh, có trách nhiệm đối với gia đình. Kết hợp công tác giáo dục, tuyên truyền giải thích, thuyết phục với duy trì chặt chẽ, nghiêm túc kỷ luật của Quân đội, đơn vị.
- Tăng cường các biện pháp nắm, quản lý của cán bộ các cấp, nhất là mối quan hệ xã hội, việc chi tiêu của quân nhân. Làm tốt công tác hậu phương quân đội, phối hợp chặt chẽ với gia đình để quản lý quân nhân.
- Thực hiện nghiêm túc việc kê khai tài sản hằng năm, phát huy vai trò nêu gương của người đứng đầu. Xác minh nguồn tài sản có giá trị không rõ nguồn gốc hoặc nghi ngờ, việc chi tiêu quá thu nhập của quân nhân.
- Thực hiện công tác kiểm tra, giám sát đúng quy định; xác định đối tượng kiểm tra, giám sát tập trung vào các lĩnh vực nhạy cảm, vị trí dễ xảy ra vi phạm; chú trọng công tác kiểm tra, giám sát việc thực hiện cam kết của cán bộ, đảng viên ở cơ quan, đơn vị và địa phương.
- Biểu dương những quân nhân, người lao động vừa hoàn thành tốt nhiệm vụ đơn vị, vừa phát triển kinh tế gia đình đúng quy định của pháp luật.
- Có chính sách, quy định chế độ khen thưởng cả về vật chất và tinh thần, bảo đảm công khai, dân chủ, công bằng. Có chế độ đãi ngộ để từng bước nâng cao đời sống vật chất, tinh thần và lợi ích thiết thực của quân nhân trong đơn vị.
26. Sử dụng tài chính, đất quốc phòng, tài sản công sai quy định
a) Dấu hiệu nhận biết
- “Giàu” lên một cách bất thường và nhanh chóng, có nhiều tài sản có giá trị như: bất động sản, xe ô tô, vàng, đồ gỗ có giá trị… không chứng minh được khoản thu nhập tăng đột biến.
- Cán bộ có thẩm quyền quản lý tài chính, đất quốc phòng, tài sản công sử dụng vào mục đích sản xuất, làm giàu cho cá nhân hoặc “nhóm lợi ích”.
- Có mối quan hệ xã hội phức tạp cả ở đời thực và trên mạng xã hội.
- Sử dụng nhiều số điện thoại, nhiều tài khoản mạng xã hội nhưng không báo cáo.
- Lập nhiều tài khoản ngân hàng; mua bán cổ phiếu, tiền ảo.
- Mua bán hóa đơn, chứng từ sai quy định. 
- Khoe khoang cuộc sống sang chảnh, giàu sang, đi du lịch, đến các nơi sang trọng.
- Hay khoe khoang có mối quan hệ với lãnh đạo địa phương, cơ quan công an, các tập đoàn, doanh nghiệp…có thể chạy việc….
- Thường xuyên có mối quan hệ làm ăn với các công ty xây dựng, khai thác khoáng sản, buôn bán bất động sản…
- Thường xuyên tiếp đãi, đưa phong bì các đoàn công tác, thanh tra, kiểm toán Nhà nước, lãnh đạo cấp trên…
- Biểu hiện lo lắng trước các thông tin khiếu nại, tố cáo, thanh tra, kiểm tra.
b) Biện pháp phòng ngừa
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định về quản lý, sử dụng tài chính, đất quốc phòng, tài sản công cho các đối tượng, nhất là các cá nhân, tổ chức có liên quan trực tiếp đến hoạt động quản lý, sử dụng.
- Làm tốt công tác lãnh đạo, chỉ đạo của cấp ủy, tổ chức đảng, cán bộ các cấp trong công tác quản lý, sử dụng tài chính, đất quốc phòng, tài sản công.
- Tăng cường kiểm tra, giám sát, kiểm toán các hoạt động liên quan đến công tác tài chính, sử dụng đất quốc phòng, tài sản công.
- Triển khai việc kê khai tài sản cá nhân chặt chẽ, minh bạch trong việc kê khai những tài sản của tập thể được giao cho cá nhân quản lý.
- Vận dụng chặt chẽ các văn bản quy phạm pháp luật và chỉ đạo của cấp trên trong công tác phân bổ kinh phí, vật chất, quy hoạch đất quốc phòng, xây dựng cơ bản… nhằm hạn chế thấp nhất các sơ hở, không để cá nhân lợi dụng trục lợi trái pháp luật.
- Thường xuyên nắm chắc các mối quan hệ xã hội của quân nhân, nhất là quan hệ làm ăn kinh tế bên ngoài đơn vị.
- Gặp gỡ, giáo dục, định hướng tư tưởng, nhận thức và hành động đối với các quân nhân có biểu hiện vi phạm.
- Thường xuyên giáo dục các phẩm chất đạo đức cách mạng, nhất là đức tính cần, kiệm, liêm, chính, chí công vô tư cho các đối tượng trong đơn vị.
- Xử lý kiên quyết, nghiêm minh các trường hợp chấp hành quy định về quản lý, sử dụng tài chính, đất quốc phòng, tài sản công sai quy định.
- Phối hợp chặt chẽ với cấp ủy, chính quyền địa phương nơi đóng quân tiếp tục rà soát, kiểm tra, bổ sung, hoàn thiện hồ sơ pháp lý, ranh giới, mốc giới, diện tích trên thực địa của từng điểm đất quốc phòng được giao quản lý.
27. Vi phạm nguyên tắc tập trung dân chủ, quy chế lãnh đạo, quy chế làm việc
a) Dấu hiệu nhận biết
- Không thực hiện nghiêm nguyên tắc thiểu số phục tùng đa số, cấp dưới phục tùng cấp trên, cá nhân phục tùng tổ chức. Không chấp hành quyết nghị của tập thể (về việc quy hoạch, bổ nhiệm, đề bạt, luân chuyển...), thậm chí cùng nhau viết, ký tên vào đơn phản ánh, tố cáo, kiến nghị, gây mất đoàn kết nội bộ. 
- Trong sinh hoạt (cấp ủy, tổ chức đảng, cơ quan, đơn vị…) không phát biểu ý kiến hoặc có thảo luận, tranh luận, đóng góp ý kiến nhưng khi ra ngoài thì phát biểu khác, nói khác với ý kiến phát biểu của mình hoặc khác với quyết nghị của tập thể.
- Lợi dụng quyền bảo lưu ý kiến của mình để có bài viết, bài nói, phát ngôn hoặc cung cấp cho báo chí đăng tin, bài trái với quan điểm, đường lối, nghị quyết của Đảng, của cấp ủy, tổ chức đảng, làm mất uy tín của tổ chức đảng và của cán bộ, đảng viên.
- Lợi dụng cơ chế, chế độ tập thể để hợp pháp hóa quyết định, ý đồ cá nhân của mình bằng việc phát biểu ý kiến dưới dạng “định hướng trước” hoặc gợi ý để các thành viên trong cấp ủy thảo luận, phát biểu ý kiến một cách xuôi chiều, miễn cưỡng theo gợi ý, định hướng, dẫn đến không khách quan, chính xác.
- Không thực hiện nghiêm quy chế làm việc của tổ chức mình, lạm quyền trong quyết định những vấn đề về công tác cán bộ thuộc trách nhiệm của tập thể (quyết định tiếp nhận, quy hoạch, bổ nhiệm, đề bạt, cử đi học, đào tạo, nâng lương, luân chuyển cán bộ; tài chính, xây dựng cơ bản, đất đai...), nhất là trong những thời điểm nhạy cảm như sắp hết nhiệm kỳ công tác, nghỉ hưu, chuyển công tác khác...; dẫn đến vi phạm nghiêm trọng nguyên tắc tập trung dân chủ, tập thể lãnh đạo, cá nhân phụ trách.
	b) Biện pháp phòng ngừa:
- Quán triệt sâu sắc các nghị quyết, chỉ thị, quy định, kết luận của Trung ương, xây dựng, bổ sung hoàn thiện các quy định để phát huy nguyên tắc tập trung dân chủ trong tổ chức và sinh hoạt đảng ở cấp ủy, tổ chức đảng ở đơn vị cho phù hợp. Cụ thể hóa nguyên tắc tập trung dân chủ bằng những văn bản hướng dẫn cụ thể, để mọi tổ chức đảng và đảng viên thực hiện.
- Đẩy mạnh học tập và làm theo tư tưởng đạo đức, phong cách Hồ Chí Minh gắn với thực hiện có hiệu quả nghị quyết, chỉ thị, kết luận của Trung ương về xây dựng đảng; kết hợp chặt chẽ công tác kiểm tra, giám sát của các cấp ủy, tổ chức đảng với việc thanh tra, kiểm tra của cơ quan chức năng, kịp thời phát hiện, ngăn chặn và xử lý nghiêm các biểu hiện vi phạm nguyên tắc tập trung dân chủ.
- Nâng cao nhận thức, trách nhiệm của mỗi cấp ủy, cán bộ, đảng viên về thực hiện nguyên tắc tập trung dân chủ, bảo đảm mọi vấn đề liên quan đến công tác lãnh đạo của Đảng đều được dân chủ bàn bạc, công khai, quyết định theo đa số trên cơ sở phân định rõ thẩm quyền và trách nhiệm tập thể, cá nhân. 
- Đẩy mạnh tự phê bình và phê bình, phát huy trách nhiệm tự soi, tự sửa của mỗi cấp ủy, tổ chức đảng và mỗi cán bộ, đảng viên; tăng cường kiểm tra, giám sát việc thực hiện nguyên tắc tập trung dân chủ, kỷ luật, kỷ cương, sự đoàn kết, thống nhất nội bộ; tránh dân chủ hình thức, khắc phục cách làm việc tắc trách, trì trệ, hoặc lạm dụng quyền lực xâm phạm nguyên tắc.
- Thực hiện tốt Quy chế dân chủ ở cơ sở, phát huy vai trò giám sát, phản biện của các tổ chức và cá nhân đối với việc thực hiện nguyên tắc của Đảng. 
- Đề cao vai trò của người đứng đầu, cán bộ chủ chốt trong giữ vững và phòng, chống tình trạng xa rời nguyên tắc tập trung dân chủ, nhất là bí thư cấp ủy; nỗ lực học tập, rèn luyện phong cách, phương pháp làm việc dân chủ, khoa học, tạo bầu không khí dân chủ trong tổ chức.
- Cầu thị lắng nghe ý kiến phản ánh về việc thực hiện nguyên tắc tập trung dân chủ ở đơn vị và định kỳ lấy phiếu tín nhiệm của cán bộ các cấp, nhất là người đứng đầu, cán bộ chủ trì, chủ chốt. Phát huy vai trò của tổ chức quần chúng, hội đồng quân nhân và tập thể quân nhân trong việc phản ánh những biểu hiện vi phạm nguyên tắc tập trung dân chủ.
- Xây dựng tốt tinh thần đoàn kết trên cơ sở nguyên tắc, quy định, kỷ luật của Đảng, pháp luật Nhà nước, kỷ luật quân đội. Chống mọi biểu hiện lợi ích nhóm, cục bộ, bè phái.
28. Sử dụng mạng xã hội phát ngôn, phát tán, truyền tải, chia sẻ thông tin, hình ảnh sai quy định

a) Dấu hiệu nhận biết	
- Biểu hiện “nghiện” Internet, mạng xã hội, thích “sống ảo”, bị lệ thuộc vào điện thoại di động, máy tính bảng....
- Thường xuyên sử dụng điện thoại di động, máy tính truy cập và bình luận vào các tài khoản mạng xã hội phản động, bạo lực, khiêu dâm,…
- Thường xuyên chia sẻ những hoạt động, công tác của cơ quan, đơn vị lên mạng xã hội.
- Tính cách bốc đồng, nóng nảy, dễ bị kích động và phát ngôn thiếu kiểm soát.
- Có tư tưởng lạc hậu, phong kiến, gia trưởng, cổ súy cho các hủ tục, mê tín, dị đoan, dâm ô, đồi trụy, không phù hợp với thuần phong, mỹ tục của dân tộc.
- Có mối quan hệ xã hội phức tạp cả ở đời thực và trên mạng xã hội.
- Sử dụng nhiều số điện thoại, nhiều tài khoản mạng xã hội nhưng không báo cáo.
- Thường xuyên chụp ảnh, quay clip và chia sẻ hình ảnh, hoạt động của đơn vị lên mạng xã hội.
- Chủ quan, mất cảnh giác, thiếu ý thức trách nhiệm, tùy tiện trong phát ngôn hoặc đưa lên mạng những thông tin, hình ảnh sai trái, gây phản cảm; tự ý trao đổi, cung cấp thông tin, tài liệu không đúng đối tượng và phạm vi phổ biến.
- Có biểu hiện bất mãn, tiêu cực với thực tế cuộc sống, cấp trên, đồng chí đồng đội…
b) Biện pháp phòng ngừa:
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định có liên quan về sử dụng mạng xã hội, quy định về phát ngôn, bảo vệ chính trị nội bộ; nâng cao nhận thức, trách nhiệm của quân nhân trong tham gia sử dụng mạng xã hội an toàn.
- Nắm tâm tư, tình cảm, nhất là những vấn đề bức xúc của quân nhân trước các vấn đề được đăng tải trên mạng xã hội có liên quan đến tình hình đất nước, Quân đội, đơn vị; kịp thời phát hiện, ngăn chặn, bóc gỡ những thông tin không chính thống, chưa được kiểm chứng, phản ánh sai sự thật hoặc làm lộ lọt bí mật quân sự.
- Chú trọng làm tốt công tác bảo vệ chính trị nội bộ, quản lý chặt chẽ đội ngũ cán bộ, nhân viên, chiến sĩ làm công tác cơ yếu, văn thư, bảo mật và làm việc trong các cơ quan tổ chức, cán bộ, thanh tra, kiểm tra, tư pháp…
- Quản lý chặt chẽ quân nhân trong đơn vị, nhất là các trường hợp có mối quan hệ phức tạp, thường xuyên sử dụng mạng xã hội để kinh doanh, buôn bán online và đăng bài chia sẻ cuộc sống cá nhân… 
- Phối hợp chặt chẽ, thường xuyên với các cá nhân, tổ chức, cơ quan, đơn vị chuyên môn có liên quan, kịp thời phát hiện, xử lý các vi phạm về quy định sử dụng mạng xã hội, bảo vệ chính trị nội bộ.
- Đẩy mạnh ứng dụng thành tựu khoa học công nghệ để làm tốt công tác bảo mật đường truyền mạng, bảo mật cổng thông tin, trang thông tin điện tử; tăng cường các giải pháp bảo đảm an ninh, an toàn thông tin mạng tại cơ quan, đơn vị.
29. Làm lộ, lọt bí mật quân sự
a) Dấu hiệu nhận biết
- Thường xuyên chụp ảnh, quay clip và chia sẻ hình ảnh, hoạt động của đơn vị lên mạng xã hội.
- Mượn các loại tài liệu của đơn vị để photo không đúng quy định. Thường để ý, dò hỏi thông tin về hoạt động, công tác của cơ quan, đơn vị.
- Truy cập internet mà không có sự kiểm soát.
- Sử dụng usb không an toàn, không đúng cách.
- Theo dõi và truy cập những tài khoản mạng xã hội có nội dung phản động, chống phá Đảng và Nhà nước.
- Có mối quan hệ xã hội phức tạp cả ở đời thực và trên mạng xã hội; quan hệ, kết nối với các đối tượng bất mãn, cá nhân hoặc tổ chức phản động trong và ngoài nước.
- Có giao dịch tiền tệ “mờ ám” từ nguồn trong nước hoặc nước ngoài gửi tới mà không thể chứng minh được nguồn gốc.
- Sử dụng nhiều số điện thoại, nhiều tài khoản mạng xã hội nhưng không báo cáo.
- Chủ quan, mất cảnh giác, thiếu ý thức trách nhiệm, tùy tiện trong phát ngôn hoặc đưa lên mạng những thông tin, hình ảnh sai trái, gây phản cảm; tự ý trao đổi, cung cấp thông tin, tài liệu không đúng đối tượng và phạm vi phổ biến.
- Chấp hành kỷ luật không nghiêm, đi lại tự do, tùy tiện.
b) Biện pháp phòng ngừa
- Tăng cường quán triệt các nghị quyết, chỉ thị của Đảng, Nhà nước, các quy định, hướng dẫn của Quân đội, đơn vị về công tác bảo vệ bí mật Nhà nước, bí mật quân sự. Chú trọng làm tốt công tác tuyên truyền, giáo dục, nâng cao nhận thức, trách nhiệm cho cán bộ, nhân viên và chiến sĩ về công tác bảo vệ bí mật quân sự trước yêu cầu mới; ý thức chấp hành pháp luật Nhà nước, kỷ luật Quân đội, kỷ luật phát ngôn; không tự ý trả lời phỏng vấn của các phương tiện truyền thông khi chưa được phép của cơ quan chức năng.
- Tổ chức tập huấn, bồi dưỡng kiến thức, kinh nghiệm, kỹ năng phòng gian, giữ bí mật Nhà nước, bí mật quân sự cho mọi quân nhân trong đơn vị.
- Làm tốt công tác bảo vệ chính trị nội bộ, nắm và quản lý chặt chẽ tình hình tư tưởng, kỷ luật và các mối quan hệ của cán bộ, chiến sĩ thuộc quyền.
- Yêu cầu kê khai đầy đủ các số điện thoại và các tài khoản mạng xã hội mà quân nhân đang sử dụng. Không để cán bộ, nhân viên, chiến sĩ truy cập vào các trang mạng có nội dung phản động, sai trái; đưa các thông tin, hình ảnh có nội dung liên quan đến bí mật quân sự hoặc “nhạy cảm” trên các phương tiện truyền thông, mạng xã hội.
- Duy trì chấp hành pháp luật Nhà nước, kỷ luật Quân đội, bảo đảm an ninh, an toàn cho các hoạt động của đơn vị. Quản lý chặt chẽ công văn, tài liệu, vũ khí, khí tài, trang bị, tài sản của Quân đội, không để lộ, lọt, mất mát. Tăng cường công tác quản lý bí mật quân sự trên các phương tiện thông tin và truyền thông, nhất là quản lý việc sử dụng dịch vụ internet và các thiết bị công nghệ thông tin. 
- Thường xuyên kiểm tra, giám sát việc chấp hành chỉ thị, quy định về phòng gian, giữ bí mật của cán bộ, chiến sĩ, nhất là các biện pháp phòng ngừa, không để lộ, lọt thông tin, tài liệu mật. 
- Thực hiện chặt chẽ quy trình xác minh, xét duyệt, tuyển chọn người vào cơ quan, đơn vị, vị trí trọng yếu, cơ mật; trong tuyển quân, tuyển sinh quân sự, đi học tập, công tác nước ngoài. Thường xuyên rà soát, đảm bảo tiêu chuẩn chính trị đối với cán bộ, nhân viên, chiến sĩ làm việc tại cơ quan, đơn vị, vị trí trọng yếu, cơ mật.
- Thực hiện nghiêm quy định trong quan hệ, tiếp xúc với các tổ chức, cá nhân nước ngoài.
- Phát huy vai trò của chiến sĩ bảo vệ, Cơ quan Bảo vệ an ninh thường xuyên nắm chắc tình hình, chủ động tham mưu đề xuất giúp cấp ủy, chỉ huy các cấp lãnh đạo, chỉ đạo và phối hợp chặt chẽ với các lực lượng, cơ quan chức năng kịp thời phát hiện, phòng ngừa, đấu tranh ngăn chặn, vô hiệu hóa các hoạt động phá hoại, đánh cắp thông tin, bí mật quân sự của các thế lực thù địch, phản động, bảo đảm an ninh, an toàn cho các hoạt động của đơn vị.
- Chủ động phát hiện, ngăn chặn kịp thời nhận thức và hành động không đúng, biểu hiện mơ hồ, mất cảnh giác, thiếu ý thức trách nhiệm, vô tình hay cố ý để lộ, lọt thông tin bí mật quân sự.
- Khi phát hiện thông tin, hình ảnh liên quan đến bí mật quân sự trên mạng xã hội, cần nhanh chóng báo cáo cấp trên và phối hợp chặt chẽ với cơ quan chức năng để có biện pháp xử lý.
30. Tự ý ra nước ngoài
a) Dấu hiệu nhận biết
- Tính cách thích ăn chơi, hưởng thụ, có điều kiện về kinh tế.
- Có người thân, bạn bè đang sinh sống và làm việc tại nước ngoài.
- Có mối quan hệ xã hội phức tạp cả ở đời thực và trên mạng xã hội, nhất là quan hệ với người nước ngoài và các trang mạng ngoài nước.
- Sử dụng nhiều số điện thoại, nhiều tài khoản mạng xã hội một cách bất thường nhưng không báo cáo.
- Tự ý làm một số giấy tờ: visa…
- Học thêm một số ngoại ngữ hoặc các ngôn ngữ nước ngoài một cách bất thường không phục vụ cho học tập, công tác và dạy dỗ con cái.
- Bán các loại tài sản có giá trị lớn như: bất động sản, cổ phiếu, vàng, xe ô tô…
- Thường xuyên tìm hiểu, bàn tán về địa lý, văn hóa,… của một hay một vài nước khác.
- Mua sắm quần áo, đồ dùng cần thiết để chuẩn bị cho một chuyến đi xa.
- Có những mối quan hệ với các đối tượng làm giả giấy tờ tùy thân, hộ chiếu; các đối tượng trong tổ chức phản động ở ngoài nước.
- Nghỉ phép, tranh thủ hoặc đi chữa bệnh dài ngày, vắng mặt tại cơ quan, đơn vị và không rõ lý do.
b) Biện pháp phòng ngừa
- Tăng cường làm tốt công tác giáo dục, quán triệt, thực hiện quy định trách nhiệm nêu gương và các quy định những điều đảng viên không được làm; xây dựng cho quân nhân có ý thức chấp hành pháp luật Nhà nước, điều lệnh, điều lệ, quy định của Quân đội, đơn vị.
- Thường xuyên giáo dục chính trị tư tưởng cho cán bộ, chiến sĩ phát huy truyền thống tốt đẹp của Quân đội, đơn vị, gia đình; nêu cao trách nhiệm xây dựng đơn vị.
- Thực hiện chặt chẽ công tác bảo vệ chính trị nội bộ, quản lý, nắm chắc tình hình tư tưởng, các mối quan hệ và ý thức chấp hành kỷ luật của quân nhân; chú trọng các mối quan hệ với các tổ chức, cá nhân người nước ngoài. Duy trì chấp hành nghiêm quy định trong quan hệ, tiếp xúc với các tổ chức, cá nhân nước ngoài.
- Tăng cường các biện pháp quản lý quân nhân thuộc quyền; gần gũi, sâu sát, nắm bắt tâm tư, tình cảm, sức khỏe, hoàn cảnh gia đình của quân nhân trong đơn vị, nhất là trường hợp có hoàn cảnh khó khăn, mắc bệnh hiểm nghèo... kịp thời quan tâm, động viên. Có biện pháp quản lý quân nhân trong nghỉ phép, nghỉ chữa bệnh dài ngày.
- Yêu cầu kê khai đầy đủ các số điện thoại và các tài khoản mạng xã hội mà quân nhân đang sử dụng.


Phần thứ hai
GỢI Ý BIỆN PHÁP XỬ LÝ CỦA CÁN BỘ CƠ SỞ ĐỐI VỚI NHỮNG TÌNH HUỐNG TƯ TƯỞNG CÓ THỂ NẢY SINH

	* NGUYÊN TẮC, QUY TRÌNH XỬ LÝ CƠ BẢN 
Tình huống tư tưởng có thể nảy sinh ở đơn vị cơ sở rất đa dạng, phức tạp với nhiều lý do khác nhau, đòi hỏi phải có các phương pháp xử lý phù hợp; quá trình xử lý thường theo một quy trình chung đó là:
Bước 1: Chuẩn bị xử lý
- Hội ý cấp uỷ, chỉ huy đơn vị, nhận định, đánh giá tính chất, tác hại, nguyên nhân, mức độ ảnh hưởng để trao đổi, thống nhất trong chỉ huy và báo cáo cấp trên xin ý kiến chỉ đạo;
- Lựa chọn chủ thể xử lý phù hợp với đối tượng xử lý (chính trị viên, chính trị viên phó, đại đội trưởng, đại đội phó, trung đội trưởng, tiểu (khẩu) đội trưởng, chiến sĩ bảo vệ, cũng có thể là người bạn thân hoặc gia đình…)
- Nhanh chóng thu thập, phân tích, kết luận thông tin bảo đảm chính xác;
- Xác định kế hoạch, nội dung xử lý, dự kiến tình huống, sử dụng các lực lượng tham gia xử lý (Hội đồng quân nhân, tổ tư vấn tâm lý, pháp lý, gia đình, địa phương …)
- Chuẩn bị môi trường, cơ sở vật chất cho việc xử lý.
Bước 2: Quá trình xử lý
- Gặp gỡ, tiếp xúc với đối tượng;
- Sử dụng các phương pháp xử lý cho phù hợp (phân tích thuyết phục; truyền đạt thông tin; hướng dẫn tư duy; ám thị gián tiếp; động viên, phê phán; tác động tình cảm; gợi nhớ);
- Quan sát, ghi nhận các biểu hiện, phản ứng của đối tượng;
- Nhận xét, đánh giá kết quả tác động;
- Điều chỉnh kế hoạch tác động cho phù hợp với thái độ, sự phản ứng của đối tượng.
Bước 3: Kết thúc xử lý: Tạm thời hay toàn bộ. Nếu đối tượng tác động có chuyển biến tư tưởng tốt, tích cực, hợp tác, quyết tâm khắc phục những biểu hiện tâm lý tư tưởng lệch lạc thì xem như kết thúc toàn bộ, còn kết thúc tạm thời là khi đối tượng có chuyển biến chậm phải tiếp tục thực hiện kế hoạch xử lý.
- Ổn định tình hình đơn vị;
- Tiếp tục theo dõi, tác động ổn định tư tưởng, củng cố lòng tin cho đối tượng;
- Đánh giá kết quả, rút ra bài học kinh nghiệm.
- Tổng hợp tình hình, báo cáo cấp trên, xin ý kiến chỉ đạo tiếp theo.

I. GỢI Ý BIỆN PHÁP XỬ LÝ NHÓM TÌNH HUỐNG TƯ TƯỞNG CÓ THỂ NẢY SINH TRONG THỰC HIỆN NHIỆM VỤ PHÒNG, CHỐNG THIÊN TAI, DỊCH BỆNH (50 tình huống).
	A. TÌNH HUỐNG TƯ TƯỞNG CÓ THỂ NẢY SINH TRONG THỰC HIỆN NHIỆM VỤ PHÒNG, CHỐNG DỊCH BỆNH
	Tình huống 01. Một chiến sĩ trong đơn vị có biểu hiện buồn chán khi bố (mẹ) ốm điều trị dài ngày ở bệnh viện (do bị nhiễm loại vi rút mới), nhưng đơn vị không giải quyết phép, vì đang trong giai đoạn dịch lây lan mạnh ngoài cộng đồng.
	Gợi ý biện pháp xử lý:
	- Hội ý chỉ huy đơn vị, đánh giá tình hình, thống nhất biện pháp xử lý.
	- Chỉ huy đơn vị triển khai quán triệt các văn bản của các cấp về các biện pháp phòng, chống đại dịch; gặp gỡ quân nhân có bố (mẹ) điều trị ở bệnh viện, chia sẻ, đồng cảm về điều kiện hoàn cảnh của gia đình; đồng thời nắm thêm về tình hình gia đình và tâm tư, nguyện vọng; động viên các quân nhân hiểu rõ yêu cầu cấp bách của nhiệm vụ phòng, chống đại dịch.
	- Báo cáo, đề xuất và xin ý kiến chỉ đạo của cấp trên: Nếu trường hợp bệnh viện ở gần nơi đơn vị đóng quân thì đề nghị cử cán bộ ra thăm hỏi, động viên gia đình. Nếu bệnh viện ở xa thì gọi điện cho người thân trong gia đình để hỏi thăm và nắm thêm tình hình.
	- Căn cứ vào tình trạng, mức độ bệnh tật của bố (mẹ) quân nhân để sinh hoạt thông báo với cán bộ, chiến sĩ trong đơn vị được biết để động viên, chia sẻ hoặc có thể quên góp ủng hộ về vật chất... giúp đỡ quân nhân yên tâm tư tưởng, xác định trách nhiệm và hoàn thành tốt nhiệm vụ.
- Phân công cán bộ, chiễn sĩ theo dõi, động viên, giúp đỡ quân nhân có bố (mẹ) đang nằm viện trong học tập, công tác, sinh hoạt, cùng gia đình khắc phục khó khăn, hoàn thành tốt nhiệm vụ nhiệm vụ được giao.
- Kết thúc thời gian giãn cách xã hội theo Chỉ thị 16, căn cứ tình hình nhiệm vụ của đơn vị đề nghị cấp trên giải quyết phép đặc biệt, hoặc phép về thăm gia đình cho quân nhân có bố (mẹ) ốm nằm viện.
Tình huống 02. Chỉ huy đơn vị nhận được thông tin, do căng thẳng, lo sợ trong thực hiện nhiệm vụ giúp nhân dân trong phòng, chống đại dịch tại tâm dịch tỉnh X, một số chiến sĩ có ý định đào ngũ.
Gợi ý biện pháp xử lý
- Hội ý chỉ huy đơn vị, đánh giá tình hình, thống nhất biện pháp xử lý.
- Tổ chức sinh hoạt đơn vị quán triệt, giáo dục cho cán bộ, chiến sĩ nhận thức sâu sắc về mục đích, ý nghĩa và yêu cầu của nhiệm vụ phòng, chống đại dịch; đây là vừa chức năng cơ bản (đội quân công tác), vừa là nhiệm vụ chiến đấu của quân đội trong thời bình; trên cơ sở đó xây dựng ý chí, quyết tâm và trách nhiệm trong thực hiện nhiệm vụ.
- Đánh giá, phân loại tư tưởng; phân công cán bộ gặp gỡ, động viên, giúp đỡ chiến sĩ có biểu hiện lo lắng, giao động tư tưởng; tập trung quản lý chặt chẽ quân số, tư tưởng, các mối quan hệ, chất lượng công tác của quân nhân.
- Đẩy mạnh đợt thi đua đặc biệt trong phòng, chống dịch, tập trung nâng cao nhận thức, trách nhiệm; chấp hành nghiêm pháp luật, kỷ luật; phát huy tốt vai trò tiền phong, gương mẫu của cán bộ đảng viên...; kịp thời biểu dương, nhân rộng những gương tập thể, cá nhân tiêu biểu trong thực hiện nhiệm vụ.
- Thường xuyên làm tốt công tác dự báo tình hình, nắm chắc tình hình tư tưởng để quản lý, không để bị động, bất ngờ. Phân công cán bộ thường xuyên gần gũi với chiến sĩ, tâm sự nắm chắc tâm tư tình cảm và chia sẻ những khó khăn vất vả với bộ đội, nhất là các quân nhân không yên tâm công tác.
- Kịp thời rút kinh nghiệm; tăng cường công tác quản lý, kiểm tra quân số (trong giờ nghỉ, ngày nghỉ, thời điểm nhạy cảm); phát huy hiệu quả hoạt động của các tổ chức, lực lượng, “tổ tư vấn tâm lý, pháp lý”, chiến sĩ dân vận, chiến sĩ bảo vệ; tổ chức  các hoạt động văn hóa tinh thần trong giờ nghỉ, ngày nghỉ thiết thực, hiệu quả. Quan tâm bảo đảm tốt đời sống vật chất, tinh thần cho bộ đội. 
Tình huống 03. Thời gian gần đây trong đơn vị xuất hiện nhiều thông tin sai sự thật về công tác phòng, chống đại dịch của Đảng, Nhà nước, Quân đội... gây hoang mang, lo lắng cho cán bộ, chiến sĩ.
Gợi ý biện pháp xử lý
- Hội ý chỉ huy đơn vị, đánh giá tình hình, thống nhất biện pháp xử lý.
- Tổ chức sinh hoạt đơn vị quán triệt, thông tin, tuyên truyền, giáo dục cán bộ, chiến sĩ nhận thức sâu sắc về quan điểm, chủ trương, chính sách của Đảng và Nhà nước ta về công tác phòng, chống dịch; trên cơ sở đó, định hướng nhận thức tư tưởng, xây dựng niềm tin, thái độ, trách nhiệm của mỗi quân nhân trước những tác động tiêu cực nảy sinh...
- Thường xuyên quán triệt sâu, kỹ về nhiệm vụ của quân đội và đơn vị; âm mưu “DBHB”, “phi chính trị hóa” Quân đội của các thế lực thù địch; kiên quyết đấu tranh phản bác những luận điệu phản ánh sai trái, bảo vệ nền tàng tư tưởng của Đảng; giữ vững niềm tin cho mọi cán bộ, chiến sĩ, yên tâm hoàn thành tốt mọi nhiệm vụ được giao. 
- Tăng cường tuyên truyền, giáo dục Lời kêu gọi của Đảng, Nhà nước, Chính phủ đối với công tác phòng, chống đại dịch; phát huy hiệu quả hoạt động tuyên truyền thông qua hệ thống thiết chế văn hóa, truyền thanh nội bộ, chế độ đọc báo, thông báo chính trị - thời sự, xem truyền hình. 
- Phối hợp chặt chẽ cấp ủy, chính quyền và các tổ chức đoàn thể địa phương trong công tác tuyên truyền, giáo dục; xây dựng đơn vị an toàn gắn với địa bàn an toàn.
- Kịp thời rút kinh nghiệm ở các cấp, thường xuyên giáo dục, tuyên truyền  nâng cao nhận thức, trách nhiệm cho bộ đội; coi trọng xây dựng ý chí quyết tâm, tinh thần khắc phục khó khăn, ý thức chấp hành pháp luật, kỷ luật; quan tâm  đảm bảo đời sống cho cán bộ, chiến sĩ; phát huy vai trò tiền phong của cán bộ, đảng viên trong thực hiện chức trách nhiệm vụ.
- Thường xuyên sâu sát, gần gũi bộ đội, kịp thời nắm bắt tâm tư, tình cảm, chia sẻ, tháo gỡ những vướng mắc, khó khăn của cán bộ, chiến sĩ. Thực hiện tốt công tác nắm, quản lý, dự báo, định hướng và giải quyết tình hình tư tưởng.
 Tình huống 04: Trong thời gian thực hiện Chỉ thị của Thủ tướng Chính phủ, do thời gian trực kéo dài, có quân nhân nảy sinh tư tưởng ngại khó khăn, xin nghỉ phép, nghỉ tranh thủ, lý do việc gia đình…
Gợi ý biện pháp xử lý:
- Tập trung phổ biến, quán triệt, tổ chức thực hiện nghiêm các văn bản của trên và đơn vị về công tác phòng, chống đại dịch.
- Tiến hành đồng bộ các tổ chức tuyên truyền, giáo dục về chức năng, nhiệm vụ của Quân đội.
-Tổ chức gặp gỡ trao đổi, động viên kịp thời, giải thích về những quy định phòng, chống đại dịch trong tình hình hiện nay.
- Thường xuyên nắm bắt tình hình tư tưởng, dư luận xã hội, mối quan hệ gia đình, địa phương, đồng chí, đồng đội của từng quân nhân; kết hợp nhiều biện pháp để giáo dục phù hợp với từng đối tượng, gần gũi nắm bắt tâm tư tình cảm.
- Tổ chức các hoạt động VHVN, TDTT tạo không khí vui tươi, lành mạnh trong đơn vị.
- Thường xuyên phối hợp với cấp ủy, chính quyền địa phương kịp thời nắm sự chỉ đạo của các cấp, sẵn sàng thực hiện các nhiệm vụ được giao trong phòng, chống dịch.
Tình huống 05: Đơn vị chuẩn bị nhận nhiệm vụ tăng cường cho tuyến đầu chống dịch, khu vực có nguy cơ lây nhiễm, tỷ lệ tử vong cao; có chiến sĩ lấy lý do sức khoẻ yếu, xin đi điều trị tại bệnh xá để không phải tham gia đợt công tác đặc biệt sắp tới, đã tác động xấu đến nhận thức nhiệm vụ của một số đồng chí khác.
Gợi ý biện pháp xử lý:
- Trao đổi thống nhất trong lãnh đạo, chỉ huy đơn vị về biện pháp xử lý; phân công cán bộ phụ trách, quan tâm, sâu sát động viên chăm sóc các đồng chí đó.
- Chỉ đạo quân y đơn vị phối hợp với quân y cấp trên kiểm tra sức khoẻ của chiến sĩ. Nếu ốm thật, đề nghị đánh giá đúng mức độ bệnh tình, chăm sóc điều trị chu đáo. Nếu không phải bị ốm mà là vì lý do ngại khó, ngại khổ, sợ lây dịch bệnh, có thể phải hy sinh trong khi thi hành nhiệm vụ thì phải xác định đây là trường hợp có biểu hiện bất thường về tư tưởng; trên cơ sở nhận định, đánh giá đúng tính chất sự việc như vậy để đưa ra biện pháp xử lý phù hợp.
- Trực tiếp gặp gỡ tìm hiểu rõ nguyên nhân; phương pháp phải khéo léo, mềm dẻo thông qua tâm sự, trò chuyện để nắm bắt tâm tư, tình cảm, vướng mắc của chiến sĩ.
- Giáo dục, động viên nâng cao nhận thức của chiến sĩ về trách nhiệm, nghĩa vụ của “Bộ đội Cụ Hồ” đối với Tổ quốc, với nhân dân; phân tích, quán triệt để chiến sĩ đó thấy được về tinh thần tương thân, tương ái, trong phóng, chống dịch, những tấm gương hy sinh quên mình nơi tuyến đầu chống dịch của đồng chí, đồng đội, các y bác sĩ và có cả những người dân thường... từ đó để nâng cao nhận thức, củng cố quyết tâm cho người chiến sĩ tự giác, tích cực tham gia thực hiện nhiệm vụ (nếu chiến sĩ đó vẫn không chuyển biến phải báo cáo với cấp trên để có biện pháp giáo dục, động viên xử lý phù hợp).
- Phát huy vai trò của các tổ chức, nhất là tổ 3 người, tiểu đội, trung đội, đoàn thanh niên, hội đồng quân nhân và các mối quan hệ bạn bè thân thiết, đồng hương, người thân, gia đình để giáo dục, động viên chiến sĩ có nhận thức tốt về nhiệm vụ, sẵn sàng tham gia thực hiện nhiệm vụ tăng cường cho tuyến đầu chống dịch. Tổ chức cho đơn vị xem, nghe các chương trình truyền hình, phát thanh đưa tin về những tấm lòng cao cả, tấm gương hy sinh quên mình trong phòng chống dịch.
- Hướng dẫn chỉ đạo tiểu đội, trung đội sinh hoạt rút kinh nghiệm về công tác quản lý tư tưởng bộ đội; xây dựng động cơ, trách nhiệm, bản lĩnh trong mọi tình huống và nhiệm vụ được giao.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 06: Trường hợp nhân viên nữ làm nhiệm vụ cấp dưỡng (nấu ăn) do thực hiện giãn cách lâu ngày không được về gia đình, đã nảy sinh tư tưởng buồn chán, trách nhiệm phục vụ không tốt trong quá trình phòng, chống dịch của đơn vị.
Gợi ý biện pháp xử lý:
- Nắm bắt tình hình diễn biến, gặp gỡ trao đổi, động viên quân nhân khắc phục tốt mọi khó khăn; tiếp tục quán triệt sâu rộng trong toàn đơn vị các văn bản của trên và đơn vị về nhiệm vụ phòng, chống dịch (đặc biệt là tầm quan trọng của việc thực hiện giãn cách xã hội).
- Các tổ chức trong đơn vị (nhất là Hội phụ nữ) kịp thời nắm bắt tâm tư, tình cảm, những khó khăn gia đình của quân nhân khi trực tại đơn vị; cùng bàn bạc, tìm biện pháp khắc phục để quân nhân yên tâm hoàn thành tốt nhiệm vụ.
- Căn cứ vào cấp độ dịch để có biện pháp nâng cao đời sống vật chất tinh thần cho cán bộ, chiến sĩ theo khả năng của đơn vị.
- Kết hợp đồng bộ công tác tuyên truyền gương người tốt, việc tốt trong phòng chống dịch.
Tình huống 07: Theo yêu cầu nhiệm vụ của trên giao đơn vị có nhiệm vụ tăng cường bảo đảm về quân số cơ động đến các địa phương có dịch để hỗ trợ trong công tác phòng chống đại dịch, thì có một số cán bộ, chiến sỹ còn băn khoăn, lo lắng không yên tâm công tác, vì phải xa nhà, xa đơn vị, thực hiện nhiệm vụ trong điều kiện khó khăn vất vả.
Gợi ý biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy đơn vị, đánh giá tình hình tư tưởng trong đơn vị, xác định các chủ trương, biện pháp khắc phục.
- Căn cứ nhiệm vụ cấp trên giao, giao cho đơn vị trực tiếp lựa chọn lực lượng nòng cốt thực hiện nhiệm vụ trước, để thực hiện công tác giáo dục, lan tỏa tư tưởng tốt trong cơ quan, đơn vị.
- Phân công các đồng chí trong cấp uỷ gặp gỡ số cán bộ, chiến sĩ không an tâm tư tưởng, giáo dục động viên làm rõ nghĩa vụ, trách nhiệm của quân nhân trong tham gia phòng chống đại dịch; giáo dục chức năng, nhiệm vụ của Quân đội; xác định đây là thời điểm nhân dân cần quân đội và các lực lượng liên quan giúp đỡ. 
- Tổ chức sinh hoạt đơn vị giáo dục, quán triệt định hướng tư tưởng cho bộ đội; giáo dục mức độ, thời gian ảnh hưởng của dịch bệnh; đơn vị tiếp tục thực hiện các nhiệm vụ khó khăn, phức tạp hơn; định hướng tư tưởng cho bộ đội an tâm, sẵn sàng nhận và thực hiện mọi nhiệm vụ được giao.
- Tổ chức diễn đàn, tọa đàm về phòng, chống dịch Covid-19, những tấm gương sáng trong thực hiện nhiệm vụ; phát động thi đua sẵn sàng nhận và hoàn thành mọi nhiệm vụ được giao, tổ chức đăng ký tự nguyện tham gia giúp đỡ nhân dân trong phòng chống đại dịch tại các địa phương
- Phân công cán bộ theo dõi, kèm cặp, giúp đỡ từng người, từng tổ; sử dụng các chiến sĩ bảo vệ của đơn vị nắm tình hình, chủ động dự kiến các vấn đề nảy sinh như đào ngũ, vắng mặt trái phép để có các biện pháp ngăn chặn và xử lý kịp thời.
Tình huống 08: Trong quá trình thực hiện nhiệm vụ giúp đỡ nhân dân phòng, chống đại dịch có chiến sỹ bị nhiễm bệnh tử vong, một số chiến sĩ có biểu hiện băn khoăn, lo lắng, dẫn đến kết quả hoàn thành nhiệm vụ thấp.
Gợi ý biện pháp xử lý:
- Người chỉ huy ra lệnh tạm dừng nhiệm vụ, phối hợp với các lực lượng, nhất là lực lượng quân y, có biện pháp khử khuẩn, bảo đảm an toàn; tổ chức bảo vệ hiện trường; sơ bộ nắm tình hình và báo cáo chỉ huy cấp trên.
- Họp cấp ủy, chỉ huy đơn vị đánh giá tình hình, xác định nguyên nhân ban đầu và biện pháp xử lý. Thực hiện các biện pháp phòng, chống dịch ở mức cao nhất.
- Xin ý kiến chỉ đạo của cấp trên; thông báo ngay cho gia đình thân nhân chiến sĩ tử vong.
- Phối hợp chặt chẽ với cấp ủy, chính quyền địa phương, cơ quan các cấp xác định nguyên nhân; thống nhất biện pháp giải quyết theo quy định.
- Cán bộ các cấp thường xuyên bám sát mọi hoạt động, động viên, nhắc nhở bộ đội ổn định tư tưởng, tâm lý; quán triệt thực hiện đúng công tác bảo đảm an toàn, giảm thiểu tối đa những hy sinh, mất mát tiếp theo.
- Tiến hành giải quyết hậu quả theo quy định, đúng chức năng, nhiệm vụ, quyền hạn và điều kiện thực tế của đơn vị.
- Động viên cán bộ, chiến sĩ đơn vị chia sẻ, giúp đỡ vật chất, tinh thần với gia đình quân nhân tử vong; phối hợp với gia đình tổ chức mai táng chu đáo.
- Kịp thời thông báo kết luận điều tra của cấp trên; kiểm điểm làm rõ trách nhiệm, rút ra bài học kinh nghiệm trong công tác lãnh đạo, chỉ đạo và tổ chức thực hiện; thực hiện tốt các chế độ, chính sách cho quân nhân.
Tình huống 09: Khi thực hiện nhiệm vụ tăng cường phòng, chống dịch, có một đồng chí sĩ quan không may nhiễm bệnh và tử vong đã gây ảnh hưởng lớn đến tâm lý, tư tưởng và kết quả thực hiện nhiệm vụ của cán bộ, chiến sĩ.
Gợi ý biện pháp xử lý:
- Nhanh chóng báo cáo cấp trên, đề nghị Quân y xử lý bước đầu đối với quân nhân nhiễm bệnh tử vong.
- Cùng với Quân y đưa thi thể quân nhân tử vong về nơi quy định để tiến hành lấy mẫu xét nghiệm vệ sinh dịch tễ để xác định chính xác nguyên nhân tử vong.
- Thực hiện các biện pháp khử khuẩn khu vực có quân nhân nhiễm bệnh và tử vong để không làm lây lan dịch bệnh ở nơi đơn vị đóng quân.
- Thông báo cho gia đình quân nhân tử vong biết về nguyên nhân ban đầu dẫn tới cái chết; động viên tư tưởng, phối hợp cùng gia đình chuẩn bị hậu sự cho quân nhân.
- Tiếp tục tổ sinh hoạt quán triệt chấp hành nghiêm quy định phòng, chống dịch bệnh của Bộ Y tế trong quá trình tăng cường phòng, chống dịch, đặc biệt là các biện pháp bảo đảm an toàn cho cá nhân; đồng thời giáo dục định hướng, ổn định tình hình tư tưởng, dư luận cho cán bộ, chiến sĩ, xây dựng quyết tâm hoàn thành tốt nhiệm vụ.
- Có thể cử một số cán bộ, chiến sĩ cùng với gia đình lo hậu sự cho quân nhân tử vong trong điều kiện phòng, chống dịch và phù hợp với nguyện vọng của gia đình, phong tục, tập quán của địa phương.
- Vận động cán bộ, chiến sĩ tham gia ủng hộ đối với gia đình quân nhân tử vong với tinh thần tương thân, tương ái.
- Phối hợp với cơ quan chức năng thực hiện tốt chế độ chính sách đối với quân nhân từ trần khi đang thực hiện nhiệm vụ.
- Tổng hợp kết quả giải quyết vụ việc, báo cáo cấp trên theo đúng quy định.
Tình huống 10: Trong thời điểm nhân dân cả nước đang tập trung phòng, chống dịch thì các thế lực thù địch lợi dụng mạng xã hội đăng tải, tuyên truyền sai sự thật về tình hình diễn biến của dịch trong đó có thông tin liên quan trực tiếp đến cán bộ, chiến sỹ trong đơn vị.
Gợi ý biện pháp xử lý:
- Chỉ đạo Lực lượng 47, các cơ quan, đơn vị liên quan nhanh chóng phối hợp với các đơn vị bạn, lực lượng địa phương, các cơ quan báo chí, truyền thông chính thống đăng tải nội dung tuyên truyền, định hướng dư luận
- Tổ chức lực lượng xây dựng nội dung tuyên truyền trên không gian mạng, đấu tranh phản bác, triệt phá, bóc gỡ các tin giả thông tin sai sự thật, xấu độc lợi dụng vụ việc để chống phá.
- Tổng hợp nhanh tình hình, thu thập tài liệu, kết quả xử lý sơ bộ báo cáo cấp trên.
Tình huống 11: Một cán bộ (trung đội trưởng) sử dụng điện thoại thông minh đăng tải không đúng tình hình phòng, chống đại dịch trong đơn vị và địa bàn đóng quân lên mạng xã hội, làm cho gia đình và bạn bè quân nhân khi truy cập, gây hoang mang, lo lắng.
* Gợi ý biện pháp xử lý
- Kiểm tra, nắm chắc tình hình vụ việc.
- Hội ý chỉ huy đơn vị đánh giá tình hình, nguyên nhân, hậu quả, thống nhất biện pháp giải quyết trong cấp ủy, chỉ huy.
- Gặp gỡ cán bộ đăng tin bài, phân tích rõ sự việc; chỉ đạo quân nhân cùng các cơ quan chức năng có liên quan tìm mọi biện pháp nhanh chóng gỡ bỏ thông tin sai trái trên mạng xã hội, thông tin định hướng tư tưởng cho gia đình. Tùy theo mức độ, hậu quả của vi phạm, triển khai cho cán bộ viết bản tường trình, bản kiểm điểm. 
- Tổ chức sinh hoạt rút kinh nghiệm trong cán bộ; xây dựng nhận thức đúng đắn quy định sử dụng mạng xã hội của đơn vị, kỷ luật quân đội; hiểu rõ tác hại, hậu quả của đăng tải thông tin sai trái, ảnh hưởng tư tưởng đồng chí, đồng đội, gây hoang mang trong đơn vị và gia đình.
- Thường xuyên giáo dục, quán triệt, nâng cao ý thức của quân nhân trong đơn vị đối với việc chấp hành pháp luật, kỷ luật quân đội và quy định của đơn vị trong bảo đảm an toàn thông tin, an ninh mạng. 
- Làm tốt công tác bảo vệ chính trị nội bộ; phát huy vai trò của BCĐ 35, lực lượng 47 trong đơn vị, không để xảy ra trường hợp cán bộ, QNCN sử dụng điện thoại đăng tải hình ảnh tin, bài sai trái làm ảnh hưởng đến an ninh, an toàn đơn vị, hình ảnh “Bộ đội Cụ Hồ”.
- Tổng hợp tình hình báo cáo cấp trên; tăng cường công tác thông tin định hướng tư tưởng dư luận và gia đình.
Tình huống 12: Một số sĩ quan, QNCN theo dõi trên mạng xã hội, nắm được thông tin Chính phủ cấp giấy chứng nhận sử dụng nhiều loại vắc xin, nảy sinh tư tưởng muốn lựa chọn vắc xin do nước ngoài sản xuất
* Biện pháp xử lý:
- Trao đổi thống nhất trong lãnh đạo, chỉ huy đơn vị về biện pháp xử lý.
- Nhanh chóng sinh hoạt quán triệt, giáo dục, tuyên truyền, nâng cao nhận thức của bộ đội về chủ trương của Đảng, Nhà nước, Chính phủ trong thực hiện Chiến lược tiêm vắc xin để thực hiện miễn dịch cộng đồng.
- Giáo dục cho bộ đội hiểu sâu sắc về chỉ đạo của Thủ tướng Chính phủ: “Phải tiếp cận bình đẳng tất cả các loại vắc xin, vắc xin tốt nhất là vắc xin được tiêm sớm nhất”; phản bác thông tin sai lệch trên mạng xã hội về vấn đề lựa chọn vắc xin.
- Tổng hợp các tập thể, đơn vị trong toàn quân, các địa bàn trên cả nước đã tiêm vắc xin trong nước hoặc các loại vắc xin thông qua con đường ngoại giao của nhà nước, viện trợ của quốc tế và các tổ chức vẫn đảm bảo an toàn, hiệu quả, tạo niềm tin cho bộ đội.
- Tổ chức rút kinh nghiệm nghiêm túc trong lãnh đạo, chỉ huy, đội ngũ cán bộ lãnh đạo, chỉ huy các cấp trong đơn vị và đối với toàn thể đơn vị về nhận thức và ý thức đối với chủ trương chung của Đảng, Nhà nước, Chính phủ.
Tình huống 13: Trong đơn vị có tin đồn sai sự thật về việc tiêm vắc xin ngừa Covid-19 sẽ ảnh hưởng đến sức khỏe sinh sản, thậm chí vô sinh đã gây hoang mang tư tưởng cho bộ đội.
Gợi ý biện pháp xử lý:
- Nắm tình hình, thông tin liên quan đến tin đồn sai sự thật trên.
- Hội ý cấp ủy, chỉ huy đơn vị nhận định tình hình, xác định nguồn gốc, mức độ ảnh hưởng của tin đồn và biện pháp giải quyết; báo cáo xin ý kiến chỉ đạo của cấp trên.
- Tìm hiểu xác định nguyên nhân của tin đồn sai sự thật (do quân nhân đơn vị nhận thức sai hay phần tử xấu ở bên ngoài bịa đặt) để ngăn chặn và có biện pháp xử lý kịp thời, không để lan rộng, kéo dài.
- Phân loại, nắm chắc và tiến hành tốt công tác tư tưởng đối với những đồng chí có biểu hiện hoang mang dao động.
- Tổ chức sinh hoạt đơn vị thông báo cho cán bộ, chiến sỹ biết về nguồn tin sai sự thật trên và nguồn tin chính thống về tác dụng của việc tiêm vắc xin ngừa Covid-19. Trên cơ sở đó định hướng tư tưởng, chỉ rõ sự cần thiết phải tiêm vắc xin ngừa Covid-19 cho bộ đội.
- Tăng cường công tác tuyên truyền, giáo dục nâng cao nhận thức cho bộ đội về mọi mặt; phát huy vai trò, trách nhiệm của chiến sĩ bảo vệ, Tổ ba người trong nắm tình hình chính trị nội bộ, chia sẻ, động viên lẫn nhau; kiên quyết phản bác những luận điệu sai trái, thù địch. 
 - Duy trì quản lý tốt tình hình chính trị nội bộ, giáo dục cho bộ đội nâng cao ý thức cảnh giác; chủ động phát hiện, ngăn chặn không để những thông tin xấu độc, những tư tưởng lệnh lạc xâm nhập vào trong đơn vị, giữ vững niềm tin cho bộ đội.
Tình huống 14: Một số chiến sĩ của đơn vị, khi huấn luyện gần khu cách ly có tâm lý lo sợ bị lây nhiễm, mất an toàn, không tích cực trong quá trình tham gia huấn luyện.
Gợi ý biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy đơn vị, thống nhất các biện pháp giải quyết (trong hội ý cán bộ đơn vị phản ánh, báo cáo tình hình tư tưởng, tâm trạng của số hạ sĩ quan, chiến sĩ có biểu hiện băn khoăn, lo lắng).
- Chỉ đạo sinh hoạt các tổ chức; tuyên truyền các tài liệu của cấp trên cho cán bộ, chiến sĩ nâng cao hiểu biết về loại vi rút và các biến thể của vi rút.
- Chỉ đạo lực lượng quân y đơn vị giải thích về khả năng lây nhiễm của vi rút trong từng điều kiện môi trường, khoảng cách để bộ đội yên tâm tham gia huấn luyện.
- Tiến hành tốt các biện pháp về công tác bảo đảm an toàn trong phòng, chống đại dịch.
- Phân công cán bộ theo dõi, động viên, ổn định tư tưởng, tâm lý cho  chiến sĩ trong quá trình huấn luyện.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 15: Chiến sĩ huấn luyện tại khu vực gần nơi cách ly có biểu hiện nóng, sốt và ngất xỉu gây hoang mang trong đơn vị; vì trước đó có tiếp xúc với người bị nhiễm bệnh (không có triệu trứng).
Gợi ý biện pháp xử lý:
- Kịp thời báo quân y về triệu trứng của chiến sĩ; đồng thời, có biện pháp cách ly, để bảo đảm an toàn cho đơn vị.
- Căn cứ vào hướng dẫn của các cơ quan truyền thông, kinh nghiệm xử lý các tình huống bị nhiễm bệnh trước đó, xử lý các tình huống ban đầu, nếu nhiễm bệnh nặng tiến hành ngay các biện pháp sơ cứu, chấp hành tốt công tác bảo đảm an toàn tránh lây lan dịch trong đơn vị.
- Kịp thời báo cáo Ban chỉ đạo phòng, chống dịch; xử lý, tập trung ổn định đội hình đơn vị, giải thích động viên tư tưởng bộ đội.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 16: Chiến sĩ trong Đại đội A có bố, mẹ và em phát hiện bị nhiễm loại vi rút mới, cả nhà phải đi cách ly, điều trị tập trung.
* Biện pháp xử lý:
- Hội ý, trao đổi trong cấp ủy, chỉ huy đại đội, thống nhất cách xử lý; phân công cán bộ đơn vị gặp gỡ, động viên chiến sĩ; báo cáo, xin ý kiến chỉ đạo của chỉ huy cấp trên.
- Chính trị viên đại đội, trung đội trưởng gặp gỡ quân nhân để nắm rõ hơn tình hình gia đình; ổn định tâm lý; giáo dục phân tích cho quân nhân thấy rõ các quy định phòng, chống dịch của đơn vị, địa phương; động viên quân nhân an tâm công tác.
- Cán bộ đại đội, tiểu đoàn gọi điện hỏi thăm, động viên gia đình chiến sỹ; chia sẻ các biện pháp tăng cường chăm sóc sức khỏe và điều trị bệnh. 
- Tạo điều kiện cho chiến sỹ thường xuyên gọi điện cho người thân trong gia đình, nhờ họ hàng, bạn bè... chăm lo, chia sẻ, hỗ trợ những khó khăn về vật chất, tinh thần cho người thân quân nhân thời gian điều trị.
- Các cấp xem xét, đề nghị trợ cấp khó khăn cho quân nhân trong điều kiện, khả năng của đơn vị.
- Phân công cán bộ, tiểu đội trưởng thường xuyên quan tâm nắm tâm tư, nguyện vọng và động viên quân nhân tích cực tham gia các hoạt động của đơn vị. Phát huy vai trò của chi đoàn, HĐQN, chiến sĩ dân vận, chiến sĩ bảo vệ, bạn bè, đồng đội thân thiết để gần gũi, chia sẻ, động viên tư tưởng tránh biểu hiện buồn chán, bi quan, ảnh hưởng đến công tác và chấp hành kỷ luật.
- Nắm chắc mọi diễn biến liên quan đến quân nhân và gia đình quân nhân để báo cáo cấp trên, xin ý kiến chỉ đạo giải quyết các vấn đề phát sinh theo quy định.
Tình huống 17: Trong thời gian thực hiện giãn cách xã hội theo Chỉ thị của Chính phủ. Quân nhân của đơn vị có thân nhân bị nhiễm bệnh tử vong, quân nhân lên báo cáo với chỉ huy đơn vị xin nghỉ phép để về viếng thân nhân.
- Hội ý cấp ủy, chỉ huy đại đội đánh giá tình hình, nắm chắc hoàn cảnh gia đình quân nhân, phân công cán bộ thường xuyên động viên tư tưởng, thống nhất biện pháp giúp đỡ quân nhân. Báo cáo lên chỉ huy cấp trên.
- Thống nhất trong chỉ huy đại đội: Phân công Chính trị viên đại đội gặp gỡ quân nhân để nắm rõ hơn tình hình, nguyện vọng của quân nhân và gia đình quân nhân.
- Thực hiện chỉ đạo của chỉ huy đơn vị: 
+ Chỉ huy cơ quan chính trị trực tiếp gặp gỡ, động viên chiến sĩ, nắm tình hình và động viên, thường xuyên chia sẻ với gia đình quân nhân; phân tích cho chiến sĩ và gia đình quân nhân những khó khăn, quy định của địa phương tổ chức tang lễ trong điều kiện diễn biến phức tạp; sự lây lan của dịch bệnh... (Địa phương sẽ tổ chức hỏa táng, không được tổ chức tang lễ đông người, mọi hoạt động đều phải chấp hành nghiêm quy định phòng dịch). Động viên chiến sĩ ở tại đơn vị, khi nào dịch bệnh ổn định, đơn vị sẽ tạo điều kiện để chiến sĩ về động viên gia đình và thắp nhang cho bố.
+ Chỉ huy cơ quan tham mưu liên lạc, phối hợp với ban chỉ huy quân sự quận, huyện (xã, phường) địa phương nơi gia đình quân nhân cư trú để giúp đỡ, hỗ trợ lo hậu sự cho bố quân nhân trong điều kiện cho phép.
- Tạo điều kiện cho chiến sĩ thường xuyên gọi điện cho người thân trong gia đình, nhờ họ hàng, bạn bè... gúp đỡ gia đình lo hậu sự trong điều kiện phòng chống dịch bệnh.
- Chỉ huy đơn vị; cán bộ, nhân viên, chiến sỹ trong đơn vị thăm hỏi, động viên, chia buồn mất mát với gia đình quân nhân và quân nhân bằng tình cảm chân thành nhất, thể hiện sâu đậm tình đồng chí đồng đội.
- Các cấp xét, đề nghị và trao trợ cấp khó khăn cho quân nhân.
- Báo cáo và đề xuất ý kiến chỉ đạo của cấp trên; lập bàn thờ bái vong tại đơn vị để các tổ chức, quân nhân đến thăm hỏi, chia buồn.
- Thông qua sinh hoạt, học tập, giao ban, hệ thống truyền thanh nội bộ... để kịp thời biểu dương việc khắc phục khó khăn, vượt qua sự mất mát người thân của chiến sĩ ở lại đơn vị, chấp hành nghiêm kỷ luật, phấn đấu hoàn thành tốt nhiệm vụ của quân nhân.
- Phân công cán bộ tiếp tục quan tâm nắm tâm tư, nguyện vọng và động viên quân nhân tích cực tham gia các hoạt động của đơn vị. Phát huy vai trò của chi đoàn, HĐQN, chiến sĩ dân vận, chiến sĩ bảo vệ, bạn bè, đồng đội thân thiết để gần gũi, chia sẻ, động viên tư tưởng tránh biểu hiện buồn chán, bi quan, ảnh hưởng đến công tác và chấp hành kỷ luật.
- Sau khi hết thực hiện giãn cách theo Chỉ thị của Chính phủ, căn cứ vào tình hình dịch và nhiệm vụ của đơn vị để đề nghị cấp trên giải quyết tranh thủ, hoặc chế độ phép cho quân nhân về thăm gia đình.
- Chỉ huy đại đội thường xuyên tổng hợp tình hình liên quan, báo cáo, xin ý chỉ huy cấp trên để kịp thời xử lý các vấn đề phát sinh.
Tình huống 18: Đơn vị lần đầu tiên nhận nhiệm vụ tham gia hỗ trợ nhân dân địa phương trong trong vùng dịch có nhiều ca nhiễm và nhiều người chết do nhiễm vi rút mới, một số chiến sĩ đã có biểu hiện băn khoăn, lo lắng
Gợi ý biện pháp xử lý: 
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng và việc chấp hành kỷ luật của chiến sĩ trong thời gian qua. Nắm vững tình hình tâm tư, nguyện vọng của chiến sĩ tham gia thực hiện nhiệm vụ để tham mưu cho cấp ủy, chỉ huy có biện pháp khắc phục.
- Gặp gỡ chiến sĩ có tâm lý lo lắng, giải thích rõ khi làm nhiệm vụ đơn vị đã có đủ các biện pháp bảo đảm an toàn (khẩu trang, tiêm vaccine, mặc quần áo bảo hộ, cách ly, theo dõi sức khỏe thường xuyên…) và khi thực hiện nhiệm vụ đã là quân nhân việc sẵn sàng hy sinh cho nhân dân, đất nước vừa là vinh dự vừa là trách nhiệm; xây dựng ý chí quyết tâm hoàn thành tốt nhiệm vụ được giao trong mọi hoàn cảnh.
- Thường xuyên giáo dục, tuyên truyền cho chiến sĩ nâng cao ý thức trách nhiệm, khắc phục khó khăn trong thực hiện nhiệm vụ, chấp hành nghiêm các biện pháp phòng, chống dịch.
- Chủ động bồi dưỡng kinh nghiệm, tổ chức luyện tập thường xuyên các phương án dập dịch cho quân nhân và phân đội, nhất là các quy tắc bảo đảm an toàn trong thực hiện nhiệm vụ
- Thường xuyên bổ sung các trang bị, vật dụng bảo đảm an toàn trong thực hiện nhiệm vụ (quần áo bảo hộ, khẩu trang…).
- Bảo đảm đúng, đủ tiêu chuẩn, chế độ chính sách cho chiến sĩ yên tâm trong thực hiện nhiệm vụ.
- Tổ chức sinh hoạt  rút kinh nghiệm sau mỗi lần thực hiện nhiệm vụ để chiến sĩ tự tin hơn trong quá trình thực hiện nhiệm vụ. Biểu dương, khen thưởng tập thể, cá nhân tham gia phòng, chống dịch.
- Thường xuyên nắm chắc tình hình đơn vị báo cáo trên theo quy định.
Tình huống 19: Khi nắm được thông tin đơn vị chuẩn bị nhận nhiệm vụ hành quân đến bệnh viện dã chiến để hỗ trợ các y, bác sĩ cứu chữa người bị dương tính với loại virut mới, một số cán bộ chiến sĩ có biểu hiện hoang mang, lo lắng, dao động về tư tưởng... 
Gợi ý biện pháp xử lý:
- Trao đổi thống nhất trong lãnh đạo, chỉ huy đơn vị về biện pháp xử lý. Nhanh chóng sinh hoạt quán triệt, giáo dục nâng cao nhận thức của cán bộ, chiến sĩ trong đơn vị hiểu sâu sắc về trách nhiệm của Quân đội nói chung, đơn vị nói riêng trong thực hiện chức năng đội quân công tác, phòng, chống dịch bệnh, giúp đỡ nhân dân; mục đích, ý nghĩa và tầm quan trọng của nhiệm vụ được giao.
- Đánh giá, phân loại tư tưởng cán bộ, chiến sĩ; phân công cán bộ gặp gỡ số chiến sĩ có biểu hiện tư tưởng dao động để nắm chắc tình hình và động viên bộ đội xác định rõ trách nhiệm được giao; khơi dậy tinh thần tham gia phòng, chống dịch vì cuộc sống của cộng đồng, của quê hương, của gia đình; kịp thời ngăn chặn những biểu hiện tư tưởng ngại khó, ngại khổ... chủ động định hướng, giải quyết, ổn định tình hình đơn vị.
- Đẩy mạnh công tác tuyên truyền, thông qua các phong trào thi đua của Chính phủ, Quân đội chung tay đẩy lùi dịch bệnh; các câu chuyện, video clip trực quan về các tấm gương sẵn sàng vì nhân dân không quản ngại khó khăn, gian khổ; những tình cảm yêu mến của nhân dân với “Bộ đội Cụ Hồ” và những việc làm ý nghĩa của các cơ quan, đơn vị toàn quân trong thời gian qua...
- Đề nghị cấp trên bồi dưỡng, tập huấn phương pháp phòng, chống dịch bệnh, bảo đảm an toàn; đơn vị tự bồi dưỡng cho cán bộ, chiến sĩ những kinh nghiệm qua thực tế, tạo niềm tin tưởng, yên tâm khi nhận nhiệm vụ.
- Tổ chức phát động đợt thi đua cao điểm, đột kích, để cán bộ, chiến sĩ hứa hẹn, ký kết giao ước thi đua, góp phần hoàn thành xuất sắc nhiệm vụ được giao.
- Quá trình thực hiện nhiệm vụ, tiếp tục đẩy mạnh các hoạt động thi đua, tuyên truyền; thường xuyên gần gũi với bộ đội, nhất là bộ phận khó khăn, phức tạp, thực hiện nhiệm vụ nhỏ lẻ, độc lập; nắm chắc tâm tư tình cảm và chia sẻ những khó khăn vất vả, khơi gợi niềm vinh dự tự hào khi được thực hiện nhiệm vụ.
Tình huống 20: Cán bộ, chiến sỹ thực hiện nhiệm vụ đặc thù (quân bưu, hậu cần...) buộc phải qua địa bàn có dịch diễn biến phức tạp, các địa phương thành lập chốt kiểm soát và duy trì, kiểm tra nghiêm ngặt người và phương tiện đi qua; nguy cơ nhiễm bệnh cao.
Gợi ý biện pháp xử lý:
- Chi ủy phải xác định các chủ trương, biện pháp lãnh đạo thực hiện nhiệm vụ sát thực tiễn, chỉ huy đơn vị đánh giá nguy cơ lây dịch bệnh, thống nhất biện pháp thực hiện nhiệm vụ, phân công cán bộ giáo dục, động viên tư tưởng; cán bộ huấn luyện bổ sung và chuẩn bị các vật chất để thực hiện nhiệm vụ; báo cáo cấp trên xin ý kiến chỉ đạo.
- Chính trị viên đại đội trực tiếp giáo dục, động viên cán bộ, chiến sỹ nhận thức sâu sắc nhiệm vụ; quyết tâm khắc phục khó khăn, bảo đảm tốt công tác phục vụ trong mọi tình huống. Trực tiếp gặp gỡ, đối thoại, tìm hiểu nắm tư tưởng, đặc biệt là biểu hiện lo sợ, do dự khi thực hiện nhiệm vụ hay không; giáo dục, động viên chiến sĩ có nhận thức đúng, không nên lo lắng, ngại khó khăn để thoái thác nhiệm vụ; động viên quân nhân tin tưởng và chấp hành các quy định trong phòng chống dịch.
- Tổ chức tốt hoạt động thi đua khắc phục khó khăn, quyết tâm hoàn thành nhiệm vụ trong toàn đơn vị. 
- Tổ chức chặt chẽ, nghiêm túc việc triển khai tổ chức thực hiện nhiệm vụ, thực hiện nghiêm các biện pháp phòng chống dịch (Bảo đảm cho 100% quân nhân thực hiện nhiệm vụ ngoài doanh trại đã được tiêm vaccine và tuân thủ đầy đủ các biện pháp bảo đảm phòng, chống dịch, hạn chế thấp nhất các nguy cơ lây nhiễm. Đồng thời, thực hiện các biện pháp phòng, chống dịch, khử khuẩn sau từng lượt, từng buổi công tác về đơn vị. Khi hoàn thành nhiệm vụ trở về đơn vị các phương tiện đều được phun khử khuẩn các phương tiện; bố trí ăn, nghỉ khu riêng cho cán bộ, chiến sĩ để hạn chế tiếp xúc, thực hiện phòng chống dịch ở mức cao hơn). 
- Tổ chức sinh hoạt đơn vị để giáo dục, tuyên truyền nâng cao hiểu biết, nhận thức về dịch bệnh và các biện pháp phòng, chống dịch; rút kinh nghiệm chung và động viên cán bộ, chiến sĩ xác định tư tưởng, trách nhiệm, khắc phục khó khăn, hoàn thành tốt nhiệm vụ được giao. 
- Phân công cán bộ theo dõi, giúp đỡ, động viên chiến sĩ trong quá trình thực hiện nhiệm vụ. Kịp thời nắm bắt và giải quyết tốt các tư tưởng nảy sinh trong quá trình thực hiện nhiệm vụ.
Tình huống 21: Trong điều kiện thực hiện giãn cách xã hội Chỉ thị của Thủ tưởng Chính phủ, đơn vị cấm trại dài ngày để phòng, chống dịch; có một số quân nhân trong đơn vị có biểu hiện nảy sinh tâm lý chủ quan, cho rằng đơn vị đã cấm trại lâu ngày, cách ly với bên ngoài nên buông lỏng, đơn giản trong thực hiện các quy định phòng, chống dịch.
Gợi ý biện pháp xử lý:
- Trao đổi trong cấp ủy, chỉ huy đơn vị, đánh giá tình hình tư tưởng của các quân nhân trong đơn vị, thống nhất biện pháp giải quyết, phân công cấp ủy viên phụ trách; báo cáo cấp trên xin ý kiến chỉ đạo.
- Tổ chức sinh hoạt đơn vị, trực tiếp đối thoại, tìm hiểu xác định rõ nguyên nhân, nắm tư tưởng của bộ đội, đặc biệt là các quân nhân có biểu hiện tâm lý chủ quan. Phân tích làm rõ tác hại của việc buông lỏng, thực hiện không nghiêm các quy định phòng dịch đối với từng quân nhân và toàn đơn vị để mọi quân nhân xác định lại trách nhiệm trong thực hiện.
- Tiếp tục tổ chức quán triệt lại các quy định của Chính phủ, cấp trên về phòng, chống dịch; các quy định tổ chức bảo đảm an toàn trong sẵn sàng chiến đấu, huấn luyện, sinh hoạt trong điều kiện thực hiện giãn cách xã hội để phòng, chống dịch theo Chỉ thị của Thủ tướng Chính phủ.
- Duy trì nghiêm nền nếp huấn luyện, sinh hoạt, chế độ chính quy phù hợp với trạng thái phòng, chống dịch đã được cấp trên quy định theo từng cấp độ. Xử lý nghiêm theo điều lệnh các quân nhân thực hiện không nghiêm các quy định phòng, chống dịch của đơn vị.
- Phát huy tác dụng của các thiết chế văn hóa, hệ thống website, truyền thanh nội bộ kịp thời lan tỏa những tấm gương tốt, những cách làm hay, mô hình hiệu quả trong phòng chống dịch bệnh; đồng thời phê bình, chấn chỉnh các biểu hiện tư tưởng lệch lạc, chủ quan trong phòng chống dịch.
- Giáo dục cho cán bộ, chiến sĩ tự rèn luyện, nâng cao sức khỏe, bảo đảm đời sống văn hóa, tinh thần lành mạnh, sẵn sàng thực hiện tốt các nhiệm vụ được giao.
- Phát huy vai trò các tổ chức thanh niên, HĐQN, chiến sĩ dân vận, chiến sĩ bảo vệ; phân công cán bộ để chia sẻ, động viên tư tưởng tránh biểu hiện buồn chán, bi quan; dẫn đến vi phạm kỷ luật, vi phạm quy định của đơn vị.
- Tổng hợp tình hình, báo cáo cấp trên theo quy định.
Tình huống 22: Một số cán bộ, chiến sĩ sau một thời gian dài thực hiện nhiệm vụ tại các chốt phòng, chống dịch Covid-19 trên biên giới có biểu hiện chủ quan, thiếu quyết tâm, lơ là trong thực hiện nhiệm vụ.
* Gợi ý biện pháp xử lý
- Cấp ủy, ban chỉ huy đơn vị rà soát nắm tình hình, kết quả thực hiện nhiệm vụ của cán bộ, chiến sĩ; tìm hiểu tâm lý, cũng như nguyên nhân tác động đến suy nghĩ của cán bộ, chiến sĩ dẫn đến có biểu hiện chủ quan thiếu quyết tâm trong quá trình thực hiện nhiệm vụ được giao, như: Điều kiện ăn, ở, sinh hoạt; hoàn cảnh gia đình; các mối quan hệ xã hội; đời sống tình cảm… 
- Phân công cấp ủy, ban chỉ huy đơn vị gặp gỡ, nắm tâm tư, nguyện vọng của cán bộ, chiến sĩ làm nhiệm vụ tại các chốt chống dịch để có biện pháp giáo dục, động viên, giúp đỡ chấn chỉnh kịp thời thái độ, tinh thần trong thực hiện chức trách, nhiệm vụ được giao.
- Dự kiến nội dung, biện pháp giải quyết những nảy sinh tư tưởng chủ quan, lơ là, thiếu quyết tâm; tổ chức sinh hoạt bộ phận và đơn vị quán triệt các văn bản của các cấp về công tác phòng, chống dịch Covid-19; tính chất nguy hiểm của dịch bệnh đối với sức khỏe và tính mạng con người; xác định nhiệm vụ phòng, chống dịch của lực lượng BĐBP là nhiệm vụ chính trị được Đảng, Nhà nước, Quân đội giao và vì Nhân dân phục vụ. Từ đó, xây dựng niềm tự hào ý thức trách nhiệm và tinh thần cảnh giác để quyết tâm khắc phục, khó khăn tiếp tục thực hiện nhiệm vụ được giao.
- Phân công nhiệm vụ cho các đồng chí chốt trưởng, bộ phận trưởng, cán bộ, đảng viên gần gũi, quan tâm, giúp đỡ, động viên các đồng chí trong quá trình thực hiện nhiệm vụ được giao; đồng thời thay mặt đơn vị, chỉ huy kết nối, động viên, thuyết phục như: Thăm hỏi gia đình, người thân quân nhân.
- Tăng cường giáo dục truyền thống Quân đội, lực lượng và đơn vị, đẩy mạnh thực hiện các phong trào thi đua trong đơn vị; tổ chức thực hiện tốt công tác tuyên truyền gương người tốt, việc tốt; nhân điển hình tiên tiến trong đơn vị.
- Duy trì nghiêm túc nền nếp, chế độ sinh hoạt, học tập, công tác theo quy định của cấp trên về từng trạng thái phòng, chống dịch bệnh; vận dụng linh hoạt trong giải quyết chế độ phép, nghỉ tranh thủ để cán bộ, chiến sĩ luân phiên được nghỉ tranh thủ, có điều kiện giải quyết công việc gia đình, bản thân. 
- Cấp ủy, chỉ huy đơn vị thường xuyên quan tâm động viên về vật chất và tinh thần cho cán bộ, chiến sĩ tại các chốt chống dịch; thực hiện tốt công tác chính sách, hậu phương Quân đội. 
- Xử lý nghiêm các trường hợp không hoàn thành nhiệm vụ, vi phạm các quy định trong quá trình thực hiện nhiệm vụ. 
Tình huống 23: Các quân nhân trong quá trình cách ly tập trung, sau khi xét nghiệm sáng lọc; thì phát hiện ra có 01 quân nhân dương tính với loại vi rút mới; làm cho cán bộ, chiến sĩ trong đơn vị nhiều đồng chí hoang mang, lo lắng.
Gợi ý biện pháp xử lý:
- Hội ý lãnh đạo, chỉ huy đơn vị báo cáo với cấp trên xin ý kiến chỉ đạo.
- Động viên tư tưởng quân nhân bị nhiễm và cán bộ, chiến sĩ trong đơn vị bình tĩnh, tự tin, tránh hoang mang dao động, tin tưởng vào công tác phòng, chống dịch tại khu cách ly và hiệu quả của vắcxin được tiêm.
- Kịp thời nắm bắt tư tưởng bộ đội, có những biện pháp xử lý phù hợp, ngăn chặn, xử lý các thông tin, dư luận gây hoang mang làm ảnh hưởng đến tư tưởng của cán bộ, chiến sĩ trong đơn vị.
- Lãnh đạo, chỉ huy đơn vị thường xuyên quan tâm, động viên thăm hỏi, chia sẻ những khó khăn, vướng mắc của quân nhân, đồng thời tạo điều kiện để quân nhân mắc loại vi rút mới có tinh thần tốt nhất trong điều trị bệnh. 
- Tổ chức bình xét khen thưởng các quân nhân đã hoàn thành nhiệm vụ tham gia trực tiếp trên tuyến đầu phòng, chống dịch.
Tình huống 24: Đơn vị nằm trong khu vực phải thực hiện giãn cách xã hội theo Chỉ thị của Chính phủ; đơn vị thực hiện nhiệm vụ sản xuất kinh doanh có hiện tượng sản xuất cầm chừng, xuất hiện luồng tư tưởng lo lắng vì thu nhập thấp.
Gợi ý biện pháp xử lý:
- Quán triệt sâu kỹ các văn bản, chỉ thị, hướng dẫn các cấp; triển khai tăng cường công tác tuyên truyền, giáo dục phòng, chống đại dịch. Qua đó giúp cán bộ, người lao động hiểu rõ về dịch bệnh và các biện pháp phòng, chống. Đẩy mạnh công tác tuyên truyền phòng, chống dịch trên hệ thống truyền thanh nội bộ, panô, băng zôn, khẩu hiệu; lồng ghép vào các buổi sinh hoạt, học tập, huấn luyện; thường xuyên cập nhật thông tin, diễn biến tình hình dịch bệnh kết hợp với định hướng tư tưởng cho người lao động.
- Ra nghị quyết chuyên đề của cấp ủy lãnh đạo thực hiện nhiệm vụ phòng,  chống dịch; cùng với những xây dựng kế hoạch, phương án được chủ động xây dựng, sẵn sàng xử trí mọi tình huống giúp cán bộ, người lao động trong quá trình sản xuất kinh doanh; không hoang mang, lo lắng trong phòng, chống dịch. 
- Các cấp ủy, tổ chức đảng, cơ quan, đơn vị trong các đơn vị sản xuất kinh doanh làm tốt công tác giáo dục chính trị, giáo dục truyền thống cho người lao động; chủ động, sáng tạo thực hiện các biện pháp phòng, chống dịch bệnh.
- Làm tốt công tác dự báo, chủ động xây dựng các phương án, kế hoạch sản xuất kinh doanh, hoạt động CTĐ, CTCT phù hợp với tình hình thực tế của từng cấp độ dịch; nắm chắc tình hình địa bàn, chủ động triển khai hoạt động sản xuất, kinh doanh bảo đảm phù hợp với quy định phòng, chống dịch; tích cực tham gia sản xuất, bảo đảm an sinh xã hội, đời sống của cán bộ, nhân viên người lao động phục vụ công cuộc, góp phần ổn định chính trị, phát triển kinh tế, văn hóa, xã hội của đất nước.
- Đẩy mạnh thực hiện tốt các phong trào thi đua, hướng vào khắc phục khâu yếu, việc khó, vươn lên hoàn thành xuất sắc nhiệm vụ phòng chống dịch; các cơ quan, đơn vị đề cao tinh thần trách nhiệm, tích cực hưởng ứng Lời kêu gọi Đảng, Nhà nước phát động. Các cơ quan, đơn vị đẩy mạnh thực hành tiết kiệm góp phần tạo nguồn lực để tập trung chống dịch, bảo đảm an sinh xã hội, chăm lo sức khỏe và đời sống cho người lao động, đặc biệt là đối tượng hoàn cảnh khó khăn. Các cấp ủy, tổ chức đảng trong đơn vị SXKD quán triệt và tổ chức triển khai thực hiện nghiêm túc, quyết liệt, sáng tạo hiệu quả những nội dung thi đua của Chính phủ và các cấp phát động.
Tình huống 25: Đồng chí B là Học viên tăng cường cho đồn Biên phòng X, đang thực hiện nhiệm vụ tại chốt phòng, chống dịch trên biên giới. Tuy nhiên, đồng chí thường xuyên có biểu hiện trầm tư; qua tìm hiểu, một số cán bộ, chiến sĩ cùng chốt cho biết, đồng chí B thường sử dụng điện thoại để lên facebook chia sẻ về những khó khăn vất vả trong thực hiện nhiệm vụ phòng, chống dịch và đã nhận được nhiều bình luận trái chiều khác nhau liên quan đến việc thực hiện nhiệm vụ phòng, chống dịch.
Gợi ý Biện pháp xử lý:
- Hội ý chỉ huy đơn vị để thống nhất biện pháp giải quyết; phân công cán bộ phụ trách.
- Kiểm tra, nắm lại số chiến sĩ sử dụng điện thoại không đúng quy định trong đơn vị, xác định nguyên nhân và trách nhiệm của cán bộ quản lý trong việc thực hiện quy định về việc Hạ sĩ quan, chiến sĩ không được sử dụng điện thoại di động trong thời gian tại ngũ.
- Tiến hành gặp gỡ đồng chí B để nắm tình hình cụ thể. Phân tích để đồng chí thấy được việc chiến sĩ tự ý sử dụng điện thoại di động trong thời gian thực hiện nhiệm vụ là sai với quy định của đơn vị, việc chia sẻ hoạt động quân sự trên facebook là vi phạm quy định, làm lộ lọt bí mật quân sự (facebook là diễn đàn tự do, ý kiến bình luận khác nhau, trong đó có nhiều ý kiến tiêu cực, tác động xấu đến nhận thức tư tưởng của chiến sĩ); động viên chiến sĩ cần nghiêm túc rút kinh nghiệm; yêu cầu đồng chí B gỡ bỏ ngay những nội dung đã đăng tải có liên quan đến Quân đội, BĐBP và đơn vị, chấm dứt ngay việc làm trên; yêu cầu chiến sĩ B gửi điện thoại về nhà hoặc gửi cho chỉ huy đơn vị giữ hộ.
- Chỉ đạo đơn vị tổ chức cho chiến sĩ vi phạm quy định về sử dụng điện thoại di động viết tường trình, kiểm điểm; tiến hành sinh hoạt đơn vị kiểm điểm theo phân cấp (căn cứ vào tính chất, mức độ để nhắc nhở, giải quyết phù hợp); đồng thời yêu cầu mọi quân nhân trong đơn vị rút kinh nghiệm, tự giác chấp hành nghiêm quy định của đơn vị. 
- Cấp uỷ, chỉ huy đơn vị sinh hoạt rút kinh nghiệm, tăng cường công tác bảo vệ chính trị nội bộ; phân công đảng viên theo dõi, giúp đỡ học viên an tâm công tác, hoàn thành tốt nhiệm vụ. 
Tình huống 26: Một số quân nhân đang làm nhiệm vụ trên tàu chưa yên tâm trong thực hiện nhiệm tuần tra, kiểm tra, kiểm soát ngăn chặn người xuất, nhập cảnh trái phép bằng đường biển trong phòng, chống đại dịch.
Gợi ý biện pháp xử lý:
- Chỉ huy tàu phải kịp thời tìm hiểu, nắm thực chất tư tưởng của số quân nhân chưa yên tâm trong thực hiện nhiệm vụ phòng, chống đại dịch.
- Trao đổi với cấp ủy, tranh thủ ý kiến của các ngành (bộ phận) để phân tích, thống nhất nhận định, đánh giá, phân loại tư tưởng, xác định rõ nguyên nhân của số quân nhân chưa yên tâm thực hiện nhiệm vụ phòng, chống dịch (sợ bị lây nhiễm dịch từ những người xuất, nhập cảnh trái phép, sợ khó khăn vất vả, do tác động của mặt trái cơ chế thị trường…). Sơ bộ báo cáo cấp trên, đề xuất biện pháp tiến hành công tác tư tưởng. 
- Gặp gỡ, giáo dục, động viên nâng cao nhận thức, trách nhiệm cho cán bộ, chiến sĩ trên tàu, đặc biệt tập trung vào số quân nhân chưa yên tâm thực hiện nhiệm vụ. Trong đó chủ yếu, trọng tâm là giáo dục động cơ, mục tiêu lý tưởng phấn đấu, các quy định, biện pháp bảo đảm an toàn trong phòng, chống dịch; trình độ và khả năng cứu chữa của đội ngũ y, bác sỹ…, giáo dục truyền thống, nhiệm vụ quân đội, lực lượng; các gương điển hình tiên tiến trong tham gia phòng, chống dịch của đơn vị, lực lượng và toàn quân.
- Giải quyết thoả đáng kịp thời những khó khăn, vướng mắc trong điều kiện khả năng cho phép của tàu.
- Tăng cường đối thoại trực tiếp, xây dựng môi trường lành mạnh, bầu không khí dân chủ, đoàn kết thống nhất, thương yêu, giúp đỡ nhau. Tạo điều kiện để các đồng chí đó tích cực tham gia vào các hoạt động chung của tàu.
- Phát huy vai trò của tổ chức đoàn, hội đồng quân nhân để động viên, thuyết phục giúp đỡ các quân nhân yên tâm công tác.
- Phối hợp, cùng với gia đình, người thân, bạn bè, đồng hương để tác động giải quyết các vướng mắc trong nhận thức và tư tưởng.
- Phân công các đồng chí trưởng ngành (trưởng bộ phận) thường xuyên theo dõi, giúp đỡ cảm hoá, động viên, nắm diễn biến tư tưởng, hành động của quân nhân chưa yên tâm công tác, kịp thời báo cáo chỉ huy tàu.
- Chỉ huy tàu thường xuyên sâu sát, quản lý tốt tình hình tư tưởng bộ đội, kịp thời có biện pháp sát, đúng, trúng giải quyết dứt điểm các vấn đề nảy sinh về tư tưởng trong quá trình thực hiện nhiệm vụ, đồng thời động viên, khích lệ khi các đồng chí đó có chuyển biến tiến bộ.
- Kết thúc nhiệm vụ, kịp thời ổn định mọi mặt, sẵn sàng nhận nhiệm vụ tiếp theo khi có lệnh; tổng hợp tình hình báo cáo chỉ huy hải đội theo quy định.
Tình huống 27: Cán bộ trẻ, có gia đình riêng ở Hà Nội, bố mẹ hai bên (bên chồng và bên vợ) đều ở quê (xa Hà Nội từ 120-300km), vợ mới sinh con được 3 tháng (phải mổ đẻ), con thứ nhất còn nhỏ mới được 3 tuổi, hiện chồng là người chăm sóc, lo toan chính các công việc trong nhà; nhận nhiệm vụ đi miền Nam tham gia phòng chống dịch.
Gợi ý biện pháp xử lý:
- Trước khi lập danh sách cử cán bộ đó đi công tác miền Nam; lãnh đạo, chỉ huy đã tiến hành rà soát toàn bộ cán bộ trong cơ quan để lập danh sách cán bộ tham gia chỉ thị của cấp trên.
- Khi cán bộ có tình huống trên được cử đi công tác, đã được lãnh đạo, chỉ huy gặp riêng, thăm dò nắm bắt nguyện vọng; đồng chí đã nhất trí nhận nhiệm vụ, nhưng có báo cáo tình hình hiện tại của gia đình.
- Lãnh đạo, chỉ huy cơ quan đã đưa ra những gợi ý, phương án giải quyết; đồng chí cán bộ đã đưa ra được phương án nhờ gia đình bên ngoại ra giúp đỡ gia đình khi đi công tác xa nhà.
- Kết quả đồng chí cán bộ đã nhận nhiệm vụ, lên đường và hiện đang công tác tại một tổ quân y lưu động tại một quận ở thành phố Hồ Chí Minh.
- Chỉ huy cơ quan có phương án thăm hỏi, động viên cán bộ và gia đình cán bộ.
- Kết thúc đợt công tác, thông qua kết quả hoàn thành nhiệm vụ của cá nhân, triển khai bình xét, khen thưởng, biểu dương thành tích trước cơ quan, đơn vị.
- Tiến hành rút kinh nghiệm chung những vấn đề đạt được và chưa đạt được của các đội công tác.
Tình huống 28: Đơn vị tiếp nhận công dân từ nước ngoài về cách ly y tế tập trung. Do điều kiện sống ở nước ngoài đầy đủ tiện nghi, nhưng khi về đến đơn vị, một số công dân không thích nghi được với điều kiện cơ sở vật chất trong khu cách ly và đòi hỏi quá mức, không tôn trọng tập thể. Khi đơn vị không đáp ứng được những yêu cầu thì đã có những hành vi gây rối mất trật tự trong khu cách ly.
Gợi ý biện pháp xử lý:
- Nắm chắc tình hình đơn vị, hội ý lãnh đạo, chỉ huy bàn biện pháp giải quyết; báo cáo lên cấp trên; thông báo tình hình cho cấp ủy, chính quyền và lực lượng làm nhiệm vụ bảo đảm an ninh, trật tự trên địa bàn.
- Rà soát phân loại đối tượng, xác định người lôi kéo và người bị lôi kéo. Phân công cán bộ tiếp xúc với những người lôi kéo, cầm đầu, người có uy tín, giải thích tính ưu việt của Đảng, Nhà nước Việt Nam trong việc tạo điều kiện cho công dân đang học tập, công tác và định cư ở nước ngoài về nước phòng, chống dịch bệnh; phân tích rõ những thuận lợi, khó khăn và kết quả các lần tiếp nhận, cách ly công dân của đơn vị.
- Lắng nghe, tiếp thu ý kiến của công dân; đáp ứng các nhu cầu chính đáng của công dân trong điều kiện cho phép của đơn vị; động viên bộ phận phục vụ tăng cường chế biến món ăn bảo đảm vệ sinh, hợp khẩu vị theo chế độ, quy định hiện hành. Tạo điều kiện để công dân tham gia giám sát việc bảo đảm chế độ tiêu chuẩn và tiếp cận lực lượng phục vụ để công dân tận mắt chứng kiến việc cán bộ, chiến sĩ đơn vị khắc phục khó khăn, hết lòng vì nhân dân phục vụ.
- Phổ biến và quán triệt lại toàn bộ các tiêu chuẩn, chế độ cũng như điều kiện của đơn vị trong phục vụ cách ly công dân; để mọi người nắm được và chấp hành nghiêm các quy định của đơn vị, không làm ảnh hưởng đến lực lượng phục vụ cũng như các công dân khác.
- Chỉ đạo lực lượng quân y làm tốt công tác thăm, khám, lấy mẫu xét nghiệm; gắn quá trình thực hiện nhiệm vụ với việc trò chuyện cùng công dân, lắng nghe, tiếp thu ý kiến để trao đổi, báo cáo lại với chỉ huy đơn vị; thường xuyên nắm chắc diễn biến về tâm lý, tư tưởng của công dân.
- Phát huy vai trò của các thiết chế văn hóa, mạng truyền thanh nội bộ và các trang, nhóm Facebook của đơn vị trong việc tuyên truyền thường xuyên về tình hình dịch bệnh, ý thức trách nhiệm của cán bộ, chiến sĩ, tính ưu việt của chế độ XHCN, chế độ được hưởng…(có thể mời các công dân có uy tín, năng khiếu cùng tham gia tuyên truyền)
- Những trường hợp cố tình chống đối, có hành vi phá hoại tài sản của đơn vị, tiến hành lập biên bản sự việc, (ghi lại hình ảnh) kịp thời báo cáo cấp trên, báo cáo với các cơ quan pháp luật và lực lượng bảo đảm an ninh trật tự để có biện pháp chấn áp kịp thời.
- Thường xuyên duy trì nghiêm nền nếp, chế độ giao ban, hội ý và chế độ báo cáo theo quy định.       
Tình huống 29: Sau khi bình xét đề nghị khen thưởng thành tích đợt tham gia phòng chống thiên tai, dịch bệnh tại địa phương, có dư luận trong đơn vị cho rằng: Việc bình xét khen thưởng chưa đúng người, đúng thành tích; có quân nhân được đề nghị khen thưởng do chỉ huy ưu ái. 
Gợi ý biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy đánh giá mức độ ảnh hưởng dư luận; phân công cán bộ xác minh làm rõ.
- Kiểm tra nắm lại các quy trình, thủ tục xét đề nghị khen thưởng của đơn vị; 
- Gặp gỡ trao đổi với cán bộ, chiến sĩ đơn vị có luận để nắm tình hình xét khen thưởng và đề nghị khen thưởng. 
- Gặp gỡ ban chỉ huy đơn vị có dư luận để trao đổi, nghe phản ánh tình hình.
- Nếu phát hiện có sai sót trong quy trình, thủ tục, tiêu chuẩn đề nghị khen thưởng thì yêu cầu cấp ủy cấp dưới tổ chức xét, đề nghị khen thưởng lại. Lãnh đạo, chỉ huy cấp trên trực tiếp dự họp để nắm, chỉ đạo trực tiếp. Có biện pháp chấn chỉnh, phê bình nghiêm túc đối với lãnh đạo, chỉ huy, cán bộ đơn vị làm không đúng quy định.
- Nếu phát hiện sai sót sau khi đã đề nghị lên cấp trên thì họp cấp ủy, thống nhất đề nghị lên cấp trên xem xét lại kết quả khen thưởng, hoặc đề nghị khen thưởng bổ sung, nhưng phải bảo đảm đúng tiêu chuẩn, tỷ lệ quy định.
- Tổ chức rút kinh nghiệm nghiêm túc ở các tổ chức, các cơ quan, đơn vị có liên quan.
Tình huống 30: Đơn vị có một đồng chí quân nhân viết đơn tình nguyện lên đường tham gia phòng, chống dịch ở địa phương xa đơn vị, thời gian dài. Trong đơn vị có dư luận cho rằng đồng chí đó làm như vậy là cơ hội. Mục đích chính là để đánh bóng bản thân và để được khen thưởng cuối năm vì đồng chí đó sắp đến hạn nâng lương, thăng quân hàm.
- Nắm nguồn dư luận trong đơn vị, gặp gỡ những quân nhân có suy nghĩ lệch lạc, tìm hiểu nguyên nhân vì sao lại có suy nghĩ về việc viết đơn của đồng chí đó như vậy.
- Hội ý chỉ huy đơn vị đánh giá tính chất, mức độ của dư luận là do mâu thuẫn cá nhân hay do thiếu hiểu biết để có biện pháp xử lý phù hợp. Báo cáo cấp trên về tình hình đơn vị.
- Gặp gỡ, động viên, khích lệ quân nhân tình nguyện lên đường tham gia phòng chống dịch.
- Thông qua sinh hoạt đơn vị quán triệt cho mọi cán bộ, chiến sĩ thấy được tình hình và sự nguy hiểm của dịch, quan điểm của Đảng, Nhà nước, Quân đội, những tấm gương sáng trong phòng chống dịch bệnh. Trước tập thể đơn vị biểu dương tinh thần, hành động cao đẹp của đồng đội, đồng thời nghiêm túc phê bình những suy nghĩ lệch lạc trong đơn vị.
- Tiến hành tuyên truyền trên hệ thống loa truyền thanh, bảng tin của đơn vị về gương của đồng chí tình nguyện lên đường tham gia phòng chống dịch.
- Sau khi đồng chí thực hiện nhiệm vụ xong trở về đơn vị, tiến hành xem xét, đánh giá chất lượng hoàn thành nhiệm vụ của quân nhân đó để thông báo cho đơn vị và đề nghị biểu dương, khen thưởng.
- Tiếp tục theo dõi, nắm tình hình tư tưởng của quân nhân tham gia phòng chống dịch sau khi thực hiện nhiệm vụ và dư luận trong đơn vị.
- Tổng hợp tình hình, báo cáo cấp trên.
Tình huống 31: Hiện tượng một số sĩ quan trong đơn vị có biểu hiện chạy thành tích, che dấu khuyết điểm vi phạm trong quá trình thực hiện nhiệm vụ phòng, chống dịch, gây dư luận xấu trong nội bộ 
Gợi ý biện pháp xử lý:
- Chính ủy, chính trị viên nắm chắc tình hình tư tưởng, chấp hành kỷ luật của cán bộ và những biểu hiện che dấu khuyết điểm, chạy theo thành tích của cán bộ trong quá trình thực hiện nhiệm vụ phòng, chống dịch, thống nhất với chỉ huy đơn vị biện pháp lãnh đạo, chỉ đạo khắc phục.
 - Họp cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, chấp hành kỷ luật, dư luận của sĩ quan, quân nhân chuyên nghiệp, nguyên nhân che dấu khuyết điểm, chạy theo thành tích, thống nhất biện pháp khắc phục.
- Gặp gỡ giáo dục, tuyên truyền cho sĩ quan, quân nhân chuyên nghiệp hiểu rõ tác hại, hậu quả của biểu hiện che dấu khuyết điểm, chạy theo thành tích là vi phạm quy định của Quân đội về chế độ báo cáo; vi phạm chế độ trách nhiệm của người chỉ huy, ảnh hưởng đến việc hoàn thành nhiệm vụ phòng, chống dịch, kết quả xây dựng chi bộ TSVM, đơn vị VMTD mẫu mực tiêu biểu. 
- Tổ chức sinh hoạt đơn vị giáo dục, tuyên truyền cho sĩ quan, quân nhân chuyên nghiệp trong đơn vị nhận thức sâu sắc nhiệm vụ phòng, chống dịch và xác định đây cũng là nhiệm vụ chính trị của đơn vị để xây dựng chi bộ TSVM, đơn vị VMTD mẫu mực tiêu biểu; kiên quyết đấu tranh với những quan điểm, tư tưởng báo cáo không trung thực, che dấu khuyết điểm, chạy theo thành tích của sĩ quan, quân nhân chuyên nghiệp trong đơn vị.
- Duy trì nghiêm chế độ báo cáo, phản ánh tình hình về tư tưởng, chấp hành kỷ luật và các mối quan hệ của sĩ quan, quân nhân chuyên nghiệp trong thực hiện nhiệm vụ phòng, chống dịch. 
- Xử lý kỷ luật nghiêm minh đối với những trường hợp vi phạm.
Tình huống 32: Ban CHQS huyện H đảm nhiệm chuẩn bị và duy trì khu cách ly phòng, chống dịch; phân công cho đồng chí A (QNCN) làm công tác bảo đảm hậu cần, tuy nhiên quá trình thực hiện có dư luận cho rằng đồng chí A thực hiện thu - chi chưa rõ ràng, thiếu tính minh bạch, tác động tư tưởng của quân nhân A.
Gợi ý biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy thống nhất đánh giá tình hình quản lý tài chính trong công tác phòng chống dịch bệnh thời gian qua, dư luận của cán bộ đơn vị, thống nhất biện pháp giải quyết, khắc phục. 
- Tổ chức lực lượng chuyên môn xác minh thông tin, nắm chắc tình hình, kiểm tra công tác chi tiêu tài chính; đề xuất Đảng ủy, Ban chỉ huy giải quyết.
- Tùy theo tính chất mức độ để tổng hợp báo cáo cấp trên xin ý kiến chỉ đạo; có thể xảy ra một trong hai trường hợp sau:
Khi có biểu hiện sai phạm:
- Gặp gỡ, phân tích quân nhân A nhận rõ sai sót, khuyết điểm, thực hiện công khai, minh bạch, không làm ảnh hưởng đến uy tín của bản thân và đơn vị; yêu cầu có biện pháp khắc phục, đền bù thâm hụt (nếu có). 
- Tổ chức kiểm điểm, kỷ luật đúng với tính chất, mức độ sai phạm
- Thông qua các hình thức thông báo cho công dân đang thực hiện cách ly và cán bộ, chiến sĩ về kết quả kiểm tra, xác minh, xử lý; rút ra bài học trong công tác lãnh đạo, chỉ đạo, quản lý tài chính đảm bảo đúng nguyên tắc, công khai, minh bạch, tạo sự thống nhất cao.
- Trường hợp đồng chí A còn yếu về chuyên môn, tổ chức bồi dưỡng, tập huấn để đáp ứng yêu cầu nhiệm vụ.
- Tổng hợp kết quả xử lý, báo cáo cấp trên. 
Khi thông tin dư luận không đúng sự thật:
- Thông qua các hình thức thông báo cho công dân đang thực hiện cách ly và cán bộ, chiến sĩ về kết quả kiểm tra, xác minh, xử lý; tuyên truyền về bản chất, truyền thống tốt đẹp của “Bộ đội Cụ Hồ”, theo dõi, định hướng dư luận.
- Gặp gỡ đồng chí A để phân tích, động viên tiếp tục thực hiện nhiệm vụ
- Thông báo rõ các chế độ, tiêu chuẩn của các đối tượng tại khu cách ly y tế; thường xuyên đối thoại, giải quyết các thắc mắc của công dân và cán bộ, chiến sĩ. 
- Báo cáo đề nghị cấp trên chỉ đạo các lực lượng phối hợp, theo dõi không gian mạng, có biện pháp đấu tranh, pha loãng, gỡ bỏ những thông tin lợi dụng sai phạm để chống phá Đảng, Nhà nước và nhiệm vụ phòng, chống dịch, gây ảnh hưởng xấu đến bản chất, truyền thống của Quân đội, đơn vị.
- Trường hợp dư luận có ảnh hưởng lớn đến uy tín Quân đội, đơn vị thì tiến hành điều tra, xử lý nghiêm trường hợp thông tin sai sự thật.
- Tổng hợp kết quả xử lý, báo cáo cấp trên. 
Tình huống 33: Qua dư luận đơn vị nắm được, một đồng chí cán bộ đã vận động tiền của người dân trong khu vực cách ly để hỗ trợ cán bộ, chiến sĩ phục vụ người dân tại khu cách ly đã gây dư luận không tốt trong đơn vị.
Gợi ý biện pháp xử lý:
- Xác định đây là sự việc nhạy cảm, liên quan đến phẩm chất, uy tín của Quân đội nói chung của cán bộ nói riêng. Vì vậy, khi tiến hành cần phải thận trọng, khách quan, kiểm tra xác minh chặt chẽ, khoa học.
- Chính ủy, chính trị viên cần xác minh lại nguồn dư luận về cán bộ thực hiện nhiệm vụ trong khu cách ly, nếu đúng sự thật thì tiến hành trao đổi thẳng thắn, chân tình với đồng chí cán bộ đó; thông báo về dư luận trong khu cách ly, kết quả kiểm tra xác minh; phân tích về sự việc trên đã ảnh hưởng không tốt đến tình hình của đơn vị và uy tín của cán bộ, hình ảnh “Bộ đội Cụ Hồ”; đề nghị đồng chí chấm dứt việc làm trên.
- Trường hợp đồng chí cán bộ không nhận lỗi thì chính ủy, chính trị viên phải báo cáo cấp trên xin ý kiến chỉ đạo, cùng với cấp trên có biện pháp xác minh, chứng minh sự phản ánh của dư luận là đúng sự thật.
- Ủy ban kiểm tra cấp trên có biện pháp kiểm tra đảng viên có dấu hiệu vi phạm kỷ luật.
- Tổ chức sinh hoạt đơn vị, ổn định tình hình tư tưởng của cán bộ, chiến sĩ nhắc nhở cán bộ, chiến sĩ, nhất là các đồng chí tham gia thực hiện nhiệm vụ trong khu cách ly nêu cao ý thức tu dưỡng, rèn luyện đạo đức, lối sống, chấp hành nghiêm các quy định trong phòng, chống dịch, các quy định khi tiếp xúc với nhân dân.
- Báo cáo kết quả giải quyết vụ việc lên cấp trên.
Tình huống 34: Một số HSQ-CS trong quá trình tham gia phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh, do tính chất nhiệm vụ khó khăn, vất vả đã thể hiện thái độ không ân cần, hòa nhã với nhân dân. 
Gợi ý biện pháp xử lý:
- Cử cán bộ đơn vị gặp gỡ nhân dân nắm lại tình hình vụ việc.
- Phân công cán bộ gặp gỡ HSQ-CS trong đơn vị cùng tham gia thực hiện nhiệm vụ với bộ phận vi phạm để đối chiếu thông tin, để có cơ sở đánh giá chính xác tình hình vụ việc.
- Hội ý cấp ủy, đánh giá tính chất, mức độ, nguyên nhân biểu hiện thái độ, hành vi thiếu ân cần, hòa nhã của HSQ-CS. Thống nhất biện pháp giáo dục, khắc phục.
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm sự việc xảy ra; kết hợp giáo dục cho cán bộ, chiến sĩ nhận thức sâu sắc về ý nghĩa của nhiệm vụ tham gia phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh; chức năng, nhiệm vụ của Quân đội; phẩm chất “Bộ đội Cụ Hồ”, truyền thống đoàn kết quân dân để củng cố ý thức, trách nhiệm cho bộ đội.
- Phân công cấp ủy viên phụ trách công tác dân vận, phối hợp với cấp ủy, chính quyền, đoàn thể địa phương gặp gỡ, trao đổi, nhận khuyết điểm trước nhân dân về thái độ, hành vi của HSQ-CS trong đơn vị.
- Tùy tình hình điều kiện phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh, nếu điều kiện cho phép có thể phối hợp tổ chức tốt các hoạt động VHVN, thể thao giữa đơn vị với đoàn viên thanh niên và nhân dân địa phương để tăng cường hiểu biết, tạo lập, củng cố mối quan hệ đoàn kết, gắn bó giữa đơn vị và nhân dân trên địa bàn.
- Tăng cường quản lý tư tưởng, ý thức kỷ luật của bộ đội trong mọi hoạt động của đơn vị trong đó có nhiệm vụ cứu hộ, cứu nạn, phòng, chống thiên tai, dịch bệnh.
Tình huống 35: Một số đồng chí dân quân tự vệ không nhận nhiệm vụ tham gia phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh với lý do chính sách chi trả tiền quá thấp, không tương xứng với công sức bỏ ra, gây dư luận không tốt trong nhân dân và lực lượng dân quân tự vệ
Gợi ý biện pháp xử lý:
- Trao đổi trong Ban chỉ huy quân sự xã nhận định tình hình tư tưởng, trách nhiệm của dân quân tự vệ trong thực hiện nhiệm vụ phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh, thống nhất biện pháp giải quyết; báo cáo xin ý kiến chỉ đạo của cấp trên để bố trí người thay thế.
- Tổ chức gặp gỡ số dân quân không nhận nhiệm vụ tham gia phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh; giáo dục, quán triệt hiểu rõ sự cần thiết phải tham gia giúp nhân dân khắc phục hậu quả thiên tai, dịch bệnh, trách nhiệm, quyền lợi, nghĩa vụ của một người dân quân; qua đó xây dựng trách nhiệm sẵn sàng nhận và hoàn thành nhiệm vụ, nâng cao ý thức chấp hành Luật Dân quân tự vệ, kỷ luật Quân đội, quy định của địa phương.
- Phối hợp với gia đình, người thân, đồng chí đồng đội, động viên số dân quân còn băn khoăn trong quá trình nhận nhiệm vụ, nâng cao ý thức, trách nhiệm của dân quân tự vệ sẵn sàng nhận và hoàn thành tốt nhiệm vụ được giao.
- Định hướng để Ban chỉ huy quân sự xã tổ chức sinh hoạt rút kinh nghiệm công tác huy động quân số tham gia thực hiện nhiệm vụ phòng, chống, khắc phục sự cố thiên tai, dịch bệnh về ý thức nhận vụ trong điều kiện khó khăn, vất vả; căn cứ tính chất vụ việc có thể đề nghị hình thức kỷ luật số dân quân chấp hành không nghiêm mệnh lệnh, đồng thời rà soát, lựa chọn những đồng chí có đủ phẩm chất chính trị, trách nhiệm trong công tác tham gia vào lực lượng dân quân của xã.
- Làm tốt công tác đánh giá kết quả hoàn thành nhiệm vụ của lực lượng tham gia phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh; kịp thời khen thưởng tập thể, cá nhân có thành tích; xử lý nghiêm minh  những đồng chí vi phạm.
- Báo cáo cấp trên theo quy định.


	B. TÌNH HUỐNG TƯ TƯỞNG CÓ THỂ NẢY SINH TRONG THỰC HIỆN NHIỆM VỤ PHÒNG, CHỐNG THIÊN TAI
Tình huống 1. Một đồng chí chiến sĩ trong đơn vị có biểu hiện rất buồn và lo lắng vì khi đang tham gia phòng chống thiên tai, cứu hộ cứu nạn ở địa phương khác thì nhận được tin gia đình mình ở quê bị lũ quét cuốn trôi một số tài sản, vật dụng trong nhà, cũng như thiệt hại về hoa màu của gia đình.
Gợi ý biện pháp xử lý:
- Hội ý cán bộ đơn vị đang thực hiện nhiệm vụ phòng, chống thiên tai để nhận định tình hình, bàn cách xử trí, phân công cán bộ theo dõi, giúp đỡ chiến sĩ.
- Liên hệ với chính quyền địa phương của gia đình đồng chí đang sinh sống để nắm bắt tình hình thiệt hại do bão lũ gây ra ở đó và cụ thể thiệt hại mà gia đình của đồng chí chiến sĩ đang phải gánh chịu và nhanh chóng báo cáo với chỉ huy các cấp.
- Gặp gỡ đồng chí chiến sĩ để kịp thời động viên tư tưởng nhằm giảm bớt đi sự lo lắng, đồng thời để đồng chí hiểu được vị trí quan trọng của nhiệm vụ, từ đó cảm thấy rõ vinh dự, trách nhiệm để khắc phục khó khăn xây dựng ý chí quyết tâm và hoàn thành tốt nhiệm vụ được giao.
- Tổ chức sinh hoạt đơn vị để thông báo về tình hình nhiệm vụ, đồng thời biểu dương tinh thần khắc phục khó khăn để tiếp tục thực hiện nhiệm vụ của đồng chí chiến sĩ để mọi người cùng nhau động viên, san sẻ.
- Tạo điều kiện để đồng chí được liên hệ về gia đình thăm hỏi và động viên người thân của mình.
- Thường xuyên làm tốt công tác tuyên truyền, giáo dục cho chiến sĩ nhận thức rõ nhiệm vụ, nâng cao trách nhiệm, khắc phục mọi khó khăn trong thực hiện nhiệm vụ phòng chống thiên tai, cứu hộ cứu nạn.
- Phân công đồng chí, đồng đội thường xuyên nắm bắt, quan tâm và thường xuyên động viên đối với đồng chí đó.
- Quan tâm bảo đảm đầy đủ về tiêu chuẩn, đề nghị giải quyết tốt các chế độ, chính sách theo quy định cho chiến sĩ gặp hoàn cảnh khó khăn yên tâm công tác, xác định tốt nhiệm vụ.
- Tổ chức sinh hoạt rút kinh nghiệm sau mỗi lần thực hiện nhiệm vụ để kịp thời khắc phục những vấn đề còn tồn tại và đề ra phương hướng cho những đợt thực hiện nhiệm vụ tiếp theo. 
Tình huống 2: Trong đơn vị quân nhân A có biểu hiện buồn chán, tiêu cực khi có thân nhân (bố, mẹ, vợ, con) điều trị ở bệnh viện nhưng đơn vị chưa giải quyết phép vì phải trực phòng chống thiên tai, sẵn sàng cứu hộ, cứu nạn.
Gợi ý biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy và tiến hành gặp gỡ quân nhân A, nắm thêm các nội dung: tình hình sức khỏe và mức độ của bệnh; tình hình người chăm sóc trong gia đình; công việc của vợ và độ tuổi của các con có ảnh hưởng đến chăm sóc người bệnh không; hoàn cảnh kinh tế gia đình. Động viên quân nhân hiểu rõ yêu cầu của nhiệm vụ trực phòng chống thiên tai, sẵn sàng cứu hộ, cứu nạn, yên tâm hoàn thành tốt nhiệm vụ.
- Liên lạc với thân nhân trong gia đình đồng chí A, nắm thêm tình hình của gia đình. 
- Căn cứ vào tình trạng sức khỏe, mức độ bệnh tật của thân nhân quân nhân A để sinh hoạt thông báo với cán bộ, chiến sĩ trong đơn vị được biết để gần gũi, động viên, hoặc thăm hỏi về vật chất.
- Thường xuyên nắm tình hình tư tưởng, đánh giá đúng kết quả thực hiện nhiệm vụ và chấp hành kỷ luật của quân nhân có thân nhân nằm viện; có biện pháp khắc phục kịp thời nếu chất lượng công việc bị ảnh hưởng, hoặc biểu dương, nhân rộng trong toàn đơn vị nếu quân nhân đó hoàn thành tốt nhiệm vụ.
- Phát huy vai trò của tổ chức công đoàn, làm tốt công tác giáo dục, định hướng và quản lý chặt chẽ tình hình tư tưởng. Tránh trường hợp quân nhân vì tư tưởng không thông suốt mà có thái độ tiêu cực, trốn ra ngoài đơn vị.
- Trong trường hợp thân nhân bị bệnh rất nặng, khả năng không qua khỏi thì báo cáo cấp trên giải quyết cho quân nhân về thăm gia đình. (Lưu ý: Trước khi về cần quán triệt cụ thể, tỉ mỉ để quân nhân chấp hành nghiêm kỷ luật, bảo đảm an toàn, gửi lời hỏi thăm của đơn vị đến gia đình).
Tình huống 03: Trong đơn vị có gia đình một đồng chí hạ sĩ quan (chiến sĩ) gặp mưa bão, nhà cửa bị đất đá sạt lở vùi lấp, không bị thiệt hại về người, có biểu hiện hoang mang, lo lắng
Gợi ý biện pháp xử lý:
- Nắm chắc tâm tư, hoàn cảnh cụ thể gia đình quân nhân thông qua các nguồn tin các mối quan hệ của quân đó (các cấp báo cáo) từ đó xác định biện pháp cách thức giải quyết.
- Tiến hành gặp gỡ, trò chuyện, nắm tâm tư, nguyện vọng, những vướng mắc của quân nhân có hoàn cảnh khó khăn; từ đó động viên, chia sẻ, giúp đỡ quân nhân đó vượt qua khó khăn, yên tâm công tác xác định rõ nhiệm vụ.
- Báo cáo chỉ huy cấp trên để cùng theo dõi động viên xác định biện pháp giải quyết.
- Chỉ đạo trung đội (đại đội) có quân nhân gặp hoàn cảnh khó khăn phân công cán bộ, đảng viên, đoàn viên ưu tú theo dõi, động viên giúp đỡ quân nhân có gia đình gặp khó khăn hoàn thành nhiệm vụ.
- Chỉ đạo đơn vị có biện pháp tác động với những quân nhân khác là bạn bè thân thiết, đồng hương… với chiến sĩ gặp khó khăn để cùng chia sẻ, động viên, an ủi.
- Trường hợp (xét thấy cần thiết) đề nghị cấp có thẩm quyền giải quyết cho quân nhân đi phép về giải quyết việc gia đình.
- Đề nghị tập thể đơn vị và chỉ huy cấp trên quan tâm động viên giúp đỡ chiến sĩ gặp khó khăn về vật chất và tinh thần để góp phần giải quyết khó khăn (đề nghị trợ cấp khó khăn cho quân nhân đó theo quy định).
- Nếu có điều kiện đề nghị chỉ huy cấp trên cử cán bộ về thăm hỏi, động viên gia đình quân nhân đó.
Tình huống 04: Đơn vị nhận được nhiệm vụ tăng cường lực lượng đi giúp dân phòng chống bão lụt nhưng qua các vụ việc mất an toàn của quân đội trong giúp dân phòng chống bão lụt một số cán bộ, quân nhân chuyên nghiệp, HSQ-CS có biểu hiện lo lắng, dao động tư tưởng, tìm các lý do để trốn tránh nhiệm vụ.
Gợi ý biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy đơn vị nhận định, đánh giá tình hình tác động đến tư tưởng của bộ đội, thống nhất biện pháp giải quyết, phân công cán bộ tích cực nắm, quản lý tư tưởng bộ đội, kịp thời xử lý các tình huống có thể xảy ra.
- Nhanh chóng tổ chức sinh hoạt, quán triệt, giáo dục nâng cao nhận thức cho cán bộ, quân nhân chuyên nghiệp, HSQ-CS trong đơn vị hiểu sâu sắc về mục đích, ý nghĩa, yêu cầu và tầm quan trọng của nhiệm vụ giúp dân phòng chống bão lụt, kết quả hoàn thành nhiệm vụ của đơn vị trong thời gian qua; thấy rõ niềm vinh dự tự hào khi được chỉ huy cấp trên tin tưởng giao nhiệm vụ cho đơn vị; trên cơ sở đó xây dựng niềm tin động cơ trách nhiệm và ý chí quyết tâm hoàn thành tốt nhiệm vụ được giao.
- Đánh giá, phân loại tư tưởng cán bộ, chiến sĩ, phân công cán bộ gặp gỡ để nắm chắc tình hình và động viên bộ đội hiểu rõ nhiệm vụ; kịp thời ngăn chặn những biểu hiện tư tưởng ngại khó, ngại khổ; chủ động định hướng giải quyết ổn định tình hình đơn vị; tổng hợp báo cáo xin ý kiến chỉ đạo của cấp trên.
- Phân công những cán bộ có trình độ năng lực, phẩm chất đạo đức, tinh thần trách nhiệm tốt chỉ huy phụ trách những nhiệm vụ khó khăn phức tạp để làm gương cho cán bộ chiến sĩ yên tâm noi theo.
- Phát huy tốt hoạt động của chiến sĩ dân vận, chiến sĩ bảo vệ, duy trì sinh hoạt tổ, tiểu đội thông qua đó tìm hiểu sâu kỹ về nguyên nhân trốn tránh nhiệm vụ.
- Tổ chức phát động đợt thi đua cao điểm, đột kích, tập trung làm rõ ý nghĩa tầm quan trọng và yêu cầu của nhiệm vụ, lòng tự hào và trách nhiệm được trên giao; xác định mục tiêu, nội dung, biện pháp xác thực nhằm nâng cao nhận thức trách nhiệm, xây dựng ý chí quyết tâm chủ động khắc phục khó khăn, ý thức chấp hành kỷ luật; quan tâm đảm bảo đời sống cho cán bộ, chiến sỹ phát huy vai trò tiền phong của cán bộ, đảng viên, số chiến sĩ có thành tích trong thực hiện chức trách nhiệm vụ, tổ chức cho cán bộ chiến sĩ viết đăng ký quyết tâm thực hiện nhiệm vụ.
- Đẩy mạnh các hoạt động tuyên truyền cổ động thực hiện nhiệm vụ, thường xuyên gần gũi bộ đội, nắm chắc tâm tư tình cảm và chia sẻ những khó khăn vất vả cũng như là vinh dự tự hào khi được thực hiện nhiệm vụ giúp dân phòng chống bão lụt.
- Duy trì chặt chẽ nghiêm túc các chế độ nề nếp, sinh hoạt đơn vị rút kinh nghiệm để biểu dương khen thưởng và chấn chỉnh những sai phạm kịp thời, chủ động làm tốt công tác tư tưởng, quản lý chặt chẽ tình hình mọi mặt của đơn vị, không để dư luận xấu xảy ra trong đơn vị.
Tình huống 05: Sau siêu bão, các đợt mưa lớn kéo dài, gây ngập lụt cục bộ, làm ách tắc giao thông nghiêm trọng; một số cán bộ, CNVC, lao động không đến đơn vị làm việc được, ảnh hưởng đến dây chuyền sản xuất, chất lượng sản phẩm và công tác an toàn. Mưa bão gây thiệt hại về tài sản, tài nguyên; sân công nghiệp một số đơn vị khai thác than hầm lò bị ngập sâu, nước và đất đá có nguy cơ tràn vào trong lò, gây sập lò và hư hỏng các trang thiết bị
Gợi ý biện pháp xử lý:
- Cấp ủy, chỉ huy, cơ quan chính trị tiếp tục quán triệt, thực hiện nghiêm túc các văn bản lãnh đạo, chỉ đạo của Trung ương, QUTW-BQP và của đơn vị về phòng, chống khắc phục hậu quả thiên tai, thảm họa, dịch bệnh, cứu hộ - cứu nạn. Hội ý nhanh cấp ủy, chỉ huy bàn các giải pháp ứng phó, phòng, chống, giảm nhẹ và khắc phục thiệt hại do mưa bão gây ra, như: Phương án sản xuất kinh doanh, bảo vệ tài nguyên trong mưa bão; huy động con người, trang thiết bị; công tác bảo đảm hậu cần đời sống (xe đưa đón công nhân, nơi ở, cung ứng thực phẩm, nhu yếu phẩm, ..); công tác phòng, chống dịch bệnh (thuốc men, vật tư y tế...).
- Tăng cường lãnh đạo, chỉ đạo công tác tuyên tuyền, giáo dục chính trị, tư tưởng làm cho cấp ủy, chỉ huy các cấp, cán bộ, đảng viên, CNVC, lao động trong đơn vị thấy được những diễn biến phức tạp, khó lường của khí hậu, thời tiết, hậu quả do thiên tai gây ra, nhất là thảm họa của bão mạnh, siêu bão; những khó khăn, hạn chế trong ứng phó siêu bão và tìm kiếm cứu nạn.
- Xây dựng, nâng cao nhận thức, trách nhiệm, ý chí quyết tâm cho cán bộ, CNVC, lao động sẵn sàng nhận và hoàn thành xuất sắc mọi nhiệm vụ được giao, chống tư tưởng ngại khó khăn gian khổ, thoái thác nhiệm vụ, tích cực tham gia khắc phục hậu quả thiên tai tại đơn vị và phối hợp với cấp ủy, chính quyền địa phương trên địa bàn đứng chân tham gia cứu trợ thảm họa, giúp đỡ nhân dân khắc phục hậu quả siêu bão theo phương châm “4 tại chỗ” và “Tích cực, chủ động, ứng phó nhanh, có hiệu quả, giảm thiểu thiệt hại thấp nhất về người và tài sản”, bảo đảm an toàn tuyệt đối về người, trang thiết bị, hệ thống kho tàng, cơ sở vật chất phục vụ sản xuất kinh doanh, doanh trại, công trình phòng, chống mưa bão của đơn vị. 
- Lãnh đạo, chỉ đạo thực hiện nghiêm kỷ luật dân vận, mệnh lệnh của cấp trên, quy tắc về bảo đảm an toàn trong thực hiện nhiệm vụ; làm tốt công tác bảo vệ chính trị nội bộ, bảo vệ bí mật, bảo đảm an ninh, an toàn; quản lý chặt chẽ quân số, vũ khí, trang bị, phương tiện, vật liệu nổ...chăm lo bảo đảm tốt đời sống vật chất, tinh thần và thực hiện đúng các chế độ, chính sách đối với cán bộ, CNVC, lao động trong đơn vị, nhất là cán bộ, người lao động bị thương, hy sinh trong khi làm nhiệm vụ phòng, chống, khắc phục hậu quả thiên tai, thảm họa, dịch bệnh, cứu hộ - cứu nạn. 
- Chỉ đạo tổ chức tốt việc sơ, tổng kết rút kinh nghiệm ở các cấp trong phòng, chống, khắc phục hậu quả thiên tai, thảm họa, dịch bệnh, cứu hộ - cứu nạn; bổ sung giải pháp thực hiện nhiệm vụ tốt hơn trong thời gian tới. Kịp thời biểu dương, khen thưởng những tập thể, cá nhân có thành tích tốt; xử lý nghiêm những trường hợp vi phạm (nếu có).
Tình huống 06: Trong quá trình thực hiện nhiệm vụ giúp đỡ Nhân dân địa phương khắc phục hậu quả thiên tai gây ra, có hai chiến sĩ trong đại đội tổ chức uống rượu sau đó gây gổ mất đoàn kết với một số thanh niên địa phương và bị thương phải đưa đi điều trị tại bệnh viện.
Gợi ý biện pháp xử lý:
- Trao đổi nhanh trong chỉ huy đại đội, thống nhất biện pháp xử lý và phân công cán bộ phụ trách giải quyết vụ việc, đưa chiến sĩ đi bệnh viện điều trị.
- Báo cáo cấp trên xin ý kiến chỉ đạo và đề nghị cử cán bộ và cơ quan chức năng phối hợp với đơn vị để giải quyết vụ việc.
- Gặp gỡ các nhân chứng của vụ việc để nắm lại tình hình vụ việc cụ thể.
- Cùng với cấp trên và cơ quan chức năng làm việc với chính quyền và cơ quan chức năng địa phương để tiến hành các biện pháp giáo dục số thanh niên có liên quan đến vụ việc xảy ra.
- Cử cán bộ thăm hỏi, động viên chiến sĩ nằm viện, nắm bắt tình hình tư tưởng, tâm trạng của bộ đội.
- Tiến hành xem xét, kiểm điểm và xử lý kỷ luật đối với các chiến sĩ vi phạm và cán bộ liên đới trách nhiệm theo đúng quy định của Bộ Quốc phòng sau khi chiến sĩ ra viện.
- Tổ chức sinh hoạt đơn vị để giáo dục, định hướng tư tưởng, dư luận, kịp thời rút kinh nghiệm chung trong toàn đơn vị về các yêu cầu khi thực hiện nhiệm vụ phòng, chống, khắc phục thiên tai và việc chấp hành kỷ luật dân vận, giữ gìn phẩm chất “Bộ đội Cụ Hồ”.
- Tổng hợp báo cáo cấp trên về kết quả giải quyết và xử lý vụ việc theo quy định.
Tình huống 07: Ban CHQS huyện giao nhiệm vụ cho một quân nhân phụ trách xã cùng một số quân nhân khác trong đơn vị phối hợp với Ban CHQS xã hỗ trợ nhân dân ven đê đang bị sạt lở và có nguy cơ vỡ bối đê do mưa lớn kéo dài, nước trên thượng nguồn xả lớn đã có biểu hiện băn khoăn, lo lắng và sợ nguy hiểm muốn thoái thác nhiệm vụ.
Gợi ý biện pháp xử lý:
- Trao đổi chỉ huy, thống nhất biện pháp, đánh giá cụ thể tư tưởng, những khó khăn, lo lắng của quân nhân khi được phân công phụ trách xã và tham gia phòng, chống thiên tai, tìm kiếm cứu nạn nơi khó khăn để thống nhất biện pháp giải quyết và phân công cán bộ phụ trách, theo dõi.
- Gặp gỡ trực tiếp động viên, giải thích cho quân nhân hiểu rõ vị trí, vai trò, chức năng, nhiệm vụ của quân đội (là đội quân công tác); tinh thần đoàn kết, kết quả thực hiện nhiệm vụ của cơ quan, đơn vị và của Đảng, nhà nước, nhân dân ta trong những năm qua; tính nguy hiểm của thiên tai bão lụt, nếu không được khắc phục, phòng chống kịp thời đối với nhân dân địa phương và chính cơ quan, đơn vị mình công tác.
- Sinh hoạt đơn vị, tổ chức giáo dục, quán triệt cho cán bộ, nhân viên những văn bản chỉ đạo của Trung ương và địa phương quyết tâm đoàn kết, chung sức, đồng lòng thi đua phòng, chống lụt bão, giảm nhẹ thiên tai, tìm kiếm cứu nạn, góp phần nâng cao ý thức trách nhiệm của mỗi quân nhân; nhất là tinh thần tự giác noi gương quyết tâm bảo vệ tính mạng, tài sản hoa màu của nhà nước và nhân dân trước nguy cơ lũ lụt.
- Quan tâm chăm lo, bảo đảm tốt chế độ chính sách, tiêu chuẩn cho quân nhân yên tâm, gắn bó với cơ quan với nhiệm vụ được phân công.
- Tổ chức sinh hoạt rút kinh nghiệm kịp thời sau mỗi lần cử cán bộ, nhân viên tham gia thực hiện những nhiệm vụ khó khăn, phức tạp nhất là tham gia nhiệm vụ phòng chống thiên tai, cứu hộ, cứu nạn.
Tình huống 08: Khi đơn vị có lệnh dự báo của cấp trên chuẩn bị lực lượng, phương tiện tham gia cứu hộ, cứu nạn một số chiến sĩ có biểu hiện lo sợ khi nhìn thấy hình ảnh các cán bộ, chiến sĩ hi sinh trong thực hiện nhiệm vụ cứu hộ, cứu nạn nên đã lấy lý do sức khỏe yếu, xin đi điều trị khám bệnh để không phải tham gia đã tác động xấu đến nhận thức về nhiệm vụ của một số đồng chí khác.
Gợi ý biện pháp xử lý:
- Nhanh chóng hội ý trao đổi, thống nhất trong chỉ huy về phương án giải quyết.
- Báo cáo cấp trên xin ý kiến chỉ đạo.
- Tiến hành kiểm tra sức khỏe của chiến sĩ. Nếu ốm thật, đề nghị quân y kiểm tra mức độ bệnh tình chăm sóc điều trị chu đáo, thay thế đồng chí khác tham gia.
- Nắm lại tình hình tư tưởng của số hạ sĩ quan, chiến sĩ sau sự việc hi sinh của một số cán bộ, chiến sĩ trong thực hiện nhiệm vụ tìm kiếm cứu hộ cứu, cứu nạn. Trường hợp một số đồng chí có tư tưởng trốn tránh nhiệm vụ thì trực tiếp gặp gỡ, nắm nguyên nhân tại sao đồng chí đó lo sợ. Chú ý: phương pháp nắm bắt phải khéo léo, mềm dẻo thông qua tâm sự, trò chuyện để nắm bắt tâm tư, tình cảm, vướng mắc của chiến sĩ.
- Hội ý cấp ủy, chỉ huy đơn vị, thống nhất các biện pháp giải quyết (trong hội ý cán bộ đơn vị phản ánh, báo cáo tình hình tư tưởng, tâm trạng của số hạ sĩ quan, chiến sĩ có biểu hiện băn khoăn, lo lắng).
- Trực tiếp gặp gỡ số hạ sĩ quan, chiến sĩ có biểu hiện băn khoăn, lo lắng phân tích cho bộ đội hiểu được nguyên nhân vụ việc là rất hiếm, động viên bộ đội an tâm thực hiện nhiệm vụ.
- Tổ chức cho bộ đội xem phim tư liệu về công tác tham gia cứu hộ cứu nạn của Quân đội nói chung và của đơn vị nói riêng trong những năm gần đây để bộ đội yên tâm, tin tưởng vào khả năng lãnh đạo, chỉ đạo thực hiện nhiệm vụ tìm kiếm, cứu hộ, cứu nạn của đơn vị.
- Tổ chức sinh hoạt đơn vị, giáo dục định hướng tư tưởng cho bộ đội, xác định vinh dự và trách nhiệm của người quân nhân cách mạng, phát huy phẩm chất “Bộ đội cụ Hồ”, khi được phân công nhiệm vụ ở những nơi nguy hiểm, vất vả, thậm chí phải hi sinh vì tính mạng, tài sản của nhân dân trước thiên tai, bão lũ. Xây dựng niềm tin vào trang bị, phương tiện cứu hộ, cứu nạn, bản lĩnh, ý chí, trình độ, kỹ năng xử lý của cán bộ, chiến sĩ đơn vị trong thực hiện nhiệm vụ cứu hộ cứu nạn. 
- Chỉ đạo chi đoàn tổ chức các hoạt động diễn đàn, tọa đàm về ý nghĩa, trách nhiệm của quân đội trong tham gia tìm kiếm, cứu hộ, cứu nạn...
- Sau khi hoàn thành nhiệm vụ hướng dẫn chỉ đạo tiểu đội, trung đội sinh hoạt rút kinh nghiệm về công tác quản lý tư tưởng bộ đội; xây dựng động cơ, trách nhiệm trong sẵn sàng thực nhiệm vụ cứu hộ, cứu nạn; biểu dương, khen thưởng kịp thời những tập thể, cá nhân có thành tích xuất sắc và phê bình, nhắc nhở những đồng chí thoái thác, ngại khó, ngại khổ… từ đó động viên chiến sĩ phát huy truyền thống của đơn vị dũng cảm, tích cực tham gia thực hiện nhiệm vụ.
- Tổ chức phân công cán bộ đơn vị tiếp tục theo dõi, kèm cặp, giúp đỡ, ổn định tư tưởng, tâm lý cho quân nhân.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 09: Phòng chống cháy rừng trong điều kiện thời tiết khắc nghiệt, vất vả, một số đồng chí có biểu hiện lo lắng, mệt mỏi, chán nản muốn thoái thác nhiệm vụ.
Gợi ý biện pháp xử lý:
	- Nắm vững tình hình tâm tư, nguyện vọng của chiến sĩ làm việc trong điều kiện khó khăn, vất vả tham mưu cho cấp ủy, chỉ huy có biện pháp khắc phục.
	- Hội ý cấp ủy, chỉ huy đánh giá tình hình tư tưởng, kỷ luật trong đơn vị đặc biệt là những đồng chí được giao nhiệm vụ phòng, chống cháy rừng. Thống nhất biện pháp giải quyết và phân công cán bộ phụ trách.
	- Gặp gỡ, động viên và giáo dục cho chiến sĩ được giao nhiệm vụ hiểu rõ về nhiệm vụ “Chiến đấu trong thời bình” vinh dự, trách nhiệm của chiến sĩ khi được giao nhiệm vụ và xây dựng quyết tâm, ý thức trách nhiệm khắc phục mọi khó khăn để thực hiện nhiệm vụ. Làm tốt công tác tuyên truyền về truyền thống cách mạng, chức năng, nhiệm vụ Quân đội, gương người tốt, việc tốt.
	- Tổ chức bồi dưỡng thêm một số kinh nghiệm, kỹ năng cho chiến sĩ khi thực hiện nhiệm vụ phòng chống, cháy rừng nhằm đảm bảo an toàn và hoàn thành tốt nhiệm vụ.
	- Làm tốt công tác chuẩn bị mọi mặt cho thực hiện nhiệm vụ và quan tâm đảm bảo chế độ tiêu chuẩn cho chiến sĩ yên tâm thực hiện nhiệm vụ.
	- Chỉ đạo Chi đoàn tổ chức diễn đàn Thanh niên với nhiệm vụ “Chiến đấu trong thời bình”.
	- Tổng hợp tình hình tư tưởng chiến sĩ trước khi thực hiện nhiệm vụ báo cáo cấp trên. 
Tình huống 10: Đơn vị chuẩn bị thực hiện nhiệm vụ cứu nạn do bão gây sạt lở ở địa bàn khó khăn, phức tạp, phân tán lực lượng; cán bộ, chiến sĩ có biểu hiện dao động về tư tưởng và xuất hiện tình trạng báo ốm.
Gợi ý biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy đơn vị nhận định tình hình, xác định chủ trương, biện pháp giải quyết.
- Triển khai cho quân y khám sàng lọc bệnh tình của các quân nhân báo ốm đau để xác định rõ nguyên nhân. 
- Nhanh chóng tổ chức sinh hoạt quán triệt, giáo dục nâng cao nhận thức cho cán bộ, chiến sĩ trong đơn vị hiểu sâu sắc về mục đích, ý nghĩa, yêu cầu và tầm quan trọng của nhiệm vụ cứu hộ cứu nạn; kết quả hoàn thành nhiệm vụ của đơn vị thời gian qua; thấy rõ niềm vinh dự, tự hào khi được chỉ huy cấp trên tin tưởng giao nhiệm vụ cho đơn vị.
- Đánh giá, phân loại tư tưởng cán bộ, chiến sĩ; phân công cán bộ gặp gỡ để nắm chắc tình hình và động viên bộ đội hiểu rõ nhiệm vụ; kịp thời ngăn chặn những biểu hiện tư tưởng ngại khó, ngại khổ… chủ động định hướng, giải quyết, ổn định tình hình đơn vị.
- Phân công cán bộ có trình độ, năng lực, phẩm chất đạo đức, tình thần trách nhiệm tốt chỉ huy, phụ trách những nhiệm vụ khó khăn, phức tạp để làm gương cho cán bộ, chiến sĩ yên tâm và noi theo.
- Phát huy tốt hoạt động của chiến sĩ bảo vệ, duy trì sinh hoạt tổ, tiểu đội, thông qua đó tìm hiểu sâu về nguyên nhân báo ốm của quân nhân.
- Phối hợp với gia đình, người thân cùng với đơn vị tăng cường các biện pháp giáo dục, quản lý bộ đội, chống hiện tượng giả bệnh trốn tránh nhiệm vụ.
- Đẩy mạnh các hoạt động tuyên truyền cổ động trong thực hiện nhiệm vụ; thường xuyên gần gũi bộ đội, nắm chắc tâm tư tình cảm và chia sẻ những khó khăn vất vả, nhưng cũng là vinh dự tự hào khi được thực hiện nhiệm vụ.
- Duy trì chặt chẽ nền nếp sinh hoạt đơn vị (rút kinh nghiệm, chấn chỉnh những sai phạm; chủ động làm công tác tư tưởng; quản lý chặt chẽ tình hình mọi mặt của đơn vị không để dư luận xấu xảy ra trong đơn vị).
- Biểu dương các cá nhân, tập thể nhân rộng điển hình tiên tiến hoàn thành tốt nhiệm vụ trong thời gian qua.
Tình huống 11: Trong đơn vị có chiến sỹ lái xe sau khi nhận nhiệm vụ đi vận chuyển hàng cứu trợ do mưa bão, sạt lở đất ở các tỉnh Miền trung đã nảy sinh tư tưởng không muốn thực hiện nhiệm vụ, tác động xấu đến nhận thức về nhiệm vụ của một số chiến sỹ lái xe khác.
¬Gợi ý biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy đơn vị nhận định tình hình, đánh giá tính chất, tác hại, nguyên nhân, mức độ ảnh hưởng để trao đổi thống nhất trong chỉ huy và báo cáo cấp trên xin ý kiến chỉ đạo.
- Phân công cán bộ động viên đồng chí đó; thu thập thông tin, phân tích, kết luận nguyên nhân đồng chí đó không muốn thực hiện nhiệm vụ vận chuyển.
- Tiến hành gặp gỡ quân nhân đó nắm thực chất lý do, nguyên nhân; nếu trường hợp quân nhân đó đang có việc gia đình quan trọng cần về để giải quyết thì cắt cử đồng chí khác thực hiện nhiệm vụ thay thế; nếu do phân công cắt cử chưa khoa học, hoặc do cường độ vận chuyển quá mức, hoặc do sức khỏe không đáp ứng được thì phải điều chỉnh lại cho phù hợp.
- Trường hợp quân nhân ngại đi vận chuyển thì trực tiếp gặp gỡ, nắm nguyên nhân, đồng thời giáo dục cho bộ đội nhận thức sâu sắc trách nhiệm, vinh dự tự hào khi được đơn vị lựa chọn đi thực hiện nhiệm vụ.
- Nếu quân nhân nảy sinh tư tưởng do ngại khó, ngại khổ, sợ vất vả nguy hiểm nên không muốn thực hiện nhiệm vụ vận chuyển mà chỉ huy các cấp đã quán triệt, giáo dục, động viên thì chỉ định dừng thực hiện nhiệm vụ, cử người khác thay thế và tổ chức sinh hoạt kiểm điểm xử lý kỷ luật theo điều lệnh, quy định của quân đội và pháp luật Nhà nước.
- Phát huy vai trò của Chi đoàn, HĐQN và các mối quan hệ bạn bè, đồng hương, người thân, gia đình để giáo dục, động viên chiến sỹ có nhận thức tốt về nhiệm vụ, tích cực tham gia các nhiệm vụ vận chuyển.
- Hướng dẫn chỉ đạo đơn vị sinh hoạt rút kinh nghiệm về công tác quản lý tư tưởng và chấp hành kỷ luật; xây dựng động cơ, trách nhiệm trong nhiệm vụ vận chuyển; phát động thi đua trong vận chuyển .…Động viên chiến sỹ tích cực tham gia.
- Tiếp tục theo dõi, quan tâm, động viên, củng cố lòng tin đối với các quân nhân thực hiện nhiệm vụ và nhất là đồng chí có biểu hiện nảy sinh tư tưởng không muốn thực hiện nhiệm vụ nơi khó khăn, vất vả.
- Kịp thời biểu dương tập thể, cá nhân có thành tích trong vận chuyển, làm tốt công tác nhân rộng điển hình tiên tiến; tổ chức rút kinh nghiệm đối với đội ngũ cán bộ về quá trình xử lý.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 12: Đơn vị nhận được lệnh đi cứu hộ, cứu nạn tàu ngư dân gặp nạn trên biển do áp thấp nhiệt đới gần bờ, một số cán bộ, chiến sĩ hoang mang, lo lắng?
Gợi ý biện pháp xử lý:
- Cấp ủy, chỉ huy đơn vị trực tiếp nắm tình hình tâm tư, nguyện vọng của cán bộ, chiến sĩ trực tiếp tham gia thực hiện nhiệm vụ cứu hộ, cứu nạn. 
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật của cán bộ, chiến sĩ trong thực hiện nhiệm cứu hộ, cứu nạn tàu ngư dân gặp nạn trên biển. Thống nhất biện pháp giải quyết, phân công cán bộ phụ trách.
- Gặp gỡ giáo dục, động viên những cán bộ, chiến sĩ có tâm lý lo lắng trong thực hiện nhiệm vụ khó khăn phức tạp hiểu rõ vinh dự, trách nhiệm, quyền lợi, nghĩa vụ, xây dựng ý chí quyết tâm hoàn thành tốt nhiệm vụđược giao.
- Thường xuyên làm tốt công tác quán triệt, giáo dục về tính chất, đặc điểm của nhiệm vụ cho cán bộ, chiến sĩ nâng cao ý thức trách nhiệm, khắc phục khó khăn trong thực hiện nhiệm vụ.
- Tổ chức bồi dưỡng kinh nghiệm cho những cán bộ, chiến sĩ mới tham gia thực hiện nhiệm vụ lần đầu, xây dựng niềm tin vào khả năng bản thân, đơn vị và tình trạng kỹ thuật phương tiện tàu thuyền của đơn vị có đủ khả năng hoàn thành tốt nhiệm vụcứu hộ, cứu nạn trên biển.
- Thường xuyên bảo đảmcác trang thiết bị có độ an toàn cao phục vụ cho công tác cứu hộ, cứu nạn; thực hiện đúng nguyên tắc bảo đảm an toàn trong suốt quá trình thực hiện nhiệm vụ.
- Quan tâm bảo đảm tiêu chuẩn, chế độ chính sách cho cán bộ, chiến sĩ yên tâm, gắn bó với nhiệm vụ.
- Kết thúc nhiệm vụ làm tốt công tác rút kinh nghiệm, kịp thời biểu dương khen thưởng những tập thể, cá nhân hoàn thành tốt nhiệm vụ. Thẳng thắn chỉ ra những hạn chế tồn tại.
- Tổ chức sinh hoạt rút kinh nghiệm sau mỗi lần thực hiện nhiệm vụ cứu hộ, cứu nạn để cho cán bộ, chiến sĩ tự tin với nhiệm vụ.
Tình huống 13: Do mưa bão lâu dài nên Điểm cao sau nhà ở đơn vị bị sụt lở và có nhiều đường nứt, có thể gây nguy hiểm nên một số cán bộ, chiến sĩ có biểu hiện tư tưởng băn khoăn, lo lắng.
Gợi ý biện pháp xử lý: 
- Thông báo ngay cho các đơn vị nhanh chóng cơ động về về tạm trú tại vị trí an toàn.
- Báo cáo tình hình về Thủ trưởng cấp trên (thông qua trực ban tác chiến, trực ban cơ quan cấp trên); đồng thời, xin ý kiến chỉ đạo của Thủ trưởng cấp trên.
- Triển khai cho đơn vị làm tốt công tác giáo dục chính trị tư tưởng, giáo dục quán triệt tác hại của sự sụt lỡ và những thuận lợi, khó khăn trong công tác phòng, chống thiên tai, bão lụt, tìm kiếm cứu nạn; xây dựng ý chí quyết tâm cho cán bộ, chiến sỹ tích cực chủ động làm tốt công tác chuẩn bị sẵn sàng nhận và hoàn thành mọi nhiệm vụ được giao.
- Thường xuyên nắm tình hình đơn vị mình, nhất là những đơn vị bị ảnh hưởng; kịp thời động viên CB,CS an tâm tư tưởng, bình tĩnh, không giao động, lo sợ; Tập trung triển khai làm tốt công tác chuẩn bị, theo phương châm 4 tại chỗ, trước hết là chuẩn bị lực lượng, cơ sở vật chất, phương tiện, trang bị…
- Tiến hành kiểm tra, khảo sát khu vực, nhất là các vị trí trọng điểm về chất đất, những nơi có biểu hiện nứt, dễ sụt lỡ ….đề xuất biện khắc phục
- Dự kiến khu vực sơ tán người, tài sản đơn vị, cá nhân và xác định bãi đỗ phương tiện tham gia cứu hộ cứu nạn…
- Thông báo cho cấp ủy và chính quyền địa phương trên địa bàn để phối hợp trong xử lý tình hình; đồng thời tuyên truyền đưa tin hoạt động của cán bộ, chiến sỹ tham gia khắc phục sạt lỡ 
- Sau khi hoàn thành nhiệm vụ:
+ Nhanh chóng tổng hợp tình hình báo cáo nhanh cấp trên theo phân cấp; 
+ Hướng dẫn, chỉ đạo các cơ quan, đơn vị nắm diễn biến tình hình tư tưởng CB, CS, tổ chức hội nghị rút kinh nghiệm kịp thời biểu dương, khen thưởng những tập thể cá nhân có thành tích xuất sắc trong tham gia khắc phục hậu quả thiên tai, đồng thời phê bình, nhắc nhỡ những tập thể cá nhân có biểu hiện hoang mang, lo sợ không hoàn thành nhiệm vụ khi được phân công.
+ Bám sát diễn biến tình hình, phát hiện giải quyết kịp thời những biểu hiện ngại khó khăn, gian khổ, giảm sút ý chí, tư tưởng giao động; tổ chức tốt phong trào thi đua và thực hiện tốt công tác chính sách đối với cán bộ, chiến sỹ trong đơn vị.
+ Bổ sung hoàn thiện kế hoạch CTĐ, CTCT trong phòng chống thiên tai, cứu hộ cứu nạn.
Tình huống 14: Trong đơn vị có gia đình một đồng chí hạ sĩ quan (chiến sĩ) gặp mưa bão, nhà cửa bị đất đá sạt lở vùi lấp, không bị thiệt hại về người, có biểu hiện hoang mang, lo lắng
Gợi ý biện pháp xử lý:
- Nắm chắc tâm tư, hoàn cảnh cụ thể gia đình quân nhân thông qua các nguồn tin các mối quan hệ của quân đó (các cấp báo cáo) từ đó xác định biện pháp cách thức giải quyết.
- Tiến hành gặp gỡ, trò chuyện, nắm tâm tư, nguyện vọng, những vướng mắc của quân nhân có hoàn cảnh khó khăn; từ đó động viên, chia sẻ, giúp đỡ quân nhân đó vượt qua khó khăn, yên tâm công tác xác định rõ nhiệm vụ.
- Báo cáo chỉ huy cấp trên để cùng theo dõi động viên xác định biện pháp giải quyết.
- Chỉ đạo trung đội (đại đội) có quân nhân gặp hoàn cảnh khó khăn phân công cán bộ, đảng viên, đoàn viên ưu tú theo dõi, động viên giúp đỡ quân nhân có gia đình gặp khó khăn hoàn thành nhiệm vụ.
- Chỉ đạo đơn vị có biện pháp tác động với những quân nhân khác là bạn bè thân thiết, đồng hương… với chiến sĩ gặp khó khăn để cùng chia sẻ, động viên, an ủi.
- Trường hợp (xét thấy cần thiết) đề nghị cấp có thẩm quyền giải quyết cho quân nhân đi phép về giải quyết việc gia đình.
- Đề nghị tập thể đơn vị và chỉ huy cấp trên quan tâm động viên giúp đỡ chiến sĩ gặp khó khăn về vật chất và tinh thần để góp phần giải quyết khó khăn (đề nghị trợ cấp khó khăn cho quân nhân đó theo quy định).
- Nếu có điều kiện đề nghị chỉ huy cấp trên cử cán bộ về thăm hỏi, động viên gia đình quân nhân đó.
Tình huống 15: Khi đơn vị thực hiện nhiệm vụ giúp Nhân dân chữa cháy rừng do điều kiện gió to, không may một chiến sĩ bị bỏng nặng gây tâm lý hoang mang, lo lắng đối với cán bộ, chiến sĩ trong đơn vị.
Gợi ý các biện pháp xử lý:
- Nhanh chóng bằng mọi biện pháp tiến hành sơ cứu cho chiến sĩ bị bỏng (đúng quy trình sơ cứu ban đầu, không để nặng thêm) và đưa đến bệnh viện gần nhất để kịp thời cứu chữa.
- Trao đổi, thống nhất nhanh trong chỉ huy đơn vị, phân công cán bộ phụ trách trên từng vị trí.
- Tổng hợp tình hình báo cáo cấp trên đúng quy định.
- Động viên cán bộ, chiến sĩ bình tĩnh, thực hiện tốt các quy định về công tác bảo đảm an toàn, tiếp tục thực hiện nhiệm vụ chữa cháy rừng.
- Tập trung lực lượng, phương tiện tạo ranh giới lửa để đám cháy không lan rộng xung quanh, nếu cần thiết đề nghị hỗ trợ thêm lực lượng, phương tiện để dập tắt đám cháy.
- Khi đám cháy được dập tắt, tổ chức thu quân, kiểm tra lại tình hình mọi mặt, cơ động về đơn vị tiến hành sinh hoạt rút kinh nghiệm về tổ chức thực hiện nhiệm vụ và công tác bảo đảm an toàn.
- Vận động cán bộ, chiến sĩ thực hiện tinh thần tương thân, tương ái giúp đỡ đồng đội bị bỏng, cử cán bộ thăm hỏi động viên chiến sĩ nằm viện.
- Phối hợp với cơ quan chức năng của địa phương, đơn vị thực hiện tốt công tác chính sách đối với quân nhân gặp nạn trong quá trình thực hiện nhiệm vụ.
- Tổng hợp tình hình mọi mặt báo cáo cấp trên.
Tình huống 16: Trong quá trình thực hiện nhiệm vụ giúp đỡ Nhân dân phòng, chống lụt bão, không may một chiến sĩ bị hy sinh gây hoang mang, lo lắng trong đơn vị 
Gợi ý biện pháp xử lý:
- Cán bộ trực tiếp chỉ huy nhanh chóng tổ chức cứu chữa cho chiến sĩ bị hy sinh (nếu còn cơ hội), đưa chiến sĩ bị hy sinh lên vị trí an toàn, nắm tình hình báo cáo chỉ huy cấp trên.
- Nhanh chóng hội ý, thống nhất trong cấp ủy, chỉ huy đơn vị đánh giá tình hình, xác định nguyên nhân ban đầu và biện pháp xử lý.
- Tiến hành thông báo ngay cho gia đình (thân nhân) chiến sĩ hy sinh.
- Phối hợp chặt chẽ với các cấp tiến hành điều tra, kết luận và làm rõ nguyên nhân xảy ra mất an toàn khi thực hiện nhiệm vụ; thống nhất biện pháp giải quyết hậu quả.
- Đội ngũ cán bộ các cấp tiếp tục bám sát quá trình thực hiện nhiệm vụ của đơn vị, động viên, nhắc nhở bộ đội ổn định tư tưởng, tâm lý; không để bộ đội hoảng loạn, lo lắng, gây xáo trộn trong các bộ phận.
- Phối hợp với địa phương tiến hành giải quyết hậu quả theo đúng quy định, đúng chức năng, nhiệm vụ, quyền hạn và điều kiện thực tế của đơn vị.
- Động viên cán bộ, chiến sĩ trong đơn vị bằng vật chất, tinh thần chia sẻ, giúp đỡ với gia đình chiến sĩ hy sinh; phối hợp cùng gia đình tổ chức lễ mai táng chu đáo, đúng phong tục, tập quán của địa phương.
- Tổ chức sinh hoạt cấp ủy, chi bộ, đội ngũ cán bộ và đơn vị để thông báo kết luận điều tra của cấp trên; kiểm điểm làm rõ trách nhiệm, rút ra bài học kinh nghiệm trong công tác lãnh đạo, chỉ đạo và tổ chức thực hiện nhiệm vụ của đơn vị trong thời gian tiếp theo để bảo đảm an toàn tuyệt đối; xem xét trách nhiệm và tiến hành xử lý kỷ luật đối với cán bộ chỉ huy trực tiếp và liên đới trách nhiệm.
- Thực hiện tốt các chế độ, chính sách đối với quân nhân hy sinh khi thực hiện nhiệm vụ.
- Tổng hợp tình hình giải quyết vụ việc báo cáo cấp trên theo quy định.
II. NHÓM TÌNH HUỐNG TƯ TƯỞNG CÓ THỂ NẢY SINH TRONG THỰC HIỆN NHIỆM VỤ HUẤN LUYỆN, SẴN SÀNG CHIẾN ĐẤU, XÂY DỰNG CHÍNH QUY, RÈN LUYỆN KỶ LUẬT (10 tình huống)
Tình huống 1. Từ một số vụ việc HSQ-BS (học viên) bị tai nạn trong quá trình đơn vị tổ chức bắn đạn thật, cá biệt đã có quân nhân dùng súng tự sát ngay trong quá trình thực hành bắn, đã gây tâm lý băn khoăn, lo lắng cho một số sĩ quan được giao nhiệm vụ chỉ huy bắn (TH3; QĐ3, TrSQLQ1 2022).
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình, chất lượng huấn luyện và kết quả bắn súng, xác định nguyên nhân, thống nhất biện pháp bồi dưỡng. Báo cáo cấp trên xin ý kiến chỉ đạo.
- Rà soát, phân loại tâm lý, khả năng bắn súng của từng quân nhân; giáo dục, quán triệt làm cho quân nhân nắm vững mục tiêu, yêu cầu, chức trách, nhiệm vụ, qua đó nâng cao ý thức học tập, rèn luyện kỹ năng bắn súng. 
- Phân công cán bộ có kinh nghiệm kèm cặp, giúp đỡ, kỹ năng, phương pháp bắn súng, giúp quân nhân tin tưởng vào khả năng của bản thân, kiên trì luyện tập.
-  Duy trì nghiêm nền nếp chế độ huấn luyện quân sự, kiểm tra bắn súng theo quy định. Thực hiện nghiêm quy trình huấn luyện, tổ chức bắn súng chặt chẽ; chú trọng làm tốt công tác kiểm tra, rà soát, đánh giá toàn diện các yếu tố, có phương án bảo đảm an toàn trong suốt quá trình trước, trong và sau khi thực hành bắn. 
- Bồi dưỡng nâng cao bản lĩnh, kỹ năng tổ chức thực hành bắn cho đội ngũ cán bộ phân đội; luyện tập thuần thục phương án xử trí các tình huống bất chắc, mất an toàn có thể xảy ra.
Tình huống 2. Một số cán bộ (có cả cán bộ chủ trì) trong đơn vị có biểu hiện che giấu khuyết điểm, chạy theo thành tích, thiếu công tâm, khách quan trong giải quyết công việc, gây dư luận không tốt trong đơn vị.
Gợi ý biện pháp xử lý
- Kịp thời rà soát, nắm tình hình tư tưởng của quân nhân trong đơn vị; kịp thời phát hiện những biểu hiện che giấu khuyết điểm, chạy theo thành tích, thiếu công tâm, khách quan trong giải quyết công việc.
- Họp cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật, dư luận của quân nhân; xác định đối tượng, hành vi, hậu quả, nguyên nhân dẫn đến hành vi che giấu khuyết điểm, chạy theo thành tích; thống nhất biện pháp khắc phục.
- Gặp gỡ giáo dục, chấn chỉnh những cá nhân có biểu hiện, hành vi vi phạm; phân tích rõ tác hại, hậu quả của biểu hiện che giấu khuyết điểm, chạy theo thành tích, thiếu công tâm, khách quan là vi phạm quy định của quân đội về chế độ báo cáo, xin ý kiến chỉ thị, vi phạm chế độ trách nhiệm của người chỉ huy, ảnh hưởng chất lượng, kết quả, xây dựng chi bộ TSVM, đơn vị VMTD. 
- Tổ chức sinh hoạt đơn vị giáo dục, tuyên truyền cho SQ, QNCN nhận thức sâu sắc vị trí, ý nghĩa của đánh giá đúng thực chất tình hình đơn vị để xây dựng chi bộ TSVM, đơn vị VMTD; qua đó có biện pháp đấu tranh quan điểm, tư tưởng báo cáo không trung thực, che dấu khuyết điểm, chạy theo thành tích, thiếu công tâm, khách quan trong đơn vị.
- Thực hiện tốt nền nếp tự phê bình và phê bình; phát huy trách nhiệm tự soi, tự sửa của mỗi cấp ủy, tổ chức đảng và mỗi cán bộ, đảng viên; tăng cường kiểm tra, giám sát việc thực hiện nguyên tắc tập trung dân chủ, kỷ luật, kỷ cương, sự đoàn kết, thống nhất nội bộ; tránh dân chủ hình thức, khắc phục cách làm việc tắc trách, trì trệ, hoặc lạm dụng quyền lực xâm phạm nguyên tắc.
- Thực hiện tốt Quy chế dân chủ ở cơ sở, phát huy vai trò giám sát, phản biện của các tổ chức và cá nhân đối với việc thực hiện nguyên tắc của Đảng. 
- Đề cao vai trò của người đứng đầu, cán bộ chủ chốt trong giữ vững và phòng, chống tình trạng xa rời nguyên tắc tập trung dân chủ, nhất là bí thư cấp ủy; nỗ lực học tập, rèn luyện phong cách, phương pháp làm việc dân chủ, khoa học, tạo bầu không khí dân chủ trong tổ chức.
- Cầu thị lắng nghe ý kiến phản ánh về việc thực hiện nguyên tắc tập trung dân chủ ở đơn vị và định kỳ lấy phiếu tín nhiệm của cán bộ các cấp, nhất là người đứng đầu, cán bộ chủ trì, chủ chốt. Phát huy vai trò của tổ chức quần chúng, hội đồng quân nhân và tập thể quân nhân trong việc phản ánh những biểu hiện vi phạm nguyên tắc tập trung dân chủ.
- Tham mưu đề xuất rà soát bổ sung, sửa đổi các quy định, quy chế báo cáo, xin chỉ thị của các tổ chức; khắc, phục biểu hiện che giấu khuyết điểm, chạy theo thành tích, đáp ứng yêu cầu, nhiệm vụ xây dựng đơn vị trong tình hình mới.
- Xây dựng tốt tinh thần đoàn kết trên cơ sở nguyên tắc, quy định, kỷ luật của Đảng, pháp luật Nhà nước, kỷ luật quân đội. Chống mọi biểu hiện lợi ích nhóm, cục bộ, bè phái.
- Duy trì nghiêm chế độ báo cáo, phản ánh tình hình về tư tưởng, kỷ luật bộ đội trong đơn vị, nhất là những khó khăn vướng mắc, có biện pháp giúp đỡ kịp thời; phê bình thẳng thắn đối với cá nhân báo cáo không trung thực, chạy theo thành tích, giải quyết kịp thời mọi tình huống phát sinh và xử lý nghiêm kỷ luật đối với những trường hợp vi phạm.
Tình huống 3. Thực hiện lộ trình thực hiện tổ chức Quân đội nhân dân Việt Nam giai đoạn 2021 - 2030 và những năm tiếp theo, theo đó một số cán bộ có tâm lý băn khoăn về vị trí, đơn vị công tác khi có sự điều chỉnh tổ chức.
Gợi ý biện pháp xử lý
- Tuyên truyền, phổ biến làm cho quân nhân nhận thức sâu sắc chủ trương của Đảng, của QUTW về tổ chức Quân đội nhân dân Việt Nam giai đoạn 2021 - 2030 và những năm tiếp theo; nắm rõ lộ trình, đối tượng, chế độ chính sách..., đồng thuận với đường lối, chủ trương, quan điểm của Đảng, pháp luật Nhà nước, xác định tinh thần, trách nhiệm, sẵn sàng nhận và hoàn thành tốt nhiệm vụ.
- Nắm bắt tâm tư, nguyện vọng, hoàn cảnh, điều kiện gia đình của quân nhân, nhất là đối tượng trong diện điều chỉnh; kịp thời tham mưu, đề xuất biện pháp giải quyết phù hợp với từng đối tượng, đáp ứng yêu cầu nhiệm vụ.
- Bảo đảm đầy đủ tiêu chuẩn, chế độ, chính sách theo đúng quy định của Bộ Quốc phòng, giúp cho các đối tượng trong diện điều chỉnh ổn định cuộc sống gia đình, yên tâm nhận nhiệm vụ.
- Tổng hợp tình hình và báo cáo cấp trên.
Tình huống 4. Một số cán bộ chưa được bố trí công việc phù hợp với nguyện vọng và chuyên môn đào tạo đã phát sinh tâm lý băn khoăn, hoài nghi từ phía gia đình, nên nảy sinh tư tưởng, thiếu yên tâm công tác, chất lượng hoàn thành nhiệm vụ không cao.
Gợi ý biện pháp xử lý
 - Rà soát tình hình tổ chức, biên chế của đơn vị, công tác bố trí sử dụng nguồn nhân lực, nắm chắc số, chất lượng của từng đối tượng, nhất là các vị trí trọng yếu, chuyên ngành chuyên sâu, đào tạo dài hạn…
- Nắm tình hình, tìm hiểu nguyên nhân của việc bố trí lực lượng trái với chuyên ngành đào tạo; tâm tư, nguyện vọng của quân nhân. 
 - Hội ý lãnh đạo, chỉ huy đánh giá thực trạng tình hình biên chế, tổ chức và những vấn đề tư tưởng trong đơn vị, thống nhất biện pháp giải quyết; báo cáo cấp trên xin ý kiến chỉ đạo.
 - Gặp gỡ giáo dục, động viên các quân nhân trong diện bố trí công việc trái với chuyên ngành đào tạo, giúp quân nhân nắm vững tình hình, đặc điểm, yêu cầu, nhiệm vụ, cơ cấu tổ chức biên chế đơn vị và việc sắp xếp một số chức danh chưa phù hợp, qua đó xác định tư tưởng, trách nhiệm, khắc phục khó khăn, hoàn thành tốt nhiệm vụ được phân công.
- Tổ chức sinh hoạt quán triệt, rút kinh nghiệm cho quân nhân nhận thức đúng về yêu cầu tổ chức biên chế của đơn vị, trình độ chuyên môn đào tạo, nâng cao ý thức chấp hành sự phân công công tác của cấp ủy đảng, chỉ huy.
- Tổ chức tập huấn, bồi dưỡng kiến thức, kỹ năng, kinh nghiệm, phương pháp công tác giúp các quân nhân trong diện bố trí công việc trái với chuyên ngành đào tạo có đủ năng lực, đáp ứng yêu cầu nhiệm vụ, yên tâm công tác. 
- Chấp hành nghiêm các quy định về tổ chức biên chế, sử dụng lực lượng; bảo đảm dân chủ, công khai, công bằng, phát huy trình độ năng lực công tác.
- Quan tâm chăm lo đời sống vật, chất tinh thần, chính sách hậu phương quân đội cho QNCN phấn khởi, yêu tâm gắn bó xây dựng đơn vị.
Tình huống 5. Một số cán bộ, nhất là cán bộ trẻ có biểu hiện dựa dẫm vào mối quan hệ với cấp trên và người thân, thiếu rèn luyện phấn đấu, giải quyết mối quan hệ cấp trên, cấp dưới, đồng chí, đồng đội không chuẩn mực, gây bất bình trong đơn vị.
Gợi ý biện pháp xử lý
-Tăng cường giáo dục cho quân nhân toàn đơn vị ý thức chấp hành pháp luật Nhà nước, kỷ luật Quân đội, quy định của đơn vị. Xây dựng ý thức tự rèn luyện phẩm chất đạo đức cách mạng của người quân nhân.
- Gặp gỡ quân nhân giáo dục nhận thức đúng, sai, tác hại của việc dựa dẫm ỷ lại, chấp hành kỷ luật không nghiêm.
- Phối hợp với gia đình, địa phương trong việc động viên quân nhân thực hiện chức trách, nhiệm vụ, ý thức chấp hành kỷ luật.
- Quản lý chặt chẽ quân nhân, dự báo những dấu hiệu vi phạm, kịp thời ngăn chặn.
- Duy trì nghiêm chế độ ngày, tuần.
- Báo cáo cấp trên xin ý kiến chỉ đạo.
Tình huống 6. Từ một số vụ việc cháy, nổ vũ khí, đạn xảy ra ở một số đơn vị, một số cán bộ làm nhiệm vụ quản lý, bảo quản, vũ khí, súng đạn; nhiệm vụ sản xuất thuốc phóng, thuốc nổ, nhất là tại các kho chứa vũ khí, đạn có niên hạn sản xuất lâu năm, đã nảy sinh tư tương băn khoăn, lo lắng.
 Gợi ý biện pháp xử lý
- Nắm chắc tình hình tư tưởng, kỷ luật QNCN, thực trạng trang bị, vũ khí, kỹ thuật, công tác bảo đảm an toàn kho tàng của đơn vị, tham mưu cho cấp ủy, chỉ huy giải quyết. 
- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình, tư tưởng QNCN làm công tác bảo quản, bảo dưỡng vũ khí trang bị kỹ thuật và những yếu tố tác động bảo đảm an toàn kho tàng, thống nhất biện pháp khắc phục.
- Gặp gỡ số QNCN làm công tác bảo quản vũ khí trang bị kỹ thuật, động viên ổn định tư tưởng, tâm lý, tự tin vào khả năng chuyên môn nghiệp vụ, quy trình, nguyên tắc bảo quản, bảo dưỡng, sử dụng súng đạn đã được học tập trang bị.
- Tổ chức tập huấn cho SQ, QNCN về quy trình, quy tắc, phương pháp bảo quản, bảo dưỡng, vũ khí súng đạn, nắm vững tính năng, niên hạn sử dụng các loại vũ khí, tạo tâm lý thoải mái, yên tâm thực hiện nhiệm vụ được giao.
- Làm tốt công tác rà soát phân loại đạn dược theo phân cấp, quá niên hạn sử dụng, báo cáo cấp trên xử lý.
- Thường xuyên tổ chức kiểm tra bổ sung, củng cố trang thiết bị phục vụ cho công tác bảo quản vũ khí, khí tài bảo đảm an toàn.
- Quan tâm chăm lo bảo đảm chế độ, tiêu chuẩn đời sống vật chất, tinh thần theo quy định của quân đội, để cho QNCN yên tâm, gắn bó với nhiệm vụ.
 Tình huống 7. Khi cán bộ kiểm tra gác phát hiện chiến sĩ làm nhiệm vụ gác chấp hành không nghiêm quy định đã có lời nói, hành vi chấn chỉnh thái quá, xúc phạm đến bản thân và gia đình quân nhân, làm cho quân nhân bức xúc hành hung lại cán bộ.
Gợi ý biện pháp xử lý
- Nhanh chóng ngăn chặn chiến sỹ có biểu hiện quấy rối do say rượu, sử dụng lực lượng khống chế, bố trí quân y kiểm tra chăm sóc sức khỏe; triển khai các biện pháp cần thiết ổn định tình hình đơn vị; bố trí chiến sỹ thay thế gác.
- Hội ý chỉ huy đơn vị đánh giá, nhận định tình hình tư tưởng, kỷ luật chiến sỹ và phương pháp quản lý, chỉ huy của đồng chí trung đội trưởng, thống nhất biện pháp giải quyết.
- Triển khai cho cán bộ trung đội trưởng và chiến sỹ viết bản tường trình, bản tự kiểm điểm, sinh hoạt đơn vị phân tích hiểu rõ hạn chế khuyết điểm, hậu quả, tác hại của vi phạm quy định canh phòng, phương pháp quản lý bộ đội của cán bộ, đề nghị hình thức kỷ luật bảo đảm khách quan, chính xác.

- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho cán bộ, chiến sỹ nâng cao ý thức chấp hành nghiêm điều lệnh canh phòng, quy định về uống rượu, bia trong khi thực hiện nhiệm vụ, phương pháp giáo dục, quản lý, chỉ huy bộ đội của đội ngũ cán bộ các cấp.
- Duy trì nghiêm chế độ, nền nếp xây dựng đơn vị chính quy, quản lý chặt chẽ tư tưởng, kỷ luật và các mối quan hệ xã hội của bộ đội để có biện pháp giáo dục khắc phục kịp thời.
- Gặp gỡ đồng chí trung đội trưởng giáo dục, nhận rõ việc làm sai trái, có biện pháp khắc phục, sửa chữa; nâng cao kỹ năng, phương pháp giáo dục, quản lý chỉ huy bộ đội theo đúng quy định quân đội, đơn vị, khắc phục cách xử phạt vi phạm nhân cách quân nhân. 
- Thường xuyên giáo dục cho chiến sỹ nâng cao ý thức, trách nhiệm chấp hành nghiêm kỷ luật quân đội, quy định canh phòng bảo đảm đúng tư thế tác phong quân nhân, bảo đảm an toàn đơn vị và địa bàn đóng quân. 
- Quan tâm chăm lo đời sống vật chất, tinh thần cho chiến sỹ, yên tâm, gắn bó với nhiệm vụ.
 - Báo cáo cấp trên theo quy định.
Tình huống 8. Một chiến sĩ có biểu hiện tự do, phát ngôn thiếu chuẩn mực, chấp hành không nghiêm quy định của đơn vị, bị kiểm điểm, kỷ luật... ảnh hưởng đến tập thể khi phải sinh hoạt nhiều lần; một số chiến sĩ đã bức xúc, hành hung đồng đội.
Gợi ý biện pháp xử lý
- Hội ý cấp ủy, chỉ huy đơn vị nhận định, đánh giá tình hình tư tưởng quân nhân và dư luận trong đơn vị, phân tích làm rõ thực trạng, xác định đối tượng, nguyên nhân vi phạm kỷ luật của hạ sĩ quan - chiến sĩ; thống nhất chủ trương, biện pháp giải quyết.
- Phân công cán bộ gặp gỡ chiến sĩ hay vi phạm kỷ luật để nắm bắt tâm tư, nguyện vọng, nguyên nhân vi phạm khuyết điểm và tác hại của việc mất đoàn kết trong nội bộ; qua đó giáo dục, thuyết phục, nâng cao ý thức tự giác chấp hành kỷ luật quân đội, quy định đơn vị, tích cực tham gia xây dựng đơn vị. Với các quân nhân vi phạm, triển khai viết bản tường trình, kiểm điểm, sinh hoạt đơn vị kiểm điểm và đề nghị hình thức kỷ luật, nghiêm túc, chặt chẽ (nếu đến mức phải xử lý kỷ luật).
- Tổ chức sinh hoạt đơn vị rút kinh nghiệm cho chiến sỹ nâng cao ý thức chấp hành kỷ luật quân đội, quy định đơn vị, tích cực học tập, rèn luyện nâng cao phẩm chất, đạo đức tư cách người quân nhân cách mạng, giữ gìn phẩm chất tốt đẹp "Bộ đội Cụ Hồ”, tình thần đoàn kết giúp đỡ lẫn nhau, xây dựng đơn vị vững mạnh.
- Duy trì nghiêm chế độ nền nếp xây dựng đơn vị chính quy, quản lý chặt chẽ tình hình tư tưởng, kỷ luật và các mối quan hệ xã hội của bộ đội, nhất là trong ngày nghỉ, giờ nghỉ, hoạt động ngoài doanh trại để có biện pháp giáo dục kịp thời.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị; tổ chức tốt hoạt động văn hóa tinh thần, tạo không khí vui tươi, lành mạnh; quan tâm chăm lo đời sống vật chất, tinh thần, kịp thời động viên cán bộ, chiến sĩ yên tâm, gắn bó xây dựng đơn vị. 
	Tình huống 9. Trong đơn vị có một số HSQ-BS chấp hành không nghiêm quy định sử dụng điện thoại của đơn vị, cá biệt có quân nhân khi uống rượu say đã hành hung cán bộ khi bị ngăn cấm sử dụng điện thoại di động.
Gợi ý biện pháp xử lý
- Nhanh chóng bố trí chiến sĩ thay thế làm nhiệm vụ gác; sử dụng lực lượng khống chế, ngăn chặn chiến sĩ có biểu hiện quấy rối do say rượu; chỉ đạo quân y kiểm tra, chăm sóc sức khỏe; triển khai các biện pháp cần thiết ổn định tình hình đơn vị.
- Hội ý chỉ huy đơn vị đánh giá, nhận định tình hình tư tưởng, kỷ luật chiến sỹ và phương pháp quản lý, chỉ huy của đồng chí trung đội trưởng, thống nhất biện pháp giải quyết.
- Triển khai cho cán bộ, chiến sĩ có liên quan viết bản tường trình, kiểm điểm; tổ chức sinh hoạt đơn vị, phân tích làm rõ khuyết điểm, lỗi phạm, tác hại, hậu quả của hành vi hành hung cán bộ và việc sử dụng rượu bia, điện thoại sai quy định; phương pháp, tác phong công tác của của cán bộ; xem xét, đề nghị hình thức kỷ luật bảo đảm khách quan, chính xác.
- Nắm tình hình tư tưởng, việc chấp hành quy định sử dụng rượu bia, điện thoại di động, Internet, mạng xã hội của hạ sĩ quan - binh sĩ, đề xuất các biện pháp giải quyết cho cấp ủy, chỉ huy đơn vị. 
- Thường xuyên giáo dục, quán triệt, tuyên truyền phổ biến nâng cao nhận  thức của cán bộ, chiến sĩ, tự giác chấp hành nghiêm Luật phòng, chống tác hại của rượu, bia và các chỉ thị, quy định, hướng dẫn sử dụng điện thoại di động, Internet, mạng xã hội, nhất là quy định về việc sử dụng điện thoại di động đối với hạ sĩ quan - binh sĩ. Tổ chức các buổi tọa đàm, sân khấu hóa trong các hội thi, hội diễn văn nghệ quần chúng để nâng cao nhận thức cho quân nhân về việc uống rượu, bia say, bê tha và sử dụng điện thoại sai quy định.
- Duy trì nghiêm chế độ, nền nếp xây dựng đơn vị chính quy, quản lý chặt chẽ tư tưởng, kỷ luật và các mối quan hệ xã hội của bộ đội để có biện pháp giáo dục khắc phục kịp thời.
- Phối hợp với địa phương và gia đình hạ sĩ quan - binh sĩ làm tốt công tác quản lý, giáo dục làm cho quân nhân nhận thức đúng và chấp hành quy định của đơn vị về sử dụng điện thoại di động.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị; quan tâm chăm lo đời sống vật chất, tinh thần, kịp thời động viên cán bộ, chiến sĩ yên tâm, gắn bó xây dựng đơn vị; có biện pháp đáp ứng nhu cầu thông tin chính đáng cho hạ sĩ quan - binh sĩ.
- Tổng hợp tình hình, báo cáo cấp trên.
Tình huống 10. Trong đơn vị xảy ra 01 trường hợp chiến sĩ tử vong trong trạng thái treo cổ; đơn vị đã tiến hành các bước giải quyết vụ việc; song do công tác cung cấp thông tin, phối hợp giải quyết chưa chu đáo, chặt chẽ, nên gia đình đã nảy sinh hoài nghi về nguyên nhân, phát tán thông tin, hình ảnh trên mạng xã hội, tạo kẽ hở để các thế lực phản động lợi dụng xuyên tạc chống phá, gây bức xúc dư luận, ảnh hưởng an ninh chính trị, trật tự an toàn xã hội.
Gợi ý biện pháp xử lý
	- Phân công cán bộ có uy tín, kinh nghiệm thay mặt chỉ huy đơn vị, đón tiếp và nắm nguyện vọng của gia đình chiến sĩ.
	- Báo cáo cấp trên xin ý kiến chỉ đạo, mời cơ quan chức năng xuống đơn vị phối hợp giải quyết vụ việc.
	- Trao đổi thống nhất trong cấp uỷ, chỉ huy đơn vị, phân công cán bộ phụ trách giải quyết vụ việc và ổn định tình hình đơn vị 
	- Mời một số cán bộ, chiến sĩ trực tiếp chứng kiến vụ việc và một số chiến sĩ cùng quê với gia đình lên cùng với chỉ huy đơn vị làm việc với gia đình chiến sĩ.
	- Cung cấp cho gia đình một số thông tin về kết quả làm việc của cơ quan chức năng như: Biên bản vụ việc, kết quả giám định pháp y, các chế độ chính sách đơn vị đã chi trả với chiến sĩ và các hoạt động hỗ trợ của cán bộ chiến sĩ đơn vị đối với gia đình (nếu có); trao đổi, chia sẻ cùng gia đình về những đau thương mất mát; cùng với các thành phần trong buổi làm việc, phân tích để gia đình hiểu rõ bản chất sự việc, động viên gia đình tin tưởng vào quy trình giải quyết của đơn vị và các cơ quan chức năng, không nghe theo luận điệu xuyên tạc; phối hợp chặt chẽ với đơn vị để lo hậu sự cho quân nhân theo phong tục, để giảm bớt nỗi khổ đau cho gia đình... (chú ý trong khi làm việc với gia đình cần có biên bản, ghi lại diễn biến, kết quả làm việc và ý kiến của gia đình, tránh về sau gia đình tiếp tục có ý kiến với đơn vị).
	- Phân công cán bộ kịp thời báo cáo xin ý kiến chỉ đạo của cấp trên và cung cấp thông tin, định hướng dư luận; phối hợp chặt chẽ với cấp ủy, chính quyền, các đoàn thể, cơ quan quân sự và những người có uy tín ở địa phương tập trung mọi nỗ lực cao nhất, tiến hành đồng bộ công tác tuyên truyền vận động với các biện pháp khác nhằm ổn định tình hình, giữ vững an ninh chính trị, trật tự an toàn xã hội; giải quyết hậu quả bảo đảm nhanh gọn, đúng nguyên tắc, quy trình, chặt chẽ, chu đáo.
- Tổ chức sinh hoạt đơn vị, thông báo cho cán bộ, chiến sĩ kết quả làm việc của các cơ quan chức năng và gia đình, ổn định tình hình tư tưởng trong đơn vị; rút kinh nghiệm từ vụ giáo dục quân nhân nêu cao ý thức chấp hành kỷ luật, quán triệt và thực hiện nghiêm túc các quy định về bảo đảm an toàn trong thực hiện nhiệm vụ; nắm, hiểu và thực hiện đúng quy trình các bước xử lý các vấn đề tư tưởng nảy sinh, nhất là các vụ việc nghiêm trọng, có tính chất phức tạp, nhạy cảm, dễ bị lợi dụng xuyên tạc, kích động, chống phá.
	
- Chỉ đạo Lực lượng 47 tăng cường nắm tình hình trên không gian mạng để kịp thời phát hiện, đề xuất xử lý các nội dung có liên quan đến vụ việc. Kiên quyết xử lý với những biểu hiện tuyên truyền, xuyên tạc gây hoang mang trong đơn vị.
- Cán bộ các cấp tăng cường công tác kiểm tra nắm chắc tình hình đơn vị, nhất là những nơi có biểu hiện hoang mang, dao động. Phát huy vai trò tổ chức hội đồng quân nhân, chi đoàn thanh niên, chiến sĩ bảo vệ trong việc phân tích, dự báo, đánh giá diễn biến tình hình tư tưởng để động viên giải quyết kịp thời.
- Đề nghị giải quyết các chế độ chính sách đối với quân nhân.
- Tổng hợp tình hình, báo cáo kết quả xử lý lên cấp trên. 
III. NHÓM TÌNH HUỐNG TƯ TƯỞNG CÓ THỂ NẢY SINH TRONG GIẢI QUYẾT MỐI QUAN HỆ ĐỒNG CHÍ ĐỒNG ĐỘI, QUÂN DÂN, GIA ĐÌNH, BẠN BÈ, NAM NỮ (10 tình huống)
Tình huống 1. Trong đơn vị có biểu hiện thiếu thống nhất trong cấp ủy, chỉ huy, gây khó khăn trong công tác lãnh đạo, chỉ đạo triển khai thực hiện nhiệm vụ và xây dựng mối đoàn kết nội bộ, gây dư luận không tốt.
Gợi ý biện pháp xử lý
- Cấp ủy, chỉ huy cấp trên nhận định, đánh giá tình hình, phân công cán bộ dự theo dõi, chỉ đạo các buổi sinh hoạt của cơ quan, đơn vị cấp dưới xảy ra mất đoàn kết nội bộ để nắm tình hình.
- Tiến hành gặp gỡ, trao đổi với cấp ủy, chỉ huy cơ quan, đơn vị để xảy ra mất đoàn kết nội bộ.
- Chỉ đạo tổ chức kiểm tra đột xuất đối với tập thể cấp ủy, cán bộ chủ trì nơi để xảy ra mất đoàn kết nội bộ, làm rõ nguyên nhân, trách nhiệm của tập thể, cá nhân.
+ Nếu mất đoàn kết do bất đồng quan điểm cá nhân thì cấp trên phân tích, định hướng để cấp ủy, chỉ huy cấp dưới thống nhất trong lãnh đạo, chỉ đạo, tổ chức thực hiện nhiệm vụ của cơ quan, đơn vị.
+ Nếu mất đoàn kết do vi phạm nguyên tắc, quy chế làm việc, quy chế lãnh đạo, chỉ huy thì phải chỉ đạo kiểm điểm, kỷ luật theo quy định (tùy theo tính chất sự việc) bảo đảm nghiêm minh, chính xác, kịp thời. 
- Nghiên cứu, đề xuất điều chuyển công tác (Nếu cần thiết).
- Tổ chức hội nghị cơ quan, đơn vị để rút kinh nghiệm, thông báo tình hình và định hướng, thống nhất tư tưởng, nhận thức cho cán bộ, chiến sĩ.
- Tổng hợp tình hình kết quả báo cáo cấp trên.
Tình huống 2. Một số chiến sĩ, nhất là chiến sĩ mới có biểu hiện ngại học, ngại rèn, bộc lộ tâm tư buồn chán qua lời nói, nhật ký (vở học tập,...) những nội dung bất thường: “Tôi lẽ ra không nên sinh ra trên đời này, tôi rất xin lỗi những người tôi làm sai, tôi chỉ mong một ngày tôi sẽ không ở trên đời này”, “Sống tới ngày bắn đạn thật”, “Cuộc đời này không đáng sống”, “Nó không còn quan trọng nữa rồi”, “Họ sẽ không thể nào làm tổn thương tôi được nữa”, “Họ sẽ nhớ về tôi khi tôi ra đi,” hoặc “Bạn sẽ thương tiếc khi tôi ra đi”, “Bạn/gia đình/bạn bè/bạn gái tôi sẽ sống tốt hơn nếu không có tôi”….
Gợi ý biện pháp xử lý
- Tăng cường giáo dục nâng cao nhận thức chính trị tư tưởng; coi trọng phát huy dân chủ gắn với hoàn thiện các quy chế, cơ chế để nắm, quản lý tình hình đơn vị, chất lượng các tổ chức, diễn biến tư tưởng của quân nhân; kết hợp chặt chẽ giáo dục nhận thức với các phong trào hành động để quản lý quân nhân.
- Chủ động, linh hoạt nắm thông tin từ vở học tập, sổ tay chiến sĩ, nhật ký, thiết bị nghe, nhìn cá nhân.
- Phân công cán bộ, đảng viên kèm cặp, giúp đỡ bộ đội. Phát huy vai trò của Chiến sĩ bảo vệ, dân vận, “Tổ 3 người”, “Tổ tư vấn tâm lý, pháp lý”, “Hòm thư góp ý”; khảo sát (điều tra xã hội học) để kịp thời nắm tình hình, tham mưu định hướng tư tưởng, giải quyết những vấn đề tư tưởng nảy sinh.
- Nghiên cứu, tìm hiểu, xác định nguyên nhân khách quan, chủ quan dẫn đến biểu hiện tư tưởng bất thường. Tư vấn về những vấn đề quân nhân gặp phải khó khăn, giải quyết nhanh chóng làm giảm căng thẳng, giải tỏa tâm lý, không để quân nhân bế tắc kéo dài, không lối thoát.
- Thường xuyên quan sát và triệt tiêu những nguy cơ có thể dẫn đến tự tử, tự sát. Tăng cường các biện pháp quản lý không để quân nhân sử dụng rượu, bia, chất kích thích, không để quân nhân có biểu hiện sang chấn tâm lý kéo dài. Tăng cường kiểm tra, quản lý chặt chẽ quân tư trang, vũ khí, cuốc, xẻng, dao, dây các loại, thuốc trừ sâu, thuốc diệt côn trùng, thuốc diệt cỏ…không để cán bộ, chiến sĩ lợi dụng những vật dụng đó nhằm thực hiện hành vi tiêu cực.
- Quân y đơn vị theo dõi chặt chẽ trường hợp quân nhân sau khi được điều trị các bệnh lý có rối loạn tâm thần, rối loạn cảm xúc, trầm cảm.
- Liên hệ địa phương, gia đình, bạn bè của quân nhân để nắm chắc mối quan hệ xã hội của quân nhân và phối hợp giải quyết những khó khăn, vướng mắc mà một mình quân nhân không giải quyết được.
- Duy trì thực chất nền nếp các khâu, các bước công tác quản lý tư tưởng quân nhân: Nắm, dự báo, quản lý, định hướng, giải quyết và đấu tranh tư tưởng;
- Tổ chức các hoạt động phong phú, đa dạng, phù hợp, lôi cuốn cán bộ, chiến sĩ tham gia vào các hoạt động của đơn vị.
- Tổ chức cho quân nhân (có ý định tự tử, tự sát) xem những phim, chương trình có những nhân vật vượt lên chính mình, vượt lên số phận để từng bước định hướng tư tưởng quân nhân.
- Thường xuyên đánh giá mức độ chuyển biến, dự báo xu hướng diễn biến tâm lý, tư tưởng của cán bộ, chiến sĩ để có biện pháp tác động kịp thời.
- Tổng hợp tình hình báo cáo cấp trên.
Tình huống 3. Trong đơn vị có dư luận về việc quân nhân yêu đồng giới, gây tâm lý băn khoăn trong một bộ phận cán bộ, chiến sĩ.
Gợi ý biện pháp xử lý
- Rà soát, đánh giá tình hình đơn vị; xác minh thông tin, đối tượng có biểu hiện yêu đồng giới. Chỉ đạo quân y đơn vị nắm và theo dõi. Tham khảo để hiểu rõ hơn về nguyên nhân và biểu hiện của những người có quan hệ đồng giới.
- Khi đã xác minh được đối tượng, chủ động phối hợp với địa phương và gia đình tìm hiểu nắm rõ điều kiện, hoàn cảnh gia đình mối quan hệ và các biểu hiện tâm sinh lý của quân nhân khi ở gia đình; kết quả sàng lọc, tuyển chọn quân nhân nhập ngũ. 
- Hội ý cấp ủy, nhận định, đánh giá tình hình, xác định chủ trương, biện pháp lãnh đạo làm chuyển biến tình hình, giữ vững ổn định đơn vị. 
- Phân công cán bộ chủ động có biện pháp khéo léo gặp gỡ, trao đổi, nắm bắt tâm tư, nguyện vọng của quân nhân, tìm hiểu bản chất, nguyên nhân; tâm sự, chia sẻ giúp quân nhân hiểu rõ bản chất, tác hại của hành vi. Động viên tích cực tham gia các hoạt động phù hợp với khả năng của cá nhân, đơn vị, giữ gìn phẩm chất, đạo đức, chuẩn mực người quân nhân.
- Phân công cán bộ, đảng viên, tổ tư vấn tâm lý, pháp lý và quần chúng nòng cốt gần gũi, động viên, từng bước giúp quân nhân nhận thức được hành vi không đúng của bản thân. Trong thực hiện nhiệm vụ thường xuyên phân công đồng đội kèm cặp, giúp đỡ; không được gây căng thẳng, kỳ thị tạo sức ép cho quân nhân.
- Không chọc ghẹo để quân nhân mặc cảm.
- Thường xuyên làm tốt công tác giáo dục, quán triệt các quy định của luật hôn nhân, gia đình, quan hệ 01 vợ, 01 chồng; thuần phong mỹ tục của dân tộc… những thông tin liên quan đến tác hại và dư luận lên tiếng về yêu đồng giới để cảnh tỉnh quân nhân, tránh để xảy ra những hệ lụy của hôn nhân. Tổ chức các buổi tọa đàm, sân khấu hóa trong các hội thi, hội diễn văn nghệ quần chúng để nâng cao nhận thức cho quân nhân về hạnh phúc, hôn nhân.
- Ngăn chặn không để lây lan.
- Duy trì nghiêm chế độ ngày, tuần, quản lý quân số và các mối quan hệ của quân nhân. 
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị; quan tâm chăm lo đời sống vật chất, tinh thần, kịp thời động viên cán bộ, chiến sĩ yên tâm, gắn bó xây dựng đơn vị.
- Tổng hợp tình hình báo cáo cấp trên.
	
Tình huống 4: Trong đơn vị có dư luận về việc cán bộ của đơn vị quan hệ nam nữ bất chính với phụ nữ địa phương nơi đóng quân.
- Tiến hành hội ý chỉ huy thống nhất biện pháp giải quyết.
- Điều tra, xác minh cụ thể mối quan hệ bất hợp pháp của quân nhân.
- Gặp gỡ quân nhân nghe trình bày rõ sự việc, giáo dục, động viên nhận rõ khuyết điểm.
- Gặp gỡ người thân, vợ con để tìm cách giải quyết.
- Tổ chức sinh hoạt rút kinh nghiệm, kiểm điểm, kỷ luật theo quy định (tùy theo tính chất sự việc).
- Nghiên cứu, đề xuất điều chuyển công tác (Nếu quân nhân không khắc phục, sửa chữa khuyết điểm).
- Tăng cường làm tốt công tác giáo dục, quán triệt các quy định của luật hôn nhân, gia đình, quan hệ 01 vợ, 01 chồng; quy định những điều đảng viên không được làm; Nghị quyết Trung ương 4 (khóa XII),… những thông tin liên quan đến việc xử lý cán bộ công chức quan hệ bất chính xảy ra trên địa bàn và cả nước để răn đe, hệ lụy của hôn nhân đổ vỡ.
- Tổng hợp tình hình báo cáo cấp trên.
	Tình huống 5. Trong đơn vị có dư luận về trường hợp một chiến sĩ mới nhập ngũ, do nhận được lời chia tay của người yêu nên đã có biểu hiện buồn chán, phát ngôn không chuẩn xác, thiếu tích cực tham gia các hoạt động tập thể, chất lượng hoàn thành nhiệm vụ thấp.
	Gợi ý biện pháp xử lý
- Nắm tình hình, xác minh quan hệ yêu đương của quân nhân qua các bạn đồng khóa đang công tác ở đơn vị, gia đình và bạn gái. Rà soát, nắm bắt những thông tin cá nhân trên mạng xã hội, trang facebook, zalo...
- Hội ý cấp ủy, chỉ huy, thống nhất biện pháp giáo dục, giải quyết.
- Phân công cán bộ,  “Tổ 3 người”, “Tổ tư vấn tâm lý, pháp lý”… gặp gỡ, động viên, tâm sự để quân nhân giãi bày, giải tỏa tâm lý; đồng thời giúp quân nhân có nhận thức đầy đủ, bình tĩnh, từng bước động viên người yêu để cùng nhau vượt qua khó khăn ban đầu, giữ được hạnh phúc lứa đôi. 
- Trao đổi với gia đình quân nhân về tình hình của quân nhân tại đơn vị, để gia đình nắm và phối hợp động viên, chia sẻ.
- Thông qua mối quan hệ bạn bè thân thiết, đồng chí, đồng đội khuyên nhủ, động viên.
- Duy trì nghiêm chế độ nền nếp xây dựng đơn vị chính quy, quản lý chặt chẽ tình hình tư tưởng, kỷ luật và các mối quan hệ xã hội của bộ đội, nhất là trong ngày nghỉ, giờ nghỉ, hoạt động ngoài doanh trại để có biện pháp giáo dục kịp thời.
- Xây dựng bầu không khí dân chủ, đoàn kết, kỷ luật trong đơn vị; tổ chức tốt hoạt động văn hóa tinh thần, tạo không khí vui tươi, lành mạnh; quan tâm chăm lo đời sống vật chất, tinh thần, kịp thời động viên cán bộ, chiến sĩ yên tâm, gắn bó xây dựng đơn vị. 
- Thường xuyên nắm chắc tình hình, báo cáo cấp trên.
	Tình huống 6. Trong đơn vị có cán bộ biểu hiện tư tưởng buồn chán, tiêu cực… vì vợ chồng bất hòa, anh em trong gia đình mất đoàn kết từ việc bố mẹ phân chia đất đai, nhà ở không công bằng, nên thiếu tập trung vào công việc, chất lượng hoàn thành nhiệm vụ thấp.
Gợi ý biện pháp xử lý 
- Hội ý chỉ huy đơn vị thống nhất đánh giá tình hình, phân công cán bộ phụ trách giải quyết tư tưởng. Lưu ý, đây là việc riêng, nhạy cảm của gia đình quân nhân; do đó chủ yếu tác động làm cho quân nhân thuộc quyền hiểu thực chất sự việc, ý kiến đề xuất gia đình "thấu tình, đạt lý ", giữ vững mối quan hệ ruột thịt trong gia đình.
- Gặp quân nhân tìm hiểu, nắm chắc hoàn cảnh gia đình, trước hết là tôn trọng quyết định của bố, mẹ; tổ tư vấn tâm lý pháp luật tuyên truyền cho quân nhân nắm chắc luật thừa kế, luật sở hữu tài sản. Chấp hành nghiêm túc luật thừa kế tài sản theo quy định của pháp luật; động viên quân nhân: vật chất, tài sản là quan trọng nhưng tình cảm gia đình còn quý giá hơn, có tiền cũng không thể mua được; tài sản có thể làm ra nhưng tình cảm gia đình mà mất đi thì rất khó lấy lại được, tình cảm, danh dự là tài sản quý nhất của con người, không bao giờ có thể đánh đổi bằng tiền bạc. Lấy ví dụ, dẫn chứng xác thực để quân nhân nhìn nhận vấn đề, tránh mắc phải khuyết điểm nóng vội, duy ý chí, chỉ thấy cái lợi trước mắt, tức thời mà bỏ quên cái lợi lâu dài... quyết định sai lầm từ vấn đề tranh chấp tài sản có thể dẫn đến mất đoàn kết gia đình khiến quân nhân phải hối hận (nếu đơn vị chưa thành lập tổ tư vấn tâm lý, pháp luật thì chính trị viên tiến hành nội dung này);
- Liên hệ, thông báo với gia đình biết về tư tưởng, tình cảm, nguyện vọng của quân nhân trước việc gia đình phân chia tài sản; đề nghị gia đình phối hợp động viên quân nhân hiểu rõ sự việc, yên tâm thực hiện nhiệm vụ.
- Cử cán bộ theo dõi, động viên quân nhân yên tâm, tư tưởng, tôn trọng bố mẹ (gia đình), chấp hành nghiêm pháp luật, đề cao trách nhiệm, hoàn thành mọi nhiệm vụ được giao.
 	Tình huống 7. Trong đơn vị có trường hợp quân nhân A vay mượn tiền của quân nhân B nhưng thiếu trách nhiệm thực hiện nghĩa vụ trả nợ, giải quyết mối quan hệ không tốt dẫn đến mâu thuẫn, ảnh hưởng không tốt đến đơn vị.
	- Hội ý chỉ huy đánh giá tình hình, báo cáo cấp trên.
	- Cán bộ gặp gỡ quân nhân, nghe quân nhân trình bày hoàn cảnh kinh tế gia đình của quân nhân, mục đích vay tiền và ý định, khả năng trả nợ; quán triệt, giáo dục làm cho quân nhân nhận thức rõ về trách nhiệm của bản thân đối với gia đình và việc trả nợ cho đồng đội; hệ lụy của việc sử dụng tiền không đúng mục đích, không hiệu quả và sự ảnh hưởng đến uy tín cá nhân, tình đồng chí, đồng đội…; bàn biện pháp khắc phục trước mắt, động viên tư tưởng cho quân nhân.
	- Gặp gỡ những người cho quân nhân vay tiền để nắm số tiền vay, gặp gỡ gia đình, nói rõ quan điểm của chỉ huy đơn vị trong việc quản lý, giáo dục quân nhân, đồng thời phối hợp cùng gia đình nắm chắc tình hình tư tưởng, động viên gia đình, khắc phục khó khăn, cùng với quân nhân có trách nhiệm trả nợ và giải quyết tốt mối quan hệ với người cho vay, tránh gây mất đoàn kết.
	- Chỉ huy đơn vị thường xuyên theo dõi diễn biến tư tưởng, hướng trả nợ của quân nhân; đồng thời giáo dục mọi cán bộ, chiến sĩ trong đơn vị rút kinh nghiệm chung, sống có trách nhiệm với hành vi của bản thân, tránh việc vay nợ để tham gia các tệ nạn xã hội với bất kỳ hình thức nào.
	- Nếu mất khả năng chi trả, xử lý kỷ luật đề nghị cho phục viên, thôi việc hoặc xử lý theo pháp luật.
	- Sinh hoạt đơn vị rút kinh nghiệm.
	- Tổng hợp tình hình báo cáo cấp trên.
	Tình huống 8. Trong quá trình nghỉ phép, một cán bộ tham gia giao lưu với một số thanh niên địa phương, do bất đồng nhận thức, quan điểm và tác phong sinh hoạt đã nảy sinh mâu thuẫn, một số người dân địa phương chứng kiến đã quay video và phát tán trên mạng xã hội; đồng chí cán bộ lo lắng vì thông tin trên mạng xã hội sẽ ảnh hưởng tới uy tín Quân đội, đã báo cáo xin ý kiến của chỉ huy đơn vị.
Gợi ý biện pháp xử lý 
- Trao đổi nhanh trong chỉ huy đơn vị, thống nhất biện pháp xử lý và phân công cán bộ phụ trách giải quyết vụ việc 
- Báo cáo cấp trên xin ý kiến chỉ đạo và đề nghị cử cán bộ và cơ quan chức năng phối hợp với đơn vị để giải quyết vụ việc, trước hết là bóc gỡ thông tin nói trên.
- Gặp gỡ đồng chí cán bộ để nắm lại tình hình, yêu cầu báo cáo cụ thể về sự việc và số thanh niên địa phương cùng giao lưu và nguyên nhân mâu thuẫn.
- Cùng với cấp trên và cơ quan chức năng làm việc với chính quyền và cơ quan chức năng địa phương để tiến hành các biện pháp giáo dục số thanh niên có liên quan
- Tùy theo lỗi phạm, tiến hành kiểm điểm, xử lý nghiêm túc đối với đồng chí cán bộ.
- Tổ chức sinh hoạt đơn vị để giáo dục, định hướng, rút kinh nghiệm chung trong toàn đơn vị về các yêu cầu khi thực hiện nhiệm vụ dân vận và việc nêu cao ý thức giữ gìn phẩm chất, tư cách “Bộ đội Cụ Hồ”  
- Tổng hợp báo cáo với cấp trên về kết quả giải quyết và xử lý vụ việc theo quy định. 
 	Tình huống 9. Trong đơn vị có một số quân nhân có biểu hiện nghiện chơi game và đam mê các trang mạng xã hội, làm ảnh hưởng đến sinh hoạt của đơn vị và kết quả hoàn thành chức trách, nhiệm vụ cá nhân.
Gợi ý biện pháp xử lý:
- Trao đổi thống nhất trong cấp ủy, chỉ huy đánh giá tình hình, báo cáo xin ý kiến chỉ đạo của cấp trên.
- Tiến hành gặp gỡ, đối thoại tìm hiểu rõ nguyên nhân, nghe tâm tư, nguyện vọng. Định hướng tư tưởng, phân tích làm rõ những tác động tiêu cực của việc nghiện game và các trang mạng xã hội đối với hệ thần kinh, và mức độ ảnh hưởng đến công việc của bản thân và đơn vị; làm cho quân nhân nhận thức đúng thực chất của sự việc. 
- Sinh hoạt toàn đơn vị quán triệt các quy định của cấp trên về việc sử dụng thiết bị thông minh trong học tập, công tác. Nhắc nhở quân nhân toàn đơn vị, chấp hành nghiêm quy định.
- Thường xuyên giao nhiệm vụ cụ thể, đưa quân nhân vào các hoạt động của đơn vị.
- Báo cáo kết quả phấn đấu, khắc phục của quân nhân nghiện game lên cấp trên và xin ý kiến chỉ đạo.
- Nếu nghiện nặng đề xuất cho quân nhân đi điều trị.
- Tổng hợp báo cáo với cấp trên về kết quả giải quyết và xử lý vụ việc theo quy định. 
Tình huống 10. Trong đơn vị có dư luận về quân nhân vay tiền của dân, quá khả năng chi trả, do túng quẫn nên đã có ý định đào ngũ, xin ra quân…
Gợi ý biện pháp xử lý:
- Hội ý cấp uỷ, chỉ huy đơn vị, nhận định, đánh giá tình hình vay nợ của quân nhân trong đơn vị đơn vị, xác định số lượng, đối tượng, mục đích vay nợ và khả năng trả nợ của quân nhân. Dự báo một số trường hợp có thể nảy sinh ý định đào bỏ ngũ nhằm “chạy nợ”; những hậu quả tiếp theo của sự việc trên có thể xảy ra như: mất an toàn giao thông, trộm cắp..., qua đó trao đổi, thống nhất biện pháp giải quyết và báo cáo cấp trên xin ý kiến chỉ đạo;
- Triển khai các biện pháp quản lý chặt số quân nhân nói trên
	- Yêu cầu các quân nhân trong đơn vị tự giác báo cáo bằng văn bản số nợ..., phương hướng sử dụng nguồn tiền để trả nợ (tiền phụ cấp, tiền thanh toán chế độ xuất ngũ, tiền gia đình hỗ trợ...)
	- Phân công cán bộ nắm tình hình vay nợ của quân nhân, đối chiếu với phần tự khai để có biện pháp giải quyết...
- Gặp gỡ số quân nhân vay nợ (nhất là số nợ xấu), nắm tình hình, phương hướng giải quyết; động viên quân nhân cùng với gia đình có biện pháp khắc phục kịp thời số nợ, không để trở thành nợ xấu; đồng thời chấp hành nghiêm kỷ luật, cần có thái độ tích cực hợp tác với các bên để giải quyết, nghiêm cấm đào ngũ và các hành vi tiêu cực khác.
	- Liên lạc với gia đình để trao đổi thống nhất các biện pháp phối hợp giải quyết (khi làm việc với gia đình quân nhân cần có văn bản ghi chép chặt chẽ).
	- Tổ chức sinh hoạt đơn vị quán triệt nhiệm vụ, định hướng tư tưởng cho quân nhân; biểu dương các đồng chí tiết kiệm trong chi tiêu giúp đỡ gia đình, người thân; phê bình nhắc nhở hành vi vay nợ quá khả năng thanh toán làm ảnh hưởng đến bản thân, gia đình và đơn vị; nêu cao ý thức chấp hành nghiêm kỷ luật đơn vị, ý thức tiết kiệm trong chi tiêu, tích cực hợp tác chặt chẽ với đơn vị và gia đình để khắc phục số nợ.
- Sau khi giải quyết xong, cần tổ chức sinh hoạt rút kinh nghiệm, kiểm điểm làm rõ trách nhiệm những cán bộ thiếu trách nhiệm trong công tác quản lý, giáo dục bộ đội.
	- Phân công cán bộ kèm cặp giáo dục, giúp đỡ quân nhân thuộc quyền không để tái diễn tình trạng trên.
- Tổng hợp báo cáo với cấp trên về kết quả giải quyết theo quy định./. 

BỘ CHQS TỈNH NINH THUẬN	CỘNG HOÀ XÃ HỘI CHỦ NGHĨA VIỆT NAM
PHÒNG CHÍNH TRỊ

Số:         /CT-TH	Độc lập - Tự do - Hạnh phúc

Ninh Thuận, ngày        tháng 9 năm 2021
V/v báo cáo kết quả xây dựng tình huống tư tưởng có thể nảy sinh trong thực hiện nhiệm vụ phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh và gợi ý biện pháp xử lý của cán bộ cơ sở”	

			
	                           Kính gửi: Phòng Tuyên huấn Quân khu.

Thực hiện chỉ đạo của Cục Chính trị Quân khu về việc rà soát xây dựng tình huống tư tưởng có thể nảy sinh trong thực hiện nhiệm vụ phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh và gợi ý biện pháp xử lý của cán bộ cơ sở”. Phòng Chính trị - Bộ CHQS tỉnh Ninh Thuận xin báo cáo kết quả như sau:
Tình huống 1: Một đồng chí cán bộ được giao nhiệm vụ công tác tại cơ sở cách ly phòng, chống dịch Covid-19, khi được thông tin vợ sinh con. Đồng chí này có trình bày chỉ huy đơn vị để được về chăm vợ, con. Căn cứ vào quy định của người đang ở tại khu vực cách ly thì chỉ huy đơn vị không được quyền giải quyết cho đồng chí này về; chính vì thế đồng chí này đã nảy sinh tư tưởng không muốn làm việc. Trên cương vị là chỉ huy đơn vị, đồng chí xử trí vấn đề này như thế nào?
	Biện pháp xử lý:
	- Gặp gỡ riêng đồng chí cán bộ nắm tình hình, tìm hiểu tâm tư, nguyện vọng và những vướng mắc bất cập trong công tác, tham mưu cho cấp ủy, chỉ huy đơn vị giải quyết.
	- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, kỷ luật, điều kiện hoàn cảnh gia đình của cán bộ, đặc điểm, yêu cầu, nhiệm vụ của đơn vị, xác định chủ trương, biện pháp lãnh đạo, chỉ đạo tổ chức thực hiện.
	- Động viên cán bộ xác định tư tưởng, trách nhiệm của người cán bộ, đảng viên, giải quyết hài hòa mối quan hệ chung, riêng để cùng với đơn vị hoàn thành tốt nhiệm vụ phòng, chống dịch Covid-19 hiện nay.
	- Tổ chức sinh hoạt đơn vị giáo dục, quán triệt rút kinh nghiệm cho đội ngũ cán bộ nắm rõ đặc điểm, yêu cầu, nhiệm vụ trong công tác phòng, chống dịch Covid-19, xây dựng ý thức, trách nhiệm khắc phục khó khăn khi được phân công làm nhiệm vụ ở khu vực cách ly.
	- Phối hợp với cấp ủy đảng, chính quyền địa phương tổ chức thăm hỏi, động viên gia đình cán bộ vượt qua hoàn cảnh khó khăn, tạo điều kiện thuận lợi để cán bộ hoàn thành nhiệm vụ.
	- Thường xuyên tổ chức giáo dục, động viên cán bộ chấp hành nghiêm kỷ luật quân đội, quy định đơn vị, tu dưỡng, rèn luyện bản thân để thích nghi với điều kiện, môi trường công tác.
	- Quan tâm bảo đảm đời sống vật chất, tinh thần cho cán bộ trong sinh hoạt, công tác, yên tâm gắn bó với đơn vị.
	- Xây dựng đơn vị có môi trường trong sạch, lành mạnh, có văn hóa, tinh thần đoàn kết, giúp đỡ lẫn nhau hoàn thành tốt nhiệm vụ.
- Tổng hợp kết quả xử lý báo cáo với cấp trên theo quy định.
Tình huống 2: Một chiến sĩ xin chỉ huy đơn vị về nhà để thăm mẹ ốm nặng, do tình hình dịch Covid-19 đơn vị không giải quyết tranh thủ, dẫn đến nảy sinh tư tưởng thiếu an tâm công tác. Trên cương vị là chỉ huy đơn vị, đồng chí xử trí vấn đề này như thế nào?
	Biện pháp xử lý:
	- Nắm chắc diễn biến tư tưởng, của chiến sĩ, tham mưu cho cấp ủy, chỉ huy đơn vị có biện pháp giải quyết tư tưởng.
	- Hội ý cấp ủy, chỉ huy đơn vị đánh giá tình hình tư tưởng, đặc điểm, yêu cầu, nhiệm vụ đơn vị, thống nhất cách thức giáo dục, định hướng tư tưởng cho chiến sĩ và gia đình quân nhân.
	- Gặp gỡ giáo dục, động viên chiến sĩ hiểu rõ quy định của quân đội về quyền lợi, nghĩa vụ, trách nhiệm trong thời gian tại ngũ, xác định tư tưởng, hoàn thành tốt nhiệm vụ được giao.
	- Tổ chức sinh hoạt đơn vị giáo dục, quán triệt rút kinh nghiệm cho cán bộ, chiến sĩ nắm rõ các văn bản các cấp, đặc điểm, yêu cầu, nhiệm vụ trong công tác phòng, chống dịch Covid-19, xây dựng ý thức, trách nhiệm khắc phục khó khăn hoàn thành tốt chức trách, nhiệm vụ được giao.
- Thông báo với gia đình chiến sĩ biết về quy định của quân đội và quyền lợi, nghĩa vụ, trách nhiệm của quân nhân trong thời gian tại ngũ; biện pháp phòng, chống dịch Covid-19 hiện nay, qua đó động viên, giáo dục con em yên tâm công tác.
- Phân công cán bộ phối hợp với cấp ủy đảng, chính quyền địa phương tổ chức thăm hỏi, động viên gia đình chiến sĩ vượt qua hoàn cảnh khó khăn, tạo điều kiện thuận lợi để quân nhân hoàn thành nhiệm vụ.
	- Tuyên truyền, động viên chiến sĩ nắm vững các biện pháp phòng, chống dịch Covid-19 của cơ quan, đơn vị để yên tâm công tác.
	- Thường xuyên tổ chức sinh hoạt đơn vị nắm chắc diễn biến tình hình tư tưởng, kỷ luật bộ đội, có biện pháp giúp đỡ, động viên kịp thời.
- Tổng hợp kết quả xử lý báo cáo với cấp trên theo quy định.
Tình huống 3: Trong đơn vị có tin đồn sai sự thật về tình hình cán bộ, chiến sĩ đã bị nhiễm Covid-19 đã gây hoang mang tư tưởng bộ đội. Trên cương vị là chỉ huy đơn vị, đồng chí xử trí vấn đề này như thế nào?
	Biện pháp xử lý:
- Hội ý cấp ủy, chỉ huy đơn vị nhận định tình hình, xác định nguồn gốc mức độ ảnh hưởng của tin đồn và biện pháp giải quyết; báo cáo xin ý kiến chỉ đạo của cấp trên.
- Tìm hiểu xác định nguyên nhân của tin đồn sai sự thật (do quân nhân trong đơn vị nhận thức sai hay phần tử xấu ở bên ngoài bịa đặt) để ngăn chặn và có biện pháp xử lý kịp thời, không để lan rộng, kéo dài.
- Phân loại, nắm chắc và tiến hành tốt công tác tư tưởng đối với những đồng chí có biểu hiện hoang mang, dao động.   
- Tổ chức sinh hoạt đơn vị thông báo cho cán bộ, chiến sĩ biết về nguồn tin đồn sai sự thật trên và hiểu rõ đâu là nguồn tin chính thống và nguồn tin không chính thống; trên cơ sở đó, định hướng tư tưởng, xây dựng niềm tin, thái độ, trách nhiệm của mỗi quân nhân trước những tác động tiêu cực nảy sinh...
- Thường xuyên quán triệt sâu, kỹ về nhiệm vụ của quân đội và đơn vị; âm mưu “diễn biến hòa bình”, “phi chính trị hoá” quân đội của các thế lực thù địch; kiên quyết phản bác những luận điệu sai trái của các thế lực thù địch, nhất là những luận điệu xuyên tạc công tác phòng chống dịch Covid-19 của Đảng và Nhà nước ta hiện nay; chủ động phát hiện, nắm chắc tình hình, ngăn chặn tư tưởng lệch lạc, không để những vấn đề tiêu cực xâm nhập vào đơn vị; giữ vững niềm tin cho mọi cán bộ, chiến sĩ, yên tâm hoàn thành tốt mọi nhiệm vụ được giao.
- Tiếp tục tuyên truyền các văn bản về phòng chống dịch Covid-19 trong đơn vị; phát huy hiệu quả hoạt động tuyên truyền thông qua hệ thống thiết chế văn hoá, chế độ đọc báo, thông báo chính trị, nghe đài, xem truyền hình; thường xuyên củng cố niềm tin, ổn định tình hình trong đơn vị.
- Phối hợp chặt chẽ với cấp ủy, chính quyền và các tổ chức đoàn thể địa phương trong công tác tuyên truyền, giáo dục; xây dựng đơn vị an toàn gắn với địa bàn an toàn; đẩy mạnh hoạt động thi đua quyết thắng, văn hóa văn nghệ, thể dục thể thao, bảo đảm và nâng cao đời sống văn hóa tinh thần cho bộ đội.
- Duy trì và quản lý tốt tình hình chính trị nội bộ, giáo dục nâng cao ý thức cảnh giác không để địch lợi dụng, lôi kéo, lừa gạt.
- Tổng hợp kết quả xử lý báo cáo với cấp trên theo quy định.
Tình huống 4: Một đồng chí dân quân không chấp hành thực hiện nhiệm vụ phòng chống bão lũ, với lý do khi thực hiện nhiệm vụ này là rất nguy hiểm đến tính mạng, gây dư luận không tốt trong Nhân dân và lực lượng dân quân tự vệ. Trên cương vị là chỉ huy Chỉ huy trưởng Ban CHQS xã, đồng chí xử trí vấn đề này như thế nào?
	Biện pháp xử lý:
	- Trao đổi trong ban chỉ huy quân sự xã nhận định tình hình tư tưởng, trách nhiệm của dân quân trong thực hiện nhiệm vụ phòng chống bão lũ, thống nhất biện pháp giải quyết. Báo cáo, xin ý kiến chỉ đạo của Đảng ủy xã để bố trí người thay thế.
	- Gặp gỡ số đội ngũ dân quân làm nhiệm vụ phòng chống bão lũ để giáo dục, quán triệt hiểu rõ đặc điểm, yêu cầu, nhiệm vụ, ý nghĩa của LLVT trong công tác phòng, chống thiên tai, trách nhiệm, quyền lợi, nghĩa vụ của mọi công dân; qua đó xây dựng trách nhiệm sẵn sàng nhận và hoàn thành nhiệm vụ, nâng cao ý thức chấp hành Luật Dân quân tự vệ, kỷ luật quân đội, quy định của địa phương.
	- Phối hợp với gia đình, người thân và đồng chí, đồng đội, động viên số dân quân còn băn khoăn trong quá trình nhận nhiệm vụ, nâng cao ý thức, trách nhiệm của dân quân sẵn sàng nhận nhiệm vụ phòng chống bão lũ. 
	- Tham mưu cho ban chỉ huy quân sự xã tổ chức sinh hoạt rút kinh nghiệm công tác huy động quân số thực hiện nhiệm vụ phòng chống bão lũ về ý thức thực hiện nhiệm vụ trong điều kiện khẩn trương, phức tạp và tác hại của sự chậm trễ; căn cứ tính chất vụ việc có thể đề nghị hình thức kỷ luật số dân quân chấp hành không nghiêm mệnh lệnh, đồng thời rà soát, lựa chọn những đồng chí có đủ phẩm chất chính trị, trách nhiệm trong công tác tham gia vào lực lượng dân quân của xã. 
	- Thường xuyên giáo dục, quán triệt các quy định, quy chế tổ chức hoạt động của dân quân trong thực hiện nhiệm vụ.
	- Làm tốt công tác đánh giá kết quả hoàn thành nhiệm vụ của lực lượng dân quân, kịp thời biểu dương, khen thưởng tập thể, cá nhân có thành tích, kỷ luật nghiêm túc những đồng chí vi phạm.
	- Tổng hợp kết quả xử lý báo cáo cấp trên theo quy định.

Trên đây là một số tình huống tư tưởng nảy sinh trong thực hiện nhiệm vụ phòng, chống, khắc phục hậu quả thiên tai, dịch bệnh và gợi ý biện pháp xử lý của cán bộ cơ sở, đơn vị xin báo cáo để cơ quan tổng hợp theo quy định./.


Nơi nhận:
- Như trên;
- Lư¬u: VT, TH. T03.
	KT.CHỦ NHIỆM
PHÓ CHỦ NHIỆM





Thượng tá Nguyễn Văn Kiểu










































































































Phần một: Ý ĐỊNH BÀI GIẢNG

I. MỤC ĐÍCH, YÊU CẦU
1. Mục đích 
Nhằm trang bị cho đội ngũ cán bộ lớp tập huấn nắm được thực trạng, nguyên nhân và những giải pháp nắm, quản lý, định hướng, giải quyết tình hình tư tưởng cho quân nhân ở đơn vị cơ sở trong LLVT tỉnh.
2. Yêu cầu 
- Nắm được vị trí, vai trò, nhiệm vụ nắm, quản lý, định hướng, giải quyết tình hình tư tưởng trong Quân đội; thực trạng, nguyên nhân đối với LLVT tỉnh hiện nay; đặc biệt nắm vững phương pháp nắm, quản lý, định hướng, giải quyết tình hình tư tưởng cho quân nhân ở đơn vị cơ sở trong LLVT tỉnh.
- Biết liên hệ, vận dụng linh hoạt vào hoạt động thực tiễn tại đơn vị.
II. NỘI DUNG: Gồm 03 phần:
Phần I. Sự cần thiết phải nâng cao hiệu quả công tác nắm, quản lý, định hướng, giải quyết tư tưởng ở đơn vị cơ sở trong LLVT tỉnh.
Phần II. Giải pháp nắm, quản lý, định hướng, giải quyết tình hình tư tưởng cho quân nhân Ở đơn vị cơ sở trong LLVT tỉnh.
Phần III. Trách nhiệm của đội ngũ cán bộ trong tiếp thu, vận dụng phương pháp nắm, quản lý, định hướng, giải quyết tình hình tư tưởng cho quân nhân ở đơn vị cơ sở.
III. ĐỐI TƯỢNG
Cán bộ lớp tập huấn quân sự giai đoạn 2 năm 2019.
IV. PHƯƠNG PHÁP
- Đối với giáo viên: Sử dụng phương pháp thuyết trình, kết hợp với trình chiếu powerpoint và liên hệ thực tiễn chất lượng nắm, quản lý, định hướng, giải quyết tình hình tư tưởng cho quân nhân ở đơn vị cơ sở trong LLVT tỉnh hiện nay để làm rõ nội dung giảng bài.
- Đối với người học: Tập trung tư tưởng nghe giảng, kết hợp ghi chép những nội dung cơ bản khi giáo viên phân tích để làm cơ sở, ôn luyện, thảo luận và kiểm tra đạt kết quả.
V. THỜI GIAN
- Thời gian toàn bài: 01 giờ 30 phút.
- Thời gian lên lớp: 01 giờ 30 phút.
- Thời gian tự nghiên cứu: Cán bộ lớp tập huấn tự nghiên cứu ngoài giờ.
VI. ĐỊA ĐIỂM: Hội trường Trường quân sự tỉnh.
VII. TÀI LIỆU
Tài liệu Tập huấn Quân sự năm 2019 do Quân khu ban hành.




























































































































































































































































































































































































































































































































































































































































































































































































































































































	Phần hai: NỘI DUNG

MỞ ĐẦU

Sinh thời, Chủ tịch Hồ Chí Minh dạy: “Tư tưởng thống nhất, hành động thống nhất thì nhiệm vụ tuy nặng nề, công việc tuy khó khăn phức tạp, ta cũng nhất định thắng lợi”. Thấm nhuần sâu sắc lời dạy của Người, những năm qua, Đảng ủy - Bộ CHQS tỉnh, cấp ủy, chỉ huy các cấp đã bám sát đặc điểm, yêu cầu nhiệm vụ và tình hình thực tiễn, chủ động ban hành, triển khai thực hiện nhiều nghị quyết, chỉ thị, hướng dẫn về công tác tư tưởng; tích cực chỉ đạo triển khai nhiều nội dung mới, mang tính đột phá; đồng thời tăng cường các biện pháp tập trung khắc phục khâu yếu, mặt yếu, qua đó tạo được bước chuyển biến khá rõ nét về nhận thức tư tưởng, ý thức chấp hành kỷ luật, pháp luật của cán bộ, chiến sỹ trong LLVT tỉnh. Tuy nhiên trước yêu cầu nhiệm vụ mới, sự tác động nhiều mặt của của tình hình thế giới, khu vực, trong nước đã ảnh hưởng không nhỏ đến tư tưởng, tình cảm, suy nghĩ, hành động, ý chí quyết tâm của cán bộ, chiến sỹ trong LLVT tỉnh, công tác tư tưởng còn nhiều mặt chưa đáp ứng yêu cầu nhiệm vụ. Đòi hỏi trong thời gian đến, công tác tư tưởng phải tích cực, chủ động, thường xuyên đổi mới nội dung, hình thức, phương pháp, phương tiện tiến hành. 
Quán triệt và thực hiện Nghị quyết lãnh đạo nhiệm vụ quân sự, quốc phòng năm 2018 của Đảng ủy Quân sự tỉnh; xuất phát từ thực trạng công tác tư tưởng và tình hình tư tưởng trong LLVT tỉnh, Phòng Chính trị biên soạn Chuyên đề “Phương pháp nắm, quản lý, định hướng, giải quyết tình hình tư tưởng cho quân nhân ở đơn vị cơ sở trong LLVT tỉnh” làm tài liệu học tập, nghiên cứu cho các đối tượng năm 2019.
I. SỰ CẦN THIẾT PHẢI NÂNG CAO HIỆU QUẢ CÔNG TÁC NẮM, QUẢN LÝ, ĐỊNH HƯỚNG, GIẢI QUYẾT TƯ TƯỞNG Ở ĐƠN VỊ CƠ SỞ TRONG LLVT TỈNH
1. Xuất phát từ vị trí, vai trò của công tác tư tưởng
Công tác tư tưởng là một bộ phận quan trọng của công tác xây dựng Đảng và hoạt động lãnh đạo của Đảng, tác động vào ý thức cán bộ, đảng viên, quần chúng nhân dân để định hướng nhận thức, giải quyết mâu thuẫn tư tưởng, khơi dậy và phát huy mọi tiềm năng sáng tạo của con người và đấu tranh chống mọi tư tưởng sai trái, làm cho thế giới quan và hệ tư tưởng của giai cấp công nhân giữ địa vị thống trị trong đời sống tinh thần xã hội, góp phần hình thành con người mới và xã hội mới xã hội chủ nghĩa.
Công tác tư tưởng trong quân đội là một bộ phận công tác tư tưởng của Đảng, một mặt hoạt động cơ bản của công tác đảng, công tác chính trị, đặt dưới sự lãnh đạo trực tiếp của cấp uỷ đảng, sự chỉ đạo của chính uỷ (chính trị viên), sự hướng dẫn tổ chức thực hiện của cơ quan chính trị, để bồi dưỡng, nâng cao trình độ lý luận, chính trị, tư tưởng văn hoá, đạo đức cách mạng, phát triển đời sống tinh thần của cán bộ, chiến sĩ, tham gia đấu tranh trên mặt trận tư tưởng nhằm xây dựng quân đội vững mạnh về chính trị, tư tưởng và tổ chức, hoàn thành thắng lợi mọi nhiệm vụ được giao.
Công tác tư tưởng có vai trò quan trọng hàng đầu trong sự nghiệp cách mạng của Đảng và sự nghiệp xây dựng, chiến đấu của quân đội. Trực tiếp truyền bá chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh, bồi dưỡng nâng cao nhận thức, hình thành ý chí, tình cảm để định hướng hành động cho cán bộ, chiến sỹ. Trực tiếp góp phần xây dựng các tổ chức Đảng vững mạnh về chính trị, tư tưởng và tổ chức; có vai trò quan trọng đáp ứng nhu cầu văn hoá tinh thần của bộ đội. Công tác tư tưởng góp phần đấu tranh trên mặt trận tư tưởng, lý luận, bảo vệ và phát triển chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh, quan điểm, đường lối của Đảng và có vai trò quan trọng hơn trong giai đoạn cách mạng hiện nay. 
2. Xuất phát từ thực trạng tình hình công tác tư tưởng trong LLVT tỉnh
a. Ưu điểm
Những năm qua, quán triệt sâu sắc các nghị quyết, chỉ thị, hướng dẫn của trên; nhận thức rõ vị trí, vai trò của công tác tư tưởng, cấp ủy, chỉ huy các cấp đã lãnh đạo, chỉ đạo và triển khai nhiều nội dung, biện pháp nâng cao nhận thức, trách nhiệm của cấp ủy, chỉ huy, chính ủy, chính trị viên, cơ quan và cán bộ chính trị trong lãnh đạo, chỉ đạo, tiến hành công tác tư tưởng. Tổ chức thực hiện quy chế dân chủ cơ sở, sinh hoạt ngày chính trị, văn hoá tinh thần có nề nếp chất lượng. Triển khai nhiều biện pháp tích cực, kiên quyết, kịp thời trong lãnh đạo, chỉ đạo phát hiện, nắm bắt và giải quyết thấu đáo những tâm tư, nguyện vọng chính đáng của cán bộ, nhân viên, chiến sỹ; xây dựng mối đoàn kết thống nhất trong nội bộ từng cơ quan, đơn vị, góp phần giảm đáng kể đơn thư khiếu nại, tố cáo. Thường xuyên bám sát mọi hoạt động của bộ đội, nhất là vào các dịp lễ, tết; giai đoạn chuyển nhiệm vụ; giao, nhận quân; diễn tập; dã ngoại...
Công tác tư tưởng được một số cơ quan, đơn vị gắn kết với sinh hoạt của tổ đảng, chi bộ; qua giao ban, hội ý chỉ huy hàng ngày. Tổ chức nhiều hoạt động mang ý nghĩa thiết thực như: thăm hỏi, động viên, tặng quà các gia đình cán bộ, chiến sỹ gặp khó khăn, hoạn nạn, ốm đau, bệnh tật; thường xuyên quan tâm củng cố, xây dựng và tổ chức hoạt động có hiệu quả các thiết chế văn hoá, cải thiện đời sống vật chất, tinh thần cho bộ đội.
Kết quả công tác tư tưởng của LLVT tỉnh trong thời gian qua đã góp phần quan trọng xây dựng các tổ chức Đảng trong sạch vững mạnh, cán bộ đảng viên có bản lĩnh chính trị vững vàng, trung thành vô hạn với Tổ quốc và Nhân dân, có tinh thần cảnh giác cách mạng cao, sẵn sàng nhận và hoàn thành mọi nhiệm vụ được giao. Đại đa số cán bộ, đảng viên, quần chúng gương mẫu về đạo đức lối sống có thái độ rõ ràng đối với các hành vi sai trái, tiêu cực trong đơn vị, thể hiện đấu tranh phê bình thẳng thắn, chân thành, gương mẫu chấp hành kỷ luật Quân đội, pháp luật Nhà nước, quy định của đơn vị. 
b. Hạn chế
Nhận thức của một số cấp ủy, chỉ huy về vị trí, vai trò công tác tư tưởng chưa đầy đủ; công tác lãnh đạo, chỉ đạo của cấp ủy, chính ủy, chính trị viên, người chỉ huy một số nơi chưa thường xuyên, liên tục, thiếu sâu sát; có nơi còn khoán trắng cho cơ quan và cán bộ chính trị; chưa có tính linh hoạt, nhạy bén trong nắm và xử lý các tình huống tư tưởng phát sinh.
Việc định hướng tư tưởng có nơi chưa kịp thời, thiếu chủ động, nhất là cán bộ quản lý trực tiếp; quản lý các mối quan hệ xã hội của cán bộ chưa chặt chẽ, do đó việc dự báo tư tưởng một số vụ việc chưa theo kịp diễn biến của tình hình. 
Công tác quán triệt, giáo dục nâng cao ý thức chấp hành pháp luật, kỷ luật, an toàn quân đội, an toàn giao thông có đơn vị hiệu quả thấp, thậm chí có nơi còn bỏ sót đối tượng nhân viên, chiến sỹ làm công tác chuyên môn (như: thợ sửa chữa, quản lý, tiếp phẩm, quân y, liên lạc…). Cán bộ quản lý trực tiếp còn biểu hiện chủ quan, thiếu gần gũi, gắn bó với chiến sĩ; biện pháp giáo dục, giải quyết tư tưởng còn nặng về mệnh lệnh, hành chính cứng nhắc, tính thuyết phục thấp. Do vậy các vụ vi phạm kỷ luật vẫn còn.
Chất lượng báo cáo tình hình tư tưởng của một số cơ quan, đơn vị còn hạn chế; có đơn vị còn báo cáo lấy lệ, đối phó, che dấu khuyết điểm, báo cáo thiếu trung thực, chưa kịp thời về tình hình tư tưởng, chấp hành kỷ luật của cán bộ, nhân viên, chiến sĩ ở đơn vị mình.
Trước yêu cầu nhiệm vụ mới, sự tác động của tình hình, một số đảng viên, cán bộ, kể cả cấp ủy viên, cán bộ chủ trì có động cơ phấn đấu chưa tốt, hiệu quả công tác thấp; chưa hết lòng, hết sức vì nhiệm vụ của đơn vị; còn có biểu hiện cơ hội, thực dụng, trung bình chủ nghĩa, thờ ơ, vô cảm, thấy đúng không bảo vệ, thấy sai không đấu tranh; cán bộ trẻ, nhiều đồng chí chưa chịu khó học tập, rèn luyện, thiếu chí tiến thủ. Một số ít cán bộ, đảng viên thiếu tu dưỡng, rèn luyện, ý thức tổ chức kỷ luật kém dẫn đến vi phạm kỷ luật phải xử lý; một bộ phận cán bộ, đảng viên có biểu hiện quan liêu, mệnh lệnh, áp đặt, thiếu dân chủ; gần đây xảy ra một số trường hợp tham gia cờ bạc, lô đề, cá độ bóng đá, nợ nần.	
c. Nguyên nhân
* Nguyên nhân khách quan
Một là,sự tác động của tình hình thế giới, khu vực cùng với sự chống phá của các thế lực thù địch.
Hai là, tác động của mặt trái kinh tế thị trường; ảnh hưởng từ những tàn dư, thủ tục lạc hậu, xuống cấp về đạo đức; tác động do thay đổi điều kiện môi trường sống.
Ba là, ảnh hưởng tiêu cực của cuộc Cách mạng công nghệ và không gian mạng (có chuyên đề riêng).
* Nguyên nhân chủ quan
Một là, nhận thức, trách nhiệm của một số chi ủy, chỉ huy, của chính trị viên đối với công tác nắm, quản lý, định hướng, giải quyết tư tưởng trong quản lý bộ đội còn hạn chế.
Hai là, quán triệt và thực hiện Quy chế quản lý tư tưởng trong lực lượng vũ trang tỉnh ban hành kèm theo Quyết định số 736/QĐ-BCH ngày 05 tháng 7 năm 2013 của Bộ Chỉ huy quân sự tỉnh còn hạn chế.
Ba là,chưa phát huy hiệu quả công tác giáo dục tư tưởng chính trị, nhiều nơi còn mệnh lệnh áp đặt, chưa coi trọng việc giải thích định hướng.
3. Xuất phát từ đặc điểm tình hình và yêu cầu nhiệm vụ của LLVT tỉnh trong tình hình mới
Tỉnh Ninh Thuận, nằm ở khu vực phí Nam Quân khu, là địa bàn có vị trí chiến lược rất quan trọng cả về chính trị, kinh tế và quốc phòng an ninh của cả nước. Tuy vậy, địa bàn tỉnh Ninh Thuận cũng là một trong những trọng điểm mà các thế lực thù địch tập trung chống phá. Các thế lực thù địch đang ra sức thực hiện âm mưu “phi chính trị hoá” quân đội, tách quân đội khỏi sự lãnh đạo của Đảng, triệt tiêu sức mạnh chính trị tinh thần của quân đội, làm cho quân đội mất sức mạnh chiến đấu. Do đó, công tác tư tưởng trong quân đội nói chung và LLVT tỉnh nói riêng phải thường xuyên giáo dục, nâng cao tinh thần cảnh giác cách mạng cho cán bộ, chiến sĩ; kịp thời đấu tranh vạch trần bản chất, âm mưu nham hiểm của kẻ thù; bồi dưỡng mục tiêu, lý tưởng chiến đấu, xây dựng lòng căm thù giặc sâu sắc, củng cố lòng tin và cổ vũ cán bộ, chiến sĩ quyết tâm hoàn thành mọi nhiệm vụ trong bất kỳ tình huống nào.  
Vì vậy, công tác tư tưởng trong LLVT tỉnh phải tăng cường giáo dục các giá trị truyền thống của Đảng, của dân tộc và của quân đội nhằm hình thành, vun đắp lòng yêu nước xã hội chủ nghĩa, tình cảm cao đẹp cho cán bộ, chiến sĩ; hun đúc ý chí quyết tâm chiến đấu, hy sinh thân mình vì độc lập dân tộc và chủ nghĩa xã hội, vì hạnh phúc của nhân dân.
II. GIẢI PHÁP NẮM, QUẢN LÝ, ĐỊNH HƯỚNG, GIẢI QUYẾT TÌNH HÌNH TƯ TƯỞNG CHO QUÂN NHÂN Ở ĐƠN VỊ CƠ SỞ TRONG LỰC LƯỢNG VŨ TRANG TỈNH
1. Tiến hành nắm, quản lý, định hướng, giải quyết tình hình tư tưởng phải thực hiện đúng nguyên tắc tiến hành công tác tư tưởng.
a. Tính đảng
Là biểu hiện tập trung tính chất giai cấp công nhân, quyết định phương hướng, mục tiêu, nội dung, đồng thời là tiêu chí đánh giá hiệu quả công tác tư tưởng. Yêu cầu phải lấy chủ nghĩa Mác – Lênin; tư tưởng Hồ Chí Minh, đường lối chủ trương, chính sách của Đảng làm cơ sở, căn cứ để xác định nội dung, hình thức, phương pháp tiến hành công tác tư tưởng.
b. Tính khoa học
Được quy định bởi bản chất cách mạng, khoa học của chủ nghĩa Mác - Lênin, tư tưởng Hồ Chí Minh, đường lối, chủ trương của Đảng. Tính khoa học của công tác tư tưởng luôn gắn liền với tính đảng, đảm bảo cho việc tiến hành công tác tư tưởng ở đơn vị luôn chủ động và đạt hiệu quả cao.
c. Công tác tư tưởng phải liên hệ chặt chẽ với đời sống, với thực tiễn
Là một nguyên tắc để tiến hành công tác tư tưởng cho sát đối tượng, cập nhật được những thông tin, mới đạt hiệu quả thiết thực. Chủ tịch Hồ Chí Minh đã dạy “Thực tiễn không có lý luận hướng dẫn thì thành thực tiễn mù quáng. Lý luận mà không liên hệ với thực tiễn là lý luận suông”.
d. Kết hợp chặt chẽ giữa xây và chống, lấy xây dựng phát huy mặt tích cực, tiến bộ của con người làm chính để khắc phục mặt tiêu cực, lạc hậu
Xây và chống là hai mặt thống nhất nhưng không đồng nhất trong quá trình tiến hành công tác tư tưởng, trong đó lấy xây làm chính. Bởi vì, trong mỗi con người bao giờ cũng có mặt tích cực và mặt lạc hậu, sự tác động khách quan vào tư tưởng con người cũng có cả mặt tích cực và mặt lạc hậu.
e. Kết hợp chặt chẽ công tác tư tưởng với công tác tổ chức và công tác chính sách
Tư tưởng chỉ đạo hành động, nhưng tư tưởng chỉ phát huy hiệu lực, khi nó biến thành hành động thực tiễn cải tạo xã hội, cải tạo tự nhiên và cải tạo con người trong một tổ chức nhất định. Do đó, phải luôn coi trọng và kết hợp cả công tác tư tưởng, công tác tổ chức và công tác chính sách trong mọi hoạt động của công tác tư tưởng.
g.Vận đụng quan điểm tổng hợp trong tiến hành công tác tư tưởng
Vận dụng quan điểm tổng hợp trong tiến hành công tác tư tưởng là thể hiện sự nhất quán với quan điểm trong lãnh đạo, chỉ đạo cách mạng của Đảng, bảo đảm công tác tư tưởng ở đơn vị phát huy sức mạnh tổng hợp, tiến hành đạt hiệu quả cao.
2. Thực hiệm nghiêm cơ chế hoạt động và phân cấp quản lý tư tưởng ở đơn vị cơ sở
a. Cơ chế hoạt động: Theo Quy chế quản lý tư tưởng trong lực lượng vũ trang tỉnh ban hành kèm theo Quyết định số 736/QĐ-BCH ngày 05 tháng 7 năm 2013 của Bộ Chỉ huy quân sự tỉnh. 
Một là, Công tác quản lý tư tưởng trong LLVT tỉnh là một nội dung quan trọng được cụ thể hóa Điều 142, 143, 144, 145, chương 6 Điều lệnh Quản lý bộ đội trong Quân đội nhân dân Việt Nam, đặt dưới sự lãnh đạo của Thường vụ Đảng ủy Quân sự tỉnh; sự quản lý, điều hành trực tiếp của Chính uỷ, Thủ trưởng Bộ chỉ huy Quân sự tỉnh.
Hai là, Phòng Chính trị giúp Thường vụ Đảng ủy, Bộ bộ chỉ huy Quân sự tỉnh chỉ đạo, hướng dẫn, định hướng, kiểm tra, theo dõi việc quản lý tư tưởng; tổng hợp báo cáo, thông báo kết quả công tác quản lý tư tưởng và tình hình tư tưởng trong LLVT tỉnh.
Ba là, Phòng Tham mưu, Phòng Hậu cần, Phòng Kỹ thuật, chỉ đạo các ban theo chức năng nhiệm vụ, phối hợp kiểm tra, theo dõi việc quản lý tư tưởng ở các cơ quan, đơn vị trực thuộc LLVT tỉnh. Khi phát hiện dấu hiệu bất thường về tư tưởng hoặc các trường hợp đặc biệt, phải báo cáo ngay về Bộ chỉ huy Quân sự tỉnh (qua Phòng Chính trị). 
Bốn là,  Công tác quản lý tư tưởng ở mỗi cấp trong LLVT tỉnh đặt dưới sự lãnh đạo của cấp uỷ đảng; quản lý, điều hành trực tiếp của chính uỷ (chính trị viên, cán bộ chủ trì công tác đảng, công tác chính trị), ban chỉ huy cùng cấp và sự chỉ đạo, hướng dẫn, định hướng của cơ quan chính trị cấp trên.
Năm là, Cơ quan chính trị các cấp giúp cấp uỷ đảng, chính uỷ (chính trị viên, cán bộ chủ trì công tác đảng, công tác chính trị), người chỉ huy chỉ đạo, hướng dẫn, định hướng, tổ chức triển khai thực hiện và theo dõi việc quản lý tư tưởng, tổng hợp báo cáo, thông báo kết quả công tác quản lý tư tưởng và tình hình tư tưởng ở cơ quan, đơn vị mình.
Sáu là, Những cơ quan, đơn vị không có biên chế cơ quan chính trị, công tác quản lý tư tưởng do chính uỷ (chính trị viên, cán bộ chủ trì công tác đảng, công tác chính trị) trực tiếp chỉ đạo, định hướng và hướng dẫn tổ chức thực hiện.
Bảy là,  Chính uỷ (chính trị viên, cán bộ chủ trì công tác đảng, công tác chính trị), người chỉ huy chịu trách nhiệm trước cấp ủy đảng cùng cấp và cấp ủy, chỉ huy cấp trên về công tác quản lý tư tưởng của cơ quan, đơn vị mình.
Tám là, Ban chỉ huy quân sự các huyện, thành phố trên địa bàn tỉnh chấp hành nghiêm sự lãnh đạo của Thường vụ Đảng ủy và chỉ đạo, hướng dẫn, định hướng của Phòng Chính trị; đồng thời bám sát sự lãnh đạo, chỉ đạo, định hướng của cấp ủy, Ban tuyên giáo các địa phương để tiến hành việc quản lý tư tưởng LLVT địa phương có hiệu quả.
b. Phân cấp quản lý tư tưởng
Một là,  Chỉ huy cấp đại đội, trung đội, tiểu đội và tương đương quản lý tư tưởng tất cả cán bộ, nhân viên, chiến sỹ trong đơn vị.
Hai là, Chỉ huy cấp tiểu đoàn và tương đương quản lý tư tưởng tất cả cán bộ từ tiểu đội phó và tương đương trở lên và những nhân viên, chiến sỹ cá biệt trong đơn vị.
Ba là, Chỉ huy, thủ trưởng cơ quan chính trị cấp trung đoàn, lữ đoàn và tương đương quản lý tư tưởng tất cả sĩ quan, quân nhân chuyên nghiệp giữ chức sĩ quan, cán bộ trung đội và tương đương trở lên và những tiểu đội trưởng, nhân viên, chiến sỹ cá biệt trong đơn vị.
Bốn là, Chỉ huy, thủ trưởng cơ quan chính trị cấp sư đoàn và tương đương quản lý tư tưởng sĩ quan đến cấp đại úy, cán bộ cấp đại đội và tương đương trở lên và những cán bộ trung đội, nhân viên cá biệt trong đơn vị.
Năm là, Đối tượng thuộc cấp nào quản lý thì cấp đó phải có đánh giá và có hồ sơ theo dõi tình hình tư tưởng và tổng hợp báo cáo cấp trên. 
Sáu là, Hệ thống sổ sách, giấy tờ liên quan đến quản lý, phân loại, đánh giá tình hình tư tưởng được lập thống nhất, đồng bộ, cụ thể, tỷ mỷ, rõ ràng và cập nhật thông tin thường xuyên, nhằm quản lý, theo dõi sử dụng lâu dài; khi thay đổi cán bộ phụ trách phải bàn giao cụ thể. 
Bảy là, Cơ quan chính trị là cơ quan quản lý, bảo quản hệ thống sổ sách theo dõi về quản lý, phân loại, đánh giá tình hình tư tưởng ở mỗi cấp. Những cơ quan, đơn vị không có biên chế cơ quan chính trị, thì việc quản lý, bảo quản hệ thống sổ sách do cán bộ chính trị đảm nhiệm (nơi không có biên chế cán bộ chính trị thì do cấp ủy phân công người đảm nhiệm).
Tám là, Người được giao nhiệm vụ quản lý hệ thống sổ sách, tài liệu theo dõi về quản lý, phân loại, đánh giá tình hình tư tưởng phải thường xuyên cập nhật thông tin, ghi chép đầy đủ, rõ ràng số liệu và có trách nhiệm bảo quản hồ sơ, sổ sách lưu trữ theo quy chế quản lý tài liệu của cơ quan, đơn vị.
3. Vận dụng tổng hợp các hoạt động chủ yếu của công tác tư tưởng trong nắm, quản lý, định hướng, giải quyết tư tưởng
a. Công tác giáo dục chính trị
Đây là một hoạt động quan trọng của công tác tư tưởng - văn hoá, một nhiệm vụ cơ bản của huấn luyện bộ đội, là khâu căn bản, trung tâm, có ý nghĩa quyết định hình thành nhân cách quân nhân, phẩm chất “Bộ đội Cụ Hồ” và năng lực hoạt động thực tiễn của quân nhân.
b. Công tác tuyên truyền, cổ động
Đây là một “mũi nhọn xung kích” của công tác tư tưởng, thông qua các hình thức và phương pháp hoạt động nhằm truyền bá lý luận chủ nghĩa Mác - Lênin, tư tưởng, đạo đức, phong cách Hồ Chí Minh, đường lối, chủ trương của Đảng, chính sách và pháp luật của Nhà nước; phổ biến kịp thời có định hướng những sự kiện chính trị, quân sự, kinh tế, văn hoá - xã hội diễn ra trong nước và thể giới; cổ vũ, động viên, khích lệ và hướng dẫn bộ đội hành động, thi đua thực hiện thắng lợi mọi nhiệm vụ.
c. Công tác văn hóa quần chúng
Thông qua các hình thức và phương pháp hoạt động bằng ngôn ngữ và hình tượng nghệ thuật để tác động vào cảm xúc, tình cảm, lý trí thẩm mỹ của cán bộ, chiến sĩ, công tác văn hoá quần chúng có tác dụng giáo dục một cách nhẹ nhàng, gây được ấn tượng sâu sắc và lâu bền. Đồng thời, góp phần đáp ứng những nhu cầu thiết yếu về đời sống tinh thần của cán bộ, chiến sĩ ở đơn vị.
d. Tổ chức phong trào thi đua xã hội chủ nghĩa
Thi đua xã hội chủ nghĩa nhằm phát huy chủ nghĩa anh hùng cách mạng, tinh thần làm chủ xã hội chủ nghĩa, động viên cao độ trí lực, thể lực của mọi cán bộ, chiến sĩ vào việc hoàn thành xuất sắc nhiệm vụ được giao. 
e. Xây dựng và hoạt động môi trường văn hoá
Các mặt hoạt động của công tác tư tưởng đều có đặc trưng và vai trò, tác dụng riêng, nhưng có mối quan hệ biện chứng, đan xen, hỗ trợ, bổ sung cho nhau. Vì vậy, trong quá trình tiến hành công tác tư tưởng phải biết vận dụng, kế thừa, phát huy và kết hợp chặt chẽ các hình thức, biện pháp, của từng mặt hoạt động để làm cho công tác này luôn sinh động, có sức sống và hiệu quả cao.
4. Sử dụng tổng hợp các phương pháp, nội dung, yêu cầu nắm tình hình tư tưởng quân nhân
a. Phương pháp nắm tư tưởng
* Phương pháp nắm trực tiếp
Trực tiếp gặp gỡ đối thoại dân chủ; quan sát các hành vi, cử chỉ, thái độ; thử thách thông qua hoạt động thực tiễn; thăm dò ý kiến qua phiếu điều tra; thông qua hồ sơ lý lịch và thông qua báo cáo của các tổ chức; phản ánh của cán bộ, đảng viên, nhân viên, chiến sĩ, của gia đình, cấp ủy, chính quyền, các đoàn thể và nhân dân địa phương…, để theo dõi nắm chắc tư tưởng của cán bộ, nhân viên, chiến sỹ theo phân cấp.
Đối với nắm tư tưởng chiến sĩ mới cần đạt được những nội dung:
- Do không thực hiện “3 gặp 4 biết” nên khi thâm nhập hồ sơ thấy các chỉ số, thông tin có vấn đề thì cần bố trí gặp trực tiếp để nắm bắt rõ hơn.
- Khi tiếp nhận chiến sĩ mới trong thời gian phúc tra sức khỏe tiến hành phúc tra các nội dung liên quan đến bản thân, gia đình và các mối quan hệ của chiến sĩ mới bằng 2 cách song song
+ Phát phiếu điều tra theo mẫu để chiến sĩ mới khai, do trong phiếu quân nhân ghi sơ sài; không có bên nội, ngoại, bạn bè, địa chỉ zalo, facebook, email, số điện thoại…
+ Bố trí cán bộ gặp trực tiếp: Trong khoản thời gian phúc tra phải bố trí, tăng cường cán bộ để bảo đảm 100% chiến sĩ mới nhập ngũ được gặp gỡ (đơn vị nào phúc tra trước, đến gặp trước; có thể tăng cường cán bộ cơ quan, cán bộ đơn vị không huấn luyện chiến sĩ mới).
- Quá trình gặp gỡ nếu phát hiện vấn đề tâm lý, mối quan hệ phức tạp, ví dụ như: đã từng tự tử; đã từng tham gia các tệ nạn như lô đề, cá độ, ma túy, vi phạm kỷ luật…; các dị tật mà khám sức khỏe không phát hiện ra phải kịp thời phối hợp với cơ quan chức năng xác minh làm rõ, nếu không đủ tiêu chuẩn thì nghiên cứu, kết luận và tiến hành loại trả.
- Quá trình nắm tình hình cần chống hiện tượng khai báo thiếu thông tin, không trung thực nhằm trốn tránh thực hiện nghĩa vụ quân sự.
* Phương pháp nắm gián tiếp
+ Thông qua hồ sơ để biết tiểu sử của quân nhân. Khi sử dụng phương pháp này, cần nắm, nghiên cứu kỹ lý lịch của quân nhân và phải khách quan, không được định kiến.
+ Thông qua phản ánh, báo cáo của tổ chức đảng, tổ chức chỉ huy, tổ chức quần chúng; của cán bộ, đảng viên; những đoàn viên, chiến sĩ ưu tú; của bạn bè, người thân, gia đình và cấp ủy, chính quyền, các đoàn thể và nhân dân địa phương… Phải động viên, đề cao tinh thần trách nhiệm, đồng thời phát huy dân chủ của những người đứng đầu tổ chức, địa phương, cá nhân để họ cung cấp thông tin một cách trung thực, khách quan, rõ ràng.
Lãnh đạo, chỉ huy đơn vị cần thường xuyên nắm chắc và báo cáo những dấu hiệu thường xảy ra có liên quan, hoặc trực tiếp dẫn đến nảy sinh tư tưởng, đó là:       
Một là, đơn vị có mâu thuẫn nội bộ cùng cấp, cấp trên với cấp dưới dẫn đến bất mãn, phát ngôn thiếu tính chất xây dựng đơn vị.
Hai là, đơn vị có quân nhân, công nhân viên quốc phòng mắc bệnh hiểm nghèo, trầm cảm, bi quan về sức khỏe, tương lai.
Ba là, bản thân hoặc gia đình quân nhân, công nhân viên quốc phòng gặp khó khăn về kinh tế hay các vấn đề xã hội khác dẫn đến bế tắc trong cuộc sống mà không tự giải quyết được.
Bốn là, đơn vị có cán bộ, chiến sĩ mà tình yêu, hạnh phúc của bản thân và gia đình bị tan vỡ.
Năm là, đơn vị có quân nhân tham gia đánh bạc, chơi huê, hụi, cá độ bóng đá, làm ăn thua lỗ, nợ nần của bản thân, của gia đình không có khả năng chi trả.
Sáu là, trong đơn vị có quân nhân quan hệ với các thành phần phức tạp ngoài xã hội.
Bảy là, cán bộ, chiến sĩ có biểu hiện hoặc hành vi quân phiệt, vô ý thức tổ chức, kỷ luật.
Tám là, có người thân trong gia đình vi phạm pháp luật, bị tòa án các cấp xét xử từ tù treo, phạt giam trở lên.
Chín là, có thông tin không chính thống hoặc ấn phẩm văn hóa xấu độc xâm nhập vào cơ quan, đơn vị.
Trên cơ sở báo cáo của các đơn vị, chỉ huy các cấp đánh giá phân loại đúng tình hình tư tưởng, tìm ra nguyên nhân, dự kiến chiều hướng phát triển để xác định phương hướng, nội dung, giải pháp giải quyết theo hướng tích cực nhất, không để xảy ra các đột biến bất ngờ, phối hợp trên dưới cùng giải quyết những vấn đề nảy sinh, tạo sự đồng thuận trong tổ chức thực hiện các nhiệm vụ được giao.

b. Nội dung nắm tư tưởng quân nhân
Một là, hoàn cảnh xã hội, lịch sử gia đình, môi trường làm việc của cán bộ, chiến sĩ. Nắm nơi sống, học tập, làm việc của quân nhân trước khi nhập ngũ. Hoàn cảnh lịch sử gia đình, bản thân; mối quan hệ với những người ruột thịt trong gia đình; các mối quan hệ xã hội. Điều kiện xã hội, truyền thống, phong tục, tập quán của địa phương.
Hai là, nắm mọi biểu hiện tư tưởng, tâm trạng của quân nhân (tính cách linh hoạt hay trầm; tự ti hay tự cao).
Cần tập trung nắm trình độ nhận thức, lập trường, quan điểm, thái độ, trách nhiệm đối với chủ trương, chính sách của Đảng và Nhà nước, nhiệm vụ và chức trách được giao; phẩm chất, đạo đức, lối sống, cử chỉ, thái độ, hành vi giao tiếp và cách ứng xử, giải quyết các mối quan hệ hàng ngày; lễ tiết tác phong, ý thức chấp hành chính sách, pháp luật của Nhà nước, kỷ luật của Quân đội và các chế độ, quy định của đơn vị…
Ba là, nắm diễn biến quá trình thực hiện nhiệm vụ và kết quả thực hiện nhiệm vụ của quân nhân. Nắm tình hình nhiệm vụ trên giao; những khó khăn, thuận lợi trong quá trình thực hiện nhiệm vụ; tinh thần, trách nhiệm trong quá trình thực hiện nhiệm vụ và kết quả hoàn thành nhiệm vụ của quân nhân.
5. Phát hiện và giải quyết kịp thời tư tưởng nảy sinh ở đơn vị cơ sở.
a.Tiến hành phân tích, đánh giá tư tưởng (04 bước)
+ Bước 1: Thu thập
Dựa vào các tư liệu đã nắm được tiến hành hệ thống (ý thức trong sinh hoạt, học tập; thái độ trước các vấn đề được thông báo, quán triệt; ý thức chấp hành nhiệm vụ của trên giao; động cơ làm việc tự giác, tích cực, chia sẻ với đồng đội; mức độ, kết quả hoàn thành nhiệm vụ); tiến hành phân tích, đánh giá sơ bộ đưa ra nhận định, dự đoán ban đầu về tư tưởng và xu hướng vận động có thể xảy ra.
+ Bước 2: Xem xét, đánh giá
Liên kết, tập hợp những biểu hiện, hiện tượng để đánh giá về bản chất của biểu hiện, tiến hành so sánh, diễn dịch, quy nạp các biểu hiện tư tưởng đã có để rút ra những điểm giống nhau, những điểm khác nhau và những điểm còn mâu thuẫn trong nhận thức tư tưởng và hành động.

+ Bước 3: Kết luận
Từ những kết luận ban đầu về tư tưởng, đưa ra những lập luận, chứng minh, chỉ ra thực chất tư tưởng hiện tại của đối tượng; đồng thời kiểm nghiệm qua hoạt động thực tiễn để rút những kết luận chính xác về tư tưởng, nguồn gốc, nguyên nhân, dự kiến được chiều hướng phát triển của tư tưởng.
+ Bước 4: Phân loại tư tưởng (xếp loại)
Căn cứ những kết luận rút ra và tình hình cụ thể của đơn vị để phân loại từng đối tượng cụ thể cho phù hợp theo các mức: A, B, C và chậm tiến (Tốt, khá, trung bình và yếu) để quản lý, chú ý những quân nhân chậm tiến; những đơn vị yếu, kém. Ngoài ra, có đơn vị hiện nay còn phân loại theo nhóm đối tượng để quản lý: (SQ; QNCN; đảng viên; đoàn viên; thanh niên; cán bộ (nhất là cán bộ chủ trì); phân nhóm quân nhân để quản lý gồm: Nhóm nòng cốt; nhóm tích cực; nhóm chậm tiến (tiêu cực, lưng chừng); nhóm chiến sĩ cũ; nhóm chiến sĩ mới....để có biện pháp quản lý giáo dục phù hợp.
b. Định hướng tư tưởng
Tăng cường công tác giáo dục truyền thống của Đảng, của dân tộc, Quân đội, LLVT tỉnh và đơn vị. Qua đó xây dựng niềm tin, lý tưởng sống cho cán bộ, chiến sĩ trong đơn vị. Tuyên truyền giáo dục chủ trương, đường lối của Đảng, chính sách, pháp luật của Nhà nước, điều lệnh, điều lệ, chế độ quy định của Quân đội, nhằm không ngừng nâng cao nhận thức, tin tưởng vào sự lãnh dạo của Đảng, quản lý điều hành của nhà nước, chấp hành nhiêm pháp luật, kỷ luật, có khả năng nhận diện, đấu tranh với các quan điểm, tư tưởng sai trái tác động vào đơn vị.
Giáo dục định hướng kỷ năng sống, có trách nhiệm với Tổ quốc, quê hương, sống có tình có nghĩa với gia đình, người thân, bạn bè,...xây dựng tinh thần lạc quan, yêu đời, xử lý tốt các mối quan hệ trong cuộc sống, giao tiếp... Kịp thời định hướng dư luận, nhất là các sự kiện mới, các vụ việc đưa tin trên các phương tiện thông tin, nhất là trên các trang mạng xã hội; đấu tranh vạch trần các tư tưởng sai trái, phản động và âm mưu, thủ đoạn chống phá của các thế lực thù địch. Đẩy mạnh các hoạt động phong trào thi đua, giao lưu văn hóa văn nghệ, tọa đàm, diễn đàn, thi tìm hiểu các sự kiện chính trị... qua đó lồng ghép định hướng tư tưởng cho quân nhân.
c. Tiến hành giải quyết diễn biến tư tưởng (03 bước)
+ Bước 1: Chuẩn bị xử lý
Phát huy vai trò của tập thể lãnh đạo, chỉ huy đơn vị trong đánh giá, nhận định tình hình và xác định biện pháp xử lý, giải quyết vấn đề tư tưởng nảy sinh (hội ý chi ủy, chỉ huy đơn vị). Báo cáo xin ý kiến chỉ đạo của cấp trên; phân công, phát huy trách nhiệm của chủ thể xử lý (lựa chọn cán bộ tham gia xử lý). Phân công thu thập nắm tình hình; xác minh làm rõ sự việc. Xác định nội dung, cách thức xử lý. Chuẩn bị điều kiện để xử lý.
+ Bước 2: Tiến hành xử lý
Phải thận trọng, đồng cảm chia sẻ, bám sát thực tiễn, yêu cầu nhiệm vụ, nhu cầu của bộ đội; giải quyết đúng quy trình, thấu tình, đạt lý. Kiên quyết chống biểu hiện quân phiệt, xúc phạm danh dự, nhân phẩm chiến sĩ và cấp dưới. Lựa chọn, phân công cán bộ gặp gỡ, tiếp xúc với đối tượng. Đánh giá đúng kết quả, công sức của quân nhân trong thực hiện nhiệm vụ và xây dựng đơn vị. Phân tích, thuyết phục; truyền đạt thông tin; hướng dẫn, động viên…
+ Bước 3: Sau xử lý
 Ổn định tình hình đơn vị; tiếp tục theo dõi; đánh giá rút kinh nghiệm; tổng hợp tình hình, báo cáo theo quy định.
6. Phát huy vai trò các tổ chức, các lực lượng trong tiến hành công tác nắm, quản lý, định hướng, giải quyết tư tưởng.
a. Đối với tổ chức Đảng
Xác định tốt các chủ trương, biện pháp giáo dục, quán triệt. Phân công, phát huy vai trò trách nhiệm của cấp ủy viên: Cập nhật tình hình, thông tin tình hình. Chỉ đạo tổ chức bồi dưỡng, truyền thụ kinh nghiệm nắm, quản lý, định hướng, giải quyết tư tưởng của bộ đội cho đội ngũ cán bộ trong đơn vị. Kiểm tra, giám sát, sơ kết đánh giá.
b. Đối với chính trị viên và người chỉ huy
Chủ động dự kiến tình huống có thể xảy ra ở đơn vị và phương pháp tiến hành xử lý từng tình huống cụ thể. Trực tiếp tiến hành hoặc phân công cán bộ cấp dưới (cấp phó) tham mưu về công tác tư tưởng, về đối tượng, nội dung, thời gian, hình thức, phương pháp tiến hành công tác tư tưởng, phải nhận định, dự báo được những quân nhân dễ bị tác động, nảy sinh tư tưởng thoái thác nhiệm vụ; từ đó có biện pháp xử lý phù hợp.
c. Đối với đội ngũ cán bộ, đảng viên; chiến sĩ bảo vệ…
Thực hiện theo sự phân công của chi bộ, đơn vị. Tạo chỗ dựa, tin tưởng để bộ đội gần gũi; kịp thời báo cáo với cấp ủy, chỉ huy các trường hợp đặc biệt để có biện pháp lãnh đạo, chỉ đạo giải quyết tư tưởng nảy sinh phức tạp.
d. Vai trò của HĐQN, các tổ chức quần chúng và Tổ 03 người
Thường xuyên giáo dục đoàn viên, hội viên, quân nhân đơn vị; tổ chức chức các hoạt động, phong trào, hoạt động kết nghĩa, giao lưu, thể dục, thể thao, văn hóa văn nghệ; sinh nhật chiến sĩ; quan tâm, chăm lo, chia sẻ, nhất là đối tượng cá biệt, đặc biệt; đấu tranh, phê bình trong sinh hoạt.
e. Phối hợp giữa đơn vị với địa phương và gia đình
Giáo dục, duy trì bộ đội chấp hành nghiêm kỷ luật khi quan hệ với nhân dân. Đẩy mạnh hoạt động giao lưu, kết nghĩa với cơ quan, đoàn thể, của địa phương, động viên giúp đỡ lẫn nhau cùng hoàn thành nhiệm vụ. Nắm vững tình hình kinh tế, đời sống, thành phần xuất thân của các đối tượng quân nhân để có các giải pháp phát huy truyền thống tốt đẹp của quê hương, dòng họ, gia đình và khắc phục những thói quen, tập tục lạc hậu làm cản trở đến quản lý tư tưởng của mỗi quân nhân ở đơn vị cơ sở. Phối hợp chặt chẽ với gia đình để giáo dục quân dân. 
7. Xây dựng môi trường sống	, hoạt động của đơn vị trong sáng, lành mạnh, phong phú.
Lãnh đạo việc xây dựng, kiện toàn và thực hiện tốt quy chế dân chủ. Xây dựng tốt mối quan hệ trong đơn vị; các mối quan hệ giữa đơn vị với địa phương và gia đình. Quan tâm chăm lo tốt đời sống vật chất, tinh thần. Thường xuyên xây dựng, bồi dưỡng, nhân điển hình và phát huy trách nhiệm của các điển hình tiên tiến trong giải quyết tư tưởng, đồng thời xử lý nghiêm minh, có tính giáo dục cao đối với các vi phạm xảy ra trong đơn vị (coi trọng việc nêu gương; xây gắn với chống, lấy xây là chính).
8. Phát huy tính tích cực, tự giác của mọi quân nhân trong quá trình tự bồi dưỡng nâng cao ý thức tự quản lý tư tưởng
Giáo dục nhận thức về tầm quan trọng của tự nâng cao ý thức tự quản lý tư tưởng đối với sự hình thành, phát triển phẩm chất nhân cách cá nhân; thường xuyên hướng dẫn, giúp đỡ từng quân nhân ở đơn vị xây dựng nội dung kế hoạch, biện pháp cụ thể tự rèn luyện. Thông qua tổ chức chính quyền đoàn thể để giáo dục, động viên họ xây dựng động cơ, tinh thần trách nhiệm trong nâng cao ý thức tự quản lý tư tưởng. Tổ chức tốt các hoạt động phong trào thi đua, bồi dưỡng tạo nguồn phát triển đảng viên, đăng ký tu dưỡng rèn luyện, kết hợp giáo dục chung với giáo dục riêng, mạn đàm trao đổi... Cần có các biện pháp tích cực cả về chính trị, tư tưởng, cả về hành chính quân sự và khuyến khích vật chất để động viên, giúp đỡ từng quân nhân có hạn chế, khiếm khuyết vững tin vào khả năng để phấn đấu hoàn thành nhiệm vụ. Chỉ đạo, tổ chức kiểm tra, đánh giá, rút kinh nghiệm việc tự bồi dưỡng, nâng cao ý thức tự quản lý tư tưởng của quân nhân trong đơn vị.
III. TRÁCH NHIỆM CỦA ĐỘI NGŨ CÁN BỘ TRONG TIẾP THU, VẬN DỤNG PHƯƠNG PHÁP NẮM, QUẢN LÝ, ĐỊNH HƯỚNG, GIẢI QUYẾT TÌNH HÌNH TƯ TƯỞNG CHO QUÂN NHÂN Ở ĐƠN VỊ CƠ SỞ
1. Phải nhận thức rõ các yếu tố tác động đến tâm lý, tư tưởng quân nhân trong tình hình hiện nay
Quá trình đẩy mạnh sự nghiệp công nghiệp hóa, hiện đại hóa, đổi mới toàn diện đất nước và hội nhập quốc tế do Đảng lãnh đạo trong những năm tới sẽ tiếp tục đặt ra nhu cầu lớn, tạo ra cơ hội lớn cùng với những cơ sở chính trị - xã hội, điều kiện vật chất cho sự phát triển của công tác tư tưởng trên tất cả các phạm vi, các mặt hoạt động. Đó là điều kiện thuận lợi nhưng cũng phải đối mặt với những thách thức gay gắt do tác động từ mặt trái của toàn cầu hoá, cơ chế thị trường, cửa tiêu cực, tệ nạn xã hội, sự chống phá của các thế lực thù địch và ảnh hưởng từ những yếu kém của bản thân công tác tư tưởng thời gian qua.
2. Phải có phương pháp tư duy khoa học, nhạy bén về chính trị, kiên định về lập trường tư tưởng
Trong xu thế phát triển của các phương tiện truyền thông hiện đại do được ứng dụng thành quả của cách mạng khoa học công nghệ, công tác tư tưởng nói riêng và các lĩnh vực lãnh đạo, quản lý xã hội nói chung, nếu thiếu thông tin, không làm chủ được thông tin hoặc không kịp thời cập nhật thông tin thì cũng đồng nghĩa với việc tự làm mất vai trò giáo dục và định hướng tư tưởng. Cho nên cần phải có khả năng nắm bắt và xử lý, chọn lọc thông tin thực sự nhanh, nhạy, chính xác, hiệu quả.
3. Phải biết vận dụng linh hoạt các hình thức tiến hành công tác tư tưởng
Trong những năm tới, trình độ dân trí, trình độ học vấn, nhu cầu nhận thức của bộ đội có sự phát triển rất nhanh chóng. Vì vậy, để công tác tư tưởng ngày càng đi sâu vào cuộc sống, phát huy vai trò to lớn của nó thì tất yếu phải đổi mới hình thức theo hướng đa dạng hoá, phong phú và kết hợp một cách linh hoạt các hình thức công tác tư tưởng; vận dụng một cách linh hoạt, đa dạng và đổi mới thường xuyên mới có thể thu hút và đáp ứng nhu cầu của bộ đội.
4. Phải biết thực hành các phương pháp công tác tư tưởng theo hướng coi trọng phát huy tính tích cực nhận thức của bộ đội
Do tác động của biến đổi cơ cấu xã hội - giai cấp, cơ cấu xã hội vùng miền, phân tầng xã hội dẫn đến thành phần xuất thân của cán bộ, chiến sĩ đa dạng, phức tạp hơn. Nhận thức chính trị, tư tưởng, đạo đức, lối sống không thuần nhất, thậm chí trái ngược nhau cùng với sự tác động nhiều chiều cũng đặt ra những vấn đề mới cho công tác giáo dục mục tiêu, lý tưởng, xây dựng bản chất giai cấp công nhân, xây dựng và phát huy truyền thống của Quân đội.
Đội ngũ cán bộ phải biết quan sát, lắng nghe, thấu hiểu cán bộ, chiến sĩ thuộc quyền; biết nói để cán bộ, chiến sĩ hiểu nhiệm vụ, hiểu bản thân mình và biết làm để cán bộ, chiến sĩ tin tưởng; hiểu, nói và làm để thuyết phục cán bộ, chiến sĩ, hướng dẫn họ biết tự thuyết phục, tự rèn luyện mình và biết hành động vì những điều có lợi cho đời sống, cho đơn vị.
5. Phải có hiểu biết nhất định về đời sống tâm lý quân nhân và tập thể quân nhân
Nắm bắt, quản lý, giải quyết diễn biến tư tưởng là hoạt động đối với đối tượng quân nhân và tập thể quân nhân. Bởi vậy, để nâng cao chất lượng, hiệu quả hoạt động này thì việc hiểu biết đời sống tâm lý quân nhân và tập thể quân nhân, trong đó hiểu và vận dụng các khí chất trong nắm bắt, giải quyết diễn biến tư tưởng cho quân nhân có ý nghĩa hết sức quan trọng.
Trên thực tế, quân nhân vi phạm kỷ luật do không biết kiềm chế, tức giận quá mức, nôn nóng hoặc trơ lỳ tâm lý, không chấp hành mệnh lệnh cấp trên, tìm cách chống đối... đã từng xảy ra ở các đơn vị thông qua các vụ vi phạm kỷ luật, điều đó cho thấy vấn đề khí chất và vận dụng khí chất trong lãnh đạo, quản lý còn chưa được quan tâm đứng mức. Do vậy, hiểu khí chất và vận dụng sáng tạo trong thực tiễn sẽ góp phần đem lại hiệu quả cao đối với hoạt động của đội ngũ cán bộ các cấp.
6. Phải nắm vững và vận dụng linh hoạt các phương pháp
- Phương pháp quán triệt mục tiêu, nhiệm vụ công tác tư tưởng.
- Phương pháp quản lý tư tưởng.
- Phương pháp điều tra nắm tình hình tư tưởng.
- Phương pháp phân tích kết quả hoạt động để nắm tư tưởng.
- Phương pháp dự báo tình hình tư tưởng.
- Phương pháp đề xuất biện pháp quản lý, xử lý tư tưởng.
- Phương pháp nắm bắt đặc điểm tâm sinh lý bộ đội.
- Phương pháp thuyết phục.
- Phương pháp nêu gương.
- Phương pháp đối thoại.
- Phương pháp tuyên truyền, cổ động.
- Phương pháp tổ chức hoạt động VHVN.
- Phương pháp phát động tư tưởng.
- Phương pháp cảm hoá đối tượng cá biệt.
- Phương pháp phát huy sức mạnh tổng hợp để giải quyết tình huống tư tưởng.
- Phương pháp tạo dư luận tích cực.
- Phương pháp tự phê bình và phê bình.
- Phương pháp rèn luyện tư tưởng.
- Phương pháp giáo dục riêng.
7. Thực hiệm nghiêm chế độ báo cáo, thông báo tình hình tư tưởng
a. Báo cáo định kỳ
* Báo cáo tuần
Hàng tuần các đơn vị từ cấp đại đội đến cấp sư đoàn và tương đương báo cáo tình hình tư tưởng lên cấp trên theo phân cấp. Các cơ quan, đơn vị tổ chức giao ban tập trung hoặc trực tuyến thì báo cáo tình hình tư tưởng của cán bộ nhân viên, chiến sỹ trong giao ban. Các cơ quan, đơn vị không tổ chức giao ban tập trung hoặc trực tuyến thì báo cáo bằng điện thoại, điện tín, fax ...; thời gian cụ thể do các cơ quan, đơn vị tự quy định. Các đơn vị trực thuộc Bộ chỉ huy Quân sự tỉnh báo cáo về Phòng Chính trị (qua Ban Tuyên huấn) vào ngày thứ 4 hàng tuần (bằng điện thoại),nội dung báo cáo gồm:
- Những yếu tố tác động đến tư tưởng của cán bộ, nhân viên, chiến sỹ và dư luận nhân dân trên địa bàn.
- Đánh giá chung về: Lòng tin, tâm trạng, dư luận, động cơ, thái độ trách nhiệm, tinh thần yêu mến gắn bó với đơn vị, với công việc được giao…; biện pháp ổn định tình hình tư tưởng của cơ quan, đơn vị, kết quả.
- Những trường hợp có vấn đề về tư tưởng hoặc có những yếu tố tác động ảnh hưởng đến nhận thức tư tưởng và hành động có thể dẫn đến hậu quả xấu cần phải báo cáo cụ thể (họ tên, cấp bậc, chức vụ, diễn biến vụ việc, biện pháp xử lý, kết quả...).
* Báo cáo tháng, quý
- Cấp đại đội, tiểu đoàn và tương đương hàng tháng phải tổng hợp phân loại tư tưởng của đơn vị và báo cáo lên cấp trên theo phân cấp.
- Cấp trung đoàn, sư đoàn và tương tương hàng tháng phải tổng hợp đánh giá khái quát tình hình tư tưởng của đơn vị mình, báo cáo lên cấp trên (kết hợp với báo cáo công tác Tuyên huấn hàng tháng); hàng quý phải tổng hợp tình hình tư tưởng của đơn vị báo cáo cấp trên và thông báo trong toàn đơn vị.
b. Báo cáo đột xuất
- Trường hợp cán bộ, nhân viên, chiến sỹ có vấn đề về tư tưởng hoặc có những yếu tố tác động có thể dẫn đến hành động khó lường, dễ dẫn đến hậu quả xấu, phải báo cáo cụ thể trong giao ban hàng ngày.
- Khi đơn vị có vụ việc nghiêm trọng hoặc dễ dẫn đến hậu quả nghiêm trọng phải báo cáo lên cấp trên trực tiếp bằng điện thoại, điện tín, fax...trong thời gian sớm nhất.
Đội ngũ cán bộ nói chung, cán bộ lãnh đạo, chỉ huy các cấp nói riêng có vai trò quan trọng đối với chất lượng xây dựng, hoàn thành nhiệm vụ của từng cơ quan, đơn vị. Để hoàn thành tốt chức trách, nhiệm vụ được giao, đòi hỏi đội ngũ cán bộ phải có phẩm chất, năng lực cần thiết, trong đó có phương pháp nắm bắt, quản lý và giải quyết diễn biến tư tưởng cho quân nhân. Góp phần tăng cường tính kỷ luật trong quân đội, đáp ứng yêu cầu nhiệm vụ, đặc điểm tình hình của đơn vị.
KẾT LUẬN
Công tác tư tưởng nói chung, công tác nắm, quản lý, định hướng, giải quyết tình hình tư tưởng cho quân nhân ở đơn vị cơ sở nói riêng là một trong những nội dung trọng tâm của hoạt động công tác đảng, công tác chính trị ở đơn vị cơ sở, có vai trò hết sức quan trọng. Đơn vị cơ sở có thật sự vững mạnh toàn diện hay không; tổ chức đảng ở đơn vị cơ sở có thật sự trong sạch vững mạnh hay không một phần tùy thuộc vào kết quả công tác tư tưởng trong quản lý bộ đội của đội ngũ cán bộ các cấp. Cán bộ, chiến sĩ có tư tưởng lành mạnh, tiến bộ sẽ hành động đúng, tích cực; ngược lại, nếu tư tưởng lạc hậu, tiêu cực sẽ hành động sai trái, kìm hãm sự phát triển của đơn vị. Trước yêu cầu nhiệm vụ xây dựng quân đội nói chung, xây dựng LLVT tỉnh trong giai đoạn hiện nay nói riêng, đòi hỏi cấp ủy, chỉ huy, chính ủy, chính trị viên, cơ quan chính trị, các tổ chức quần chúng, Hội đồng quân nhân, đội ngũ cán bộ, đảng viên và toàn thể quân nhân ở đơn vị phải vào cuộc và tiến hành một cách thường xuyên, quyết liệt và thực hiện đồng bộ các giải pháp nhằm giữ vững ổn định về chính trị, phòng ngừa, hạn chế thấp nhất các vụ việc vi phạm kỷ luật thông thường, chấm dứt tình trạng vi phạm pháp luật, kỷ luật nghiêm trọng. Xây dựng bản lĩnh chính trị, ý chí quyêt tâm cho cán bộ, chiến sĩ sẵn sàng nhận và hoàn thành mọi nhiệm vụ được giao, góp phần xây dựng tổ chức đảng trong sạch vững mạnh, cơ quan, đơn vị vững mạnh toàn diện, giữ vững và phát huy phẩm chất truyền thống “Bộ đội Cụ Hồ”./.




















Phần ba: HƯỚNG DẪN THẢO LUẬN, ÔN TẬP

I. NỘI DUNG
Vấn đề 1: Đồng chí cho biết Sự cần thiết phải nâng cao hiệu quả công tác nắm, quản lý, định hướng, giải quyết tư tưởng ở đơn vị cơ sở trong LLVT tỉnh hiện nay?
Vấn đề 2: Đồng chí cho biết những giải pháp nắm, quản lý, định hướng, giải quyết tình hình tư tưởng cho quân nhân Ở đơn vị cơ sở trong LLVT tỉnh?
Vấn đề 3: Đồng chí cho biết trách nhiệm của đội ngũ cán bộ trong tiếp thu, vận dụng phương pháp nắm, quản lý, định hướng, giải quyết tình hình tư tưởng cho quân nhân ở đơn vị cơ sở?
II. TỔ CHỨC, PHƯƠNG PHÁP
1. Tổ chức: Theo đội hình của từng Trung đội.
2. Phương pháp:
Từng cá nhân nghiên tự cứu kỹ nội dung câu hỏi của chuyên đề.
III. THỜI GIAN
Các Trung đội tận dụng thời gian, tổ chức nghiên cứu, thảo luận ngoài giờ.
IV. ĐỊA ĐIỂM
Vị trí phòng họp của từng Trung đội.
V. THÀNH PHẦN
Cán bộ lớp tập huấn.
VI. PHỤ TRÁCH
Phụ trách các đồng chí Trung đội trưởng.
VII. VẬT CHẤT BẢO ĐẢM
- Tài liệu Tập huấn quân sự năm 2019.
	- Vở, viết …
				
	Ngày      tháng 7 năm 2019
NGƯỜI SOẠN BÀI GIẢNG






Đại tá Trần Ngọc Sương

""
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
