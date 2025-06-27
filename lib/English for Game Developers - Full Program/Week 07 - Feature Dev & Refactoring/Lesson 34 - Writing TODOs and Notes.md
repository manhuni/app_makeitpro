**Lesson 34 - Writing TODOs and Notes (Viết ghi chú và công việc cần làm trong mã nguồn)**:

---

## 📘 **Mục tiêu bài học:**

---

### ✅ 1. Từ vựng chính (IPA + nghĩa)

| Từ vựng           | Phiên âm IPA          | Nghĩa tiếng Việt                         |
| ----------------- | --------------------- | ---------------------------------------- |
| TODO              | /tuːˈduː/             | việc cần làm (thường ghi chú trong code) |
| comment           | /ˈkɒment/             | chú thích (trong mã nguồn)               |
| placeholder       | /ˈpleɪshəʊldər/       | phần giữ chỗ                             |
| reminder          | /rɪˈmaɪndər/          | lời nhắc                                 |
| note              | /nəʊt/                | ghi chú                                  |
| temporary fix     | /ˈtɛmpərəri fɪks/     | cách sửa tạm thời                        |
| follow-up         | /ˈfɒləʊ ʌp/           | công việc tiếp theo / theo dõi tiếp      |
| clarification     | /ˌklærɪfɪˈkeɪʃən/     | sự làm rõ                                |
| clean-up          | /ˈkliːn ʌp/           | dọn dẹp / làm gọn lại                    |
| legacy workaround | /ˈleɡəsi ˈwɜːkəraʊnd/ | giải pháp tạm thời cho mã cũ             |

---

### ✅ 2. Câu mẫu thực tế

| Mẫu câu / Ghi chú thường gặp trong mã                    | Giải thích tiếng Việt                                   |
| -------------------------------------------------------- | ------------------------------------------------------- |
| `// TODO: Refactor this method to improve readability.`  | TODO: Tái cấu trúc phương thức này để dễ đọc hơn.       |
| `// NOTE: This function only works with valid inputs.`   | Ghi chú: Hàm này chỉ hoạt động với dữ liệu hợp lệ.      |
| `// FIXME: This is a temporary fix for the login bug.`   | Sửa lỗi: Đây là cách xử lý tạm thời cho lỗi đăng nhập.  |
| `// TODO: Add unit tests for edge cases.`                | TODO: Thêm kiểm thử đơn vị cho các trường hợp đặc biệt. |
| `// HACK: Using legacy workaround until API is updated.` | Tạm dùng giải pháp cũ cho đến khi API được cập nhật.    |

---

### ✅ 3. Bài luyện viết ✍️

**Đề bài:**
Hãy viết 5 dòng ghi chú giả định mà bạn có thể thêm vào trong một đoạn mã thật (TODO, NOTE, FIXME, HACK…). Mỗi dòng nên thể hiện rõ mục đích và dễ hiểu cho người khác.

**Ví dụ:**

```js
// TODO: Optimize this loop for better performance.
// FIXME: Handle null values returned from the API.
// NOTE: This component uses a deprecated method.
// TODO: Migrate this file to TypeScript.
// HACK: Delay added to avoid race condition (needs fix).
```

---

### ✅ 4. Bài luyện nói 🎤

**Chủ đề:**
**Explain the purpose of a TODO or note you recently wrote.**
(Hãy giải thích mục đích của một ghi chú hoặc TODO bạn đã viết gần đây.)

**Gợi ý trình bày (30–60 giây):**

* What was the context?
* What did the TODO/note say?
* Why was it important?
* Did you or someone follow up on it?

---

### ✅ 5. Ghi chú mở rộng

* **Khi nào nên viết TODO?**

  * Khi bạn phát hiện điều gì đó cần làm nhưng chưa làm ngay được.
  * Khi cần đồng đội xử lý một phần riêng.
  * Khi biết có vấn đề nhưng cần thêm thông tin / quyết định.

* **Cấu trúc thường dùng:**

  * `TODO: [việc cần làm]`
  * `FIXME: [lỗi cần sửa]`
  * `NOTE: [lưu ý cho người đọc mã]`
  * `HACK: [giải pháp tạm thời]`

* **Tips để TODO hiệu quả:**

  * Viết rõ ràng, ngắn gọn, có mục tiêu.
  * Có thể thêm tên người phụ trách: `TODO (John): Refactor...`
  * Đừng để TODO quá lâu không giải quyết — nên lập kế hoạch xử lý.

---

Bạn muốn mình giúp viết một ví dụ TODO cho dự án cụ thể hoặc luyện nói theo mẫu không?
