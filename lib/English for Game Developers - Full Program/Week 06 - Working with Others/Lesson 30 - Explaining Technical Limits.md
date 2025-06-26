Dưới đây là nội dung chi tiết cho:

---

# ✅ Lesson 30 – Explaining Technical Limits

> 📘 **Mục tiêu bài học:**

* ✅ Diễn đạt rào cản kỹ thuật bằng tiếng Anh rõ ràng, chuyên nghiệp.
* ✅ Trình bày giải pháp thay thế hoặc giải thích lý do kỹ thuật.
* ✅ Giao tiếp hiệu quả với non-dev (quản lý, thiết kế, khách hàng).

---

## 📚 Từ vựng chính (IPA + nghĩa)

| Từ / Cụm từ            | IPA                           | Nghĩa tiếng Việt              |
| ---------------------- | ----------------------------- | ----------------------------- |
| technical limitation   | /ˈtek.nɪ.kəl ˌlɪ.mɪˈteɪ.ʃən/  | giới hạn kỹ thuật             |
| performance bottleneck | /pəˈfɔː.məns ˈbɒt.l̩.nek/     | điểm nghẽn hiệu năng          |
| hardware constraint    | /ˈhɑːd.weə kənˈstreɪnt/       | ràng buộc phần cứng           |
| memory usage           | /ˈmem.ər.i ˈjuː.sɪdʒ/         | mức sử dụng bộ nhớ            |
| resolution cap         | /ˌrez.əˈluː.ʃən kæp/          | giới hạn độ phân giải         |
| fallback option        | /ˈfɔːl.bæk ˈɒp.ʃən/           | phương án dự phòng            |
| optimization           | /ˌɒp.tɪ.maɪˈzeɪ.ʃən/          | tối ưu hóa                    |
| rendering engine       | /ˈren.də.rɪŋ ˈen.dʒɪn/        | bộ máy dựng hình (đồ họa)     |
| computational cost     | /ˌkɒm.pjʊˈteɪ.ʃən.əl kɒst/    | chi phí tính toán             |
| device compatibility   | /dɪˈvaɪs ˌkɒm.pə.təˈbɪ.lə.ti/ | khả năng tương thích thiết bị |

---

## 🗣️ Câu mẫu thực tế

### A. Mô tả vấn đề:

* This feature would **exceed the memory limit** on lower-end devices.
* We're currently hitting a **performance bottleneck** with the particle system.
* Unfortunately, that resolution is **not supported on mobile browsers**.

### B. Đề xuất phương án thay thế:

* A possible workaround is to use a **simplified model**.
* We could **reduce the texture size** without affecting visual quality.
* Let’s implement a **lower quality fallback** for weaker devices.

### C. Thảo luận với non-tech team:

* From a technical standpoint, this interaction is **too heavy to render** in real-time.
* We’ll need to **optimize the codebase** before supporting this feature.
* It's doable, but it would require **significant development time**.

---

## ✍️ Bài luyện viết (Writing Practice)

> Viết email giải thích vì sao một hiệu ứng animation không thể chạy trên thiết bị cấu hình thấp.

**Mẫu:**

```text
Hi [PM/Designer],

Thanks for your feedback on the animation effect. While it looks great in the prototype, unfortunately, the current implementation causes major performance issues on low-end Android devices.

The main problem is that the particle system consumes too much memory and CPU. As a workaround, we could switch to a lighter version or remove the background particles on mobile.

Let me know which direction you'd prefer.

Best regards,  
[Your Name]
```

---

## 🎤 Bài luyện nói (Speaking Practice)

> Tình huống: Trình bày lý do tại sao không thể hỗ trợ hiệu ứng 3D blur trong trình duyệt di động.

**Ví dụ thoại:**

> “Right now, 3D blur effects are not supported on most mobile browsers due to WebGL limitations. Even if we simulate it, the performance impact is too high. We can try a 2D blur fallback or static image instead.”

---

## 🧠 Ghi chú mở rộng

### 🎯 Mẹo giao tiếp kỹ thuật hiệu quả:

* Luôn **giải thích đơn giản** nếu người nghe không phải dev.
* Đưa ra **giải pháp thay thế** ngay sau khi nêu vấn đề.
* Dùng các từ “currently”, “at this stage”, “based on our tests” để tránh nói cứng.

### 🧩 Gợi ý mẫu câu mở rộng:

* “Currently, we don’t support...”
* “It’s technically possible, but...”
* “We’ll need to explore other approaches.”

---

Bạn muốn tiếp tục Lesson 31 – “Discussing Performance Optimization” không? Hoặc xuất toàn bộ lessons thành file `.md`?
