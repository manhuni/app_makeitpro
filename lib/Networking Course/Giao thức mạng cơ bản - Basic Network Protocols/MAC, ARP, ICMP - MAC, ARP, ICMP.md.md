# MAC, ARP, ICMP   MAC, ARP, ICMP

## 🎯 Mục tiêu học tập / Learning Objectives

- Hiểu vai trò và chức năng của địa chỉ MAC, giao thức ARP và ICMP trong mạng.
- Biết cách các thiết bị sử dụng ARP để ánh xạ địa chỉ IP thành địa chỉ MAC.
- Nắm được ICMP hoạt động như thế nào trong việc kiểm tra và báo lỗi kết nối.

---

## 📘 Nội dung chính / Main Content

### 🧩 Địa chỉ MAC / What is a MAC Address?

- Là địa chỉ phần cứng duy nhất của mỗi card mạng (Network Interface Card).
- Gồm 48 bit, biểu diễn dạng hex: `00:1A:2B:3C:4D:5E`
- Dùng trong tầng liên kết dữ liệu (Data Link Layer) của mô hình OSI.
- Được sử dụng trong LAN để định danh thiết bị trong cùng mạng.

> A MAC (Media Access Control) address is a unique identifier assigned to a network interface for communications on the physical network.

---

### 🔄 ARP – Address Resolution Protocol

- Giao thức ánh xạ địa chỉ IP → MAC.
- Thiết bị gửi yêu cầu ARP trong mạng LAN để biết địa chỉ MAC tương ứng với một IP.
- Gói ARP Request: Broadcast → mọi thiết bị trong mạng.
- Gói ARP Reply: Trả về địa chỉ MAC từ thiết bị sở hữu IP.

> ARP maps IP addresses to MAC addresses in a local network.

---

#### 🧠 Ví dụ ARP

1. Máy A muốn gửi dữ liệu đến IP `192.168.1.10`
2. A không biết MAC, nên gửi ARP Request: “Ai có IP 192.168.1.10?”
3. Máy B (chủ của IP đó) phản hồi bằng ARP Reply: “Địa chỉ MAC của tôi là xx:xx:xx”

---

### 📡 ICMP – Internet Control Message Protocol

- ICMP là giao thức được sử dụng để báo lỗi, kiểm tra tình trạng kết nối.
- Ping và Traceroute sử dụng ICMP để xác minh hoạt động của mạng.
- Các loại gói ICMP phổ biến:
  - Echo Request / Reply (ping)
  - Destination Unreachable
  - Time Exceeded

> ICMP is used for error messages and operational queries in network diagnostics.

---

## 🔍 Lệnh và công cụ thực hành / Useful Tools & Commands

- `ping [IP/hostname]` → Kiểm tra kết nối (ICMP Echo)
- `arp -a` → Xem bảng ARP hiện tại
- `tracert` (Windows) / `traceroute` (Linux) → Xem đường đi của gói
- Wireshark filters:
  - `arp` → xem các gói ARP
  - `icmp` → xem các gói ICMP (ping)

---

## 📝 Bài tập / Exercises

1. Sử dụng lệnh `arp -a` để xem bảng ánh xạ IP → MAC của máy bạn.
2. Dùng Wireshark để bắt gói `ARP` khi truy cập thiết bị mới trong mạng LAN.
3. Ping `8.8.8.8` và quan sát gói ICMP trong Wireshark.
4. Giải thích ý nghĩa của thông báo “Destination Host Unreachable”.

---

## 📚 Tài liệu tham khảo / Further Reading

- [What is MAC Address – Cisco](https://www.cisco.com/c/en/us/products/collateral/switches/campus-lan-switches-802-11ac/white-paper-c11-740091.html)
- [ARP Explained – GeeksforGeeks](https://www.geeksforgeeks.org/address-resolution-protocol-arp/)
- [ICMP Details – Cloudflare](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/)
