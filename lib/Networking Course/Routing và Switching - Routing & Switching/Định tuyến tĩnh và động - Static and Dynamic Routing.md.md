Dưới đây là nội dung đầy đủ bài học **Định tuyến tĩnh và động / Static and Dynamic Routing**, được gộp từ 3 phần trước:

---

# Định tuyến tĩnh và động / Static and Dynamic Routing

## 🧭 Định tuyến là gì?

Định tuyến (routing) là quá trình chọn đường đi cho các gói tin trong một mạng để chúng có thể đến được đích. Quá trình này thường được thực hiện bởi các thiết bị định tuyến (router).

> Routing is the process of selecting a path for traffic in a network or across multiple networks.

---

## 📌 Phần 1: Tổng quan về định tuyến / Routing Overview

### ✔️ Tại sao cần định tuyến?

* Cho phép các mạng khác nhau giao tiếp với nhau.
* Hướng dẫn đường đi của gói tin qua nhiều thiết bị trung gian.
* Cốt lõi trong hệ thống Internet và các mạng nội bộ lớn.

### 🗺 Các loại định tuyến chính

1. **Định tuyến tĩnh (Static Routing)** – Thiết lập thủ công
2. **Định tuyến động (Dynamic Routing)** – Học đường đi tự động
3. **Default Routing** – Định tuyến mặc định cho những gói tin không khớp bất kỳ tuyến nào khác

---

## ⚙️ Phần 2: Định tuyến tĩnh / Static Routing

### 🔧 Đặc điểm

* Được thiết lập thủ công bởi quản trị viên.
* Không thay đổi trừ khi có can thiệp của con người.
* Phù hợp với mạng nhỏ, đơn giản, ít thay đổi.

### 📘 Ví dụ cấu hình:

Giả sử:

* Router A kết nối với mạng 192.168.1.0/24
* Router B kết nối với mạng 192.168.2.0/24
* Họ kết nối với nhau qua mạng 10.0.0.0/30

```bash
RouterA(config)# ip route 192.168.2.0 255.255.255.0 10.0.0.2
RouterB(config)# ip route 192.168.1.0 255.255.255.0 10.0.0.1
```

### ✅ Ưu điểm:

* Đơn giản, dễ kiểm soát.
* Tiết kiệm tài nguyên CPU và băng thông.
* An toàn hơn vì không chia sẻ thông tin định tuyến.

### ❌ Nhược điểm:

* Không tự động cập nhật nếu có sự cố.
* Dễ xảy ra lỗi nếu quên cấu hình ngược chiều.
* Không phù hợp với mạng lớn.

---

## 🔄 Phần 3: Định tuyến động / Dynamic Routing

### 📗 Đặc điểm

* Router tự động trao đổi thông tin định tuyến.
* Thích nghi với sự thay đổi trong mạng (mất kết nối, tuyến mới…).
* Cần cấu hình giao thức định tuyến cụ thể.

### 🔧 Giao thức phổ biến:

| Giao thức | Loại            | Ưu điểm chính                 |
| --------- | --------------- | ----------------------------- |
| RIP       | Distance-vector | Đơn giản, dễ cấu hình         |
| OSPF      | Link-state      | Nhanh, chính xác, mở rộng tốt |
| EIGRP     | Hybrid          | Cân bằng tốc độ và độ tin cậy |
| BGP       | Path-vector     | Sử dụng trên Internet         |

### ✅ Ưu điểm:

* Tự động phát hiện và cập nhật thay đổi.
* Quản lý dễ hơn trong mạng lớn.
* Tối ưu hóa đường đi một cách liên tục.

### ❌ Nhược điểm:

* Phức tạp hơn để cấu hình ban đầu.
* Tiêu tốn tài nguyên hơn (CPU, RAM, băng thông).
* Dễ bị tấn công nếu không bảo mật đúng cách.

---

## 🔍 So sánh nhanh

| Tiêu chí              | Static Routing | Dynamic Routing     |
| --------------------- | -------------- | ------------------- |
| Cấu hình              | Thủ công       | Tự động             |
| Phản ứng với thay đổi | Không          | Có                  |
| Quy mô mạng           | Nhỏ            | Trung bình / Lớn    |
| Hiệu suất tài nguyên  | Cao            | Thấp                |
| Dễ bảo trì            | Không          | Có (trong mạng lớn) |

---

## 🧠 Tổng kết

* Định tuyến là phần không thể thiếu trong bất kỳ hệ thống mạng nào.
* Định tuyến tĩnh phù hợp cho các hệ thống nhỏ, cố định.
* Định tuyến động linh hoạt và cần thiết cho hệ thống lớn, phức tạp.
* Hiểu rõ cả hai loại là điều cần thiết cho bất kỳ kỹ sư mạng nào.

---

Nếu bạn cần bài tập thực hành với Cisco Packet Tracer hoặc ví dụ cấu hình thực tế (OSPF, RIP…), mình có thể cung cấp ngay. Bạn muốn loại nào?
