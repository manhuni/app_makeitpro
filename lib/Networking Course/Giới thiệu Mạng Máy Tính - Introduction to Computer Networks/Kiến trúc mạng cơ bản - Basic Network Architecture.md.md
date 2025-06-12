# Kiến trúc mạng cơ bản   Basic Network Architecture

## 🎯 Mục tiêu học tập / Learning Objectives

- Hiểu kiến trúc tổng quát của một mạng máy tính.
- Nắm được các mô hình phổ biến như Client-Server và Peer-to-Peer.
- Phân biệt các thiết bị mạng theo vai trò và chức năng.
- Biết được các lớp trong mô hình TCP/IP hoạt động như thế nào trong thực tế.

---

## 📘 Nội dung chính / Main Content

### 🏗️ Kiến trúc mạng là gì? / What is Network Architecture?

Kiến trúc mạng là cách tổ chức và cấu trúc các thành phần trong một mạng để đảm bảo việc truyền thông tin hiệu quả giữa các thiết bị.

> Network architecture refers to the design and layout of a computer network, including its physical components, functional organization, protocols, and technologies.

---

### 🧭 Các mô hình mạng phổ biến / Common Network Models

#### 1. Mô hình Client-Server

- Máy chủ (Server) cung cấp dịch vụ; máy khách (Client) sử dụng dịch vụ.
- Dễ quản lý, phổ biến trong doanh nghiệp và Internet.
- Ví dụ: Web server – trình duyệt, Mail server – email client.

#### 2. Mô hình Peer-to-Peer (P2P)

- Các thiết bị ngang hàng, vừa là client vừa là server.
- Ít tốn chi phí, khó mở rộng.
- Ví dụ: chia sẻ file qua mạng nội bộ, torrent.

---

### 🔌 Thiết bị trong mạng / Network Devices

| Thiết bị / Device | Chức năng / Function                                       |
|------------------|-------------------------------------------------------------|
| **Hub**          | Phát tín hiệu đến mọi cổng (ít dùng hiện nay)              |
| **Switch**       | Chuyển mạch thông minh trong mạng LAN                      |
| **Router**       | Định tuyến giữa các mạng khác nhau                         |
| **Access Point** | Phát sóng Wi-Fi cho thiết bị không dây                     |
| **Modem**        | Kết nối mạng nội bộ với Internet thông qua nhà cung cấp ISP |

---

### 📐 Mô hình lớp TCP/IP / TCP/IP Model

| Tầng / Layer           | Chức năng / Function                        | Ví dụ / Examples                   |
|------------------------|---------------------------------------------|------------------------------------|
| **Application**        | Giao tiếp ứng dụng                         | HTTP, FTP, DNS                     |
| **Transport**          | Truyền dữ liệu, kiểm lỗi                  | TCP, UDP                           |
| **Internet**           | Định tuyến gói dữ liệu                    | IP                                 |
| **Network Access**     | Truyền vật lý qua mạng                    | Ethernet, Wi-Fi                    |

---

### 🖼️ Sơ đồ mạng cơ bản / Basic Network Diagram

```plaintext
[PC1] --\
         \
         [Switch] -- [Router] -- [Internet]
         /
[PC2] --/
📝 Bài tập / Exercises
Vẽ sơ đồ mạng của nhà bạn hoặc lớp học, xác định vai trò các thiết bị.

So sánh mô hình Client-Server và Peer-to-Peer: ưu nhược điểm.

Kể tên ít nhất 3 thiết bị mạng bạn từng sử dụng và vai trò của chúng.

Giải thích từng tầng của mô hình TCP/IP bằng ví dụ cụ thể.

📚 Tài liệu tham khảo / Further Reading
Network Architectures – Cisco

TCP/IP Layers – GeeksforGeeks

Network Topologies & Design – IBM