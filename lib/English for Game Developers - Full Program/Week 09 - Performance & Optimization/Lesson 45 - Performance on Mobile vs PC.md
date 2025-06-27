**Lesson 45 - Performance on Mobile vs PC (Hiệu suất trên thiết bị di động so với máy tính)**:

---

## 📘 **Mục tiêu bài học**

---

### ✅ 1. Từ vựng chính (IPA + nghĩa)

| Từ vựng                        | Phiên âm IPA                 | Nghĩa tiếng Việt                   |
| ------------------------------ | ---------------------------- | ---------------------------------- |
| mobile device                  | /ˈməʊbaɪl dɪˈvaɪs/           | thiết bị di động                   |
| desktop                        | /ˈdesktɒp/                   | máy tính để bàn                    |
| thermal throttling             | /ˈθɜːməl ˈθrɒtlɪŋ/           | giới hạn hiệu suất do quá nhiệt    |
| resource constraints           | /rɪˈzɔːs kənˈstreɪnts/       | giới hạn tài nguyên                |
| battery drain                  | /ˈbætəri dreɪn/              | hao pin                            |
| optimization strategy          | /ˌɒptɪmaɪˈzeɪʃən ˈstrætədʒi/ | chiến lược tối ưu hóa              |
| frame rate (FPS)               | /freɪm reɪt/                 | tốc độ khung hình                  |
| GPU vs CPU                     | /ˌdʒiːpiːˈjuː ˌsiːpiːˈjuː/   | card đồ họa so với bộ xử lý        |
| background processes           | /ˈbækɡraʊnd ˈprəʊsesɪz/      | tiến trình nền                     |
| platform-specific optimization | /ˈplætfɔːm spəˈsɪfɪk/        | tối ưu hóa riêng cho từng nền tảng |

---

### ✅ 2. Câu mẫu thực tế

| Câu mẫu                                                               | Dịch nghĩa                                                          |
| --------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Mobile performance is limited due to battery and thermal constraints. | Hiệu suất di động bị giới hạn bởi pin và nhiệt độ.                  |
| We had to lower the graphics quality on mobile to maintain 60 FPS.    | Chúng tôi phải giảm chất lượng đồ họa trên di động để giữ 60 FPS.   |
| Desktop machines can handle more intensive background processes.      | Máy tính có thể xử lý nhiều tiến trình nền nặng hơn.                |
| Our optimization strategy differs between Android and PC platforms.   | Chiến lược tối ưu của chúng tôi khác nhau giữa Android và PC.       |
| On mobile, we prioritize power efficiency over raw performance.       | Trên di động, chúng tôi ưu tiên tiết kiệm pin hơn là hiệu suất thô. |

---

### ✅ 3. Bài luyện viết ✍️

**Đề bài:**
So sánh hiệu suất giữa phiên bản ứng dụng trên PC và trên thiết bị di động. Viết khoảng 80–100 từ.

**Mẫu:**

```
The mobile version of our app performs well on most devices but requires aggressive optimization due to hardware limitations. On desktop, we can use higher-resolution assets and more complex animations. Mobile devices suffer from thermal throttling and limited memory, so we prioritize load time and battery efficiency. Meanwhile, the desktop version focuses on smooth transitions and visual fidelity.
```

---

### ✅ 4. Bài luyện nói 🎤

**Chủ đề gợi ý:**
**Compare the performance of your app/game on mobile vs desktop.**

**Gợi ý trình bày (30–60 giây):**

* What differences in performance did you notice?
* What did you do to optimize each version?
* What challenges did mobile devices present?
* What platform do you think is harder to optimize for, and why?

---

### ✅ 5. Ghi chú mở rộng

#### 📉 **Những giới hạn thường gặp trên mobile:**

* **CPU yếu hơn**, nhiều lõi nhưng xung nhịp thấp
* **GPU giới hạn** về shader và texture
* **Bộ nhớ RAM ít hơn** (thường 4–8GB)
* **Nhiệt độ dễ nóng**, dẫn đến **thermal throttling**
* **Thời lượng pin** là ưu tiên → tránh background tasks, dùng hiệu quả

#### ⚙️ **Chiến lược tối ưu hóa khác biệt:**

| Tiêu chí       | Trên Mobile                             | Trên PC                                        |
| -------------- | --------------------------------------- | ---------------------------------------------- |
| Đồ họa         | Giảm chất lượng textures, resolution    | Có thể bật hiệu ứng nâng cao                   |
| Đa nhiệm       | Hạn chế background processing           | Chấp nhận nhiều tiến trình song song           |
| Bộ nhớ         | Sử dụng ít RAM hơn, tái sử dụng dữ liệu | Có thể preload hoặc cache nhiều dữ liệu hơn    |
| Nhiệt độ & Pin | Tránh xử lý kéo dài                     | Không cần quan tâm đến pin hoặc giới hạn nhiệt |

#### 🔍 **Mẹo kiểm thử hiệu suất trên di động:**

* Dùng các công cụ như: Android Profiler, Xcode Instruments, Firebase Performance
* Kiểm thử trên thiết bị thật thay vì chỉ dùng giả lập
* Thử nghiệm trong điều kiện pin yếu, nóng máy hoặc bị giới hạn hiệu năng

---

Bạn muốn mình tạo một bảng checklist tối ưu hóa cho cả mobile và desktop? Hay bạn cần một đoạn code demo để thử benchmark?
