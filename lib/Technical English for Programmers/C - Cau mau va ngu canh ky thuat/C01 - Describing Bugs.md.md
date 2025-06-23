Dưới đây là nội dung bài giảng **C01 – Describing Bugs**, trình bày theo định dạng **Markdown (.md)**. Bài học này giúp lập trình viên sử dụng tiếng Anh chính xác và chuyên nghiệp để mô tả lỗi phần mềm (bugs) trong báo cáo hoặc trong quá trình giao tiếp nhóm.

---

# C01 – Describing Bugs

## 🎯 Lesson Objective

Learn how to describe **software bugs** clearly and professionally in English. Practice using technical vocabulary, structured formats, and common expressions in bug reports and discussions.

---

## 🧩 Key Vocabulary

| Term/Phrase        | IPA Pronunciation         | Vietnamese Meaning    | Description (EN)                                  |
| ------------------ | ------------------------- | --------------------- | ------------------------------------------------- |
| bug                | /bʌɡ/                     | lỗi phần mềm          | An error in code causing incorrect behavior       |
| issue              | /ˈɪʃ.uː/ or /ˈɪs.juː/     | vấn đề                | A general problem or task to be fixed             |
| glitch             | /ɡlɪtʃ/                   | trục trặc             | A small or temporary malfunction                  |
| crash              | /kræʃ/                    | sập ứng dụng          | Program closes unexpectedly                       |
| freeze             | /friːz/                   | đơ, treo máy          | App stops responding                              |
| reproduce          | /ˌriː.prəˈduːs/           | tái hiện lỗi          | To make the bug happen again                      |
| consistent         | /kənˈsɪs.tənt/            | xảy ra liên tục       | Happens every time under the same conditions      |
| intermittent       | /ˌɪn.təˈmɪt.ənt/          | thỉnh thoảng xảy ra   | Happens occasionally or randomly                  |
| steps to reproduce | /steps tuː rɪˈprəʊ.djuːs/ | các bước tái hiện lỗi | Instructions to recreate the bug                  |
| expected behavior  | /ɪkˈspek.tɪd bɪˈheɪ.vjər/ | hành vi mong đợi      | What the software should do                       |
| actual behavior    | /ˈæk.tʃu.əl bɪˈheɪ.vjər/  | hành vi thực tế       | What the software actually does                   |
| environment        | /ɪnˈvaɪ.rən.mənt/         | môi trường chạy       | System setup where bug occurs (OS, browser, etc.) |

---

## 🧠 Common Structure of a Bug Report

```text
Title: [Clear summary of the issue]

Environment:
- OS: Windows 10
- Browser: Chrome 124
- App version: 1.3.5

Steps to Reproduce:
1. Log into the admin dashboard.
2. Click on “Settings”.
3. Try to update the user role.
4. Observe the error.

Expected Behavior:
- The role should be updated and a success message should appear.

Actual Behavior:
- A 500 server error is returned and nothing changes.

Frequency:
- Happens every time.
```

---

## 🗣️ Useful Phrases

### ✅ Describing the Problem

* “There’s a bug where the app crashes when…”
* “The issue occurs when the user tries to…”
* “Sometimes the page freezes after clicking…”

### ⚙️ Talking About Frequency

* “It happens every time I do X.”
* “This issue is intermittent.”
* “It only occurs under certain conditions.”

### 📍 Localizing the Bug

* “It only happens in the mobile version.”
* “The bug appears in Firefox, but not in Chrome.”
* “It happens on iOS 16 but not iOS 17.”

---

## 🧑‍💻 Examples

### 🔸 Example 1 – Simple Bug

> **Title:** Button doesn’t respond on mobile
> **Steps to Reproduce:**
>
> 1. Open app on iPhone
> 2. Go to homepage
> 3. Tap the “Start” button
>
> **Expected:** Page navigates to /start
> **Actual:** Nothing happens

---

### 🔸 Example 2 – Intermittent Bug

> **Title:** Intermittent logout on session renew
> **Environment:** macOS 13, Safari
> **Steps:**
>
> * Log in
> * Leave the browser idle for \~10 minutes
> * Sometimes the user is logged out unexpectedly
>
> **Expected:** User stays logged in
> **Actual:** App logs the user out

---

## 📝 Mini Quiz

**Choose the best description:**

1. A user clicks "Save" and sees a 404 error. This is:
   a) Expected behavior
   b) A crash
   ✅ c) A bug

2. The app works fine on desktop, but not on mobile. This describes:
   ✅ a) Environment-specific issue
   b) Consistent issue
   c) Reproduced behavior

3. The app fails only 1 in 10 times. It is:
   a) Consistent
   ✅ b) Intermittent
   c) Expected

---

## 🎯 Homework

1. Mô tả một bug bạn từng gặp gần đây bằng tiếng Anh theo cấu trúc:

   * Title
   * Environment
   * Steps to Reproduce
   * Expected vs Actual Behavior
2. Luyện nói phần mô tả bug và nhờ bạn sửa lỗi phát âm.

---

Bạn có muốn tiếp tục với bài **C05 – Writing Bug Reports in GitHub / JIRA**, hoặc gộp toàn bộ Module C thành một tài liệu `.md`?
