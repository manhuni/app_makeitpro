Dưới đây là nội dung bài học:

---

# Thực hành Ping, Traceroute / Practice: Ping & Traceroute

## 🎯 Mục tiêu

* Hiểu cách sử dụng lệnh `ping` và `traceroute` để kiểm tra kết nối mạng.
* Phân tích đường đi của gói tin từ thiết bị đến đích.
* Ứng dụng để chẩn đoán sự cố mạng đơn giản.

> Learn to use `ping` and `traceroute` to diagnose basic network connectivity issues and analyze the path data takes across a network.

---

## 🟢 Ping là gì?

`ping` là công cụ kiểm tra kết nối giữa hai thiết bị mạng bằng cách gửi các gói ICMP Echo Request và nhận lại Echo Reply.

### ✅ Cú pháp:

```bash
ping [địa chỉ IP hoặc hostname]
```

### 📌 Ví dụ:

```bash
ping 8.8.8.8
ping www.google.com
```

### 📋 Kết quả trả về:

* **TTL (Time To Live)**: số hop còn lại trước khi gói bị loại bỏ.
* **Thời gian phản hồi (ms)**: độ trễ mạng.
* **Packet loss**: mất gói (nếu có).

### 🔍 Khi nào dùng `ping`?

* Kiểm tra có thể kết nối đến một IP/host hay không.
* Phát hiện gián đoạn kết nối mạng.

---

## 🛤 Traceroute là gì?

`traceroute` cho biết **các điểm trung gian (hop)** mà gói tin đi qua để đến đích.

### ✅ Cú pháp:

```bash
traceroute [địa chỉ IP hoặc hostname]   # Trên Linux/macOS
tracert [địa chỉ IP hoặc hostname]      # Trên Windows
```

### 📌 Ví dụ:

```bash
traceroute 8.8.8.8
tracert www.google.com
```

### 📋 Kết quả trả về:

* Danh sách địa chỉ IP của các router trung gian.
* Thời gian phản hồi từng hop.
* Giúp xác định chỗ "nghẽn cổ chai" trong đường truyền.

---

## 🧪 Bài tập thực hành

### Bài 1: Kiểm tra kết nối nội bộ

```bash
ping 192.168.1.1    # Gateway nội bộ
ping 192.168.1.100  # Một máy khác trong cùng mạng
```

### Bài 2: Kiểm tra kết nối Internet

```bash
ping 8.8.8.8
ping www.facebook.com
```

### Bài 3: Phân tích đường đi

```bash
tracert www.microsoft.com
traceroute www.youtube.com
```

> Nếu gói dừng ở hop nào đó → kiểm tra thiết bị tương ứng hoặc định tuyến.

---

## ⚠️ Lưu ý

* Một số hệ thống **chặn ICMP** → `ping` sẽ không trả về kết quả dù vẫn kết nối được.
* `traceroute` phụ thuộc vào TTL và có thể bị tường lửa chặn.

---

## 🧠 Tổng kết

* `ping` giúp kiểm tra nhanh kết nối.
* `traceroute` giúp phân tích tuyến đường và xác định vị trí lỗi.
* Đây là những công cụ quan trọng nhất trong xử lý sự cố mạng căn bản.

---

Bạn có muốn mình tạo mô phỏng thực hành bằng **Cisco Packet Tracer** hay sơ đồ minh họa đường đi của traceroute không?
