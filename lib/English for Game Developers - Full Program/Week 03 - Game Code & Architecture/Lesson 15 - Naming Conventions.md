Dưới đây là nội dung chi tiết cho:

---

# ✅ Lesson 15 – Naming Conventions

> 📘 **Mục tiêu bài học:**

* ✅ Hiểu rõ tầm quan trọng của quy tắc đặt tên trong lập trình.
* ✅ Sử dụng được từ vựng chuyên môn khi thảo luận về naming.
* ✅ Diễn đạt rõ ràng lý do nên/không nên chọn một tên biến, hàm hoặc lớp.

---

## 📚 Từ vựng chính (IPA + nghĩa)

| Từ vựng / Cụm từ  | Phiên âm IPA             | Nghĩa                                             |
| ----------------- | ------------------------ | ------------------------------------------------- |
| naming convention | /ˈneɪ.mɪŋ kənˈven.ʃən/   | quy ước đặt tên                                   |
| descriptive       | /dɪˈskrɪp.tɪv/           | có tính mô tả rõ ràng                             |
| self-explanatory  | /ˌself.ɪkˈsplæn.ə.tər.i/ | tự giải thích, rõ nghĩa                           |
| camelCase         | /ˈkæm.əl keɪs/           | kiểu viết camelCase (ví dụ: `myVariableName`)     |
| snake\_case       | /sneɪk keɪs/             | kiểu viết snake\_case (ví dụ: `my_variable_name`) |
| PascalCase        | /ˈpæs.kəl keɪs/          | kiểu viết PascalCase (ví dụ: `MyClassName`)       |
| prefix            | /ˈpriː.fɪks/             | tiền tố (chữ đứng đầu tên biến/hàm)               |
| suffix            | /ˈsʌf.ɪks/               | hậu tố (chữ đứng cuối tên biến/hàm)               |
| misleading        | /ˌmɪsˈliː.dɪŋ/           | gây hiểu nhầm                                     |
| consistency       | /kənˈsɪs.tən.si/         | tính nhất quán                                    |

---

## 🗣️ Câu mẫu thực tế

### 1. Giới thiệu naming conventions:

* We follow a consistent **naming convention** across the whole codebase.
* All variable names should be **descriptive** and **self-explanatory**.
* In JavaScript, we usually use **camelCase** for variables and functions.

### 2. Khi review code:

* Can you rename this variable? It's a bit **misleading**.
* Let's use **PascalCase** for component names in React.
* This function name doesn't explain what it does — it should be more descriptive.

### 3. Thảo luận về consistency:

* Having consistent names makes the code easier to understand.
* Even small inconsistencies can confuse new developers.
* Naming is important — bad names can lead to bugs.

---

## ✍️ Bài luyện viết (Writing Practice)

> Viết đoạn văn ngắn (4–6 câu) giải thích tại sao quy tắc đặt tên lại quan trọng trong lập trình.

**Gợi ý mẫu:**

> I think naming conventions are very important in software development.
> Descriptive names make the code easier to read and understand.
> I try to use `camelCase` for variables and functions, and `PascalCase` for class names.
> A bad or vague name can cause confusion or even bugs.
> That’s why I always pay attention when choosing names.

---

## 🎤 Bài luyện nói (Speaking Practice)

> Trả lời các câu hỏi sau bằng tiếng Anh:

1. What naming conventions do you use in your projects?
2. Why is it important to choose clear names for variables and functions?
3. How do you handle naming when working in a team?

**Gợi ý mở đầu:**

* “In my projects, I usually follow camelCase for variables and PascalCase for classes…”
* “Clear naming helps the team understand the logic faster and reduces mistakes…”

---

## 🧠 Ghi chú mở rộng

* **Ví dụ về các kiểu đặt tên:**

```js
// camelCase:
let userName = 'Tom';

// snake_case:
let user_name = 'Tom';

// PascalCase:
class UserProfile { ... }

// Bad naming:
let x = 'Tom'; // không rõ nghĩa
```

* **Gợi ý đặt tên tốt:**

  * Tên biến nên là danh từ: `userProfile`, `gameLevel`.
  * Tên hàm nên là động từ: `getUserData()`, `calculateScore()`.

* **Tips**:

  * Tránh viết tắt mơ hồ: `res`, `val`, `tmp` – chỉ dùng khi thật sự rõ nghĩa.
  * Đặt tên dài nhưng có ý nghĩa còn tốt hơn tên ngắn mà khó hiểu.

---

Bạn có muốn mình tạo tiếp **Lesson 16 – Code Review & Giving Feedback** không?
