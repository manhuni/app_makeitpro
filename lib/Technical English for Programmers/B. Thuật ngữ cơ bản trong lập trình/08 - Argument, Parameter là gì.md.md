Dưới đây là bài học tiếng Anh cho lập trình viên về sự khác nhau giữa **Argument** và **Parameter**, được trình bày theo định dạng `.md` dễ học và dễ dạy.

---

# 08 – Argument, Parameter là gì (English for Programmers)

## 🎯 Mục tiêu bài học

* Hiểu rõ sự khác nhau giữa **parameter** và **argument**
* Học từ vựng chuyên ngành + phát âm chuẩn
* Luyện mẫu câu mô tả khi viết hoặc đọc hàm

---

## 🧩 Từ vựng chính (Key Vocabulary)

| Từ / Cụm từ        | IPA                 | Nghĩa tiếng Việt   | Ghi chú thêm                       |
| ------------------ | ------------------- | ------------------ | ---------------------------------- |
| parameter          | /pəˈræmɪtə(r)/      | tham số            | Tên biến được định nghĩa trong hàm |
| argument           | /ˈɑːɡjumənt/        | đối số             | Giá trị truyền vào khi gọi hàm     |
| function signature | /ˈfʌŋkʃn ˈsɪɡnətʃə/ | chữ ký hàm         | Định nghĩa tên hàm + tham số       |
| pass a value       | /pɑːs ə ˈvæljuː/    | truyền một giá trị | Gửi giá trị vào hàm                |
| default value      | /dɪˈfɔːlt ˈvæljuː/  | giá trị mặc định   | Nếu không truyền argument nào vào  |

---

## 🔄 So sánh nhanh

| Đặc điểm | Parameter            | Argument                        |
| -------- | -------------------- | ------------------------------- |
| Vị trí   | Trong định nghĩa hàm | Khi gọi hàm                     |
| Là gì?   | Biến                 | Giá trị                         |
| Ví dụ    | `function add(a, b)` | `add(3, 5)` → 3, 5 là arguments |

---

## 📚 Ví dụ minh họa

```javascript
function greet(name) {      // "name" là parameter
  console.log("Hello, " + name);
}

greet("Alice");             // "Alice" là argument
```

---

## 🔤 Câu mẫu (Example Sentences)

| Câu tiếng Anh                                           | Dịch tiếng Việt                               |
| ------------------------------------------------------- | --------------------------------------------- |
| A parameter is a variable in a function definition.     | Tham số là một biến trong định nghĩa hàm.     |
| An argument is the actual value passed to the function. | Đối số là giá trị thực được truyền vào hàm.   |
| You can have default parameters in JavaScript.          | Bạn có thể dùng giá trị mặc định cho tham số. |

---

## 🗣️ Phát âm luyện nói

* parameter → /pəˈræmɪtə(r)/
* argument → /ˈɑːɡjumənt/
* value → /ˈvæljuː/
* default → /dɪˈfɔːlt/

---

## 💬 Hội thoại mẫu

> 👨‍💻 **A:** What’s the difference between a parameter and an argument?
> 👩‍💻 **B:** A parameter is like a placeholder. An argument is the actual data you pass in.
> 👨‍💻 **A:** So in `sum(3, 4)`, 3 and 4 are arguments?
> 👩‍💻 **B:** Exactly!

---

## ✅ Bài tập nhanh

Hoàn thành câu:

1. A \_\_\_\_\_\_ is part of the function definition.
2. An \_\_\_\_\_\_ is used when we call the function.
3. A function can have multiple \_\_\_\_\_\_.

> **Đáp án:** 1) parameter, 2) argument, 3) parameters

---

Bạn có muốn tôi tiếp tục bài 09 như: `Return`, `Loop`, hay `Conditionals` không? Hoặc chuyển sang chủ đề `React`, `JIRA`, `Phỏng vấn kỹ thuật`, v.v.?
