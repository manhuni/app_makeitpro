import os

# Cấu trúc khóa học
course_structure = [ 
    # 24 phụ âm
    "p", "b", "t", "d", "k", "g", "tʃ", "dʒ", "f", "v", "θ", "ð",
    "s", "z", "ʃ", "ʒ", "h", "m", "n", "ŋ", "l", "r", "j", "w",
    # 12 nguyên âm đơn
    "iː", "ɪ", "e", "æ", "ʌ", "ɑː", "ɒ", "ɔː", "ʊ", "uː", "ɜː", "ə",
    # 8 nguyên âm đôi (diphthongs)
    "eɪ", "aɪ", "ɔɪ", "aʊ", "əʊ", "ɪə", "eə", "ʊə" 
]

# Hoặc thay bằng dict nếu có nhiều chương
# course_structure = {
#     "1-Chuong-mot": ["01-Bai-1", "02-Bai-2"],
#     "2-Chuong-hai": ["01-Bai-1", "02-Bai-2"]
# }

# Tên thư mục gốc
root_dir = "44ipa"

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
