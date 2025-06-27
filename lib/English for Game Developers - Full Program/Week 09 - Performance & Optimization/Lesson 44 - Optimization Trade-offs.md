**Lesson 44 - Optimization Trade-offs (Sự đánh đổi trong tối ưu hóa)**:

---

## 📘 **Mục tiêu bài học:**

---

### ✅ 1. Từ vựng chính (IPA + nghĩa)

| Từ vựng                | Phiên âm IPA                 | Nghĩa tiếng Việt            |
| ---------------------- | ---------------------------- | --------------------------- |
| trade-off              | /ˈtreɪd ˌɒf/                 | sự đánh đổi giữa hai yếu tố |
| performance            | /pəˈfɔːməns/                 | hiệu suất                   |
| readability            | /ˌriːdəˈbɪləti/              | tính dễ đọc (của mã nguồn)  |
| maintainability        | /meɪnˌteɪnəˈbɪləti/          | khả năng bảo trì            |
| memory consumption     | /ˈmeməri kənˈsʌmpʃən/        | lượng bộ nhớ tiêu thụ       |
| processing speed       | /ˈprəʊsesɪŋ spiːd/           | tốc độ xử lý                |
| over-optimization      | /ˌəʊvərˌɒptɪmaɪˈzeɪʃən/      | tối ưu hóa quá mức          |
| code complexity        | /kəʊd kəmˈpleksəti/          | độ phức tạp của mã          |
| premature optimization | /ˈpriːmətʃər ɒptɪmaɪˈzeɪʃən/ | tối ưu hóa quá sớm          |
| bottleneck             | /ˈbɒtlnek/                   | điểm nghẽn                  |

---

### ✅ 2. Câu mẫu thực tế

| Câu mẫu                                                               | Dịch nghĩa                                                          |
| --------------------------------------------------------------------- | ------------------------------------------------------------------- |
| There’s a trade-off between speed and code readability.               | Có sự đánh đổi giữa tốc độ và khả năng đọc hiểu mã.                 |
| We avoided premature optimization to keep the code simple.            | Chúng tôi tránh tối ưu hóa sớm để giữ mã đơn giản.                  |
| Improving memory usage added some complexity to the logic.            | Việc cải thiện sử dụng bộ nhớ đã làm tăng độ phức tạp logic.        |
| Sometimes performance gains aren’t worth the cost in maintainability. | Đôi khi việc cải thiện hiệu suất không đáng so với chi phí bảo trì. |
| The optimization helped reduce latency, but increased CPU usage.      | Tối ưu hóa giúp giảm độ trễ nhưng làm tăng sử dụng CPU.             |

---

### ✅ 3. Bài luyện viết ✍️

**Đề bài:**
Viết một đoạn ngắn mô tả một tình huống trong dự án mà bạn (hoặc nhóm bạn) phải cân nhắc giữa hiệu suất và các yếu tố khác như độ dễ đọc hoặc khả năng bảo trì.

**Mẫu:**

```
During a performance review, we optimized a function to run 3x faster.

However, the new version used bitwise operations and complex recursion, making the code hard to read.

We eventually rewrote it with a more readable structure, accepting a slight performance drop.

The final version balanced both performance and maintainability.
```

---

### ✅ 4. Bài luyện nói 🎤

**Chủ đề:**
**Describe a situation where you had to make a performance trade-off.**

**Gợi ý trình bày (30–60 giây):**

* What were the two things you had to balance?
* Why was the trade-off necessary?
* What choice did you make and why?
* What was the result?

---

### ✅ 5. Ghi chú mở rộng

#### ⚖️ **Các kiểu đánh đổi phổ biến trong tối ưu hóa:**

| Đánh đổi                               | Mô tả ví dụ thực tế                                                   |
| -------------------------------------- | --------------------------------------------------------------------- |
| **Hiệu suất vs. Tính dễ đọc**          | Dùng thuật toán nhanh nhưng khó hiểu vs. mã đơn giản, dễ hiểu hơn     |
| **Tốc độ vs. Tiêu thụ bộ nhớ**         | Lưu sẵn dữ liệu (tốn RAM) vs. tính toán lại mỗi lần (tốn CPU)         |
| **Thời gian phát triển vs. Hiệu suất** | Làm nhanh để ra MVP vs. mất thời gian tối ưu kỹ càng                  |
| **Đơn giản vs. Mở rộng linh hoạt**     | Giải pháp đơn giản nhưng không mở rộng tốt vs. kiến trúc phức tạp hơn |

#### 🧠 **Mẹo tư duy khi tối ưu hóa:**

* **Tối ưu đúng chỗ**: tập trung vào bottleneck, không phải chỗ “có thể” nhanh hơn
* **Đo trước khi tối ưu**: dùng profiler, log, thống kê thực tế
* **Tối ưu từng bước**: ưu tiên cải thiện mà vẫn giữ mã rõ ràng
* **Tối ưu hóa là nghệ thuật cân bằng**, không phải chạy theo “tối đa mọi chỉ số”

---

Bạn có muốn mình tạo một bài thảo luận nhóm mô phỏng tình huống đánh đổi tối ưu hóa không? Hoặc giúp bạn viết lại đoạn code “dễ đọc hơn” mà vẫn giữ hiệu suất?
