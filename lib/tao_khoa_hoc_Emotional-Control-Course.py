import os

# Cấu trúc khóa học
course_structure = {
    "0-Introduction": [
        "00-Gioi-thieu-Khoa-hoc",
        "01-Cach-su-dung-Khoa-hoc"
    ],
    "1-Nhan-Dien-Cam-Xuc": [
        "01-Nhan-biet-cam-xuc-ban-than",
        "02-Ghi-nhan-phan-xa-co-the",
        "03-Tap-phan-tich-bieu-cam",
        "04-Phan-tich-phong-thai-trong-giao-tiep"
    ],
    "2-Kiem-Soat-Phan-Xa-Cam-Xuc": [
        "01-Bai-tap-im-lang-bi-dong",
        "02-Kiem-soat-phoi-hop-hoi-tho-tim-mach",
        "03-Chong-phan-xa-khi-bi-lam-nhuc",
        "04-Chiu-dung-noi-dau-the-chat",
        "05-Bai-test-nuoc-da"
    ],
    "3-Chia-Cat-Nhan-Thuc": [
        "01-Tao-thong-tin-gia-hop-ly",
        "02-Cach-ke-chuyen-nguoc-logic",
        "03-Ky-thuat-doublethink-Orwell",
        "04-Chia-tach-tri-nho-thanh-phan",
        "05-Thu-luyen-ho-so-gia"
    ],
    "4-Khoi-Truong-Khang-Ep-Cung": [
        "01-Ky-thuat-tri-hoan-cau-tra-loi",
        "02-Tao-mantra-tu-phong-thu",
        "03-Trai-nghiem-trang-tri-nho-Whiteout",
        "04-Tu-lap-trinh-khong-noi-giong-the",
        "05-Tinh-huong-mo-phong-bi-chat-van"
    ],
    "5-Phu-Tro-Cong-Nghe-OPSEC": [
        "01-Gioi-thieu-Gray-Man-Theory",
        "02-Ky-thuat-phong-van-nguoc",
        "03-Chong-doc-vi-CIA-style",
        "04-Lam-mo-danh-tinh-qua-ngon-ngu-co-the",
        "05-Nhac-nho-OPSEC-hang-ngay"
    ],
    "6-Lich-Luyen-Tap": [
        "01-Lich-30-ngay-Co-ban",
        "02-Lich-lap-lai-cho-3-thang",
        "03-Lich-ket-hop-thuc-te-song-hang-ngay"
    ],
    "7-Tai-Lieu-Tham-Khao": [
        "01-Sach-Spy-the-Lie-Tom-tat",
        "02-Tra-cuu-tu-khoa-YouTube-SERE",
        "03-Cac-ung-dung-ho-tro-thuc-hanh",
        "04-Bai-doc-tam-ly-phan-khang-dieu-tra"
    ]
}

# Tên thư mục gốc
root_dir = "ecc"

# Tạo thư mục và file
for folder, files in course_structure.items():
    folder_path = os.path.join(root_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    for filename in files:
        file_path = os.path.join(folder_path, f"{filename}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {filename.replace('-', ' ')}\n")

print("✅ Đã tạo xong cây thư mục khóa học.")
