**Lesson 33 - Refactoring Legacy Code (Tái cấu trúc mã cũ)**:

---

## 📘 **Mục tiêu bài học:**

---

### ✅ 1. Từ vựng chính (IPA + nghĩa)

| Từ vựng         | Phiên âm IPA        | Nghĩa tiếng Việt                                         |
| --------------- | ------------------- | -------------------------------------------------------- |
| refactor        | /ˌriːˈfæktər/       | tái cấu trúc (mã nguồn)                                  |
| legacy code     | /ˈleɡəsi kəʊd/      | mã cũ (mã từ hệ thống cũ, thường khó bảo trì)            |
| maintainability | /meɪnˌteɪnəˈbɪləti/ | khả năng bảo trì                                         |
| readability     | /ˌriːdəˈbɪləti/     | khả năng đọc hiểu (mã, tài liệu)                         |
| modular         | /ˈmɒdʒələr/         | theo mô-đun                                              |
| duplicate code  | /ˈdjuːplɪkət kəʊd/  | mã trùng lặp                                             |
| function        | /ˈfʌŋkʃən/          | hàm                                                      |
| variable naming | /ˈveəriəbl ˈneɪmɪŋ/ | cách đặt tên biến                                        |
| codebase        | /ˈkəʊd.beɪs/        | toàn bộ mã nguồn của dự án                               |
| regression bug  | /rɪˈɡreʃən bʌɡ/     | lỗi tái phát (do thay đổi code gây lỗi cũ xuất hiện lại) |

---

### ✅ 2. Câu mẫu thực tế

| Mẫu câu                                                      | Dịch nghĩa                                                                    |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| We need to refactor this legacy code to improve performance. | Chúng ta cần tái cấu trúc mã cũ này để cải thiện hiệu suất.                   |
| The current codebase has a lot of duplicate logic.           | Mã nguồn hiện tại có rất nhiều đoạn logic trùng lặp.                          |
| Improving readability will make future maintenance easier.   | Việc cải thiện khả năng đọc hiểu sẽ giúp bảo trì dễ dàng hơn trong tương lai. |
| We split the logic into smaller, modular functions.          | Chúng tôi đã tách logic thành các hàm nhỏ theo mô-đun.                        |
| Refactoring introduced a regression bug in the payment flow. | Việc tái cấu trúc đã gây ra lỗi tái phát trong quy trình thanh toán.          |

---

### ✅ 3. Bài luyện viết ✍️

**Đề bài:**
Viết một đoạn văn (5–7 câu) mô tả một lần bạn hoặc nhóm của bạn phải tái cấu trúc mã cũ. Tập trung vào lý do, những thay đổi chính và kết quả.

**Gợi ý khởi đầu:**

> Last month, we had to refactor a large section of legacy code because...

---

### ✅ 4. Bài luyện nói 🎤

**Chủ đề:**
**Talk about a time when you worked with legacy code.**
(Hãy nói về một lần bạn làm việc với mã cũ.)

**Gợi ý trình bày (dưới 1 phút):**

* What was the problem with the legacy code?
* How did you approach refactoring it?
* What challenges did you face?
* What was the outcome?

---

### ✅ 5. Ghi chú mở rộng

* **Tips khi refactor legacy code:**

  * Viết test trước khi sửa (write tests before refactoring).
  * Giữ thay đổi nhỏ và có thể đo lường.
  * Luôn commit theo từng bước.

* **Cụm từ kỹ thuật hữu ích:**

  * *code smell*: dấu hiệu cho thấy code cần được cải tiến.
  * *technical debt*: nợ kỹ thuật (mã cũ chưa được tối ưu gây khó khăn sau này).
  * *unit test coverage*: phạm vi được kiểm thử đơn vị.

---

Bạn có muốn mình viết đoạn văn hoặc mô phỏng đoạn luyện nói để bạn thực hành không?
