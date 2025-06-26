Dưới đây là nội dung đầy đủ cho:

---

# ✅ Lesson 27 – Describing Bugs Clearly

> 📘 **Mục tiêu bài học:**

* ✅ Biết cách trình bày lỗi rõ ràng, logic, dễ hiểu bằng tiếng Anh.
* ✅ Thực hành dùng từ vựng và cấu trúc để mô tả bug đúng cách.
* ✅ Viết và nói về lỗi một cách chuyên nghiệp trong môi trường làm việc.

---

## 📚 Từ vựng chính (IPA + nghĩa)

| Từ / Cụm từ         | Phiên âm IPA                  | Nghĩa tiếng Việt                     |
| ------------------- | ----------------------------- | ------------------------------------ |
| bug                 | /bʌɡ/                         | lỗi                                  |
| unexpected behavior | /ˌʌn.ɪkˈspek.tɪd bɪˈheɪ.vjər/ | hành vi không mong đợi               |
| crash               | /kræʃ/                        | sập chương trình                     |
| freeze              | /friːz/                       | treo máy                             |
| steps to reproduce  | /stɛps tuː ˌriː.prəˈdjuːs/    | các bước để tái hiện lỗi             |
| error message       | /ˈɛr.ər ˈmɛs.ɪdʒ/             | thông báo lỗi                        |
| stack trace         | /stæk treɪs/                  | dấu vết ngăn xếp (log call function) |
| glitch              | /ɡlɪtʃ/                       | lỗi nhỏ, bất thường                  |
| intermittent        | /ˌɪn.təˈmɪt.ənt/              | xảy ra không liên tục                |
| severity            | /sɪˈver.ə.ti/                 | mức độ nghiêm trọng của lỗi          |

---

## 🗣️ Câu mẫu thực tế

### A. Mô tả lỗi cơ bản:

* The app **crashes** when switching between scenes quickly.
* There's an **intermittent glitch** with the sound not playing.
* An **unexpected behavior** occurs when the user presses "Back".

### B. Mô tả lỗi có logic:

```
Bug: Score is not updated after the player finishes a level.

Steps to Reproduce:
1. Start a new game.
2. Complete level 1.
3. Observe the score screen.

Expected Result: The score should display "100".
Actual Result: The score remains at "0".
```

### C. Giao tiếp trong nhóm:

* Can you check the **stack trace** for this crash?
* It works fine on my side, can you send the **steps to reproduce**?
* What’s the **severity** of this bug — blocker or minor?

---

## ✍️ Bài luyện viết (Writing Practice)

> Viết một mô tả lỗi rõ ràng bằng tiếng Anh, dựa theo cấu trúc:

* Bug:
* Steps to Reproduce:
* Expected Result:
* Actual Result:
* Notes / Logs:

**Ví dụ:**

```
Bug: Game freezes on the loading screen.

Steps to Reproduce:
1. Launch the game.
2. Tap "Continue" on the home screen.
3. Wait for the loading bar.

Expected Result: Game should proceed to the main menu.
Actual Result: The game freezes at 80%.

Notes: Happens consistently on Android 11. No error message.
```

---

## 🎤 Bài luyện nói (Speaking Practice)

> Hãy luyện nói một lỗi mà bạn từng gặp thực tế theo mẫu sau:

1. What was the bug?
2. How did you find it?
3. How did you describe or report it?
4. Was it easy or hard to fix?

**Ví dụ thoại:**

> "I found a bug where the game crashed after using the back button. I described it in Jira with the steps and attached a screenshot. It was hard to reproduce at first, but once we got the logs, the issue was clear."

---

## 🧠 Ghi chú mở rộng

### ✅ Cấu trúc chuẩn để mô tả bug (SOP – Standard Operating Procedure):

| Thành phần  | Ví dụ                                  |
| ----------- | -------------------------------------- |
| Title       | Button does nothing when clicked       |
| Environment | iOS 17.1, iPhone 13, Cocos Creator 3.8 |
| Steps       | 1. Open screen A → 2. Tap button B     |
| Expected    | Action should trigger                  |
| Actual      | Nothing happens                        |
| Severity    | Medium                                 |
| Attachment  | Log file, video clip                   |

### ✅ Những cụm từ hay dùng:

* “This issue only happens under certain conditions.”
* “I couldn’t reproduce the bug on the staging server.”
* “Please check the console logs or network tab for more info.”

---

Bạn muốn tiếp tục Lesson 28 hay cần xuất toàn bộ bài học sang `.md` hoặc Python script để tự động tạo thư mục + file?
