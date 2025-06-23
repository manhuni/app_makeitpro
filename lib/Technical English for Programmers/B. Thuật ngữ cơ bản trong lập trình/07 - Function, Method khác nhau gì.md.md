Dưới đây là bài học dạng Markdown để giúp lập trình viên học tiếng Anh qua khái niệm: **Function vs. Method**.

---

# 07 – Function & Method khác nhau gì (English for Programmers)

## 🎯 Mục tiêu bài học

* Phân biệt “function” và “method” bằng tiếng Anh
* Học từ vựng, phát âm chuẩn, ví dụ minh họa
* Giao tiếp, mô tả đoạn code bằng tiếng Anh cơ bản

---

## 🧩 Từ vựng chính (Key Vocabulary)

| Từ / Cụm từ     | IPA               | Nghĩa tiếng Việt               | Ghi chú thêm                         |
| --------------- | ----------------- | ------------------------------ | ------------------------------------ |
| function        | /ˈfʌŋkʃn/         | hàm (độc lập)                  | Không phụ thuộc vào object           |
| method          | /ˈmeθəd/          | phương thức (của object/class) | Gắn với một object cụ thể            |
| parameter       | /pəˈræmɪtə(r)/    | tham số                        | Biến được truyền vào function/method |
| return value    | /rɪˈtɜːn ˈvæljuː/ | giá trị trả về                 | Kết quả sau khi thực thi hàm         |
| call a function | /kɔːl ə ˈfʌŋkʃn/  | gọi hàm                        | Thực thi function                    |

---

## 🔄 So sánh nhanh

| Đặc điểm          | Function                       | Method                        |
| ----------------- | ------------------------------ | ----------------------------- |
| Định nghĩa        | Đoạn mã thực hiện một nhiệm vụ | Function gắn với object/class |
| Gọi               | `functionName()`               | `object.methodName()`         |
| Cần object không? | ❌ Không                        | ✅ Có                          |

---

## 📚 Ví dụ minh họa

```javascript
// Function
function greet(name) {
  return "Hello, " + name;
}

// Method
const person = {
  name: "Anna",
  greet() {
    return "Hello, " + this.name;
  }
};

console.log(greet("John"));       // Function: Hello, John
console.log(person.greet());      // Method: Hello, Anna
```

---

## 🔤 Câu mẫu (Example Sentences)

| Câu tiếng Anh                                     | Dịch tiếng Việt                        |
| ------------------------------------------------- | -------------------------------------- |
| A function is a reusable block of code.           | Hàm là một khối mã có thể tái sử dụng. |
| A method is a function that belongs to an object. | Method là function gắn với một object. |
| We call the method using the object name.         | Gọi phương thức bằng tên object.       |

---

## 🗣️ Phát âm luyện nói

* function → /ˈfʌŋkʃn/
* method → /ˈmeθəd/
* parameter → /pəˈræmɪtə(r)/
* return → /rɪˈtɜːn/

---

## 💬 Hội thoại mẫu

> 👩‍💻 **A:** Is `greet` a method or a function?
> 👨‍💻 **B:** If it's inside an object, it's a method. Otherwise, it’s just a function.

> 👩‍💻 **A:** Can we call it without an object?
> 👨‍💻 **B:** Not if it’s a method.

---

## ✅ Bài tập nhanh

Điền từ còn thiếu:

1. A \_\_\_\_\_\_ is not attached to any object.
2. A \_\_\_\_\_\_ is always called using an object.
3. You can \_\_\_\_\_\_ a function using its name.

> **Đáp án:** 1) function, 2) method, 3) call

---

Bạn muốn tiếp theo là bài gì?
👉 Gợi ý: `Return`, `Loop`, `Parameter vs. Argument`, hoặc đi sâu vào `React Vocabulary`?
