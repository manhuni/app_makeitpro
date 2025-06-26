Dưới đây là nội dung chi tiết cho:

---

# ✅ Lesson 14 – Writing Clean Code

> 📘 **Mục tiêu bài học:**

* ✅ Nắm được khái niệm và nguyên tắc cơ bản của **clean code** (mã sạch).
* ✅ Mô tả và phân tích một đoạn mã có hoặc không sạch.
* ✅ Giao tiếp tốt bằng tiếng Anh khi nói về code quality, refactoring, và best practices.

---

## 📚 Từ vựng chính (IPA + nghĩa)

| Từ vựng / Cụm từ  | Phiên âm IPA           | Nghĩa                                            |
| ----------------- | ---------------------- | ------------------------------------------------ |
| clean code        | /kliːn kəʊd/           | mã sạch – dễ đọc, dễ hiểu và dễ bảo trì          |
| readable          | /ˈriː.də.bəl/          | dễ đọc                                           |
| maintainable      | /meɪnˈteɪ.nə.bəl/      | dễ bảo trì                                       |
| naming convention | /ˈneɪ.mɪŋ kənˈven.ʃən/ | quy ước đặt tên                                  |
| indentation       | /ˌɪn.denˈteɪ.ʃən/      | thụt đầu dòng                                    |
| modular           | /ˈmɒd.jʊ.lər/          | theo mô-đun (tách thành các phần nhỏ dễ quản lý) |
| refactor          | /ˌriːˈfæk.tər/         | tái cấu trúc mã                                  |
| code smell        | /kəʊd smel/            | dấu hiệu của mã xấu (dễ gây lỗi hoặc khó hiểu)   |
| best practice     | /best ˈpræk.tɪs/       | phương pháp tốt nhất                             |
| comment (in code) | /ˈkɒm.ent/             | chú thích trong mã                               |

---

## 🗣️ Câu mẫu thực tế

### 1. Giới thiệu clean code:

* Clean code is code that is easy to read, understand, and maintain.
* Writing clean code helps teams collaborate more effectively.
* We follow standard **naming conventions** and proper **indentation**.

### 2. Nói về code hiện tại:

* This function is too long — we should **refactor** it into smaller pieces.
* There are some **code smells** here, like duplicated logic and vague variable names.
* I prefer **modular code** so each function does only one thing.

### 3. Khi review code:

* Can you add comments to explain this logic?
* Let's use more descriptive names for variables and functions.
* I think this part can be improved for **readability**.

---

## ✍️ Bài luyện viết (Writing Practice)

> Viết một đoạn văn ngắn (4–6 câu) mô tả clean code theo kinh nghiệm hoặc ý kiến cá nhân.

**Gợi ý mẫu:**

> To me, clean code means code that other developers can read and understand easily.
> I try to use meaningful variable names, consistent formatting, and clear logic.
> I often **refactor** long functions into smaller ones.
> Clean code helps reduce bugs and makes maintenance much easier.

---

## 🎤 Bài luyện nói (Speaking Practice)

> Trả lời các câu hỏi sau bằng tiếng Anh:

1. What is clean code?
2. Why is clean code important in a team project?
3. What techniques do you use to keep your code clean?

**Gợi ý mở đầu:**

* “I believe clean code is not just about style — it’s about communication…”
* “I always try to follow best practices like keeping functions short and using proper naming…”

---

## 🧠 Ghi chú mở rộng

* **Một số nguyên tắc Clean Code (theo Robert C. Martin):**

  * Use meaningful names.
  * Keep functions small and focused.
  * Don't repeat yourself (DRY principle).
  * Write code for humans, not machines.
  * Remove dead code and unnecessary comments.

* **Ví dụ cải thiện:**

```js
// Bad:
function d(x, y) {
    return x + y;
}

// Clean:
function addTwoNumbers(firstNumber, secondNumber) {
    return firstNumber + secondNumber;
}
```

* **Một số công cụ hỗ trợ:**

  * ESLint, Prettier (JavaScript)
  * SonarQube, CodeClimate
  * EditorConfig

---

Bạn muốn tiếp tục Lesson 15 – Code Review & Giving Feedback không?
