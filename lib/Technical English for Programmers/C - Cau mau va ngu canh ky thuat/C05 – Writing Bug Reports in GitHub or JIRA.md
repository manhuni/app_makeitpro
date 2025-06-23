Dưới đây là bài giảng **C05 – Writing Bug Reports in GitHub / JIRA**, định dạng **Markdown (.md)**. Bài học hướng dẫn cách viết báo cáo lỗi (bug report) rõ ràng, hiệu quả và chuyên nghiệp bằng tiếng Anh trên các nền tảng như GitHub và JIRA.

---

# C05 – Writing Bug Reports in GitHub / JIRA

## 🎯 Lesson Objective

Learn how to write **clear, structured bug reports** in English using GitHub Issues and JIRA. Improve your ability to describe bugs in a way that helps other developers quickly understand and fix them.

---

## 📚 Why Good Bug Reports Matter

✅ Save developers time
✅ Prevent misunderstandings
✅ Speed up resolution
✅ Show your professionalism

---

## 🧩 Key Vocabulary

| Term / Phrase      | IPA                       | Vietnamese Meaning       | Description                            |
| ------------------ | ------------------------- | ------------------------ | -------------------------------------- |
| bug report         | /bʌɡ rɪˈpɔːt/             | báo cáo lỗi              | A detailed description of a bug        |
| severity           | /sɪˈvɛr.ə.ti/             | mức độ nghiêm trọng      | How serious the bug is                 |
| priority           | /praɪˈɒr.ə.ti/            | mức độ ưu tiên           | How soon it needs fixing               |
| steps to reproduce | /stɛps tuː rɪˈprəʊ.djuːs/ | các bước để tái hiện lỗi | Clear, repeatable actions              |
| expected behavior  | /ɪkˈspek.tɪd bɪˈheɪ.vjər/ | hành vi mong đợi         | What should happen                     |
| actual behavior    | /ˈæk.tʃu.əl bɪˈheɪ.vjər/  | hành vi thực tế          | What really happens                    |
| environment        | /ɪnˈvaɪ.rən.mənt/         | môi trường chạy          | OS, browser, device, etc.              |
| logs               | /lɒɡz/                    | nhật ký hệ thống         | Debug or error logs                    |
| regression         | /rɪˈɡreʃ.ən/              | lỗi tái xuất hiện        | A bug that reappears after being fixed |

---

## 🗂 Standard Bug Report Structure (for both GitHub & JIRA)

```markdown
## 🐞 Bug Summary
[Short and clear description of the issue]

## 📍 Environment
- OS: Windows 11
- Browser: Firefox 127
- App Version: v2.0.1
- Device: Desktop

## 🔁 Steps to Reproduce
1. Log in as admin
2. Go to "User Management"
3. Click "Delete" on any user
4. Observe error

## ✅ Expected Behavior
The selected user is deleted and a success message is shown.

## ❌ Actual Behavior
The system returns a 403 Forbidden error.

## 📎 Additional Info
- Severity: High
- Priority: P1
- Logs:  
```

DELETE /api/user/12 → 403 Forbidden

```

- Screenshot:  
![screenshot](URL-to-image-if-applicable)
```

---

## 🧠 GitHub Specific Tips

* Use labels: `bug`, `high priority`, `UI`, etc.
* Assign to the right team member
* Use **checklists** for reproducibility
* Link related issues using `#issue_number`

> 📌 Example GitHub Title:
> ❌ “App broken”
> ✅ “500 Error when submitting form on mobile Chrome”

---

## 🧠 JIRA Specific Tips

* Choose the correct **issue type**: Bug, Task, Story
* Use the **"Affects Version"** and **"Fix Version"** fields
* Include **screenshots or video recordings**
* Set severity and priority using dropdowns

> 📌 Example JIRA Summary:
> ❌ “Something not working”
> ✅ “Save button fails with JS error in settings panel (v2.1)”

---

## 🔄 Bug Severity vs. Priority (How to Classify)

| Severity | Meaning                               | Example                     |
| -------- | ------------------------------------- | --------------------------- |
| Blocker  | App is unusable                       | App crashes on launch       |
| Critical | Key feature is broken                 | Cannot submit payment       |
| Major    | Important but not breaking everything | UI broken in mobile view    |
| Minor    | Small inconvenience                   | Misaligned icon             |
| Trivial  | Cosmetic or typo                      | Spelling mistake in tooltip |

---

## 🗣️ Common Phrases in Bug Reports

* “This issue occurs after…”
* “Expected behavior is that…”
* “Currently, the app returns a…”
* “This seems to be a regression from version…”
* “Happens consistently on…”
* “Unable to reproduce on Safari, only on Chrome.”

---

## 📝 Mini Quiz

**Which is the best bug title?**

1. “Problem with login”
2. ✅ “Login fails with 401 error on Safari mobile”
3. “App not working”

---

## 🎯 Homework

1. Viết một bug report theo template đã học, từ một lỗi thực tế bạn từng gặp.
2. Dán vào GitHub hoặc một file Markdown giả lập để luyện tập.
3. Gửi cho một đồng nghiệp (hoặc AI) để kiểm tra độ rõ ràng.

---

Bạn có muốn tiếp tục sang **Module D – Developer Productivity Tools Vocabulary**, hay cần gộp toàn bộ Module C vào một file tổng hợp?
