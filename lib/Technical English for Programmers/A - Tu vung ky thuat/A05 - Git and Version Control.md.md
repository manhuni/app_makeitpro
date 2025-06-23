Dưới đây là bài giảng **A05 - Git and Version Control**, trình bày theo định dạng **Markdown (.md)**, chuyên dành cho lập trình viên học tiếng Anh kỹ thuật. Bài học bao gồm:

* Từ vựng Git & Version Control
* Phiên âm IPA
* Nghĩa tiếng Việt
* Mô tả ngắn bằng tiếng Anh
* Ví dụ sử dụng
* Luyện nói + bài tập

---

# A05 - Git and Version Control

## 🎯 Lesson Objective

Learn essential English vocabulary and expressions related to **Git** and **version control**, including how to use them in both code and conversations.

---

## 🔄 What Is Version Control?

**Version control** helps developers track, manage, and collaborate on code changes over time.
**Git** is the most popular version control system today.

---

## 🧩 Vocabulary Table

| Term              | IPA Pronunciation     | Vietnamese Meaning      | Description (EN)                                 |
| ----------------- | --------------------- | ----------------------- | ------------------------------------------------ |
| repository (repo) | /rɪˈpɒz.ɪ.tɔː.ri/     | kho lưu trữ mã          | A storage location for code                      |
| commit            | /kəˈmɪt/              | cam kết thay đổi        | A saved change in the code history               |
| branch            | /brɑːntʃ/             | nhánh                   | A separate line of development                   |
| merge             | /mɜːdʒ/               | gộp                     | Combine changes from one branch into another     |
| conflict          | /ˈkɒn.flɪkt/          | xung đột                | Happens when two changes clash                   |
| push              | /pʊʃ/                 | đẩy lên (lên server)    | Upload local commits to a remote repo            |
| pull              | /pʊl/                 | kéo về (từ server)      | Download changes from the remote repo            |
| clone             | /kləʊn/               | sao chép                | Copy a remote repo to your machine               |
| fork              | /fɔːk/                | tạo nhánh sao chép      | Make a personal copy of someone else's repo      |
| remote            | /rɪˈməʊt/             | từ xa                   | A reference to a repository hosted online        |
| origin            | /ˈɒr.ɪ.dʒɪn/          | tên mặc định của remote | Default remote name when cloning a repo          |
| staging area      | /ˈsteɪ.dʒɪŋ ˈeə.ri.ə/ | khu vực tạm             | Place where changes are prepared before commit   |
| checkout          | /ˈtʃek.aʊt/           | chuyển nhánh            | Move to a different branch                       |
| revert            | /rɪˈvɜːt/             | hoàn tác                | Undo a previous commit                           |
| log               | /lɒɡ/                 | nhật ký thay đổi        | Shows commit history                             |
| tag               | /tæɡ/                 | gắn nhãn                | Mark a specific commit (e.g., a release version) |

---

## 🔧 Common Git Commands

```bash
git clone https://github.com/example/repo.git
git checkout -b feature/login
git add .
git commit -m "Add login functionality"
git push origin feature/login
git pull origin main
git merge main
```

### Vocabulary in context:

* `clone` – sao chép repo về máy
* `checkout -b` – tạo và chuyển sang nhánh mới
* `add`, `commit`, `push` – lưu và đẩy thay đổi
* `pull`, `merge` – cập nhật và kết hợp mã

---

## 🗣️ Speaking Practice

Say these aloud:

* “I cloned the repository and checked out a new branch.”
* “There was a merge conflict when I pulled the latest changes.”
* “Let’s push this feature and open a pull request.”

---

## 📝 Mini Quiz

**Match the term to its meaning:**

1. `commit`
2. `branch`
3. `conflict`
4. `remote`
5. `tag`

**Options:**

a. gắn nhãn cho 1 commit đặc biệt
b. xung đột giữa 2 thay đổi
c. lưu lại 1 thay đổi
d. phiên bản repo lưu trên server
e. nhánh phát triển độc lập

<details>
<summary>🧾 Answers</summary>

1. c
2. e
3. b
4. d
5. a

</details>

---

## 📚 Homework

1. Tạo một repo Git mới và thêm vài file TypeScript.
2. Tạo một nhánh `feature/test`, thực hiện thay đổi và `commit`.
3. Mô tả lại quy trình này bằng 3–5 câu tiếng Anh sử dụng từ vựng đã học.
4. Thực hành giải thích bằng tiếng Anh:

   > "How do you resolve a merge conflict?"

---

Bạn muốn mình tiếp tục với bài **A06 - Frontend UI/UX Vocabulary**, hay tạo file `.md` tổng hợp từ A01–A05?
