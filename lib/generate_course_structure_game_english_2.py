import os

# Danh sách cấu trúc tiếng Anh biểu thị phỏng đoán, suy đoán, cảm xúc, đánh giá...
modality_course = {
    "Week 01 - Expressing Uncertainty": [
        "Lesson 1 - Using Maybe, Probably, Perhaps",
        "Lesson 2 - I Think, I Guess, I Suppose",
        "Lesson 3 - Apparently, Supposedly, Presumably",
        "Lesson 4 - It Seems, It Looks, It Sounds",
        "Lesson 5 - Practice: Guessing & Reacting in Conversation"
    ],
    "Week 02 - Expressing Possibility & Doubt": [
        "Lesson 6 - Can, Could, May, Might",
        "Lesson 7 - Modal Verbs: Degrees of Certainty",
        "Lesson 8 - Should, Must (Logical Deductions)",
        "Lesson 9 - Combining Modals for Nuance",
        "Lesson 10 - Practice: Discussing Rumors & Assumptions"
    ],
    "Week 03 - Softening Language & Hedging": [
        "Lesson 11 - Using Kind of, Sort of, A Bit",
        "Lesson 12 - Using Seem, Appear, Tend to",
        "Lesson 13 - Using Apparently vs Actually",
        "Lesson 14 - Adding I Think, I Feel, In My Opinion",
        "Lesson 15 - Practice: Polite & Indirect Opinions"
    ],
    "Week 04 - Reacting to Uncertain Information": [
        "Lesson 16 - Expressing Surprise or Doubt",
        "Lesson 17 - Confirming or Clarifying What You Heard",
        "Lesson 18 - Using Oh Really?, Are You Sure?, That Makes Sense",
        "Lesson 19 - Tone of Voice in Uncertainty",
        "Lesson 20 - Practice: Natural Dialogues with Uncertainty"
    ]
}

# Tên thư mục gốc
root_dir = "English Modality & Uncertainty"

# Tạo thư mục và file bài học
for week_name, lessons in modality_course.items():
    week_path = os.path.join(root_dir, week_name)
    os.makedirs(week_path, exist_ok=True)
    for lesson in lessons:
        file_path = os.path.join(week_path, f"{lesson}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {lesson}\n\n")
            f.write("> 📘 **Mục tiêu bài học:**\n\n")
            f.write("- [ ] Từ vựng chính (IPA + nghĩa)\n")
            f.write("- [ ] Cấu trúc ngữ pháp / cách dùng\n")
            f.write("- [ ] Câu mẫu thực tế (với ngữ cảnh)\n")
            f.write("- [ ] Bài luyện nói (vai trò, tình huống)\n")
            f.write("- [ ] Bài luyện nghe hoặc phân tích đoạn hội thoại\n")
            f.write("- [ ] Ghi chú mở rộng (thành ngữ, lối nói tương đương)\n")

print("✅ Đã tạo xong khóa học 'English Modality & Uncertainty'.")
