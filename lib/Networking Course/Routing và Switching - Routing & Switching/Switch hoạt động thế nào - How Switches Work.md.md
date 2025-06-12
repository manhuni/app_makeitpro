Dưới đây là nội dung bài học **Switch hoạt động thế nào / How Switches Work**, trình bày trực tiếp:

---

# Switch hoạt động thế nào / How Switches Work

## 🧩 Switch là gì?

Switch (bộ chuyển mạch) là thiết bị mạng hoạt động ở lớp 2 (Data Link Layer) của mô hình OSI. Nó dùng để kết nối nhiều thiết bị trong cùng một mạng LAN và chuyển tiếp dữ liệu một cách thông minh dựa trên địa chỉ MAC.

> A switch is a network device that connects devices within a LAN and forwards frames based on MAC addresses.

---

## ⚙️ Cách switch hoạt động

1. **Học địa chỉ MAC**
   Khi một thiết bị gửi dữ liệu, switch đọc địa chỉ MAC nguồn và lưu vào bảng MAC (MAC address table) kèm theo cổng tương ứng.

2. **Chuyển tiếp frame**
   Khi switch nhận được frame, nó tra bảng MAC:

   * Nếu biết địa chỉ MAC đích, nó gửi trực tiếp đến cổng tương ứng.
   * Nếu không biết, nó gửi (flood) frame ra tất cả các cổng (trừ cổng nguồn).

3. **Lọc (Filtering)**
   Switch ngăn không cho các frame nội bộ đi ra cổng không liên quan — điều này giảm broadcast và tăng hiệu quả mạng.

---

## 📥 Bảng địa chỉ MAC (MAC address table)

Bảng này chứa:

* Địa chỉ MAC nguồn
* Cổng vật lý tương ứng (interface)
* Thời gian lưu (aging time)

Switch tự động cập nhật bảng này khi thấy frame mới từ các cổng khác nhau.

---

## 📊 Ưu điểm của switch

* Chuyển tiếp nhanh và thông minh theo MAC.
* Giảm tình trạng collision trong mạng (so với hub).
* Hỗ trợ VLAN, QoS, và nhiều tính năng nâng cao (trong switch layer 3).
* Tối ưu hóa lưu lượng bằng cách phân chia collision domain.

---

## 🔍 Sự khác biệt giữa switch và hub

| Đặc điểm         | Hub              | Switch                       |
| ---------------- | ---------------- | ---------------------------- |
| Hoạt động lớp    | Lớp 1 (Physical) | Lớp 2 (Data Link)            |
| Cách chuyển tiếp | Gửi tất cả cổng  | Gửi đúng cổng đích           |
| Collision domain | Một toàn bộ      | Mỗi cổng là một domain riêng |
| Hiệu suất        | Thấp             | Cao                          |

---

## 🛠 Tình huống thực tế

* Trong văn phòng: mỗi máy tính kết nối tới switch → switch kết nối tới router → ra Internet.
* Switch quản lý luồng dữ liệu nội bộ, giúp tránh tình trạng tắc nghẽn và đảm bảo thông tin đến đúng nơi.

---

## 📝 Tổng kết

* Switch là thiết bị không thể thiếu trong mạng LAN.
* Nó hoạt động thông minh dựa trên địa chỉ MAC.
* Switch mang lại hiệu năng, bảo mật và khả năng mở rộng vượt trội so với hub.

---

Nếu bạn muốn mở rộng thêm phần về **VLAN**, **Layer 3 Switch**, hoặc **chuyển mạch full-duplex vs half-duplex**, mình có thể viết tiếp nhé. Bạn cần phần nào?
