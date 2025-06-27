**Lesson 40 - Fixing Regression Bugs (Sửa lỗi hồi quy)**:

---

## 📘 **Mục tiêu bài học:**

---

### ✅ 1. Từ vựng chính (IPA + nghĩa)

| Từ vựng                | Phiên âm IPA              | Nghĩa tiếng Việt                                    |
| ---------------------- | ------------------------- | --------------------------------------------------- |
| regression bug         | /rɪˈɡreʃ.ən bʌɡ/          | lỗi hồi quy (lỗi xuất hiện lại sau khi đã được sửa) |
| recent change          | /ˈriːsənt ʧeɪndʒ/         | thay đổi gần đây                                    |
| unintended behavior    | /ʌnɪnˈtendɪd bɪˈheɪvjər/  | hành vi không mong muốn                             |
| root cause             | /ruːt kɔːz/               | nguyên nhân gốc                                     |
| rollback               | /ˈrəʊlbæk/                | quay lui lại phiên bản cũ                           |
| patch                  | /pætʃ/                    | bản vá lỗi                                          |
| test suite             | /tɛst swiːt/              | bộ kiểm thử                                         |
| version control        | /ˈvɜːʃən kənˈtrəʊl/       | hệ thống quản lý phiên bản (Git, SVN...)            |
| backward compatibility | /ˈbækwəd kəmˌpætəˈbɪləti/ | khả năng tương thích ngược (với phiên bản cũ)       |
| hotfix                 | /ˈhɒt.fɪks/               | bản vá nóng, sửa lỗi khẩn cấp                       |

---

### ✅ 2. Câu mẫu thực tế

| Câu mẫu                                                                 | Dịch nghĩa                                                                            |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| We introduced a regression bug in the login flow after the last update. | Sau bản cập nhật gần đây, chúng tôi vô tình gây ra lỗi hồi quy trong luồng đăng nhập. |
| The root cause was a missing check in the authentication module.        | Nguyên nhân gốc là thiếu kiểm tra trong mô-đun xác thực.                              |
| We fixed the regression and added a test to prevent it in the future.   | Chúng tôi đã sửa lỗi hồi quy và thêm kiểm thử để ngăn lỗi tái diễn.                   |
| A rollback was needed because the bug affected production users.        | Phải quay lại phiên bản cũ vì lỗi ảnh hưởng đến người dùng thật.                      |
| Regression bugs are often caused by poor test coverage.                 | Lỗi hồi quy thường do độ bao phủ kiểm thử kém gây ra.                                 |

---

### ✅ 3. Bài luyện viết ✍️

**Đề bài:**
Viết một báo cáo lỗi hồi quy ngắn gọn gồm các phần:

* Mô tả lỗi
* Khi nào xuất hiện
* Nguyên nhân gốc
* Giải pháp

**Mẫu:**

```
Regression Bug Report:
- Bug: Clicking “Submit” no longer saves the form.
- When: After deploying v2.3
- Cause: A recent refactor removed the onClick handler.
- Fix: Re-added the handler and created a test for form submission.
```

---

### ✅ 4. Bài luyện nói 🎤

**Chủ đề:**
**Describe how you discovered and fixed a regression bug.**

**Gợi ý trình bày (30–60 giây):**

* What was the symptom of the bug?
* When did it start happening?
* How did you investigate it?
* What was the fix?
* What did you do to prevent it in the future?

---

### ✅ 5. Ghi chú mở rộng

* **Lỗi hồi quy (Regression bug)** là lỗi:

  * Đã từng được sửa
  * Nhưng quay trở lại do thay đổi mới (refactor, thêm tính năng, update thư viện…)

* **Cách phòng tránh lỗi hồi quy:**

  * Tăng độ bao phủ của kiểm thử tự động (unit test, integration test)
  * Dùng CI/CD để kiểm tra lại sau mỗi lần đẩy mã
  * Code review kỹ khi thay đổi các phần cốt lõi

* **Chiến lược xử lý khi gặp regression:**

  1. Xác nhận lỗi là mới phát sinh.
  2. So sánh thay đổi gần đây (git diff).
  3. Dùng git bisect để tìm commit gây lỗi.
  4. Sửa lỗi và cập nhật kiểm thử liên quan.
  5. Nếu lỗi nghiêm trọng: rollback hoặc hotfix.

---

Bạn muốn mình tạo thêm ví dụ về lỗi hồi quy trong một đoạn mã cụ thể (JS, Python, v.v.) để bạn luyện mô tả hoặc phân tích không?
