import os

# Cấu trúc khóa học
course_structure = {
    "A. Dấu câu trong lập trình": [
        "01 - Dấu ngoặc đơn ( ) gọi là gì.md",
        "02 - Dấu ngoặc nhọn { } dùng khi nào.md",
        "03 - Dấu hai chấm : có nghĩa gì trong code.md",
        "04 - Dấu phẩy , và dấu chấm . khác nhau ra sao.md",
        "05 - Dấu chấm phẩy ; thường gặp ở đâu.md"
    ],
    "B. Thuật ngữ cơ bản trong lập trình": [
        "06 - Variable là gì.md",
        "07 - Function, Method khác nhau gì.md",
        "08 - Argument, Parameter là gì.md",
        "09 - Statement, Expression là gì.md",
        "10 - Bug, Debug nghĩa là gì.md"
    ],
    "C. Câu và từ trong tài liệu kỹ thuật": [
        "11 - 'Return a value' nghĩa là gì.md",
        "12 - 'Pass by reference' dịch sao.md",
        "13 - 'Compile the code' nghĩa là gì.md",
        "14 - 'Throw an exception' là gì.md"
    ]
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
