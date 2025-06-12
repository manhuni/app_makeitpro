# Tường lửa và ACL   Firewalls and ACLs

## 🎯 Mục tiêu học tập / Learning Objectives

- Hiểu khái niệm và chức năng của tường lửa.
- Biết sự khác biệt giữa các loại tường lửa: packet filtering, stateful, application-level.
- Hiểu Access Control List (ACL) là gì và cách hoạt động trong router/firewall.
- Áp dụng quy tắc ACL cơ bản để cho phép hoặc chặn lưu lượng mạng.

---

## 📘 Nội dung chính / Main Content

### 🔥 Tường lửa là gì? / What is a Firewall?

Tường lửa là một hệ thống bảo mật được thiết kế để giám sát và kiểm soát lưu lượng mạng vào và ra theo các quy tắc bảo mật được xác định trước.

> A firewall is a security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules.

#### Các loại tường lửa / Types of Firewalls:

- **Packet Filtering Firewall** – Kiểm tra các gói tin riêng lẻ dựa trên IP, cổng và giao thức.
- **Stateful Firewall** – Theo dõi trạng thái kết nối và cho phép lưu lượng dựa trên trạng thái.
- **Application Layer Firewall** – Kiểm soát lưu lượng tại tầng ứng dụng (HTTP, FTP,...).

---

### 🛂 ACL là gì? / What is an ACL?

ACL (Access Control List) là một danh sách các quy tắc cho phép hoặc từ chối lưu lượng dựa trên thông tin như IP nguồn, IP đích, cổng và giao thức.

> ACLs are rule sets that permit or deny traffic based on source/destination IP, port, and protocol.

#### Hai loại ACL chính:

- **Standard ACL** – Chỉ lọc theo địa chỉ IP nguồn.
- **Extended ACL** – Lọc theo IP nguồn, IP đích, giao thức, và cổng.

---

## 🧠 Ví dụ minh họa / Example

```bash
access-list 101 permit tcp 192.168.1.0 0.0.0.255 any eq 80
access-list 101 deny ip any any
