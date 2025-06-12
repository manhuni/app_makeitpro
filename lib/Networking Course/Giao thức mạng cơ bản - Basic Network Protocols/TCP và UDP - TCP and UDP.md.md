# TCP và UDP   TCP and UDP

## 🎯 Mục tiêu học tập / Learning Objectives

- Phân biệt hai giao thức truyền tải chính: TCP và UDP.
- Hiểu cách hoạt động, ưu – nhược điểm của từng giao thức.
- Nắm được các ứng dụng thường sử dụng TCP hoặc UDP.
- Quan sát luồng TCP và UDP bằng Wireshark.

---

## 📘 Nội dung chính / Main Content

### 📦 TCP – Transmission Control Protocol

- Là giao thức hướng kết nối (connection-oriented).
- Đảm bảo truyền dữ liệu đầy đủ, đúng thứ tự và không mất mát.
- Sử dụng cơ chế bắt tay 3 bước (three-way handshake).
- Phù hợp cho các ứng dụng cần độ tin cậy cao như: HTTP, FTP, Email.

> TCP provides reliable, ordered, and error-checked delivery of data.

#### 🌐 Cơ chế hoạt động TCP

1. **Three-way handshake**:
   - SYN → SYN-ACK → ACK
2. **Truyền dữ liệu**: có đánh số thứ tự, kiểm tra lỗi, xác nhận (ACK)
3. **Kết thúc kết nối**: FIN → ACK

---

### 📨 UDP – User Datagram Protocol

- Giao thức không kết nối (connectionless).
- Gửi dữ liệu mà không xác minh đã đến nơi hay chưa.
- Ít độ trễ, tốc độ nhanh hơn nhưng không đảm bảo toàn vẹn dữ liệu.
- Phù hợp với: video streaming, VoIP, DNS, game online.

> UDP sends messages, called datagrams, without establishing a connection beforehand.

---

### 🔍 So sánh TCP và UDP

| Đặc điểm / Feature       | TCP                                | UDP                              |
|--------------------------|-------------------------------------|----------------------------------|
| Kiểu kết nối             | Hướng kết nối (Connection-oriented) | Không kết nối (Connectionless)  |
| Độ tin cậy               | Cao – có xác nhận, kiểm lỗi         | Thấp – không có xác nhận        |
| Tốc độ truyền            | Chậm hơn                            | Nhanh hơn                        |
| Dùng cho ứng dụng        | Web, Email, FTP                     | Video, DNS, VoIP, Game          |
| Trình tự dữ liệu         | Được đảm bảo                        | Không đảm bảo                   |

---

## 🧪 Quan sát TCP/UDP bằng Wireshark

- Dùng bộ lọc:  
  - `tcp` – hiển thị các gói TCP  
  - `udp` – hiển thị các gói UDP  
- Quan sát trình tự: handshake, retransmission (TCP)
- So sánh kích thước header TCP (~20 byte) và UDP (~8 byte)

---

## 📝 Bài tập / Exercises

1. Dùng Wireshark bắt gói truy cập web (HTTP) và phân tích handshake TCP.
2. Thực hiện ping và phân tích xem dùng TCP hay UDP (gợi ý: ICMP).
3. Viết bảng so sánh các dịch vụ phổ biến và giao thức truyền tải tương ứng.
4. Tạo đoạn mô tả ngắn giải thích khi nào nên dùng TCP, khi nào nên dùng UDP.

---

## 📚 Tài liệu tham khảo / Further Reading

- [TCP vs UDP – Cloudflare](https://www.cloudflare.com/learning/ddos/glossary/tcp-udp/)
- [How TCP Works – Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Glossary/TCP)
- [UDP Overview – GeeksforGeeks](https://www.geeksforgeeks.org/user-datagram-protocol-udp/)
