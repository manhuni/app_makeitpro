# Bắt gói và phân tích cơ bản   Packet Capturing & Basic Analysis

## 🎯 Mục tiêu học tập / Learning Objectives

- Hiểu khái niệm "bắt gói" (packet capturing) trong mạng.
- Biết cách sử dụng công cụ Wireshark để bắt và phân tích gói tin.
- Nhận diện các loại gói tin phổ biến (ARP, ICMP, TCP, UDP).
- Thực hành quan sát lưu lượng mạng thực tế.

---

## 📘 Nội dung chính / Main Content

### 📦 Bắt gói là gì? / What is Packet Capturing?

Bắt gói là quá trình ghi lại các gói tin được truyền qua mạng nhằm phục vụ mục đích giám sát, phân tích, hoặc khắc phục sự cố.

> Packet capturing is the process of intercepting and logging traffic that passes over a digital network.

---

### 🛠 Công cụ phổ biến / Common Tools

- **Wireshark** (GUI) – Công cụ mạnh mẽ, trực quan.
- **tcpdump** (CLI) – Công cụ dòng lệnh phổ biến trên Linux/Unix.

---

### 🔍 Các loại gói tin thường gặp / Common Packet Types

| Loại gói / Packet Type | Mục đích / Purpose                    |
|------------------------|----------------------------------------|
| **ARP**                | Tìm địa chỉ MAC từ địa chỉ IP          |
| **ICMP**               | Gửi thông báo lỗi, kiểm tra (ping)     |
| **TCP**                | Giao thức truyền tin có kiểm soát      |
| **UDP**                | Giao thức truyền tin không kiểm soát   |
| **DNS/HTTP/HTTPS**     | Ứng dụng tầng cao sử dụng TCP/UDP      |

---

### 🔄 Cách bắt và phân tích gói tin với Wireshark

1. Mở Wireshark và chọn giao diện mạng.
2. Nhấn nút “Start” để bắt đầu bắt gói.
3. Duyệt web hoặc thực hiện tác vụ mạng để tạo lưu lượng.
4. Dừng quá trình và lọc theo từ khóa: `http`, `tcp.port == 80`, `icmp`, v.v.
5. Nhấp vào từng gói để xem chi tiết: Header, Payload, Protocol layers.

---

## 🧠 Ví dụ minh họa / Example

- Dùng Wireshark lọc theo `icmp` và thực hiện lệnh `ping google.com`.
- Quan sát gói ICMP Request và ICMP Reply.
- So sánh thời gian phản hồi và TTL (Time To Live).

---

## 📝 Bài tập / Exercises

1. Cài đặt và bắt thử gói tin với Wireshark.
2. Tìm một gói tin TCP và mô tả 3 bước bắt tay (3-way handshake).
3. Dùng bộ lọc Wireshark để chỉ hiển thị gói DNS.
4. Ghi lại tên giao thức của 5 gói đầu tiên bạn bắt được.

---

## ⚠️ Ghi chú về đạo đức / Ethical Note

> ❗ Chỉ bắt gói trên mạng bạn được phép. Bắt gói trái phép có thể vi phạm pháp luật và đạo đức nghề nghiệp.

---

## 📚 Tài liệu tham khảo / Further Reading

- [Wireshark User Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
- [Packet Analysis Basics – GeeksForGeeks](https://www.geeksforgeeks.org/introduction-to-packet-sniffing/)
- [ICMP Explained – Cloudflare](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/)
