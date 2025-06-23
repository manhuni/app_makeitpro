Dưới đây là nội dung bài giảng **B03 – Reporting Issues and Solutions**, định dạng **Markdown (.md)**. Bài học này giúp lập trình viên trình bày lỗi (bugs) và đề xuất giải pháp bằng tiếng Anh một cách rõ ràng, chuyên nghiệp, đặc biệt trong môi trường làm việc nhóm hoặc báo cáo QA/dev.

---

# B03 – Reporting Issues and Solutions

## 🎯 Lesson Objective

Learn to **describe software issues**, report them clearly in English, and suggest possible **solutions or workarounds**. This includes bug reporting, discussing technical problems, and communicating fixes.

---

## 🧩 Key Vocabulary

| Term/Phrase         | IPA Pronunciation             | Vietnamese Meaning     | Description (EN)                            |
| ------------------- | ----------------------------- | ---------------------- | ------------------------------------------- |
| bug                 | /bʌɡ/                         | lỗi phần mềm           | An error or flaw in code                    |
| issue               | /ˈɪʃ.uː/                      | sự cố, vấn đề          | A problem affecting software functionality  |
| crash               | /kræʃ/                        | sập, văng chương trình | App unexpectedly stops or exits             |
| freeze              | /friːz/                       | treo                   | Application stops responding                |
| glitch              | /ɡlɪtʃ/                       | trục trặc nhỏ          | A small, unexpected problem                 |
| unexpected behavior | /ˌʌn.ɪkˈspek.tɪd bɪˈheɪ.vjər/ | hành vi không mong đợi | Something happens differently than expected |
| reproduction steps  | /ˌriː.prəˈdʌk.ʃən steps/      | các bước tái hiện      | Steps to recreate the issue                 |
| workaround          | /ˈwɜː.kə.raʊnd/               | giải pháp tạm thời     | A temporary way to bypass the problem       |
| root cause          | /ruːt kɔːz/                   | nguyên nhân cốt lõi    | The main reason a bug occurs                |
| fix / patch         | /fɪks/ - /pætʃ/               | sửa lỗi / bản vá       | Code change to solve a problem              |
| resolved            | /rɪˈzɒlvd/                    | đã được giải quyết     | Problem has been fixed                      |

---

## 🧾 Reporting an Issue – Structure

Use this format for bug reports:

```
**Title**: App crashes when clicking "Submit"

**Environment**: Android 12, App v1.3.5

**Steps to Reproduce**:
1. Open the app
2. Navigate to "Form" screen
3. Tap "Submit" without filling the fields

**Expected Result**:
User sees validation message

**Actual Result**:
App crashes instantly

**Frequency**: 100% (always happens)

**Workaround**: Fill at least one field before submitting
```

---

## ✍️ Useful English Phrases

### ✅ Describing the Problem

* “The app crashes when the user taps the login button.”
* “There’s a bug in the image loading logic.”
* “We found a glitch that causes duplicated entries.”
* “The UI freezes under low memory conditions.”

### 🔍 Asking for Clarification

* “Can you confirm the steps to reproduce this?”
* “Is this issue happening in production or staging?”
* “Was this working in the previous version?”

### 💡 Suggesting Solutions

* “We could handle this with a null check.”
* “One fix would be to debounce the input event.”
* “A possible workaround is to refresh the page.”

### 🧪 Verifying Fixes

* “The issue has been resolved in commit `a1b2c3d`.”
* “Please re-test and let us know if it still occurs.”
* “The patch has been applied to the staging environment.”

---

## 🧑‍💻 Common Bug Report Vocabulary in Context

| Sentence                                        | Vietnamese Translation                               |
| ----------------------------------------------- | ---------------------------------------------------- |
| “It crashes only on iOS 17.”                    | Nó chỉ bị crash trên iOS 17.                         |
| “We can't reproduce it on our side.”            | Chúng tôi không tái hiện được lỗi đó.                |
| “It seems related to a missing dependency.”     | Có vẻ liên quan đến một dependency bị thiếu.         |
| “It works fine after restarting the app.”       | Sau khi khởi động lại app thì hoạt động bình thường. |
| “The root cause was an incorrect state update.” | Nguyên nhân là do cập nhật trạng thái sai.           |

---

## 🗣️ Speaking Practice

Say these aloud:

* “There’s a crash when switching tabs too quickly.”
* “We fixed it by updating the dependency version.”
* “Try clearing the cache — that worked for me.”

---

## 📝 Mini Quiz

**Choose the correct expression:**

1. The best way to describe steps to recreate a bug is called:
   a) Fix log
   b) Reproduction steps ✅
   c) Update note

2. If a bug is not fixed yet but has a bypass, it’s a:
   a) Patch
   b) Workaround ✅
   c) Feature

3. “The UI stops responding” =
   a) Crashes
   b) Freezes ✅
   c) Closes

---

## 📚 Homework

1. Viết một báo cáo lỗi giả bằng tiếng Anh theo mẫu đã học.
2. Đọc lại một bug thật bạn từng gặp và mô tả bằng tiếng Anh: nguyên nhân, cách khắc phục.
3. Tạo 2 câu đề xuất giải pháp cho lỗi đó bằng ngôn ngữ chuyên nghiệp.

---

Bạn có muốn tiếp tục với bài tiếp theo – **C01 – Technical Interview Vocabulary** không? Hoặc tạo file Markdown tổng hợp Module B?
