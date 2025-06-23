Dưới đây là bài giảng **A04 - Debugging Vocabulary** – bài học từ vựng tiếng Anh chuyên ngành lập trình, tập trung vào **gỡ lỗi (debugging)**. Nội dung chuẩn **Markdown (.md)**, gồm:

* Từ vựng
* Phiên âm IPA
* Nghĩa tiếng Việt
* Giải thích bằng tiếng Anh
* Code mẫu
* Bài tập

---

# A04 - Debugging Vocabulary

## 🎯 Lesson Objective

Learn essential English vocabulary related to **debugging**, understand their pronunciation, meaning, and how to use them in context during software development.

---

## 🐞 What is Debugging?

> Debugging is the process of **identifying, analyzing, and fixing** errors (bugs) in your code.

It is one of the most critical skills in programming.

---

## 🧩 Common Debugging Terms

| Term           | IPA Pronunciation    | Vietnamese Meaning        | Description (EN)                                           |
| -------------- | -------------------- | ------------------------- | ---------------------------------------------------------- |
| bug            | /bʌɡ/                | lỗi                       | A flaw or defect in the program that causes wrong behavior |
| debug          | /diːˈbʌɡ/            | gỡ lỗi                    | To find and fix bugs in the code                           |
| breakpoint     | /ˈbreɪk.pɔɪnt/       | điểm dừng                 | A marked line where execution stops during debugging       |
| stack trace    | /stæk treɪs/         | dấu vết ngăn xếp          | A report showing function calls leading to an error        |
| log            | /lɒɡ/                | bản ghi                   | A record of events printed during code execution           |
| console        | /ˈkɒn.səʊl/          | bảng điều khiển           | Interface to view output or logs                           |
| exception      | /ɪkˈsep.ʃən/         | ngoại lệ                  | A runtime error that disrupts normal flow                  |
| error          | /ˈer.ər/             | lỗi nghiêm trọng          | Mistake in code that causes failure                        |
| warning        | /ˈwɔː.nɪŋ/           | cảnh báo                  | Non-fatal issue that may lead to bugs                      |
| assertion      | /əˈsɜː.ʃən/          | câu khẳng định kiểm tra   | A condition that must be true, or the program fails        |
| step over      | /step ˈəʊ.vər/       | bước qua                  | Move to the next line in debugging                         |
| step into      | /step ˈɪn.tuː/       | đi vào hàm                | Enter into a function call                                 |
| step out       | /step aʊt/           | thoát khỏi hàm            | Exit the current function being debugged                   |
| variable watch | /ˈveə.ri.ə.bəl wɒtʃ/ | theo dõi biến             | Monitor variable values while debugging                    |
| call stack     | /kɔːl stæk/          | ngăn xếp gọi hàm          | Sequence of nested function calls                          |
| runtime error  | /ˈrʌn.taɪm ˈer.ər/   | lỗi khi chạy chương trình | Error that happens during execution                        |

---

## 🧠 Example (JavaScript)

```js
function divide(a, b) {
    if (b === 0) {
        throw new Error("Cannot divide by zero");
    }
    return a / b;
}

console.log(divide(10, 2)); // OK
console.log(divide(5, 0));  // Throws exception
```

### Vocabulary in context:

* `throw` – ném lỗi
* `Error` – lỗi nghiêm trọng
* `console.log` – ghi log ra bảng điều khiển

---

## 🗣️ Speaking Practice

Read aloud:

* "I set a breakpoint to find out why the value is undefined."
* "The debugger shows a runtime error on line 42."
* "Check the stack trace to locate the bug."

---

## 📝 Mini Quiz

**Match the term to its meaning:**

1. `breakpoint`
2. `exception`
3. `console`
4. `assertion`
5. `step into`

**Options:**

a. điều kiện kiểm tra trong code
b. lỗi xảy ra khi chương trình đang chạy
c. bảng điều khiển hiển thị log
d. dừng tại một dòng cụ thể
e. đi sâu vào hàm đang gọi

<details>
<summary>🧾 Answers</summary>

1. d
2. b
3. c
4. a
5. e

</details>

---

## 📚 Homework

1. Viết một hàm có thể gây lỗi (`divide`, `parseJSON`, etc.).
2. Thêm `try-catch` để xử lý lỗi và ghi log ra `console`.
3. Chụp ảnh hoặc ghi lại `stack trace` nếu có lỗi xảy ra.
4. Trình bày lại quy trình gỡ lỗi đó bằng tiếng Anh (viết + đọc to).

---

Bạn muốn mình tiếp tục với **A05 - Version Control Vocabulary** (Git terms) hay cần bản tóm tắt/tệp `.md` cho toàn bộ bài A01–A04?
