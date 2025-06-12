# Giới thiệu Wireshark   Introduction to Wireshark

## 🎯 Mục tiêu học tập / Learning Objectives

- Hiểu Wireshark là gì và vai trò của nó trong phân tích mạng.
- Biết cách cài đặt và khởi động Wireshark.
- Làm quen với giao diện và các thành phần chính của Wireshark.
- Biết cách bắt gói đơn giản và sử dụng bộ lọc.

---

## 📘 Nội dung chính / Main Content

### 🧐 Wireshark là gì? / What is Wireshark?

Wireshark là một công cụ mã nguồn mở dùng để bắt và phân tích gói tin mạng theo thời gian thực. Nó được sử dụng bởi quản trị mạng, nhà phát triển, chuyên gia bảo mật và giảng viên.

> Wireshark is a free and open-source packet analyzer used for network troubleshooting, analysis, software and communications protocol development, and education.

---

### 💻 Cài đặt Wireshark / Installing Wireshark

- Truy cập trang: [https://www.wireshark.org](https://www.wireshark.org)
- Chọn hệ điều hành (Windows, macOS, Linux)
- Làm theo hướng dẫn cài đặt
- (Windows) Cài thêm `Npcap` nếu được hỏi

---

### 🖥️ Giao diện người dùng / User Interface Overview

| Thành phần / Component     | Mô tả / Description |
|----------------------------|----------------------|
| **Menu Bar**               | Các chức năng chính như File, Capture, Analyze |
| **Toolbar**                | Nút Start/Stop Capture, Save, Open… |
| **Packet List Pane**       | Danh sách các gói tin đã bắt được |
| **Packet Details Pane**    | Cấu trúc chi tiết của gói đang chọn |
| **Packet Bytes Pane**      | Dữ liệu thô của gói (hex + ASCII) |

---

### 🧪 Bắt gói đầu tiên / Your First Packet Capture

1. Mở Wireshark
2. Chọn giao diện mạng đang hoạt động (thường là Ethernet/Wi-Fi)
3. Nhấn nút **Start Capturing**
4. Duyệt một trang web để tạo lưu lượng
5. Nhấn nút **Stop** khi đủ gói
6. Quan sát các gói TCP, DNS, HTTP, ICMP,…

---

### 🎯 Sử dụng bộ lọc cơ bản / Using Basic Filters

- `http` – chỉ hiện gói HTTP  
- `ip.addr == 8.8.8.8` – gói đến/từ Google DNS  
- `tcp.port == 443` – chỉ gói HTTPS  
- `icmp` – chỉ hiện các gói ICMP (ping)

---

## 🧠 Ví dụ minh họa / Example

- Lọc `dns` và truy cập `wikipedia.org`
- Quan sát truy vấn DNS (Query) và phản hồi (Response)
- Click gói DNS để xem domain và IP trả về

---

## 📝 Bài tập / Exercises

1. Cài đặt Wireshark và chạy thử bắt gói.
2. Lọc `http` và truy cập một trang web không HTTPS.
3. Xác định địa chỉ IP của máy bạn và địa chỉ IP của server mà bạn truy cập.
4. Ghi lại tên 3 giao thức bạn thấy trong danh sách gói tin.

---

## ⚠️ Lưu ý đạo đức / Ethical Note

> ❗ Chỉ sử dụng Wireshark trên hệ thống và mạng mà bạn được phép. Việc bắt gói trái phép có thể vi phạm pháp luật và đạo đức nghề nghiệp.

---

## 📚 Tài liệu tham khảo / Further Reading

- [Wireshark Official Docs](https://www.wireshark.org/docs/)
- [Wireshark Wiki](https://wiki.wireshark.org/)
- [Wireshark Beginner Tutorial – Guru99](https://www.guru99.com/wireshark-tutorial.html)
