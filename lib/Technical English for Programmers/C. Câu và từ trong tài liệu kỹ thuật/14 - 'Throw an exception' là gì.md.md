Dưới đây là bài học tiếng Anh chuyên ngành lập trình, tập trung vào cụm từ phổ biến khi xử lý lỗi:

---

# 14 – "Throw an exception" là gì?

## 🎯 Mục tiêu bài học

* Hiểu cụm **“throw an exception”** trong lập trình
* Phân biệt các khái niệm liên quan như **error**, **try-catch**, **throw**
* Giao tiếp được bằng tiếng Anh về xử lý lỗi

---

## 🧩 Từ vựng chính (Key Vocabulary)

| Từ / Cụm từ   | IPA         | Nghĩa tiếng Việt                 | Ghi chú thêm                          |
| ------------- | ----------- | -------------------------------- | ------------------------------------- |
| throw (v)     | /θrəʊ/      | ném (gây ra)                     | Trong lập trình: tạo lỗi có kiểm soát |
| exception (n) | /ɪkˈsepʃn/  | ngoại lệ (lỗi có thể xử lý được) | Khác với lỗi nghiêm trọng (error)     |
| catch (v)     | /kætʃ/      | bắt (ngoại lệ)                   | Dùng để xử lý lỗi sau khi "throw"     |
| try-catch     | /traɪ kætʃ/ | khối thử và bắt lỗi              | Cấu trúc xử lý lỗi                    |
| runtime       | /ˈrʌntaɪm/  | khi chương trình đang chạy       | Nơi xảy ra ngoại lệ                   |

---

## ❓ "Throw an exception" nghĩa là gì?

> Trong lập trình, **"throw an exception"** nghĩa là **cố ý tạo ra một lỗi** (exception) khi có tình huống bất thường xảy ra, để chương trình có thể **xử lý lỗi đó một cách có kiểm soát**.

📌 Nghĩa tiếng Việt:
→ **"throw an exception"** = **ném ra một ngoại lệ**

---

## 📚 Ví dụ minh họa

### 🧠 JavaScript:

```javascript
function divide(a, b) {
  if (b === 0) {
    throw new Error("Cannot divide by zero");
  }
  return a / b;
}
```

➡ Nếu `b = 0`, đoạn `throw` sẽ tạo ra một ngoại lệ.
Chương trình **không crash**, mà bạn có thể dùng `try-catch` để xử lý.

---

## 🔄 Cấu trúc phổ biến

```javascript
try {
  // đoạn có thể gây lỗi
  throw new Error("Something went wrong");
} catch (err) {
  // xử lý lỗi ở đây
  console.error(err.message);
}
```

---

## 🆚 Exception vs Error

| Thuật ngữ | Nghĩa                                      |
| --------- | ------------------------------------------ |
| Error     | Lỗi nghiêm trọng, có thể dừng chương trình |
| Exception | Ngoại lệ, có thể xử lý được                |

---

## 🔤 Câu mẫu tiếng Anh

| Câu tiếng Anh                                             | Dịch tiếng Việt                                        |
| --------------------------------------------------------- | ------------------------------------------------------ |
| The function throws an exception if the input is invalid. | Hàm sẽ ném ngoại lệ nếu đầu vào không hợp lệ.          |
| You can catch the exception using a try-catch block.      | Bạn có thể bắt ngoại lệ bằng khối try-catch.           |
| Throwing exceptions helps you handle errors gracefully.   | Việc ném ngoại lệ giúp bạn xử lý lỗi một cách mượt mà. |

---

## 🗣️ Phát âm luyện nói

* throw → /θrəʊ/
* exception → /ɪkˈsepʃn/
* catch → /kætʃ/
* error → /ˈerə(r)/
* runtime → /ˈrʌntaɪm/

---

## 💬 Hội thoại mẫu

> 👨‍💻 **A:** What happens if the file doesn’t exist?
> 👩‍💻 **B:** The code will throw an exception.
> 👨‍💻 **A:** Do we catch it?
> 👩‍💻 **B:** Yes, there's a try-catch block.

---

## ✅ Bài tập nhanh

Điền từ còn thiếu:

1. The code will \_\_\_\_\_\_ an exception if the input is wrong.
2. Always \_\_\_\_\_\_ exceptions to prevent crashing.
3. A try-\_\_\_\_\_\_ block helps handle exceptions.

> **Đáp án:** 1) throw, 2) catch, 3) catch

---

Bạn muốn tiếp tục với:

* 🔁 `"try-catch-finally"` là gì?
* 🧩 `"Custom exception"` trong OOP
* 📜 `"Error stack trace"` đọc như thế nào?

Hoặc bạn chọn chủ đề tiếp theo nhé!
