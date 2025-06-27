**Lesson 35 - Writing Code Comments (Viết chú thích trong mã nguồn)**:

---

## 📘 **Mục tiêu bài học:**

---

### ✅ 1. Từ vựng chính (IPA + nghĩa)

| Từ vựng          | Phiên âm IPA           | Nghĩa tiếng Việt              |
| ---------------- | ---------------------- | ----------------------------- |
| comment          | /ˈkɒment/              | chú thích (trong mã nguồn)    |
| inline comment   | /ˈɪnlaɪn ˈkɒment/      | chú thích trong dòng          |
| block comment    | /blɒk ˈkɒment/         | chú thích nhiều dòng          |
| self-explanatory | /ˌself.ɪkˈsplænə.təri/ | tự giải thích được, dễ hiểu   |
| intention        | /ɪnˈtenʃən/            | mục đích (của đoạn mã)        |
| clarify          | /ˈklærɪfaɪ/            | làm rõ                        |
| annotation       | /ˌænəˈteɪʃən/          | chú giải / ghi chú            |
| maintainability  | /meɪnˌteɪnəˈbɪləti/    | khả năng duy trì, bảo trì mã  |
| confusing logic  | /kənˈfjuːzɪŋ ˈlɒdʒɪk/  | logic gây nhầm lẫn            |
| best practice    | /best ˈpræktɪs/        | phương pháp tối ưu, chuẩn mực |

---

### ✅ 2. Câu mẫu thực tế

| Câu ví dụ / Ghi chú trong mã nguồn                                  | Giải thích tiếng Việt                                          |
| ------------------------------------------------------------------- | -------------------------------------------------------------- |
| `// Check if the user is logged in before proceeding.`              | Kiểm tra người dùng đã đăng nhập chưa trước khi tiếp tục.      |
| `// This function handles file uploads via drag-and-drop.`          | Hàm này xử lý việc tải tệp bằng cách kéo thả.                  |
| `/* This loop calculates the total score from all test cases. */`   | Vòng lặp này tính tổng điểm từ tất cả các trường hợp kiểm thử. |
| `// Avoid modifying this value directly – use setConfig() instead.` | Tránh thay đổi trực tiếp giá trị này – dùng setConfig().       |
| `// TODO: Refactor to remove duplication with fetchData()`          | TODO: Tái cấu trúc để loại bỏ trùng lặp với hàm fetchData().   |

---

### ✅ 3. Bài luyện viết ✍️

**Đề bài:**
Viết 4–5 dòng chú thích phù hợp cho các phần mã sau (bạn có thể tưởng tượng mã là gì). Mỗi chú thích nên rõ ràng, mô tả mục đích hoặc hành vi chính.

**Gợi ý ví dụ:**

```js
// Initialize user profile with default values

// Return error if file size exceeds 5MB

// This block handles token expiration and refresh

// Disable button if required fields are empty
```

---

### ✅ 4. Bài luyện nói 🎤

**Chủ đề:**
**Explain a code comment you wrote recently.**
(Hãy giải thích một chú thích bạn đã viết gần đây.)

**Gợi ý trình bày (30–60 giây):**

* What part of the code did it describe?
* Why did you add the comment?
* Was the logic unclear or complex?
* Did someone give feedback on it?

---

### ✅ 5. Ghi chú mở rộng

* **Khi nào nên viết comment?**

  * Khi đoạn mã không tự giải thích rõ ràng.
  * Khi cần cảnh báo lập trình viên khác (ví dụ: logic phức tạp, lỗi tiềm ẩn).
  * Khi ghi chú TODO, FIXME hoặc lý do dùng workaround.

* **Viết comment hiệu quả:**

  * Ngắn gọn, rõ ràng, không dư thừa.
  * Tránh viết những điều hiển nhiên (ví dụ: `// add 1 to x` sau `x = x + 1` là không cần thiết).
  * Sử dụng tiếng Anh chuẩn, dễ hiểu với người đọc sau.

* **Best practices:**

  * Viết để người khác hiểu mục đích, không chỉ hành vi.
  * Ưu tiên viết mã dễ hiểu trước khi thêm comment.
  * Định kỳ kiểm tra comment cũ để cập nhật hoặc loại bỏ khi không còn đúng.

---

Bạn muốn mình đưa ví dụ thực tế (ví dụ: comment cho mã Python/JS) hoặc giúp luyện nói theo một đoạn mã cụ thể không?
