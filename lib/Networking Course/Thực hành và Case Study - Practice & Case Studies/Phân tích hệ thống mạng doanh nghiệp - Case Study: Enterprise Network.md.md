Dưới đây là nội dung bài học:

---

# Phân tích hệ thống mạng doanh nghiệp / Case Study: Enterprise Network

## 🏢 Mục tiêu

Hiểu cách thiết kế và phân tích một hệ thống mạng trong môi trường doanh nghiệp thực tế, bao gồm các thành phần, kiến trúc, bảo mật, và hiệu năng.

> Learn how enterprise networks are structured, how they function, and how to analyze their components for security and performance.

---

## 🧱 Cấu trúc tổng thể của mạng doanh nghiệp

Một hệ thống mạng doanh nghiệp thường có ba lớp chính:

1. **Lớp truy cập (Access Layer)**

   * Kết nối trực tiếp với thiết bị đầu cuối như máy tính, máy in.
   * Dùng switch lớp 2 hoặc lớp 3.
   * Hỗ trợ VLAN, bảo mật cổng (port security).

2. **Lớp phân phối (Distribution Layer)**

   * Kết nối các switch truy cập.
   * Xử lý định tuyến nội bộ (OSPF, EIGRP...).
   * Áp dụng chính sách bảo mật và QoS.

3. **Lớp lõi (Core Layer)**

   * Tốc độ cao, định tuyến nhanh giữa các phân vùng mạng.
   * Ít hoặc không xử lý phức tạp, chỉ tập trung tốc độ và ổn định.

---

## 🔗 Các thành phần chính

* **Switch / Router doanh nghiệp**
  Thiết bị có khả năng xử lý lưu lượng lớn, hỗ trợ các giao thức nâng cao.

* **Firewall**
  Bảo vệ khỏi truy cập trái phép và các mối đe dọa bên ngoài.

* **VPN Gateway**
  Hỗ trợ truy cập từ xa an toàn cho nhân viên.

* **Server nội bộ**
  File server, DNS, DHCP, AD server,...

* **Wireless Controller & Access Point**
  Cung cấp kết nối không dây quản lý tập trung.

---

## 🔒 Bảo mật trong mạng doanh nghiệp

* Sử dụng **VLAN** để phân tách các bộ phận (HR, IT, Kế toán,...).
* Áp dụng **ACLs** để giới hạn truy cập giữa các mạng.
* **802.1X** cho xác thực thiết bị đầu cuối.
* **IDS/IPS** để phát hiện và ngăn chặn xâm nhập.

---

## 📊 Hiệu năng & giám sát

* Dùng SNMP để theo dõi switch/router.
* Phân tích lưu lượng bằng Wireshark hoặc NetFlow.
* Áp dụng QoS cho các dịch vụ quan trọng như VoIP.
* Triển khai dự phòng (redundancy): HSRP, VRRP, link aggregation.

---

## 📘 Tình huống ví dụ

**Doanh nghiệp ABC:**

* 1 trụ sở chính, 3 chi nhánh.
* Mỗi chi nhánh có 2 VLAN: nội bộ & khách.
* Kết nối site-to-site VPN về trung tâm.
* Firewall tại trụ sở áp dụng chính sách lọc URL.
* Phân tích phát hiện gói tin lạ qua cổng 23 (Telnet) → triển khai kiểm soát truy cập và tắt dịch vụ không an toàn.

---

## 🧠 Tổng kết

* Mạng doanh nghiệp yêu cầu thiết kế chặt chẽ, bảo mật cao, và hiệu suất ổn định.
* Cần kết hợp nhiều công nghệ: routing, switching, firewall, wireless, và monitoring.
* Phân tích định kỳ giúp duy trì hiệu năng và ngăn chặn sự cố kịp thời.

---

Bạn có muốn mình vẽ sơ đồ minh họa mạng doanh nghiệp ví dụ để dễ hình dung không?
