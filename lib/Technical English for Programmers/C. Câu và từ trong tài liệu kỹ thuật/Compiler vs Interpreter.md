Dưới đây là bài học so sánh giữa hai khái niệm quan trọng trong lập trình:

---

# Compiler vs Interpreter

## 🎯 Mục tiêu bài học

* Hiểu sự khác biệt giữa **compiler** và **interpreter**
* Sử dụng tiếng Anh để mô tả quá trình biên dịch và thông dịch
* Biết ví dụ cụ thể cho từng loại ngôn ngữ

---

## 🧩 Từ vựng chính (Key Vocabulary)

| Từ / Cụm từ    | IPA                 | Nghĩa tiếng Việt   | Ghi chú thêm                         |
| -------------- | ------------------- | ------------------ | ------------------------------------ |
| compiler       | /kəmˈpaɪlə(r)/      | trình biên dịch    | Dịch toàn bộ mã trước khi chạy       |
| interpreter    | /ɪnˈtɜːprɪtə(r)/    | trình thông dịch   | Dịch và chạy từng dòng mã            |
| compile        | /kəmˈpaɪl/          | biên dịch          | Chuyển mã nguồn → mã máy             |
| interpret      | /ɪnˈtɜːprɪt/        | thông dịch         | Đọc và chạy mã từng dòng             |
| source code    | /sɔːs kəʊd/         | mã nguồn           | Mã lập trình viên viết               |
| machine code   | /məˈʃiːn kəʊd/      | mã máy             | Mã CPU hiểu được                     |
| execution time | /ˌeksɪˈkjuːʃn taɪm/ | thời gian thực thi | Quan trọng khi so sánh 2 phương pháp |

---

## 💡 So sánh nhanh

| Đặc điểm          | Compiler                            | Interpreter                  |
| ----------------- | ----------------------------------- | ---------------------------- |
| Dịch mã khi nào?  | Trước khi chạy chương trình         | Trong khi chạy chương trình  |
| Tốc độ thực thi   | Nhanh hơn (vì đã dịch sẵn)          | Chậm hơn (vì dịch từng dòng) |
| Phát hiện lỗi     | Phát hiện toàn bộ lỗi khi biên dịch | Phát hiện lỗi tại dòng lỗi   |
| Tạo file thực thi | Có                                  | Không                        |
| Ví dụ ngôn ngữ    | C, C++, Java                        | Python, JavaScript           |

---

## 🗣️ Câu mẫu tiếng Anh

| Câu tiếng Anh                                            | Dịch tiếng Việt                                       |
| -------------------------------------------------------- | ----------------------------------------------------- |
| C++ uses a compiler to generate machine code.            | C++ dùng trình biên dịch để tạo mã máy.               |
| Python runs with an interpreter, executing line by line. | Python chạy với trình thông dịch, từng dòng một.      |
| Interpreters are slower, but great for scripting.        | Trình thông dịch chậm hơn, nhưng rất tốt cho script.  |
| Compilers detect all syntax errors before execution.     | Trình biên dịch phát hiện lỗi cú pháp trước khi chạy. |

---

## 📚 Ví dụ minh họa

### 🖥️ Compiler (C++)

```cpp
int main() {
  return 0;
}
```

✅ → Biên dịch bằng `g++`, tạo file `.exe` hoặc file thực thi
📦 Chạy file mà không cần mã nguồn

---

### 🖥️ Interpreter (Python)

```python
print("Hello, world!")
```

➡ Dịch từng dòng khi chạy bằng `python file.py`
📜 Không tạo file thực thi riêng

---

## 🗣️ Phát âm luyện nói

* compiler → /kəmˈpaɪlə(r)/
* interpreter → /ɪnˈtɜːprɪtə(r)/
* compile → /kəmˈpaɪl/
* interpret → /ɪnˈtɜːprɪt/
* execution → /ˌeksɪˈkjuːʃn/

---

## 💬 Hội thoại mẫu

> 👨‍💻 **A:** Is Java compiled or interpreted?
> 👩‍💻 **B:** Actually, it’s both. Java code is compiled to bytecode, then interpreted by the JVM.
> 👨‍💻 **A:** Oh, that makes sense.

---

## ✅ Bài tập nhanh

1. Python uses an \_\_\_\_\_\_\_\_\_\_\_\_\_\_ to execute the code.
2. A \_\_\_\_\_\_\_\_\_\_\_\_\_\_ translates the whole program before running.
3. Compiled languages usually run \_\_\_\_\_\_\_\_\_\_\_\_\_\_ than interpreted ones.

> **Đáp án:**

1. interpreter
2. compiler
3. faster

---

Bạn muốn tiếp tục với:

* 🧱 `"Bytecode"` là gì trong Java?
* 🚀 `"Just-In-Time (JIT)"` compiler?
* 🧩 `"Hybrid languages"` như Kotlin, Java?

Hoặc bạn chọn chủ đề tiếp theo nhé!
