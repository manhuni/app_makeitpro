Dưới đây là nội dung chi tiết cho **Lesson 36 - Describing Test Cases (Mô tả các trường hợp kiểm thử)**:

---

## 📘 **Mục tiêu bài học:**

---

### ✅ 1. Từ vựng chính (IPA + nghĩa)

| Từ vựng         | Phiên âm IPA         | Nghĩa tiếng Việt                        |
| --------------- | -------------------- | --------------------------------------- |
| test case       | /test keɪs/          | trường hợp kiểm thử                     |
| input           | /ˈɪnpʊt/             | dữ liệu đầu vào                         |
| expected output | /ɪkˈspektɪd ˈaʊtpʊt/ | đầu ra mong đợi                         |
| edge case       | /ɛdʒ keɪs/           | trường hợp đặc biệt, giới hạn           |
| invalid         | /ɪnˈvælɪd/           | không hợp lệ                            |
| assertion       | /əˈsɜːʃən/           | điều kiện kiểm tra (mệnh đề xác nhận)   |
| pass            | /pɑːs/               | vượt qua (kiểm thử thành công)          |
| fail            | /feɪl/               | thất bại (kiểm thử không thành công)    |
| scenario        | /səˈnɑːriəʊ/         | kịch bản (tình huống thử nghiệm cụ thể) |
| boundary value  | /ˈbaʊndəri ˈvæljuː/  | giá trị biên                            |

---

### ✅ 2. Câu mẫu thực tế

| Mẫu câu                                                       | Dịch nghĩa                                                            |
| ------------------------------------------------------------- | --------------------------------------------------------------------- |
| This test case checks if the login fails with wrong password. | Trường hợp kiểm thử này kiểm tra đăng nhập thất bại khi mật khẩu sai. |
| We need to add edge cases for empty input values.             | Chúng ta cần thêm các trường hợp đặc biệt khi dữ liệu đầu vào rỗng.   |
| The expected output for this scenario is an error message.    | Đầu ra mong đợi cho tình huống này là một thông báo lỗi.              |
| All test cases passed successfully.                           | Tất cả các trường hợp kiểm thử đã vượt qua thành công.                |
| This function fails when the input is null.                   | Hàm này thất bại khi đầu vào là null.                                 |

---

### ✅ 3. Bài luyện viết ✍️

**Đề bài:**
Viết mô tả cho **3 test cases** đơn giản của một chức năng quen thuộc, ví dụ: kiểm tra hàm đăng nhập, tính tổng, hoặc lọc danh sách.

**Mẫu mô tả:**

```
Test Case 1: Valid login
- Input: username = "john", password = "1234"
- Expected Output: Redirect to dashboard

Test Case 2: Invalid password
- Input: username = "john", password = "wrongpass"
- Expected Output: Show error message: "Invalid credentials"

Test Case 3: Empty input
- Input: username = "", password = ""
- Expected Output: Show error: "Please enter username and password"
```

---

### ✅ 4. Bài luyện nói 🎤

**Chủ đề:**
**Describe one of your test cases.**

**Gợi ý trình bày (30–60 giây):**

* What feature were you testing?
* What was the input?
* What was the expected result?
* Did the test pass or fail?
* Any edge cases you considered?

---

### ✅ 5. Ghi chú mở rộng

* **Phân loại test cases:**

  * **Positive case**: kiểm tra hành vi đúng.
  * **Negative case**: kiểm tra hành vi sai hoặc lỗi.
  * **Edge case**: kiểm tra giới hạn, biên độ.
  * **Null/empty input**: kiểm tra với dữ liệu thiếu hoặc rỗng.

* **Cụm từ hữu ích khi mô tả test cases:**

  * *Handles gracefully* → xử lý một cách ổn định
  * *Throws an exception* → ném ra ngoại lệ
  * *Matches expected behavior* → khớp với hành vi mong đợi
  * *Under specific condition* → dưới điều kiện cụ thể

* **Tips khi mô tả test cases:**

  * Nêu rõ mục tiêu kiểm thử.
  * Ghi rõ input và output.
  * Dễ hiểu với cả người viết mã và kiểm thử viên.

---

Bạn muốn mình viết test cases mẫu cho một tính năng cụ thể bạn đang làm không? Hoặc bạn muốn thực hành nói theo một tình huống thật?
