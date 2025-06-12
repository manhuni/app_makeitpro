# Tổng quan định tuyến / Routing Overview

## 🧭 Định tuyến là gì?

Định tuyến (routing) là quá trình chọn đường đi tốt nhất để chuyển tiếp gói tin từ thiết bị nguồn đến thiết bị đích thông qua nhiều mạng trung gian.

> Routing is the process of selecting the optimal path for data to travel from a source to a destination across interconnected networks.

---

## 🔗 Router là gì?

Router (bộ định tuyến) là thiết bị mạng hoạt động ở lớp 3 của mô hình OSI. Nó xác định đường đi của gói dữ liệu và chuyển tiếp chúng giữa các mạng khác nhau.

> A router is a network device that forwards data packets between computer networks.

---

## 🗺️ Các loại định tuyến chính

| Loại định tuyến       | Mô tả ngắn                                             |
|-----------------------|---------------------------------------------------------|
| Định tuyến tĩnh        | Tuyến đường được thiết lập thủ công bởi quản trị viên. |
| Định tuyến động        | Tuyến đường được thiết lập tự động nhờ các giao thức. |

---

## 📥 Bảng định tuyến là gì?

Bảng định tuyến (routing table) là tập hợp các tuyến đường mà router lưu giữ để quyết định nơi gửi gói tin.

| Trường                  | Ý nghĩa                                                |
|-------------------------|---------------------------------------------------------|
| Destination network     | Mạng đích của gói tin                                   |
| Subnet mask             | Mặt nạ mạng để xác định kích thước mạng con             |
| Next hop                | Địa chỉ IP của bước kế tiếp (router tiếp theo)          |
| Interface               | Giao diện mạng mà gói tin sẽ được gửi đi                 |
| Metric / Cost           | Giá trị đánh giá chi phí của tuyến (dùng để chọn đường) |

---

## 🧠 Vì sao định tuyến quan trọng?

- Kết nối các mạng nội bộ và Internet.
- Tối ưu hóa hiệu suất truyền dữ liệu.
- Đảm bảo đường truyền tin cậy và linh hoạt.
- Giúp mạng mở rộng và quản lý dễ dàng hơn.

---

## 🔄 Tổng kết

- Định tuyến là chức năng cốt lõi trong mạng.
- Router sử dụng bảng định tuyến để xác định nơi gửi gói tin.
- Có hai loại chính: định tuyến tĩnh và định tuyến động.

Dưới đây là nội dung **phần 2: Định tuyến tĩnh / Static Routing.md** ở dạng plaintext thuần (không có khung code hay markdown hiển thị đặc biệt):

---

# Định tuyến tĩnh / Static Routing

## ✅ Định tuyến tĩnh là gì?

Định tuyến tĩnh là hình thức cấu hình đường đi cố định cho các gói tin trong mạng. Các tuyến đường được thiết lập thủ công bởi quản trị viên và không thay đổi trừ khi được chỉnh sửa.

> Static routing involves manually configuring fixed paths for network traffic.

## 🔧 Ví dụ cấu hình đơn giản

Giả sử: Bạn có 2 mạng:

* Mạng A: 192.168.1.0/24 nằm sau Router A
* Mạng B: 192.168.2.0/24 nằm sau Router B

Trên Router A, cấu hình để tới mạng B:

RouterA(config)# ip route 192.168.2.0 255.255.255.0 10.0.0.2

Trên Router B, cấu hình để tới mạng A:

RouterB(config)# ip route 192.168.1.0 255.255.255.0 10.0.0.1

## 📊 Ưu điểm của định tuyến tĩnh

* Dễ triển khai cho mạng nhỏ.
* Tiết kiệm tài nguyên vì không cần tính toán hay gửi cập nhật định kỳ.
* Tăng cường bảo mật do không có cập nhật định tuyến từ bên ngoài.
* Quản trị viên có toàn quyền kiểm soát tuyến đường.

## ⚠️ Nhược điểm

* Không tự động thích ứng nếu có sự cố mạng.
* Quản lý phức tạp khi mạng mở rộng.
* Dễ xảy ra lỗi do thao tác thủ công.

## 🛠 Khi nào nên dùng định tuyến tĩnh?

* Mạng nhỏ hoặc đơn giản (≤ 5 router).
* Môi trường bảo mật cao, không muốn tự động học tuyến.
* Các kết nối backup dự phòng.

## 🧠 Gợi ý thực hành

1. Cấu hình static route giữa hai router trên Packet Tracer.
2. Dùng lệnh `show ip route` để kiểm tra bảng định tuyến.
3. Dùng `ping` hoặc `traceroute` để kiểm tra đường đi dữ liệu.

## 📝 Tổng kết

* Định tuyến tĩnh phù hợp với môi trường đơn giản, ít thay đổi.
* Cần quản trị viên hiểu rõ cấu trúc mạng để cấu hình chính xác.
* Thiết lập dễ dàng nhưng thiếu linh hoạt so với định tuyến động.

---

Bạn có muốn mình tiếp tục với **phần 3 – Định tuyến động / Dynamic Routing.md** không?
Dưới đây là nội dung **phần 3: Định tuyến động / Dynamic Routing.md** dạng plaintext thuần:

---

# Định tuyến động / Dynamic Routing

## 🔄 Định tuyến động là gì?

Định tuyến động là phương pháp trong đó các router tự động học hỏi và cập nhật thông tin định tuyến bằng cách sử dụng các giao thức định tuyến.

> Dynamic routing uses routing protocols that allow routers to learn and adjust to network changes automatically.

## 🧠 Giao thức định tuyến phổ biến

| Giao thức | Loại            | Đặc điểm chính                               |
| --------- | --------------- | -------------------------------------------- |
| RIP       | Distance-vector | Dễ cấu hình, tốc độ chậm, giới hạn hop       |
| OSPF      | Link-state      | Chính xác, nhanh, sử dụng trong doanh nghiệp |
| EIGRP     | Hybrid          | Kết hợp ưu điểm của distance và link-state   |
| BGP       | Path-vector     | Dùng trong Internet, giữa các tổ chức lớn    |

## ⚙️ Cách hoạt động

* Router gửi thông tin định tuyến cho các router láng giềng.
* Thông tin này được xử lý để cập nhật bảng định tuyến.
* Khi có thay đổi (mất kết nối, thêm mạng mới), bảng định tuyến được điều chỉnh tự động.

## 📊 Ưu điểm

* Tự động cập nhật khi có sự thay đổi trong mạng.
* Phù hợp với hệ thống lớn, phức tạp.
* Giảm nguy cơ lỗi do cấu hình thủ công.

## ⚠️ Nhược điểm

* Tốn tài nguyên hệ thống (CPU, RAM).
* Có thể chậm phản hồi trong một số giao thức.
* Cần kiến thức sâu hơn để cấu hình và giám sát.

## 🛠 Khi nào nên dùng định tuyến động?

* Mạng lớn, nhiều router, topology thay đổi thường xuyên.
* Môi trường yêu cầu khả năng thích ứng cao.
* Hệ thống doanh nghiệp hoặc tổ chức lớn.

## 💡 Gợi ý thực hành

1. Cấu hình OSPF cho 3 router nối mạng với nhau.
2. Sử dụng lệnh `show ip protocols` và `show ip route` để kiểm tra thông tin định tuyến.
3. Ngắt kết nối một router và quan sát cách mạng thích ứng.

## 📝 Tổng kết

* Định tuyến động giúp mạng phản ứng linh hoạt với thay đổi.
* Các giao thức như OSPF, RIP, EIGRP... hỗ trợ tự động hóa việc định tuyến.
* Cần hiểu rõ giao thức và quản lý kỹ để đạt hiệu quả cao và tránh rủi ro.

---

Nếu bạn muốn mình gộp 3 phần vào một thư mục hoặc tạo thêm mục lục tổng quan, chỉ cần nói nhé.
