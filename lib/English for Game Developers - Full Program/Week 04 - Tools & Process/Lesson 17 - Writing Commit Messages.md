Dưới đây là nội dung chi tiết cho:

---

# ✅ Lesson 17 – Writing Commit Messages

> 📘 **Mục tiêu bài học:**

* ✅ Hiểu được vai trò của commit message trong quá trình phát triển phần mềm.
* ✅ Sử dụng từ vựng chuyên ngành để mô tả hành động thay đổi mã nguồn.
* ✅ Viết được commit message rõ ràng, ngắn gọn, có mục đích.

---

## 📚 Từ vựng chính (IPA + nghĩa)

| Từ vựng / Cụm từ | Phiên âm IPA        | Nghĩa                                                    |
| ---------------- | ------------------- | -------------------------------------------------------- |
| commit message   | /kəˈmɪt ˈmes.ɪdʒ/   | tin nhắn đi kèm khi commit thay đổi vào Git              |
| concise          | /kənˈsaɪs/          | ngắn gọn, súc tích                                       |
| descriptive      | /dɪˈskrɪp.tɪv/      | có tính mô tả                                            |
| refactor         | /ˌriːˈfæk.tər/      | tái cấu trúc (code) mà không thay đổi hành vi            |
| feature          | /ˈfiː.tʃər/         | tính năng                                                |
| bug fix          | /bʌɡ fɪks/          | sửa lỗi                                                  |
| breaking change  | /ˈbreɪ.kɪŋ tʃeɪndʒ/ | thay đổi làm hỏng tính năng cũ / không tương thích ngược |
| initial commit   | /ɪˈnɪʃ.əl kəˈmɪt/   | commit đầu tiên của dự án                                |
| revert           | /rɪˈvɜːt/           | hoàn tác một commit trước đó                             |
| changelog        | /ˈtʃeɪndʒ.lɒɡ/      | nhật ký thay đổi                                         |

---

## 🗣️ Câu mẫu thực tế

### 1. Mô tả commit:

* This commit **adds a new login feature**.
* I **refactored** the game loop to improve performance.
* Fixed a **bug** related to audio playback on mobile.

### 2. Giải thích commit message:

* Your commit message should be **clear** and **concise**.
* Use the imperative mood: e.g., "Add", "Fix", "Update", not "Added" or "Fixed".
* Avoid vague messages like “update” or “change code”.

### 3. Theo convention:

* We follow the **Conventional Commits** format in our project.
* Example: `feat: add support for multiplayer mode`
* Example: `fix: resolve crash when loading assets`

---

## ✍️ Bài luyện viết (Writing Practice)

> Viết 5 commit message rõ ràng cho những hành động sau:

1. Thêm màn hình cài đặt vào game.
2. Sửa lỗi không phát nhạc khi vào menu.
3. Tối ưu hóa code xử lý chuyển cảnh.
4. Tạo file README.md đầu tiên cho project.
5. Xóa chức năng chưa dùng đến.

**Gợi ý:**

* `feat: add settings screen`
* `fix: audio not playing in main menu`
* `refactor: optimize scene transition logic`
* `docs: add initial README file`
* `chore: remove unused feature toggle`

---

## 🎤 Bài luyện nói (Speaking Practice)

> Trả lời và luyện nói các câu sau:

1. How do you usually write your commit messages?
2. Why are clear commit messages important in a team?
3. What do you think of using a commit message format (like Conventional Commits)?

**Gợi ý mở đầu:**

* “I usually write short but clear commit messages that describe what I changed…”
* “Clear messages help us review changes faster and avoid misunderstandings…”
* “We use a format like `type: short message` to stay consistent…”

---

## 🧠 Ghi chú mở rộng

### ⚙️ Format phổ biến: Conventional Commits

```bash
<type>(optional scope): <short description>

types phổ biến:
- feat: thêm tính năng mới
- fix: sửa lỗi
- refactor: tái cấu trúc mà không thay đổi hành vi
- chore: công việc lặt vặt, không ảnh hưởng tới logic chính
- docs: tài liệu
- test: thêm/sửa test
- style: format code, không ảnh hưởng logic
```

**Ví dụ:**

* `feat(game): add level selection screen`
* `fix(ui): button not responding on click`
* `chore: update dependencies`

---

Bạn có muốn Lesson 18 – “Code Review & Giving Feedback” không?
