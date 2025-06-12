# Ngăn xếp TCP/IP   TCP IP Stack

## 🎯 Mục tiêu học tập / Learning Objectives

- Hiểu ngăn xếp giao thức TCP/IP là gì và vì sao nó quan trọng.
- Nắm rõ bốn tầng của TCP/IP và vai trò của từng tầng.
- Phân biệt mô hình TCP/IP với mô hình OSI.
- Liên hệ các giao thức thực tế với từng tầng TCP/IP.

---

## 📘 Nội dung chính / Main Content

### 🌐 Ngăn xếp TCP/IP là gì? / What is the TCP/IP Stack?

Ngăn xếp TCP/IP (TCP/IP Stack) là một tập hợp các giao thức được thiết kế để truyền dữ liệu qua Internet. Nó gồm 4 tầng hoạt động từ thấp đến cao.

> The TCP/IP stack is a four-layer model used to understand how data moves through a network from one device to another.

---

### 🧱 4 Tầng trong TCP/IP / The 4 Layers of TCP/IP

| Tầng | Tên tầng (VN)              | Tên tầng (EN)           | Mô tả / Description |
|------|-----------------------------|--------------------------|---------------------|
| 4    | Ứng dụng                    | Application Layer        | Giao tiếp giữa ứng dụng và mạng (HTTP, FTP, DNS...) |
| 3    | Giao vận                    | Transport Layer          | Truyền dữ liệu giữa các điểm cuối (TCP, UDP) |
| 2    | Mạng                        | Internet Layer           | Định tuyến, địa chỉ IP, định danh thiết bị (IP, ICMP) |
| 1    | Truy cập mạng               | Network Access Layer     | Kết nối vật lý và liên kết dữ liệu (Ethernet, Wi-Fi) |

---

### 🔄 So sánh TCP/IP với OSI / TCP/IP vs OSI Model

| Mô hình OSI               | Mô hình TCP/IP         |
|---------------------------|------------------------|
| 7. Application             | 4. Application         |
| 6. Presentation            | 4. Application         |
| 5. Session                 | 4. Application         |
| 4. Transport               | 3. Transport           |
| 3. Network                 | 2. Internet            |
| 2. Data Link               | 1. Network Access      |
| 1. Physical                | 1. Network Access      |

👉 TCP/IP gộp các tầng Application, Presentation và Session của OSI lại thành một tầng duy nhất.

---

### 📦 Giao thức phổ biến theo tầng / Common Protocols by Layer

- **Application**: HTTP, HTTPS, FTP, SMTP, DNS
- **Transport**: TCP, UDP
- **Internet**: IP, ICMP, ARP
- **Network Access**: Ethernet, Wi-Fi, PPP

---

### 🔁 Dòng chảy dữ liệu / Data Flow in TCP/IP Stack

1. **Gửi dữ liệu**: Dữ liệu từ ứng dụng → transport → internet → network access → gửi đi.
2. **Nhận dữ liệu**: Tầng network access nhận dữ liệu → internet → transport → ứng dụng hiển thị.

---

### 🛠️ Ví dụ thực tế

Khi bạn truy cập một trang web:
- Trình duyệt (Application) gửi yêu cầu HTTP.
- TCP (Transport) chia nhỏ dữ liệu thành các segment.
- IP (Internet) định tuyến các gói tin.
- Ethernet/Wi-Fi (Network Access) truyền qua cáp hoặc sóng.

---

## 📝 Bài tập / Exercises

1. Kể tên ít nhất 2 giao thức cho mỗi tầng của mô hình TCP/IP.
2. Vẽ sơ đồ so sánh tầng TCP/IP và OSI với giao thức tương ứng.
3. Sử dụng Wireshark để bắt gói HTTP và phân tích các tầng trong ngăn xếp TCP/IP.
4. Trình bày lại dòng chảy dữ liệu khi gửi email từ góc nhìn TCP/IP.

---

## 📚 Tài liệu tham khảo / Further Reading

- [TCP/IP Model – Cisco](https://www.cisco.com/c/en/us/solutions/enterprise-networks/tcp-ip-model.html)
- [TCP/IP Protocol Suite – GeeksforGeeks](https://www.geeksforgeeks.org/tcp-ip-model/)
- [TCP/IP Explained – Cloudflare](https://www.cloudflare.com/learning/network-layer/what-is-tcp-ip/)
