import os

# Cấu trúc chi tiết khóa học 12 tuần - English for Game Developers
course_structure = {
    "Week 1 - Self Introduction & Daily Work": [
        "Lesson 1 - Introducing Yourself Professionally",
        "Lesson 2 - Describing Your Tech Stack",
        "Lesson 3 - Talking About Your Daily Routine",
        "Lesson 4 - Time Management & Prioritization",
        "Lesson 5 - Describing Your Team and Role"
    ],
    "Week 2 - Task Management & Reporting": [
        "Lesson 6 - Reporting Task Status",
        "Lesson 7 - Asking for Clarification",
        "Lesson 8 - Talking About Workload",
        "Lesson 9 - Estimating Time for Tasks",
        "Lesson 10 - Talking About Blockers"
    ],
    "Week 3 - Game Code & Architecture": [
        "Lesson 11 - Describing Game Architecture",
        "Lesson 12 - Explaining the Game Loop",
        "Lesson 13 - Entity-Component Systems",
        "Lesson 14 - Writing Clean Code",
        "Lesson 15 - Naming Conventions"
    ],
    "Week 4 - Tools & Process": [
        "Lesson 16 - Using Version Control (Git)",
        "Lesson 17 - Writing Commit Messages",
        "Lesson 18 - Explaining Git Workflow",
        "Lesson 19 - Using Jira Trello",
        "Lesson 20 - Writing Documentation"
    ],
    "Week 5 - Communication & Meetings": [
        "Lesson 21 - Standup Meeting Language",
        "Lesson 22 - Planning Meetings",
        "Lesson 23 - Retrospective Meetings",
        "Lesson 24 - Receiving and Giving Feedback",
        "Lesson 25 - Saying No Professionally"
    ],
    "Week 6 - Working with Others": [
        "Lesson 26 - Working with QA",
        "Lesson 27 - Describing Bugs Clearly",
        "Lesson 28 - Collaboration with Designers",
        "Lesson 29 - Collaboration with Artists",
        "Lesson 30 - Explaining Technical Limits"
    ],
    "Week 7 - Feature Dev & Refactoring": [
        "Lesson 31 - Describing a Feature Implementation",
        "Lesson 32 - Breaking Down a Task",
        "Lesson 33 - Refactoring Legacy Code",
        "Lesson 34 - Writing TODOs and Notes",
        "Lesson 35 - Writing Code Comments"
    ],
    "Week 8 - Testing & Debugging": [
        "Lesson 36 - Describing Test Cases",
        "Lesson 37 - Talking About Unit Tests",
        "Lesson 38 - Debugging a Game",
        "Lesson 39 - Logs and Stack Traces",
        "Lesson 40 - Fixing Regression Bugs"
    ],
    "Week 9 - Performance & Optimization": [
        "Lesson 41 - Talking About FPS & Lag",
        "Lesson 42 - Memory Management",
        "Lesson 43 - Using Profilers",
        "Lesson 44 - Optimization Trade-offs",
        "Lesson 45 - Performance on Mobile vs PC"
    ],
    "Week 10 - Polishing & Deployment": [
        "Lesson 46 - Talking About Game Polish",
        "Lesson 47 - Describing Visual Bugs",
        "Lesson 48 - Build Process and Errors",
        "Lesson 49 - Publishing to Stores",
        "Lesson 50 - Handling Feedback After Release"
    ],
    "Week 11 - Soft Skills & Workplace Culture": [
        "Lesson 51 - Communicating Across Cultures",
        "Lesson 52 - Handling Team Conflicts",
        "Lesson 53 - Talking About Career Growth",
        "Lesson 54 - Negotiating Deadlines",
        "Lesson 55 - Talking About Motivation"
    ],
    "Week 12 - Interview Prep & Review": [
        "Lesson 56 - Interview: Tell Me About Yourself",
        "Lesson 57 - Interview: Project Deep Dive",
        "Lesson 58 - Interview: Behavioral Questions",
        "Lesson 59 - Interview: Technical Questions",
        "Lesson 60 - Final Review & Self-assessment"
    ]
}

# Thư mục gốc chứa toàn bộ chương trình
root_dir = "English for Game Developers - Full Program"

# Tạo cấu trúc thư mục + file .md
for week_name, lessons in course_structure.items():
    week_path = os.path.join(root_dir, week_name)
    os.makedirs(week_path, exist_ok=True)
    for lesson in lessons:
        filename = f"{lesson}.md"
        file_path = os.path.join(week_path, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {lesson}\n\n")
            f.write("> 📘 **Mục tiêu bài học:**\n\n")
            f.write("- [ ] Từ vựng chính (IPA + nghĩa)\n")
            f.write("- [ ] Câu mẫu thực tế\n")
            f.write("- [ ] Bài luyện viết\n")
            f.write("- [ ] Bài luyện nói\n")
            f.write("- [ ] Ghi chú mở rộng\n")

print("✅ Đã tạo xong chương trình học đầy đủ 12 tuần, 60 bài.")
