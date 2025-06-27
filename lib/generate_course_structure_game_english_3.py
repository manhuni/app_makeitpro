import os

# Cấu trúc khóa học English for Understanding ADHD
adhd_course = {
    "Week 01 - What is ADHD?": [
        "Lesson 01 - Definition and Types of ADHD",
        "Lesson 02 - Common Symptoms in Adults and Children",
        "Lesson 03 - ADHD vs Laziness: Misconceptions",
        "Lesson 04 - Causes and Risk Factors",
        "Lesson 05 - Practice: Explaining ADHD Simply"
    ],
    "Week 02 - Living with ADHD": [
        "Lesson 06 - Time Management Challenges",
        "Lesson 07 - Emotional Regulation and Impulsivity",
        "Lesson 08 - ADHD in School and Workplace",
        "Lesson 09 - Strengths of People with ADHD",
        "Lesson 10 - Practice: Describing Daily Struggles"
    ],
    "Week 03 - Diagnosis & Treatment": [
        "Lesson 11 - How ADHD is Diagnosed",
        "Lesson 12 - Medications and How They Work",
        "Lesson 13 - Behavioral Therapy and Coaching",
        "Lesson 14 - ADHD in Women and Girls",
        "Lesson 15 - Practice: Discussing Treatment Options"
    ],
    "Week 04 - Social Impact & Self-Advocacy": [
        "Lesson 16 - Talking to Family and Friends about ADHD",
        "Lesson 17 - ADHD and Relationships",
        "Lesson 18 - Coping Strategies and Tools",
        "Lesson 19 - Disclosing ADHD at Work",
        "Lesson 20 - Practice: Telling Your ADHD Story"
    ]
}

# Thư mục gốc cho khóa học
root_dir = "English for Understanding ADHD"

# Tạo thư mục và file bài học .md
for week_name, lessons in adhd_course.items():
    week_path = os.path.join(root_dir, week_name)
    os.makedirs(week_path, exist_ok=True)

    for lesson in lessons:
        file_path = os.path.join(week_path, f"{lesson}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {lesson}\n\n")
            f.write("> 📘 **Lesson Objective:**\n\n")
            f.write("- [ ] Key Vocabulary (IPA + meaning)\n")
            f.write("- [ ] Grammar/Usage Structures\n")
            f.write("- [ ] Realistic Example Sentences\n")
            f.write("- [ ] Speaking Practice (scenarios, roles)\n")
            f.write("- [ ] Listening Practice / Dialogue Analysis\n")
            f.write("- [ ] Additional Notes (idioms, collocations, extra context)\n")

print("✅ ADHD course created successfully!")
