# DNS hoạt động ra sao   How DNS Works

## 🎯 Mục tiêu học tập / Learning Objectives

- Hiểu khái niệm hệ thống tên miền (DNS).
- Biết cách DNS chuyển tên miền thành địa chỉ IP.
- Nắm được quá trình phân giải tên miền từng bước.
- Phân biệt các loại máy chủ DNS: Root, TLD, Authoritative.

---

## 📘 Nội dung chính / Main Content

### 🌐 DNS là gì? / What is DNS?

DNS (Domain Name System) là “danh bạ điện thoại” của Internet. Nó giúp chuyển đổi tên miền dễ nhớ (vd: www.google.com) thành địa chỉ IP máy tính có thể hiểu (vd: 142.250.72.36).

> DNS is the Internet’s system for converting alphabetic names into numeric IP addresses.

---

### 🔄 Quá trình phân giải tên miền / DNS Resolution Process

1. **Trình duyệt kiểm tra cache** cục bộ xem đã có IP cho tên miền chưa.
2. **Hỏi DNS resolver (thường là router hoặc ISP)** nếu không có.
3. **Resolver hỏi Root DNS Server** để tìm máy chủ TLD.
4. **Root server trả lời máy chủ TLD** (vd: .com, .org).
5. **TLD trả lời DNS server có thẩm quyền (Authoritative)** cho tên miền.
6. **Authoritative server trả về địa chỉ IP** thực sự.
7. **Trình duyệt kết nối đến IP đó** và tải trang web.

> The DNS lookup process involves multiple servers to resolve a domain to an IP address.

---

### 🧭 Các loại máy chủ DNS / Types of DNS Servers

| Loại server / Server Type       | Vai trò / Role |
|----------------------------------|----------------|
| **Root DNS Server**              | Điểm khởi đầu, trỏ đến TLD server |
| **TLD Server (.com, .org, v.v.)** | Trỏ đến DNS server chính thức |
| **Authoritative DNS Server**     | Chứa thông tin IP thật của tên miền |
| **Recursive Resolver**           | Trung gian hỏi và thu thập kết quả |

---

## 🧠 Ví dụ minh họa / Example

Bạn gõ `www.wikipedia.org`:

1. Trình duyệt → hỏi hệ điều hành.
2. Hệ điều hành → hỏi DNS resolver (vd: 8.8.8.8).
3. Resolver thực hiện quá trình phân giải như trên.
4. Kết quả trả về: `208.80.154.224`.
5. Trình duyệt dùng IP này để tải trang.

---

## 📝 Bài tập / Exercises

1. Mô tả từng bước khi bạn truy cập `www.google.com`.
2. Dùng lệnh `nslookup` hoặc `dig` để tra IP của một website bạn chọn.
3. So sánh Recursive và Authoritative DNS server.
4. Thử ping một tên miền và sau đó ping địa chỉ IP tương ứng.

---

## 📚 Tài liệu tham khảo / Further Reading

- [How DNS Works – Cloudflare](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [Google Public DNS Overview](https://developers.google.com/speed/public-dns)
- [RFC 1034 & 1035 – DNS Standards](https://datatracker.ietf.org/doc/html/rfc1034)
