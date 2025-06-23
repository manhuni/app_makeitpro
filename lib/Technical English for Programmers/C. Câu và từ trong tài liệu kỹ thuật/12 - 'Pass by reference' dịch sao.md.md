Dưới đây là bài học tiếng Anh chuyên ngành lập trình, tập trung vào cụm từ chuyên dùng:

---

# 12 – "Pass by reference" dịch sao?

## 🎯 Mục tiêu bài học

* Hiểu nghĩa "pass by reference" là gì trong lập trình
* Dùng tiếng Anh để giải thích khái niệm
* Phân biệt với "pass by value"
* Luyện kỹ năng nói và viết mô tả kỹ thuật

---

## 🧩 Từ vựng chính (Key Vocabulary)

| Từ / Cụm từ       | IPA                 | Nghĩa tiếng Việt    | Ghi chú thêm                            |
| ----------------- | ------------------- | ------------------- | --------------------------------------- |
| pass by reference | /pɑːs baɪ ˈrefrəns/ | truyền (tham chiếu) | Truyền địa chỉ vùng nhớ                 |
| pass by value     | /pɑːs baɪ ˈvæljuː/  | truyền (giá trị)    | Tạo bản sao, không ảnh hưởng gốc        |
| reference         | /ˈrefrəns/          | tham chiếu          | Chỉ đến vị trí thật trong bộ nhớ        |
| copy              | /ˈkɒpi/             | bản sao             | Giá trị mới, không liên kết với ban đầu |
| modify            | /ˈmɒdɪfaɪ/          | chỉnh sửa           | Làm thay đổi nội dung                   |
| original          | /əˈrɪdʒənl/         | gốc, ban đầu        | Biến hoặc dữ liệu gốc                   |

---

## 🔁 Giải thích nhanh

### 📌 "Pass by reference" nghĩa là:

> **Truyền tham chiếu** → truyền **địa chỉ vùng nhớ** của biến vào hàm
> → Khi hàm thay đổi giá trị bên trong, **giá trị gốc cũng thay đổi**

### 📌 "Pass by value" nghĩa là:

> **Truyền giá trị** → truyền **bản sao** vào hàm
> → Thay đổi trong hàm **không ảnh hưởng** đến biến ban đầu

---

## 📚 Ví dụ minh họa

```javascript
function modify(obj) {
  obj.name = "Alice";  // sửa trực tiếp đối tượng gốc
}

let user = { name: "Bob" };
modify(user);
console.log(user.name); // 👉 "Alice"
```

→ **Vì `user` được truyền bằng tham chiếu (`pass by reference`)**, nên thay đổi trong hàm ảnh hưởng tới biến ngoài.

---

### 🔁 So sánh:

| Loại truyền       | Tác động tới biến gốc | Ví dụ dữ liệu  |
| ----------------- | --------------------- | -------------- |
| Pass by value     | ❌ Không thay đổi      | number, string |
| Pass by reference | ✅ Có thể thay đổi     | object, array  |

---

## 🗣️ Câu mẫu tiếng Anh

| Câu tiếng Anh                                                                             | Dịch tiếng Việt                                                              |
| ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| In JavaScript, objects are passed by reference.                                           | Trong JavaScript, object được truyền theo tham chiếu.                        |
| Primitives are passed by value, so the original stays unchanged.                          | Kiểu nguyên thủy được truyền bằng giá trị, nên biến gốc không đổi.           |
| When you pass an array by reference, any changes inside the function affect the original. | Khi bạn truyền mảng theo tham chiếu, mọi thay đổi sẽ ảnh hưởng đến mảng gốc. |

---

## 🗣️ Phát âm luyện nói

* pass by reference → /pɑːs baɪ ˈrefrəns/
* pass by value → /pɑːs baɪ ˈvæljuː/
* modify → /ˈmɒdɪfaɪ/
* original → /əˈrɪdʒənl/

---

## 💬 Hội thoại mẫu

> 👩‍💻 **A:** Why is the user name changed?
> 👨‍💻 **B:** Because we passed the object by reference.
> 👩‍💻 **A:** Oh, so the function modified the original object?
> 👨‍💻 **B:** Exactly.

---

## ✅ Bài tập nhanh

Điền từ còn thiếu:

1. In JavaScript, arrays are passed by \_\_\_\_\_\_.
2. Strings are passed by \_\_\_\_\_\_, so they stay the same.
3. When you \_\_\_\_\_\_ an object in a function, it changes globally.

> **Đáp án:** 1) reference, 2) value, 3) modify

---

Bạn muốn tiếp tục với:

* 🧠 `"Deep copy" vs "Shallow copy"`
* 🧩 `"Immutable"` là gì trong lập trình?
* 🔍 `"Call by reference"` có khác không?

Hoặc bạn chọn chủ đề tiếp theo nhé!
