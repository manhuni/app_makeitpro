Dưới đây là bài học tiếng Anh chuyên ngành về cụm từ **"Runtime error"** – một khái niệm rất phổ biến với lập trình viên:

---

# Runtime Error

## 🎯 Mục tiêu bài học

* Hiểu ý nghĩa của **runtime error** trong lập trình
* Phân biệt với **compile-time error**
* Giao tiếp bằng tiếng Anh khi mô tả lỗi lúc chương trình đang chạy

---

## 🧩 Từ vựng chính (Key Vocabulary)

| Từ / Cụm từ   | IPA                | Nghĩa tiếng Việt          | Ghi chú thêm                            |
| ------------- | ------------------ | ------------------------- | --------------------------------------- |
| runtime       | /ˈrʌntaɪm/         | thời gian chạy            | Khi chương trình đang hoạt động         |
| error         | /ˈerə(r)/          | lỗi                       | Tình trạng chương trình không chạy đúng |
| runtime error | /ˈrʌntaɪm ˈerə(r)/ | lỗi khi chạy chương trình | Ví dụ: chia cho 0, null reference       |
| crash (v/n)   | /kræʃ/             | sập chương trình          | Do lỗi nghiêm trọng khi chạy            |
| bug           | /bʌɡ/              | lỗi nhỏ trong mã          | Có thể gây ra runtime error             |

---

## ❓ Runtime error là gì?

> A **runtime error** happens **while the program is running**.
> It causes the program to **crash**, freeze, or behave unexpectedly.

📌 Nghĩa tiếng Việt:
→ **Runtime error** là **lỗi xảy ra khi chương trình đang chạy**, không phải lỗi cú pháp.

📍 Ví dụ:

* Gọi một biến chưa được khai báo
* Truy cập vào phần tử không tồn tại trong mảng
* Gọi hàm trên một biến có giá trị `null` hoặc `undefined`

---

## 🆚 Compile-time vs Runtime error

| Loại lỗi           | Khi nào xảy ra             | Ví dụ                               |
| ------------------ | -------------------------- | ----------------------------------- |
| Compile-time error | Khi biên dịch mã nguồn     | Sai cú pháp, sai kiểu dữ liệu       |
| Runtime error      | Khi chương trình đang chạy | Chia cho 0, gọi hàm chưa định nghĩa |

---

## 📚 Ví dụ minh họa

### ✅ JavaScript:

```javascript
let user;
console.log(user.name); // ❌ Runtime error: Cannot read property 'name' of undefined
```

➡ Biên dịch (nếu có) không báo lỗi
➡ Nhưng khi chạy, chương trình **crash**

---

## 🗣️ Câu mẫu tiếng Anh

| Câu tiếng Anh                                              | Dịch tiếng Việt                                        |
| ---------------------------------------------------------- | ------------------------------------------------------ |
| We got a runtime error when trying to access a null value. | Chúng tôi gặp lỗi runtime khi truy cập giá trị null.   |
| Runtime errors can be hard to detect without testing.      | Lỗi khi chạy có thể khó phát hiện nếu không test.      |
| I fixed the bug that caused the app to crash.              | Tôi đã sửa lỗi khiến ứng dụng bị sập.                  |
| This only happens at runtime, not during compilation.      | Lỗi này chỉ xảy ra khi chạy, không phải khi biên dịch. |

---

## 🗣️ Phát âm luyện nói

* runtime → /ˈrʌntaɪm/
* error → /ˈerə(r)/
* crash → /kræʃ/
* bug → /bʌɡ/
* exception → /ɪkˈsepʃn/ (ngoại lệ – đôi khi là runtime error)

---

## 💬 Hội thoại mẫu

> 👩‍💻 **A:** I ran the program, and it just crashed.
> 👨‍💻 **B:** Was there a runtime error?
> 👩‍💻 **A:** Yeah, something about “undefined is not a function.”

---

## ✅ Bài tập nhanh

Điền từ còn thiếu:

1. A \_\_\_\_\_\_\_\_\_\_ error happens while the app is running.
2. The program \_\_\_\_\_\_\_\_\_\_ because of a bug.
3. Compile-time errors are different from \_\_\_\_\_\_\_\_\_\_ errors.

> **Đáp án:** 1) runtime, 2) crashed, 3) runtime

---

Bạn muốn tiếp tục với:

* ⚠️ `"Exception vs Error"`?
* 🔄 `"Try-catch"` để xử lý runtime error
* 🧪 `"Unit testing"` giúp phát hiện lỗi chạy?

Hãy chọn chủ đề tiếp theo nhé!
