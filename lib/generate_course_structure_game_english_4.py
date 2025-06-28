import os

# Danh sách bài học chuẩn hóa không dùng dấu "/"
weak_form_course = {
    "Week 01 - Gioi thieu va Rut gon Tro dong tu": [
        "Lesson 01 - Weak Forms la gi - Vi sao chung quan trong",
        "Lesson 02 - Will thanh ll - Shall thanh ll",
        "Lesson 03 - Have Has Had thanh ve s d",
        "Lesson 04 - Would thanh d - Should Could rut gon am",
        "Lesson 05 - Practice - Nghe Noi voi cac tro dong tu"
    ],
    "Week 02 - Tu chuc nang bi rut gon": [
        "Lesson 06 - To thanh tə - For thanh fə",
        "Lesson 07 - Of thanh əv - From thanh frəm",
        "Lesson 08 - And thanh ənd hoac ən",
        "Lesson 09 - At In On rut gon thanh ət ən ɪn",
        "Lesson 10 - Practice - Luyen hoi thoai voi tu chuc nang"
    ],
    "Week 03 - Rut gon dai tu va cum tu": [
        "Lesson 11 - Them thanh em - Us thanh s - You thanh ya",
        "Lesson 12 - Going to thanh gonna - Want to thanh wanna",
        "Lesson 13 - Got to thanh gotta - Have to thanh hafta",
        "Lesson 14 - Let me thanh lemme - Give me thanh gimme",
        "Lesson 15 - Practice - Shadowing rut gon cum tu"
    ],
    "Week 04 - Connected Speech va Bien am": [
        "Lesson 16 - Noi phu am va nguyen am",
        "Lesson 17 - Intrusion - Chen am w j r khi noi",
        "Lesson 18 - Elision - Roi am next day thanh nex day",
        "Lesson 19 - Assimilation - Bien am good boy thanh goob boy",
        "Lesson 20 - Practice - Nhan dien va doc noi am"
    ],
    "Week 05 - Bien am trong Anh My va Luyen noi nang cao": [
        "Lesson 21 - Flap T - Water thanh wa der",
        "Lesson 22 - Glottal Stop - Butter thanh buh uh",
        "Lesson 23 - Cau hoi nhanh - Did you thanh didja - Dont you thanh dontcha",
        "Lesson 24 - Nghe va bat loi khi thieu weak form",
        "Lesson 25 - Tong on - Hoi thoai that va luyen tap"
    ]
}

# Tên thư mục gốc
root_dir = "English Pronunciation - Weak Forms and Connected Speech"

# Tạo thư mục và file bài học
for week_name, lessons in weak_form_course.items():
    week_path = os.path.join(root_dir, week_name)
    os.makedirs(week_path, exist_ok=True)
    for lesson in lessons:
        safe_filename = lesson.replace("/", "-")  # Dự phòng nếu còn sót
        file_path = os.path.join(week_path, f"{safe_filename}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {lesson}\n\n")
            f.write("> 🎯 **Muc tieu bai hoc:**\n\n")
            f.write("- [ ] Hieu ro cach noi rut gon hoac noi am\n")
            f.write("- [ ] Luyen phat am dung voi nhip dieu tu nhien\n")
            f.write("- [ ] Thuc hanh nhan biet qua hoi thoai thuc te\n")
            f.write("- [ ] So sanh van noi va van viet de dung linh hoat\n")
            f.write("- [ ] Shadowing, nghe, noi lai de noi giong nguoi ban xu\n")

print("✅ Da tao xong khoa hoc 'Weak Forms and Connected Speech'.")
