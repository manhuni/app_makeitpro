# Địa chỉ IP   IP Addressing

## 🎯 Mục tiêu học tập / Learning Objectives

- Hiểu khái niệm địa chỉ IP và vai trò trong mạng máy tính.
- Phân biệt IPv4 và IPv6.
- Nắm rõ cấu trúc địa chỉ IP và cách phân chia mạng (subnetting).
- Hiểu các loại địa chỉ: Public, Private, Static, Dynamic.

---

## 📘 Nội dung chính / Main Content

### 🌐 Địa chỉ IP là gì? / What is an IP Address?

Địa chỉ IP (Internet Protocol Address) là mã định danh duy nhất cho mỗi thiết bị trong mạng. Nó giúp định tuyến và truyền dữ liệu giữa các thiết bị.

> An IP address is a unique identifier assigned to each device on a network that uses the Internet Protocol for communication.

---

### 🧮 Phân loại địa chỉ IP / IP Address Types

| Loại / Type     | Mô tả / Description                          |
|------------------|-----------------------------------------------|
| **IPv4**        | Địa chỉ 32-bit, định dạng: `192.168.1.1`     |
| **IPv6**        | Địa chỉ 128-bit, định dạng: `2001:0db8::1`   |
| **Private IP**  | Dành cho mạng nội bộ (vd: 192.168.x.x)       |
| **Public IP**   | Có thể truy cập qua Internet                 |
| **Static IP**   | Cố định, không thay đổi                     |
| **Dynamic IP**  | Được cấp phát tự động qua DHCP              |

---

### 🧱 Cấu trúc địa chỉ IPv4 / IPv4 Address Structure

- IPv4 gồm 4 octet, mỗi octet 8 bit → tổng 32 bit
- Ví dụ: `192.168.0.1` = `11000000.10101000.00000000.00000001`

### 🔢 Lớp địa chỉ IPv4 / IPv4 Classes

| Lớp / Class | Phạm vi địa chỉ / Address Range     | Sử dụng / Usage       |
|-------------|-------------------------------------|------------------------|
| A           | 1.0.0.0 – 126.255.255.255           | Mạng lớn               |
| B           | 128.0.0.0 – 191.255.255.255         | Mạng trung bình        |
| C           | 192.0.0.0 – 223.255.255.255         | Mạng nhỏ               |
| D           | 224.0.0.0 – 239.255.255.255         | Multicast              |
| E           | 240.0.0.0 – 255.255.255.255         | Nghiên cứu             |

---

### 🧮 Subnetting cơ bản / Basic Subnetting

- Subnet mask dùng để phân chia mạng thành các mạng con.
- Ví dụ: `192.168.1.0/24` → 256 địa chỉ (254 usable)
- CIDR: `/8`, `/16`, `/24`… biểu thị độ dài phần mạng.

---

## 🧠 Ví dụ minh họa / Example

- Địa chỉ: `192.168.10.5/24`
- Subnet Mask: `255.255.255.0`
- Network: `192.168.10.0`
- Broadcast: `192.168.10.255`
- Host khả dụng: `192.168.10.1 – 192.168.10.254`

---

## 📝 Bài tập / Exercises

1. Phân tích địa chỉ `10.0.0.1/8`. Tìm network, broadcast, số host.
2. Phân biệt `Public IP` và `Private IP`. Tìm IP máy bạn đang dùng.
3. Dùng lệnh `ipconfig` (Windows) hoặc `ifconfig/ip a` (Linux) để xem IP.
4. Tính số mạng con có thể tạo từ `192.168.1.0/24` nếu dùng `/26`.

---

## 📚 Tài liệu tham khảo / Further Reading

- [CIDR and Subnetting – Cisco Docs](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)
- [IPv4 vs IPv6 – Cloudflare](https://www.cloudflare.com/learning/ddos/glossary/internet-protocol/)
- [IP Address Guide – WhatIsMyIP.com](https://www.whatismyip.com/ip-address-classes/)
