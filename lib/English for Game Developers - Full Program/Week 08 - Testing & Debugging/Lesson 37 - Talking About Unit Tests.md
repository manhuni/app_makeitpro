**Lesson 37 - Talking About Unit Tests (Nói về kiểm thử đơn vị)**:

---

## 📘 **Mục tiêu bài học:**

---

### ✅ 1. Từ vựng chính (IPA + nghĩa)

| Từ vựng       | Phiên âm IPA     | Nghĩa tiếng Việt                                |
| ------------- | ---------------- | ----------------------------------------------- |
| unit test     | /ˈjuːnɪt test/   | kiểm thử đơn vị (kiểm thử từng phần nhỏ của mã) |
| function      | /ˈfʌŋkʃən/       | hàm / chức năng                                 |
| test coverage | /test ˈkʌvərɪdʒ/ | độ bao phủ kiểm thử                             |
| assertion     | /əˈsɜːʃən/       | điều kiện kiểm tra (kỳ vọng đúng/sai)           |
| mock          | /mɒk/            | mô phỏng (dữ liệu hoặc đối tượng giả)           |
| dependency    | /dɪˈpendənsi/    | thành phần phụ thuộc                            |
| pass          | /pɑːs/           | vượt qua (kiểm thử thành công)                  |
| fail          | /feɪl/           | thất bại (kiểm thử không thành công)            |
| isolated      | /ˈaɪsəleɪtɪd/    | tách biệt (kiểm thử một đơn vị độc lập)         |
| regression    | /rɪˈɡreʃ.ən/     | lỗi phát sinh khi thay đổi mã                   |

---

### ✅ 2. Câu mẫu thực tế

| Câu mẫu                                                          | Dịch nghĩa                                                |
| ---------------------------------------------------------------- | --------------------------------------------------------- |
| This unit test checks if the function returns the correct value. | Bài kiểm thử này kiểm tra hàm có trả giá trị đúng không.  |
| We use mocks to isolate the dependencies.                        | Chúng tôi dùng mock để tách biệt các phần phụ thuộc.      |
| All unit tests passed after the refactoring.                     | Tất cả kiểm thử đơn vị đều vượt qua sau khi tái cấu trúc. |
| The test failed because the input was not handled correctly.     | Kiểm thử thất bại do đầu vào không được xử lý đúng.       |
| Increasing test coverage is our next priority.                   | Tăng độ bao phủ kiểm thử là ưu tiên tiếp theo của nhóm.   |

---

### ✅ 3. Bài luyện viết ✍️

**Đề bài:**
Viết mô tả cho **2 unit tests** bạn sẽ viết cho một hàm tính tổng (`sum(a, b)`).

**Ví dụ:**

```
Test: sum of two positive numbers
- Input: a = 2, b = 3
- Expected Output: 5

Test: sum with negative number
- Input: a = -2, b = 5
- Expected Output: 3
```

---

### ✅ 4. Bài luyện nói 🎤

**Chủ đề:**
**Describe a unit test you wrote or reviewed.**

**Gợi ý trình bày (30–60 giây):**

* What was the function being tested?
* What were the inputs and expected outputs?
* Was it a positive or negative test case?
* Did you use mocking or stubbing?
* What was the result?

---

### ✅ 5. Ghi chú mở rộng

* **Unit test là gì?**

  * Kiểm tra hành vi của **một đơn vị mã nhỏ nhất** (thường là một hàm hoặc phương thức).
  * Giúp phát hiện lỗi sớm và đảm bảo các thay đổi không gây **regression**.

* **Các công cụ thường dùng:**

  * JavaScript: Jest, Mocha
  * Python: unittest, pytest
  * Java: JUnit
  * C#: NUnit, xUnit

* **Tips khi viết unit tests:**

  * Viết test cho cả **trường hợp thường** và **ngoại lệ**.
  * Đảm bảo mỗi test chỉ kiểm tra **một hành vi cụ thể**.
  * Tránh phụ thuộc vào môi trường ngoài (dùng mock nếu cần).
  * Đặt tên test rõ ràng: `shouldReturnZeroWhenInputsAreZero()`

---

Bạn muốn mình tạo ví dụ unit test bằng ngôn ngữ cụ thể (JavaScript, Python, v.v.) hoặc giúp luyện nói theo một đoạn mã bạn đang có không?
