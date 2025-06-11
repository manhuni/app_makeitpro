import os

# Cấu trúc khóa học
course_structure = {
    "A - Tu vung ky thuat": {
        "A01 - Programming Keywords.md": "Programming-related terms (e.g., variable, function, return, class)",
        "A02 - Game Dev Terms.md": "Game development terms (e.g., sprite, scene, node, animation)",
        "A03 - Cocos-specific Vocabulary.md": "Terms used in Cocos Creator",
        "A04 - TypeScript Vocabulary.md": "TypeScript-specific terms",
        "A05 - Git and Version Control.md": "Terms like commit, merge, branch, etc."
    },
    "B - Giao tiep cong viec": {
        "B01 - JIRA and Task Language.md": "Words used in project management (task, bug, backlog)",
        "B02 - Email and Meeting Vocabulary.md": "Common phrases for meetings and emails",
        "B03 - Reporting Issues and Solutions.md": "How to describe problems and propose fixes"
    },
    "C - Cau mau va ngu canh ky thuat": {
        "C01 - Describing Bugs.md": "How to explain bugs in English",
        "C02 - Describing Features.md": "How to describe a feature or function",
        "C03 - Asking for Clarification.md": "Useful sentences to clarify tasks"
    },
    "D - Phat am va viet tat": {
        "D01 - Pronunciation of Code Symbols.md": "IPA and English name of special characters",
        "D02 - Acronyms in Tech.md": "Terms like API, SDK, FPS, IDE, etc.",
        "D03 - Common Mispronunciations.md": "Words like cache, null, async, syntax"
    },
    "E - Bai tap thuc hanh": {
        "E01 - Dich mo ta cong viec.md": "Translate job descriptions or specs",
        "E02 - Viet lai bug report bang tieng Anh.md": "Rewrite technical issues in English",
        "E03 - Tu dien ky thuat ca nhan.md": "Build your own technical vocabulary"
    }
}
# course_structure = {
#     "Present Simple - Hiện tại đơn": [],
#     "Present Continuous - Hiện tại tiếp diễn": [],
#     "Present Perfect - Hiện tại hoàn thành": [],
#     "Present Perfect Continuous - Hiện tại hoàn thành tiếp diễn": [],
#     "Past Simple - Quá khứ đơn": [],
#     "Past Continuous - Quá khứ tiếp diễn": [],
#     "Past Perfect - Quá khứ hoàn thành": [],
#     "Past Perfect Continuous - Quá khứ hoàn thành tiếp diễn": [],
#     "Future Simple - Tương lai đơn": [],
#     "Future Continuous - Tương lai tiếp diễn": [],
#     "Future Perfect - Tương lai hoàn thành": [],
#     "Future Perfect Continuous - Tương lai hoàn thành tiếp diễn": []
# }

# Hoặc thay bằng dict nếu có nhiều chương
# course_structure = {
#     "1-Chuong-mot": ["01-Bai-1", "02-Bai-2"],
#     "2-Chuong-hai": ["01-Bai-1", "02-Bai-2"]
# }

# Tên thư mục gốc
root_dir = "Technical_English_for_Programmers"

if isinstance(course_structure, dict):
    # Trường hợp có thư mục chương
    for folder, files in course_structure.items():
        folder_path = os.path.join(root_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        for filename in files:
            file_path = os.path.join(folder_path, f"{filename}.md")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# {filename.replace('-', ' ')}\n")
else:
    # Trường hợp chỉ là danh sách file .md, không có thư mục
    os.makedirs(root_dir, exist_ok=True)
    for filename in course_structure:
        file_path = os.path.join(root_dir, f"{filename}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {filename.replace('-', ' ')}\n")

print("✅ Đã tạo xong cây thư mục khóa học.")
