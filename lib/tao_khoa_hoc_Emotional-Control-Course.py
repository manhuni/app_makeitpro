import os

# Cấu trúc khóa học
course_structure = [
    "01-Dopamine-la-gi",
    "02-Vong-lap-phan-thuong",
    "03-Dopamine-va-hoc-tap",
    "04-Nghien-cuu-dopamine",
    "05-Ung-dung-lop-hoc",
    "06-Gamification-va-dopamine",
    "07-Nguoi-lon-va-dopamine",
    "08-Dopamine-tu-nhien-va-nghien",
    "09-Tang-dopamine-lanh-manh",
    "10-Mo-hinh-he-thong-hoc",
    "11-Case-duolingo",
    "12-Tong-ket-va-dinh-huong"
]

# Hoặc thay bằng dict nếu có nhiều chương
# course_structure = {
#     "1-Chuong-mot": ["01-Bai-1", "02-Bai-2"],
#     "2-Chuong-hai": ["01-Bai-1", "02-Bai-2"]
# }

# Tên thư mục gốc
root_dir = "dopamine"

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
