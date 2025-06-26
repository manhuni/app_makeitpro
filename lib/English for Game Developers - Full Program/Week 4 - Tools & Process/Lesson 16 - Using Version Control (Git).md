Dưới đây là nội dung chi tiết cho:

---

# ✅ Lesson 16 – Using Version Control (Git)

> 📘 **Mục tiêu bài học:**

* ✅ Làm quen với từ vựng và cách nói về Git trong môi trường chuyên nghiệp.
* ✅ Biết cách mô tả các thao tác cơ bản trong Git (commit, push, merge…).
* ✅ Luyện tập nói/viết về quy trình sử dụng Git trong dự án.

---

## 📚 Từ vựng chính (IPA + nghĩa)

| Từ vựng / Cụm từ  | Phiên âm IPA          | Nghĩa                                          |
| ----------------- | --------------------- | ---------------------------------------------- |
| version control   | /ˈvɜː.ʒən kənˈtrəʊl/  | hệ thống quản lý phiên bản                     |
| repository (repo) | /rɪˈpɒz.ɪ.tər.i/      | kho chứa mã (repository)                       |
| commit            | /kəˈmɪt/              | cam kết thay đổi vào hệ thống                  |
| push              | /pʊʃ/                 | đẩy thay đổi lên server (GitHub, GitLab, v.v.) |
| pull              | /pʊl/                 | kéo mã từ server về máy local                  |
| merge             | /mɜːdʒ/               | gộp nhánh                                      |
| conflict          | /ˈkɒn.flɪkt/          | xung đột                                       |
| branch            | /brɑːntʃ/             | nhánh phát triển                               |
| staging area      | /ˈsteɪ.dʒɪŋ ˈeə.ri.ə/ | vùng tạm trước khi commit                      |
| rollback          | /ˈrəʊl.bæk/           | quay lại phiên bản cũ                          |

---

## 🗣️ Câu mẫu thực tế

### 1. Nói về quy trình dùng Git:

* We use Git for **version control** in all of our projects.
* I created a new **branch** to work on the login feature.
* Don’t forget to **pull** the latest changes before starting.

### 2. Khi thao tác với Git:

* I’ve just **committed** the changes and pushed them to the main branch.
* Can you **merge** your feature branch into `develop`?
* There’s a **merge conflict** we need to resolve before deploying.

### 3. Thảo luận nhóm:

* We follow Git Flow as our **branching strategy**.
* Please add a clear commit message explaining what you changed.
* If anything goes wrong, we can **rollback** to a stable commit.

---

## ✍️ Bài luyện viết (Writing Practice)

> Viết đoạn văn ngắn (4–6 câu) mô tả bạn thường sử dụng Git như thế nào trong công việc.

**Gợi ý mẫu:**

> In my projects, we use Git to manage source code.
> I usually create a new branch for each feature or bug fix.
> After finishing the work, I commit the changes and push to the remote repository.
> Before merging, I always pull the latest updates to avoid conflicts.
> We also write clear commit messages to make the history easy to understand.

---

## 🎤 Bài luyện nói (Speaking Practice)

> Trả lời các câu hỏi sau bằng tiếng Anh:

1. How do you use Git in your daily work?
2. What do you do when there is a merge conflict?
3. What is your preferred Git workflow?

**Gợi ý mở đầu:**

* “I usually use Git to create separate branches for each feature…”
* “If I face a conflict, I try to resolve it manually and test everything again…”
* “We follow the Git Flow model to manage our branches…”

---

## 🧠 Ghi chú mở rộng

* **Câu lệnh Git phổ biến:**

```bash
git status             # Kiểm tra trạng thái
git add .              # Thêm file vào staging area
git commit -m "message" # Commit với message
git push origin branch-name # Đẩy thay đổi
git pull               # Lấy code mới nhất
git checkout -b new-branch  # Tạo nhánh mới
git merge branch-name  # Gộp nhánh
```

* **Tips:**

  * Luôn đặt tên nhánh theo chức năng: `feature/login`, `bugfix/payment-error`.
  * Commit message nên rõ ràng, ví dụ: `feat: add login screen` hoặc `fix: resolve payment crash`.

---

Bạn muốn mình tiếp tục Lesson 17 – “Code Review & Giving Feedback” không?
