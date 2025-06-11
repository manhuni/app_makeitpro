import os

# Cấu trúc khóa học
course_structure = {
    "Present Simple - Hiện tại đơn": [],
    "Present Continuous - Hiện tại tiếp diễn": [],
    "Present Perfect - Hiện tại hoàn thành": [],
    "Present Perfect Continuous - Hiện tại hoàn thành tiếp diễn": [],
    "Past Simple - Quá khứ đơn": [],
    "Past Continuous - Quá khứ tiếp diễn": [],
    "Past Perfect - Quá khứ hoàn thành": [],
    "Past Perfect Continuous - Quá khứ hoàn thành tiếp diễn": [],
    "Future Simple - Tương lai đơn": [],
    "Future Continuous - Tương lai tiếp diễn": [],
    "Future Perfect - Tương lai hoàn thành": [],
    "Future Perfect Continuous - Tương lai hoàn thành tiếp diễn": []
}

# Hoặc thay bằng dict nếu có nhiều chương
# course_structure = {
#     "1-Chuong-mot": ["01-Bai-1", "02-Bai-2"],
#     "2-Chuong-hai": ["01-Bai-1", "02-Bai-2"]
# }

# Tên thư mục gốc
root_dir = "English Tenses"

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
