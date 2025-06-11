import os

# Cấu trúc khóa học
course_structure  = {
    "A. Đại từ và Mệnh đề": [
        "01 - 'What' không phải là từ để hỏi.md",
        "02 - What, That, Which dùng thế nào.md",
        "03 - Phân biệt Who, Whom, Whose.md",
        "04 - 'That' có phải là từ để hỏi không.md",
        "05 - Dùng 'that' hay 'which' cho đúng.md",
        "06 - Khi nào được bỏ 'that' trong câu.md",
        "07 - Mệnh đề danh ngữ và mệnh đề quan hệ.md",
        "08 - Câu có hai mệnh đề 'what' thì giải thế nào.md"
    ],

    "B. Câu và Cấu trúc hay nhầm": [
        "09 - Câu gián tiếp không đảo như câu hỏi.md",
        "10 - Sai lầm phổ biến với 'what is it'.md",
        "11 - 'It's me' hay 'It's I'.md",
        "12 - Mệnh đề danh ngữ không phải câu hỏi.md",
        "13 - 'If I were' hay 'If I was'.md",
        "14 - Tại sao sai khi viết 'Do you know what is it'.md"
    ],

    "C. Thì và Cấu trúc rối não": [
        "15 - 'Have gone' và 'Have been' khác nhau ra sao.md",
        "16 - Hiện tại hoàn thành vs Quá khứ đơn.md",
        "17 - Used to, Be used to, Get used to.md",
        "18 - 'Would' khác gì 'used to'.md",
        "19 - Dùng 'will' hay 'be going to'.md",
        "20 - Quá khứ đơn và quá khứ tiếp diễn.md",
        "21 - Dùng 'since' và 'for' sao cho đúng.md",
        "22 - Không phải lúc nào cũng dùng present perfect.md"
    ],

    "D. Từ dễ dịch sai": [
        "23 - Say, Tell, Speak và Talk khác nhau thế nào.md",
        "24 - Remember doing vs Remember to do.md",
        "25 - Stop doing vs Stop to do.md",
        "26 - Look, See, Watch khác nhau ra sao.md",
        "27 - Hear và Listen có giống nhau không.md",
        "28 - Win và Beat dùng thế nào cho đúng.md",
        "29 - Bring và Take dùng sai là mất điểm.md",
        "30 - Lend và Borrow dễ lẫn lộn.md",
        "31 - Raise và Rise khác nhau gì.md",
        "32 - Find, Find out, Figure out khác gì nhau.md"
    ],

    "E. Những lỗi cơ bản nhưng dễ sai": [
        "33 - Phân biệt Some và Any.md",
        "34 - A few, Few, A little, Little khác nhau ra sao.md",
        "35 - Much, Many và A lot of dùng thế nào.md",
        "36 - 'I'm boring' và 'I'm bored' khác nhau hoàn toàn.md",
        "37 - Because và Because of không giống nhau.md",
        "38 - Khi nào dùng 'to' và khi nào dùng 'for'.md",
        "39 - Good at và Good in dùng thế nào.md",
        "40 - So that vs So that (cấu trúc mục đích và kết quả).md",
        "41 - All, Every và Each khác nhau gì.md"
    ],

    "F. Các câu hỏi dễ gây hiểu lầm": [
        "42 - Cách dùng Why don't you đúng cách.md",
        "43 - Would you mind if I V2 là gì.md",
        "44 - Phân biệt Would you mind và Do you mind.md",
        "45 - Câu hỏi đuôi phủ định kiểu 'Isn't it'.md",
        "46 - 'How come' có nghĩa là gì.md",
        "47 - Could you possibly khác gì Can you.md"
    ],

    "G. Ngữ cảnh và lịch sự trong giao tiếp": [
        "48 - Dùng May I hay Can I trong tình huống trang trọng.md",
        "49 - Nên chọn Do you want hay Would you like.md",
        "50 - Cách mở đầu và kết thúc email lịch sự bằng tiếng Anh.md"
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
root_dir = "Real English Pitfalls"

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
