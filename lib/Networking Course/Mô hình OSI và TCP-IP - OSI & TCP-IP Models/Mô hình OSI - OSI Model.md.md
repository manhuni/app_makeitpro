# Mô hình OSI   OSI Model

## 🎯 Mục tiêu học tập / Learning Objectives

- Hiểu rõ mô hình OSI và vai trò của từng tầng trong truyền thông mạng.
- Nắm được chức năng, giao thức và ví dụ cụ thể ở mỗi tầng.
- Phân biệt OSI với mô hình TCP/IP.
- Áp dụng kiến thức mô hình OSI để phân tích lưu lượng mạng bằng Wireshark.

---

## 📘 Nội dung chính / Main Content

### 🧱 Mô hình OSI là gì? / What is the OSI Model?

Mô hình OSI (Open Systems Interconnection) là một chuẩn tham chiếu do ISO phát triển để mô tả cách các hệ thống mạng giao tiếp với nhau qua 7 tầng.

> The OSI model is a conceptual framework used to understand and standardize the functions of a telecommunication or computing system in seven distinct layers.

---

### 🔢 7 Tầng của OSI / The 7 Layers of OSI

| Tầng | Tên tầng (Tiếng Việt)        | Tên tầng (Tiếng Anh)    | Chức năng chính / Main Functions                      |
|------|-------------------------------|--------------------------|--------------------------------------------------------|
| 7    | Tầng Ứng dụng                 | Application Layer        | Giao tiếp giữa người dùng và ứng dụng mạng             |
| 6    | Tầng Trình bày                | Presentation Layer       | Mã hóa, nén, định dạng dữ liệu                         |
| 5    | Tầng Phiên                    | Session Layer            | Quản lý phiên giao tiếp (session)                      |
| 4    | Tầng Giao vận                 | Transport Layer          | Truyền dữ liệu tin cậy (TCP), không tin cậy (UDP)      |
| 3    | Tầng Mạng                     | Network Layer            | Định tuyến gói dữ liệu, địa chỉ IP                     |
| 2    | Tầng Liên kết dữ liệu         | Data Link Layer          | Địa chỉ MAC, phát hiện lỗi khung                       |
| 1    | Tầng Vật lý                   | Physical Layer           | Truyền bit qua phương tiện vật lý (dây, sóng...)       |

---

### 🔁 Cách hoạt động của mô hình OSI

- Khi bạn gửi dữ liệu (ví dụ: email), dữ liệu đi từ tầng 7 → tầng 1 (gói thành bit).
- Khi đến đích, dữ liệu được giải mã từ tầng 1 → tầng 7 để hiển thị với người dùng.

> “All People Seem To Need Data Processing” – Mẹo nhớ từ dưới lên.

---

### 🔍 Ví dụ thực tế / Practical Examples

- **Tầng 4 – Transport**: TCP đảm bảo email đến đúng thứ tự.
- **Tầng 3 – Network**: Gói dữ liệu định tuyến qua Internet tới đúng IP.
- **Tầng 2 – Data Link**: MAC dùng để giao tiếp trong mạng nội bộ.
- **Tầng 1 – Physical**: Dữ liệu truyền qua cáp Ethernet hoặc Wi-Fi.

---

### 🔄 So sánh với TCP/IP

| Mô hình OSI         | Mô hình TCP/IP     |
|---------------------|--------------------|
| 7. Application       | Application         |
| 6. Presentation      | Application         |
| 5. Session           | Application         |
| 4. Transport         | Transport           |
| 3. Network           | Internet            |
| 2. Data Link         | Network Access      |
| 1. Physical          | Network Access      |

---

## 🧪 Quan sát với Wireshark

- Gói dữ liệu trong Wireshark hiển thị từ tầng 2 (Ethernet) đến tầng 7.
- Ví dụ: Một gói HTTP có thể quan sát:
  - Ethernet (Data Link)
  - IP (Network)
  - TCP (Transport)
  - HTTP (Application)

---

## 📝 Bài tập / Exercises

1. Liệt kê 3 giao thức thường gặp ở mỗi tầng OSI.
2. Giải thích tại sao TCP nằm ở tầng 4 còn IP nằm ở tầng 3.
3. Mô tả dòng chảy dữ liệu từ tầng 7 đến tầng 1 khi bạn gửi tin nhắn qua mạng.
4. Sử dụng Wireshark để phân tích một gói HTTP, xác định các lớp OSI trong gói đó.

---

## 📚 Tài liệu tham khảo / Further Reading

- [OSI Model – Cisco](https://www.cisco.com/c/en/us/solutions/service-provider/osi-model.html)
- [Explaining the OSI Model – Cloudflare](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/)
- [Layers of OSI – GeeksforGeeks](https://www.geeksforgeeks.org/layers-of-osi-model/)
