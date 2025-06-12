# Cơ chế cấp phát IP với DHCP   DHCP Overview

## 🎯 Mục tiêu học tập / Learning Objectives

- Hiểu DHCP là gì và tại sao nó quan trọng trong mạng máy tính.
- Mô tả quy trình cấp phát địa chỉ IP qua DHCP.
- Phân biệt giữa các trạng thái địa chỉ IP (Dynamic, Static, Reserved).
- Nắm được cấu trúc của gói tin DHCP.

---

## 📘 Nội dung chính / Main Content

### 📡 DHCP là gì? / What is DHCP?

DHCP (Dynamic Host Configuration Protocol) là giao thức mạng giúp tự động gán các thông số IP (địa chỉ IP, subnet mask, gateway, DNS) cho các thiết bị trong mạng.

> DHCP is a network management protocol used to dynamically assign IP addresses and other network configuration parameters to devices on a network.

---

### 🔄 Quy trình cấp phát IP qua DHCP / DHCP IP Assignment Process

Quy trình 4 bước (DORA):

1. **Discover** – Máy khách gửi broadcast để tìm DHCP server.
2. **Offer** – DHCP server phản hồi với một địa chỉ IP khả dụng.
3. **Request** – Máy khách chọn 1 IP và gửi yêu cầu xác nhận.
4. **Acknowledge** – DHCP server xác nhận và gán IP đó.

> The DORA process: Discover → Offer → Request → Acknowledge.

---

### 🧱 Cấu trúc gói tin DHCP / DHCP Packet Structure

Một gói DHCP thường chứa:
- Client MAC Address
- Assigned IP Address
- Lease Time
- DHCP Message Type (Discover, Offer, etc.)
- Optional fields (DNS, Router...)

---

### 🛠️ Các loại cấu hình IP / IP Assignment Types

| Loại cấu hình / Type     | Mô tả / Description |
|--------------------------|----------------------|
| **Dynamic IP**           | Địa chỉ IP được gán tạm thời. |
| **Static IP**            | Cấu hình IP thủ công, không qua DHCP. |
| **Reserved IP (Static DHCP)** | Gán IP cố định dựa trên MAC address. |

---

## 🧠 Ví dụ minh họa / Example

1. Laptop mới kết nối Wi-Fi:
   - Gửi DHCP Discover.
   - Nhận Offer từ router (DHCP Server).
   - Gửi DHCP Request.
   - Nhận Acknowledge và được gán IP: `192.168.0.15`.

2. Router lưu lại địa chỉ MAC + IP trong bảng DHCP Lease.

---

## 📝 Bài tập / Exercises

1. Mô tả quy trình DORA với ví dụ cụ thể.
2. Phân biệt giữa địa chỉ Dynamic và Reserved IP.
3. Tìm và giải thích bảng DHCP Lease trên modem/router nhà bạn.
4. Dùng lệnh `ipconfig /renew` (Windows) hoặc `dhclient` (Linux) để yêu cầu DHCP mới.

---

## 📚 Tài liệu tham khảo / Further Reading

- [How DHCP Works – Cisco](https://www.cisco.com/c/en/us/support/docs/ip/dynamic-address-allocation-resolution/27470-bootp-dhcp.html)
- [DHCP Explained – Cloudflare](https://www.cloudflare.com/learning/network-layer/what-is-dhcp/)
- [RFC 2131 – Dynamic Host Configuration Protocol](https://datatracker.ietf.org/doc/html/rfc2131)
