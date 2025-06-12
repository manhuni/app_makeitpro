# VPN, SSL và TLS   VPN, SSL and TLS

## 🎯 Mục tiêu học tập / Learning Objectives

- Hiểu khái niệm VPN và mục đích sử dụng.
- Nắm được cách hoạt động cơ bản của SSL và TLS trong bảo mật kết nối.
- Phân biệt giữa VPN, SSL, và TLS về chức năng và phạm vi sử dụng.
- Biết cách ứng dụng VPN và TLS vào bảo mật mạng thực tế.

---

## 📘 Nội dung chính / Main Content

### 🔐 VPN là gì? / What is a VPN?

VPN (Virtual Private Network) là một công nghệ cho phép tạo kết nối an toàn qua mạng công cộng như Internet.

> A VPN is a technology that creates a secure, encrypted connection over a less secure network, such as the internet.

#### Mục đích chính / Key Purposes:
- Ẩn danh địa chỉ IP và bảo vệ quyền riêng tư.
- Truy cập tài nguyên mạng nội bộ từ xa.
- Mã hóa toàn bộ lưu lượng để chống theo dõi.

#### Các loại VPN phổ biến:
- Site-to-Site VPN
- Remote Access VPN
- SSL VPN

---

### 🔒 SSL và TLS là gì? / What are SSL and TLS?

SSL (Secure Sockets Layer) và TLS (Transport Layer Security) là giao thức mã hóa được sử dụng để bảo vệ dữ liệu truyền qua Internet.

> SSL and TLS are cryptographic protocols designed to provide secure communication over a computer network.

#### So sánh SSL và TLS:

| Tiêu chí / Feature     | SSL         | TLS             |
|------------------------|-------------|------------------|
| Phiên bản mới hơn      | ❌           | ✅ (TLS > SSL)   |
| Bảo mật tốt hơn        | ❌           | ✅               |
| Sử dụng hiện nay       | Không nên dùng| Được khuyến nghị |

---

### 🔄 VPN vs TLS – Có gì khác biệt?

- **VPN**: Mã hóa toàn bộ kết nối mạng (tầng 3 – Network Layer).
- **TLS/SSL**: Mã hóa kết nối ứng dụng (tầng 7 – Application Layer).
- **VPN** thường được dùng để truy cập hệ thống từ xa, **TLS** thường bảo vệ web/email.

---

## 🧠 Ví dụ minh họa / Example

- Khi bạn truy cập một trang web HTTPS (vd: https://example.com), trình duyệt sử dụng TLS để mã hóa dữ liệu.
- Nhân viên công ty làm việc từ nhà có thể dùng VPN để kết nối vào mạng nội bộ công ty.

---

## 📝 Bài tập / Exercises

1. So sánh giữa VPN và TLS theo từng lớp OSI.
2. Phân tích rủi ro nếu không dùng TLS khi gửi thông tin đăng nhập trên website.
3. Cài đặt thử một phần mềm VPN miễn phí và mô tả trải nghiệm của bạn.
4. Tìm 2 website sử dụng HTTPS và phân tích chứng chỉ bảo mật của chúng.

---

## 📚 Tài liệu tham khảo / Further Reading

- [TLS Overview – Mozilla Developer Docs](https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security)
- [How VPN Works – Cloudflare](https://www.cloudflare.com/learning/network-layer/what-is-a-vpn/)
- [SSL vs TLS – DigiCert](https://www.digicert.com/ssl/ssl-vs-tls.htm)
