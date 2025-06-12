import os

# Cấu trúc khóa học
course_structure  = {
    "Giới thiệu Mạng Máy Tính - Introduction to Computer Networks": [
        "Giới thiệu mạng - Introduction to Networking.md",
        "Kiến trúc mạng cơ bản - Basic Network Architecture.md"
    ],
    "Mô hình OSI và TCP-IP - OSI & TCP-IP Models": [
        "Mô hình OSI - OSI Model.md",
        "Ngăn xếp TCP-IP - TCP-IP Stack.md"
    ],
    "Giao thức mạng cơ bản - Basic Network Protocols": [
        "Địa chỉ IP - IP Addressing.md",
        "MAC, ARP, ICMP - MAC, ARP, ICMP.md",
        "TCP và UDP - TCP and UDP.md"
    ],
    "Routing và Switching - Routing & Switching": [
        "Switch hoạt động thế nào - How Switches Work.md",
        "Định tuyến tĩnh và động - Static and Dynamic Routing.md",
        "Subnetting và CIDR - Subnetting and CIDR.md"
    ],
    "DNS, DHCP và NAT - DNS, DHCP & NAT": [
        "DNS hoạt động ra sao - How DNS Works.md",
        "Cơ chế cấp phát IP với DHCP - DHCP Overview.md",
        "Chuyển đổi địa chỉ mạng (NAT) - Network Address Translation (NAT).md"
    ],
    "Bảo mật mạng cơ bản - Basic Network Security": [
        "Tường lửa và ACL - Firewalls and ACLs.md",
        "VPN, SSL và TLS - VPN, SSL and TLS.md"
    ],
    "Giám sát và Phân tích mạng (Wireshark) - Network Monitoring & Analysis (Wireshark)": [
        "Giới thiệu Wireshark - Introduction to Wireshark.md",
        "Bắt gói và phân tích cơ bản - Packet Capturing & Basic Analysis.md",
        "Phát hiện lỗi và bất thường - Troubleshooting & Anomaly Detection.md"
    ],
    "Thực hành và Case Study - Practice & Case Studies": [
        "Thực hành Ping, Traceroute - Practice: Ping & Traceroute.md",
        "Phân tích hệ thống mạng doanh nghiệp - Case Study: Enterprise Network.md"
    ]
}
# course_structure = {
#     "Present Simple - Hiện tại đơn": [],
#     "Present Continuous - Hiện tại tiếp diễn": [],
#     "Present Perfect - Hiện tại hoàn thành": [],
#     "Present Perfect Continuous - Hiện tại hoàn thành tiếp diễn": [],
#     "Past Simple - Quá khứ đơn": [],
#     "Past Continuous - Quá khứ tiếp diễn": [],
#     "Past Perfect - Quá khứ hoàn thành": [],
#     "Past Perfect Continuous - Quá khứ hoàn thành tiếp diễn": [],
#     "Future Simple - Tương lai đơn": [],
#     "Future Continuous - Tương lai tiếp diễn": [],
#     "Future Perfect - Tương lai hoàn thành": [],
#     "Future Perfect Continuous - Tương lai hoàn thành tiếp diễn": []
# }

# Hoặc thay bằng dict nếu có nhiều chương
# course_structure = {
#     "1-Chuong-mot": ["01-Bai-1", "02-Bai-2"],
#     "2-Chuong-hai": ["01-Bai-1", "02-Bai-2"]
# }

# Tên thư mục gốc
root_dir = "Networking Course"

if isinstance(course_structure, dict):
    # Trường hợp có thư mục chương
    for folder, files in course_structure.items():
        folder_path = os.path.join(root_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        for filename in files:
            file_path = os.path.join(folder_path, f"{filename}.md")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# {filename.replace('-', ' ')}\n")
else:
    # Trường hợp chỉ là danh sách file .md, không có thư mục
    os.makedirs(root_dir, exist_ok=True)
    for filename in course_structure:
        file_path = os.path.join(root_dir, f"{filename}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {filename.replace('-', ' ')}\n")

print("✅ Đã tạo xong cây thư mục khóa học.")
