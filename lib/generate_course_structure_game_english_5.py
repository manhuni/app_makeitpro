import os

# Cấu trúc khóa học - 12 tuần: Tư duy & phản xạ tiếng Anh cho người học từ gốc
course_structure = {
    "Week 1 - Foundations of Thinking in English": [
        "Lesson 1 - Why Think in English?",
        "Lesson 2 - Stop Translating in Your Head",
        "Lesson 3 - Thinking with Simple Sentences",
        "Lesson 4 - Daily Routine Descriptions",
        "Lesson 5 - Mirror Practice (Nói một mình)"
    ],
    "Week 2 - Talking About Yourself": [
        "Lesson 6 - Name, Age, and Where You're From",
        "Lesson 7 - Family & Friends",
        "Lesson 8 - Hobbies and Interests",
        "Lesson 9 - Personality and Habits",
        "Lesson 10 - Likes, Dislikes, and Opinions"
    ],
    "Week 3 - Daily Life Scenarios": [
        "Lesson 11 - At the Supermarket",
        "Lesson 12 - Ordering Food & Drinks",
        "Lesson 13 - At the Bus Stop",
        "Lesson 14 - In a Coffee Shop",
        "Lesson 15 - At the Doctor's Office"
    ],
    "Week 4 - Talking About Time": [
        "Lesson 16 - Days of the Week & Months",
        "Lesson 17 - Telling the Time",
        "Lesson 18 - Talking About Schedules",
        "Lesson 19 - Making Appointments",
        "Lesson 20 - Time Expressions & Frequency"
    ],
    "Week 5 - Expressing Emotions & Reactions": [
        "Lesson 21 - How Are You? - Basic Emotions",
        "Lesson 22 - Expressing Surprise & Excitement",
        "Lesson 23 - Expressing Sadness & Frustration",
        "Lesson 24 - Reacting to Good-Bad News",
        "Lesson 25 - Using Tone & Body Language"
    ],
    "Week 6 - Everyday Conversations": [
        "Lesson 26 - Starting a Conversation",
        "Lesson 27 - Small Talk in English",
        "Lesson 28 - Asking for and Giving Directions",
        "Lesson 29 - Making Requests Politely",
        "Lesson 30 - Agreeing & Disagreeing"
    ],
    "Week 7 - Vocabulary Building with Images": [
        "Lesson 31 - Kitchen & Cooking",
        "Lesson 32 - Home & Furniture",
        "Lesson 33 - City & Transportation",
        "Lesson 34 - Clothing & Shopping",
        "Lesson 35 - Weather & Seasons"
    ],
    "Week 8 - Describe What You See & Do": [
        "Lesson 36 - Describe a Picture (5W1H)",
        "Lesson 37 - Talk About What You're Doing",
        "Lesson 38 - Describe Someone's Actions",
        "Lesson 39 - Picture Storytelling Practice",
        "Lesson 40 - Talk About Your Day (Past Tense)"
    ],
    "Week 9 - From Words to Thoughts": [
        "Lesson 41 - Connectors: And, But, Because",
        "Lesson 42 - Cause & Effect in Daily Life",
        "Lesson 43 - Explaining Simple Ideas",
        "Lesson 44 - Talking About Future Plans",
        "Lesson 45 - Giving Reasons & Preferences"
    ],
    "Week 10 - Thinking Aloud Exercises": [
        "Lesson 46 - Describe a Process (e.g., making coffee)",
        "Lesson 47 - Think Aloud with a Timer",
        "Lesson 48 - Practice Talking Without Notes",
        "Lesson 49 - Mind Mapping with Words",
        "Lesson 50 - Reacting to Random Situations"
    ],
    "Week 11 - Role Plays & Improvisation": [
        "Lesson 51 - Buying a Train Ticket",
        "Lesson 52 - Visiting a New City",
        "Lesson 53 - Meeting a Stranger",
        "Lesson 54 - Emergency Situation",
        "Lesson 55 - Talking on the Phone"
    ],
    "Week 12 - Final Review & Reflection": [
        "Lesson 56 - Revisit Your First Recording",
        "Lesson 57 - Reflect on Your Progress",
        "Lesson 58 - Write Your Daily Journal",
        "Lesson 59 - Self-Speaking Test",
        "Lesson 60 - Your English Thinking Plan"
    ]
}

# Thư mục chính
root_dir = "Thinking in English - Full Program"

# Tạo thư mục + file markdown cho mỗi bài học
for week_name, lessons in course_structure.items():
    week_path = os.path.join(root_dir, week_name)
    os.makedirs(week_path, exist_ok=True)
    for lesson in lessons:
        filename = f"{lesson}.md"
        file_path = os.path.join(week_path, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {lesson}\n\n")
            f.write("> 🎯 **Mục tiêu bài học:**\n\n")
            f.write("- [ ] Từ vựng chính (có hình nếu có)\n")
            f.write("- [ ] Câu mẫu + kịch bản ngắn\n")
            f.write("- [ ] Bài luyện nói tư duy (think & speak)\n")
            f.write("- [ ] Bài luyện viết phản xạ\n")
            f.write("- [ ] Ghi chú thêm (ngữ pháp nếu cần)\n")

print("✅ Đã tạo xong chương trình học 'Tư Duy bằng Tiếng Anh' 12 tuần, 60 bài.")
