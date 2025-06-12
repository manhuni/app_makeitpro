# Phát hiện lỗi và bất thường   Troubleshooting & Anomaly Detection

## 🎯 Mục tiêu học tập / Learning Objectives

- Hiểu các bước cơ bản trong quy trình khắc phục sự cố mạng.
- Nhận biết các dấu hiệu bất thường trong lưu lượng mạng.
- Sử dụng Wireshark và các công cụ phân tích để phát hiện lỗi phổ biến.
- Phân tích các tình huống mạng thực tế như chậm, mất kết nối, tấn công.

---

## 📘 Nội dung chính / Main Content

### 🛠 Khắc phục sự cố mạng là gì? / What is Network Troubleshooting?

Là quá trình xác định và giải quyết các vấn đề ảnh hưởng đến hiệu năng, tính ổn định hoặc khả năng kết nối của mạng máy tính.

> Network troubleshooting is the process of diagnosing and resolving problems within a computer network.

---

### 🔍 Các bước khắc phục sự cố / Troubleshooting Steps

1. **Xác định vấn đề** – Người dùng báo lỗi hoặc phát hiện qua giám sát.
2. **Thu thập dữ liệu** – Dùng lệnh (ping, tracert, ipconfig) hoặc công cụ (Wireshark, SNMP).
3. **Phân tích nguyên nhân** – Dựa trên mẫu lưu lượng, log, latency, packet loss.
4. **Áp dụng giải pháp** – Cấu hình lại thiết bị, khởi động lại, đổi DNS/IP, v.v.
5. **Kiểm tra lại** – Đảm bảo sự cố không còn.

---

### 🚨 Các biểu hiện bất thường / Common Anomalies

| Biểu hiện / Symptom     | Nguyên nhân tiềm năng / Potential Cause        |
|-------------------------|-----------------------------------------------|
| **Ping thất bại**       | Mất kết nối, firewall chặn ICMP               |
| **Chậm kết nối**        | Tắc nghẽn, DNS chậm, quá tải băng thông       |
| **Kết nối không ổn định**| Truy cập intermittent, lỗi switch/router      |
| **Gói bị rớt (packet loss)**| Sự cố cáp, xung đột IP, tấn công từ chối dịch vụ |

---

### 🧪 Phân tích với Wireshark / Analysis with Wireshark

- Lọc gói `tcp.analysis.flags && !tcp.analysis.ack_rtt` để tìm lỗi TCP.
- Kiểm tra `ICMP Destination Unreachable` để phát hiện route sai.
- Xem RTT cao hoặc TCP Retransmissions để xác định độ trễ và rớt gói.
- Tìm lưu lượng DNS bất thường (DNS Flood).

---

## 🧠 Ví dụ minh họa / Example

Tình huống: Người dùng truy cập website rất chậm.

1. Dùng Wireshark lọc theo `ip.addr == IP_user`
2. Phát hiện nhiều `TCP Retransmissions` và `Out-of-order` gói
3. So sánh RTT với các phiên bình thường
4. Giải pháp: Kiểm tra switch, kiểm tra cáp hoặc cấu hình router

---

## 📝 Bài tập / Exercises

1. Sử dụng Wireshark để phân tích một kết nối bị mất.
2. Gây lỗi (vd: ping địa chỉ không tồn tại) và phân tích kết quả.
3. Dùng `ping`, `tracert`, `netstat` để kiểm tra lỗi mạng cục bộ.
4. Tìm các gói DNS bị trễ hoặc lỗi khi truy cập trang web không tồn tại.

---

## ⚠️ Lưu ý an toàn / Safety Note

> ❗ Việc phát hiện bất thường có thể liên quan đến tấn công mạng. Luôn tuân thủ đạo đức nghề nghiệp và pháp luật khi phân tích lưu lượng.

---

## 📚 Tài liệu tham khảo / Further Reading

- [Troubleshooting with Wireshark – Wireshark Docs](https://www.wireshark.org/docs/)
- [Common Network Issues and Fixes – Cisco](https://www.cisco.com/c/en/us/support/docs.html)
- [TCP Retransmissions and Delays – Cloudflare Blog](https://blog.cloudflare.com/)
