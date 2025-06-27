**Lesson 48 - Build Process and Errors (Quy trình build và lỗi khi build)**:

---

## 📘 **Mục tiêu bài học**

---

### ✅ 1. Từ vựng chính (IPA + nghĩa)

| Từ vựng                | Phiên âm IPA               | Nghĩa tiếng Việt                         |
| ---------------------- | -------------------------- | ---------------------------------------- |
| build process          | /bɪld ˈprəʊses/            | quy trình biên dịch / đóng gói phần mềm  |
| build error            | /bɪld ˈerə(r)/             | lỗi khi biên dịch hoặc đóng gói          |
| dependency             | /dɪˈpendənsi/              | sự phụ thuộc (giữa các thư viện/module)  |
| compile                | /kəmˈpaɪl/                 | biên dịch (chuyển mã nguồn thành mã máy) |
| syntax error           | /ˈsɪntæks ˈerə(r)/         | lỗi cú pháp                              |
| missing file           | /ˈmɪsɪŋ faɪl/              | thiếu file                               |
| incompatible version   | /ɪnˌkɒmpətəˈbəl ˈvɜːʃn/    | phiên bản không tương thích              |
| environment variable   | /ɪnˈvaɪrənmənt ˈveəriəbl/  | biến môi trường (hệ thống)               |
| configuration          | /kənˌfɪɡjəˈreɪʃn/          | cấu hình                                 |
| continuous integration | /kənˈtɪnjuəs ˌɪntɪˈɡreɪʃn/ | tích hợp liên tục (CI)                   |

---

### ✅ 2. Câu mẫu thực tế

| Câu mẫu                                                                   | Dịch nghĩa                                                         |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| The build failed due to a missing dependency.                             | Quá trình build thất bại do thiếu thư viện phụ thuộc.              |
| We’re getting a syntax error in the main configuration file.              | Chúng tôi đang gặp lỗi cú pháp trong file cấu hình chính.          |
| The build works locally but fails on the CI server.                       | Build chạy được trên máy cá nhân nhưng bị lỗi khi chạy trên CI.    |
| The error message suggests that the compiler couldn’t find a header file. | Thông báo lỗi cho biết trình biên dịch không tìm thấy file header. |
| I fixed the issue by updating the environment variables.                  | Tôi đã sửa lỗi bằng cách cập nhật biến môi trường.                 |

---

### ✅ 3. Bài luyện viết ✍️

**Đề bài:**
Viết một đoạn mô tả lỗi build mà bạn từng gặp. Bao gồm thông báo lỗi chính, nguyên nhân, và cách bạn đã sửa.

**Mẫu:**

```
During the build, we encountered the following error:

"ModuleNotFoundError: No module named 'xyz'"

It turned out that the 'xyz' module was not included in the project’s requirements file. 
To fix this, we added it to `requirements.txt` and re-ran the build. 
The issue was resolved after that.
```

---

### ✅ 4. Bài luyện nói 🎤

**Chủ đề:**
**Talk about a build error and how you solved it.**

**Gợi ý trình bày (30–60 giây):**

* What was the error message?
* When did it happen (local or CI)?
* What was the root cause?
* How did you fix or work around it?

---

### ✅ 5. Ghi chú mở rộng

#### ⚙️ **Các lỗi build phổ biến**

| Lỗi                  | Mô tả                                             |
| -------------------- | ------------------------------------------------- |
| Missing dependency   | Chưa cài module / thư viện cần thiết              |
| Compilation error    | Lỗi biên dịch (cú pháp, kiểu dữ liệu sai...)      |
| Path error           | File không tồn tại hoặc đường dẫn sai             |
| Environment mismatch | Cấu hình máy local khác với môi trường build      |
| Version conflict     | Hai thư viện dùng hai phiên bản không tương thích |

#### 🛠️ **Mẹo xử lý lỗi build**

* Đọc kỹ **log lỗi**, đặc biệt là dòng đầu và cuối
* Kiểm tra **cấu hình môi trường**
* So sánh **máy local vs CI**
* Thử chạy lại sau khi **dọn cache**
* Sử dụng lệnh như:

  * `npm ci` (Node.js)
  * `--stacktrace` (Gradle)
  * `make clean && make` (C/C++)

#### 🧪 **Tích hợp liên tục (CI) thường gây lỗi gì?**

| Tình huống                              | Lý do thường gặp                                          |
| --------------------------------------- | --------------------------------------------------------- |
| Build lỗi trên CI nhưng không lỗi local | Thiếu thiết lập biến môi trường, phiên bản tool khác nhau |
| Test bị fail bất thường                 | Dữ liệu giả lập không nhất quán hoặc sai cấu hình         |

---

Bạn có muốn mình giúp tạo **một mẫu báo cáo lỗi build chuyên nghiệp** hoặc đoạn hội thoại kỹ thuật (developer chat) về lỗi build?
