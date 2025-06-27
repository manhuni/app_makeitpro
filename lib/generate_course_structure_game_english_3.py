import os

# Danh sách bài học tiếng Anh theo chủ đề "League of Legends"
lol_english_course = {
    "Week 01 - Basics of Gaming Language": [
        "Lesson 1 - Common Game Roles: Top, Jungle, Mid, ADC, Support",
        "Lesson 2 - Items & Buffs: What Do They Mean?",
        "Lesson 3 - In-Game Communication: Ping, Signal, Chat",
        "Lesson 4 - KDA, CS, Gank, Feed: Game Stats Explained",
        "Lesson 5 - Practice: Describe a Match Summary in English"
    ],
    "Week 02 - Teamplay & Strategy": [
        "Lesson 6 - Giving & Following Instructions in Game",
        "Lesson 7 - Talking About Objectives: Drake, Baron, Tower",
        "Lesson 8 - Describing Tactics: Engage, Peel, Split Push",
        "Lesson 9 - Reacting to Teammates: Encouragement or Complaints",
        "Lesson 10 - Practice: Voice Chat Simulation (Friendly/Competitive)"
    ],
    "Week 03 - Game Emotions & Reactions": [
        "Lesson 11 - Expressing Frustration & Excitement",
        "Lesson 12 - Using Slang: GG, OP, Nerf, Buff",
        "Lesson 13 - Polite vs Toxic Language in Game",
        "Lesson 14 - Responding to Victory or Defeat",
        "Lesson 15 - Practice: Roleplay Post-Game Chat"
    ],
    "Week 04 - Game Lore & Champion Talk": [
        "Lesson 16 - Champion Quotes & Catchphrases (e.g., Yasuo, Jinx)",
        "Lesson 17 - Describing Abilities & Skills in English",
        "Lesson 18 - Talking About Lore: Factions, Regions, Backstories",
        "Lesson 19 - Comparing Champions: Strengths & Weaknesses",
        "Lesson 20 - Practice: Champion Spotlight Presentation"
    ]
}

# Tên thư mục gốc
root_dir = "English for League of Legends"

# Tạo thư mục và file bài học
for week_name, lessons in lol_english_course.items():
    week_path = os.path.join(root_dir, week_name)
    os.makedirs(week_path, exist_ok=True)
    for lesson in lessons:
        file_path = os.path.join(week_path, f"{lesson}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {lesson}\n\n")
            f.write("> 🎮 **Mục tiêu bài học:**\n\n")
            f.write("- [ ] Từ vựng & thuật ngữ trong game (IPA + nghĩa)\n")
            f.write("- [ ] Mẫu câu giao tiếp trong tình huống game\n")
            f.write("- [ ] Ngữ cảnh sử dụng thật (với hội thoại mẫu)\n")
            f.write("- [ ] Luyện nói qua vai trò nhân vật hoặc bình luận trận đấu\n")
            f.write("- [ ] Nghe các đoạn hội thoại game hoặc phân tích lời thoại\n")
            f.write("- [ ] Ghi chú mở rộng (slang, biểu cảm, trích dẫn thú vị)\n")

print("✅ Đã tạo xong khóa học 'English for League of Legends'.")
