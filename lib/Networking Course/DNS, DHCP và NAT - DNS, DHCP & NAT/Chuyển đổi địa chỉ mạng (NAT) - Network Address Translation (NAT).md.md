# Chuyển đổi địa chỉ mạng (NAT)   Network Address Translation (NAT)

## 🎯 Mục tiêu học tập / Learning Objectives

- Hiểu NAT là gì và tại sao nó được sử dụng trong mạng máy tính.
- Phân biệt các loại NAT: Static NAT, Dynamic NAT, PAT.
- Biết cách hoạt động của NAT khi truyền dữ liệu qua Internet.
- Xác định ưu và nhược điểm của NAT trong thực tế.

---

## 📘 Nội dung chính / Main Content

### 🌐 NAT là gì? / What is NAT?

NAT (Network Address Translation) là quá trình thay đổi địa chỉ IP trong gói tin khi nó đi qua một thiết bị mạng như router hoặc firewall.

> NAT is the process of modifying IP address information in IP packet headers while in transit across a routing device.

Mục đích:
- Giúp nhiều thiết bị trong mạng nội bộ chia sẻ một địa chỉ IP công cộng.
- Tăng cường bảo mật bằng cách ẩn cấu trúc mạng nội bộ.
- Tiết kiệm địa chỉ IPv4 công cộng.

---

### 🔁 Các loại NAT / Types of NAT

| Loại NAT / Type      | Mô tả / Description |
|----------------------|----------------------|
| **Static NAT**       | Ánh xạ 1-1 giữa IP nội bộ và IP công cộng. |
| **Dynamic NAT**      | Ánh xạ từ một nhóm IP nội bộ sang một nhóm IP công cộng. |
| **PAT (Port Address Translation)** | Nhiều IP nội bộ dùng chung 1 IP công cộng bằng cách gán cổng khác nhau. (còn gọi là NAT Overload) |

---

### 🔧 Cách NAT hoạt động / How NAT Works

Ví dụ:  
Một máy tính nội bộ 192.168.1.100 gửi gói tin đến trang web công cộng. NAT thay đổi IP nguồn thành IP công cộng của router (vd: 203.0.113.1) và lưu ánh xạ đó. Khi phản hồi đến, NAT thay IP đích từ công cộng → IP nội bộ tương ứng.

---

## 🧠 Ví dụ minh họa / Example

```text
Internal IP: 192.168.1.10
Public IP:   203.0.113.2

1. PC gửi request đến google.com.
2. NAT đổi IP nguồn thành 203.0.113.2.
3. Google phản hồi → NAT định tuyến lại về 192.168.1.10.
