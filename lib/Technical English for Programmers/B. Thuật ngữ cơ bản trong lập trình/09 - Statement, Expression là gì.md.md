Dưới đây là bài học tiếng Anh dành cho lập trình viên với chủ đề:

---

# 09 – Statement, Expression là gì (English for Programmers)

## 🎯 Mục tiêu bài học

* Phân biệt rõ **statement** và **expression** bằng tiếng Anh
* Nắm từ vựng, ví dụ minh họa và mẫu câu sử dụng
* Giao tiếp và đọc hiểu code tốt hơn khi làm việc nhóm

---

## 🧩 Từ vựng chính (Key Vocabulary)

| Từ / Cụm từ | IPA          | Nghĩa tiếng Việt    | Ghi chú thêm                 |
| ----------- | ------------ | ------------------- | ---------------------------- |
| statement   | /ˈsteɪtmənt/ | câu lệnh            | Thực hiện một hành động      |
| expression  | /ɪkˈspreʃn/  | biểu thức           | Tạo ra (trả về) một giá trị  |
| evaluate    | /ɪˈvæljueɪt/ | đánh giá, tính toán | Tính kết quả của biểu thức   |
| assignment  | /əˈsaɪnmənt/ | phép gán            | Gán giá trị cho biến         |
| execute     | /ˈeksɪkjuːt/ | thực thi            | Chạy lệnh trong chương trình |

---

## 🔄 So sánh nhanh

| Đặc điểm        | Expression                   | Statement                          |
| --------------- | ---------------------------- | ---------------------------------- |
| Kết quả         | Trả về một giá trị           | Không nhất thiết trả về giá trị    |
| Có thể gán được | ✅ Có thể dùng trong phép gán | ❌ Không thể gán trực tiếp          |
| Ví dụ           | `2 + 3`, `"Hello"`, `a * b`  | `let x = 5;`, `if (x > 0) { ... }` |

---

## 📚 Ví dụ minh họa

```javascript
// Expression
let a = 10 + 5;     // "10 + 5" là expression
let b = greet();    // "greet()" là expression

// Statement
if (a > b) {
  console.log("A is greater");
}                   // Cả block là một statement
```

---

## 🔤 Câu mẫu (Example Sentences)

| Câu tiếng Anh                              | Dịch tiếng Việt                           |
| ------------------------------------------ | ----------------------------------------- |
| An expression evaluates to a value.        | Một biểu thức được tính ra giá trị.       |
| A statement performs an action.            | Một câu lệnh thực hiện một hành động.     |
| You can use expressions inside statements. | Có thể dùng biểu thức bên trong câu lệnh. |

---

## 🗣️ Phát âm luyện nói

* statement → /ˈsteɪtmənt/
* expression → /ɪkˈspreʃn/
* evaluate → /ɪˈvæljueɪt/
* assignment → /əˈsaɪnmənt/

---

## 💬 Hội thoại mẫu

> 👨‍💻 **A:** Is `x + y` a statement or an expression?
> 👩‍💻 **B:** It’s an expression. It returns a value.
> 👨‍💻 **A:** And what about `if (x > y) {...}`?
> 👩‍💻 **B:** That’s a statement. It controls the flow.

---

## ✅ Bài tập nhanh

Điền từ còn thiếu:

1. An \_\_\_\_\_\_ returns a value.
2. A(n) \_\_\_\_\_\_ performs an action like declaring or looping.
3. You can combine multiple expressions into one \_\_\_\_\_\_.

> **Đáp án:** 1) expression, 2) statement, 3) statement

---

Bạn muốn tiếp bài số **10** là chủ đề nào?

👉 Gợi ý:

* `Return vs console.log`
* `Loop keywords: for, while, break`
* `Conditionals: if, else, switch`
* Hay chuyển sang `React Vocabulary` hoặc `Debugging Language`?
