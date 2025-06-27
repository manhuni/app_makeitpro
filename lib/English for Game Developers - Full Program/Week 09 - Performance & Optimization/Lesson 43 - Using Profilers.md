**Lesson 43 - Using Profilers (Sử dụng trình phân tích hiệu suất)**:

---

## 📘 **Mục tiêu bài học:**

---

### ✅ 1. Từ vựng chính (IPA + nghĩa)

| Từ vựng                | Phiên âm IPA           | Nghĩa tiếng Việt                                   |
| ---------------------- | ---------------------- | -------------------------------------------------- |
| profiler               | /ˈprəʊfaɪlər/          | trình phân tích hiệu suất                          |
| CPU usage              | /siː piː juː ˈjuːsɪdʒ/ | mức sử dụng CPU                                    |
| memory allocation      | /ˈmeməri ˌæləˈkeɪʃən/  | việc cấp phát bộ nhớ                               |
| performance bottleneck | /pəˈfɔːməns ˈbɒtlnek/  | điểm nghẽn hiệu suất                               |
| stack trace            | /stæk treɪs/           | dấu vết ngăn xếp (gọi hàm)                         |
| sampling               | /ˈsɑːmplɪŋ/            | lấy mẫu (trong phân tích hiệu suất)                |
| instrumentation        | /ˌɪnstrəmenˈteɪʃən/    | chèn mã đo đạc vào chương trình                    |
| flame graph            | /fleɪm ɡrɑːf/          | đồ thị lửa (hiển thị các hàm chiếm thời gian chạy) |
| call hierarchy         | /kɔːl haɪˈrɑːki/       | hệ thống lời gọi hàm                               |
| optimize               | /ˈɒptɪmaɪz/            | tối ưu hóa                                         |

---

### ✅ 2. Câu mẫu thực tế

| Câu mẫu                                                                   | Dịch nghĩa                                                                       |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| We used a profiler to identify a memory bottleneck in the rendering code. | Chúng tôi dùng trình phân tích để xác định điểm nghẽn bộ nhớ trong mã dựng hình. |
| The flame graph shows that 70% of CPU time is spent on sorting.           | Đồ thị lửa cho thấy 70% thời gian CPU dành cho sắp xếp.                          |
| Sampling profilers are lighter but less precise than instrumented ones.   | Trình phân tích lấy mẫu nhẹ hơn nhưng kém chính xác hơn loại có đo đạc.          |
| We reduced CPU usage by optimizing nested loops.                          | Chúng tôi giảm mức sử dụng CPU bằng cách tối ưu vòng lặp lồng nhau.              |
| The call stack revealed a recursive function causing performance issues.  | Ngăn xếp lời gọi cho thấy một hàm đệ quy gây vấn đề hiệu suất.                   |

---

### ✅ 3. Bài luyện viết ✍️

**Đề bài:**
Viết một báo cáo ngắn sau khi sử dụng profiler để phân tích hiệu suất ứng dụng.

**Mẫu:**

```
Profiler Report Summary:

- Tool Used: Chrome DevTools
- Issue: High CPU usage when scrolling the page
- Cause: Expensive layout recalculations triggered on every scroll event
- Fix: Debounced the scroll handler and removed unnecessary DOM manipulations
- Result: CPU usage dropped by 40%, and scroll is now smooth
```

---

### ✅ 4. Bài luyện nói 🎤

**Chủ đề:**
**Explain how you used a profiler to improve app performance.**

**Gợi ý trình bày (30–60 giây):**

* What tool did you use?
* What was the performance issue?
* What did the profiler reveal?
* How did you fix the problem?
* What was the result?

---

### ✅ 5. Ghi chú mở rộng

#### 🛠 **Các loại profiler phổ biến:**

| Loại                         | Đặc điểm                                                               |
| ---------------------------- | ---------------------------------------------------------------------- |
| **Sampling** (lấy mẫu)       | Ghi lại ảnh chụp ngẫu nhiên stack → nhanh, nhẹ, dùng khi cần tổng quan |
| **Instrumentation** (đo đạc) | Chèn mã vào mọi lời gọi → chính xác, chi tiết hơn nhưng nặng           |
| **Memory profiler**          | Theo dõi cấp phát và giải phóng bộ nhớ                                 |
| **CPU profiler**             | Theo dõi thời gian thực thi từng hàm                                   |

#### 🔧 **Một số công cụ profiler:**

| Công cụ                        | Nền tảng      |
| ------------------------------ | ------------- |
| Chrome DevTools                | Web           |
| Xcode Instruments              | iOS/macOS     |
| Android Profiler               | Android       |
| Visual Studio Diagnostic Tools | Windows       |
| Py-Spy / cProfile              | Python        |
| Perf / Valgrind / gprof        | Linux / C/C++ |

#### 💡 **Mẹo khi dùng profiler:**

* Chạy profiler với **case thực tế**, không phải mẫu nhỏ.
* **So sánh trước-sau** khi tối ưu hóa.
* Kết hợp với **logs và test case** để xác minh hiệu quả.
* Chú ý các **hàm chạy lâu nhất hoặc bị gọi nhiều lần**.

---

Bạn muốn mình tạo một đoạn mã Python hoặc JavaScript có vấn đề về hiệu suất để luyện phân tích bằng profiler không? Hoặc tạo bài luyện nói với phản hồi mẫu?
