Dưới đây là nội dung bài học **Subnetting và CIDR / Subnetting and CIDR** trình bày trực tiếp, không định dạng `.md`:

---

# Subnetting và CIDR / Subnetting and CIDR

## 📌 Subnetting là gì?

Subnetting là quá trình chia một mạng IP lớn thành nhiều mạng con nhỏ hơn (subnet) để quản lý hiệu quả hơn và tối ưu việc sử dụng địa chỉ IP.

> Subnetting is the practice of dividing a large IP network into smaller, manageable subnetworks.

## 🧮 Tại sao cần subnetting?

* Giảm tắc nghẽn mạng bằng cách giới hạn phạm vi broadcast.
* Tăng cường bảo mật bằng cách cô lập các phần mạng.
* Quản lý tốt hơn cho hệ thống có nhiều phòng ban, chi nhánh.
* Tiết kiệm địa chỉ IP bằng cách chỉ cấp phát những gì cần.

## 🧩 Các khái niệm cơ bản

* **Network Address**: Địa chỉ đại diện cho toàn bộ mạng con (ví dụ: 192.168.1.0).
* **Broadcast Address**: Địa chỉ gửi tới toàn bộ thiết bị trong mạng con (ví dụ: 192.168.1.255).
* **Host Address**: Địa chỉ có thể gán cho thiết bị (PC, router...).
* **Subnet Mask**: Mặt nạ mạng xác định phần nào là mạng và phần nào là host.

Ví dụ:

* IP: 192.168.1.10
* Subnet mask: 255.255.255.0
  → Network: 192.168.1.0
  → Broadcast: 192.168.1.255
  → Host range: 192.168.1.1 đến 192.168.1.254

## 📐 CIDR là gì?

CIDR (Classless Inter-Domain Routing) là cách biểu diễn mạng không dựa vào các lớp A/B/C cố định, cho phép linh hoạt hơn.

* Thay vì viết: 255.255.255.0 → ta dùng: **/24**
* CIDR giúp tiết kiệm IP và hỗ trợ định tuyến hiệu quả hơn.

Ví dụ:

* 192.168.1.0/24: 256 địa chỉ (254 usable hosts)
* 10.0.0.0/8: 16.777.216 địa chỉ
* 192.168.1.0/30: 4 địa chỉ (2 usable hosts)

## 🧠 Tính toán subnet cơ bản

Ví dụ: 192.168.1.0/26 → Bao nhiêu host?

* Subnet mask: 255.255.255.192
* 2^(32 - 26) = 64 địa chỉ
* Trừ 2 (network và broadcast): 62 usable hosts

## ⚙️ Ứng dụng thực tế

* Phân chia mạng cho các bộ phận (HR, IT, Kế toán…).
* Thiết lập VLAN theo subnet.
* Tối ưu hóa địa chỉ IP trong hạ tầng cloud hoặc datacenter.

## 📝 Tổng kết

* Subnetting giúp chia nhỏ mạng để dễ quản lý và bảo mật hơn.
* CIDR cung cấp cách biểu diễn mạng ngắn gọn và linh hoạt.
* Nắm vững cách tính số host, subnet mask là rất cần thiết khi thiết kế mạng.

---

Nếu bạn cần bài tập thực hành về Subnetting hoặc bảng quy đổi CIDR → Subnet mask, mình có thể cung cấp tiếp. Bạn muốn chứ?
