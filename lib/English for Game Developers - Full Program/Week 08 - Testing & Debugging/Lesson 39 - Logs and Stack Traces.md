**Lesson 39 - Logs and Stack Traces (Nhật ký và dấu vết ngăn xếp)**:

---

## 📘 **Mục tiêu bài học:**

---

### ✅ 1. Từ vựng chính (IPA + nghĩa)

| Từ vựng        | Phiên âm IPA      | Nghĩa tiếng Việt                             |
| -------------- | ----------------- | -------------------------------------------- |
| log            | /lɒɡ/             | nhật ký (ghi lại hoạt động của chương trình) |
| logging        | /ˈlɒɡɪŋ/          | việc ghi log                                 |
| stack trace    | /stæk treɪs/      | dấu vết ngăn xếp (thông tin khi lỗi xảy ra)  |
| error message  | /ˈerər ˈmesɪdʒ/   | thông báo lỗi                                |
| exception      | /ɪkˈsepʃən/       | ngoại lệ                                     |
| line number    | /laɪn ˈnʌmbər/    | số dòng (trong mã nguồn)                     |
| trace          | /treɪs/           | lần theo, theo dõi                           |
| output         | /ˈaʊtpʊt/         | đầu ra                                       |
| crash log      | /kræʃ lɒɡ/        | log khi chương trình sập                     |
| debugging tool | /ˌdiːˈbʌɡɪŋ tuːl/ | công cụ gỡ lỗi                               |

---

### ✅ 2. Câu mẫu thực tế

| Câu mẫu                                                               | Dịch nghĩa                                                           |
| --------------------------------------------------------------------- | -------------------------------------------------------------------- |
| The error log shows a null pointer exception at line 54.              | Nhật ký lỗi hiển thị lỗi con trỏ null tại dòng 54.                   |
| I used the stack trace to find where the function failed.             | Tôi đã dùng stack trace để tìm nơi hàm bị lỗi.                       |
| Logging the response helped us identify the API issue.                | Việc ghi log phản hồi giúp chúng tôi xác định lỗi từ API.            |
| The app crashed, but we found the reason in the crash log.            | Ứng dụng bị sập, nhưng chúng tôi tìm ra nguyên nhân trong crash log. |
| The logger prints useful debug info when the level is set to "debug". | Logger sẽ in thông tin gỡ lỗi khi mức được đặt là "debug".           |

---

### ✅ 3. Bài luyện viết ✍️

**Đề bài:**
Giả sử bạn vừa gặp một lỗi và thấy một stack trace. Viết mô tả lỗi như một ghi chú trong báo cáo lỗi.

**Mẫu:**

```
Error Report:
- Error: TypeError - Cannot read property 'length' of undefined
- Location: file.js, line 27
- Cause: The variable "data" was undefined when trying to access its length.
- Fix: Add a check to ensure "data" is defined before calling .length
```

---

### ✅ 4. Bài luyện nói 🎤

**Chủ đề:**
**Describe how you used logs or stack traces to debug a problem.**

**Gợi ý trình bày (30–60 giây):**

* What was the problem?
* What log or message did you see?
* What did the stack trace show?
* How did you fix or trace the root cause?

---

### ✅ 5. Ghi chú mở rộng

* **Mục đích của log:**

  * Theo dõi hoạt động (debug, info, warn, error)
  * Phân tích hành vi người dùng hoặc hệ thống
  * Gỡ lỗi mà không cần tái tạo lỗi ngay lập tức

* **Các mức độ log phổ biến:**

  * `DEBUG`: Thông tin chi tiết cho lập trình viên
  * `INFO`: Thông tin bình thường về tiến trình
  * `WARN`: Cảnh báo, không gây crash nhưng cần chú ý
  * `ERROR`: Lỗi nghiêm trọng, cần xử lý
  * `FATAL`: Lỗi nghiêm trọng khiến hệ thống ngừng hoạt động

* **Stack trace thường gồm:**

  * Loại lỗi (exception type)
  * Thông điệp lỗi
  * Danh sách các hàm đã được gọi trước khi lỗi xảy ra
  * Tên tệp + số dòng (giúp định vị mã nguồn)

* **Tips:**

  * Luôn log thông tin cần thiết, tránh log quá mức (log noise).
  * Không log dữ liệu nhạy cảm (mật khẩu, thông tin người dùng).
  * Đọc stack trace từ **trên xuống dưới** để thấy lỗi gốc.

---

Bạn muốn mình mô phỏng một stack trace thực tế và hướng dẫn cách phân tích nó không? Hoặc bạn có log cụ thể cần giải thích?
