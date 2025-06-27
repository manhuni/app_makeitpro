**Lesson 47 - Describing Visual Bugs (Mô tả lỗi hiển thị hình ảnh)**:

---

## 📘 **Mục tiêu bài học**

---

### ✅ 1. Từ vựng chính (IPA + nghĩa)

| Từ vựng            | Phiên âm IPA         | Nghĩa tiếng Việt                             |
| ------------------ | -------------------- | -------------------------------------------- |
| visual bug         | /ˈvɪʒuəl bʌɡ/        | lỗi hiển thị hình ảnh                        |
| glitch             | /ɡlɪtʃ/              | lỗi hình ảnh tạm thời (thường do render sai) |
| overlapping        | /ˌəʊvəˈlæpɪŋ/        | chồng chéo (các phần tử đè lên nhau)         |
| flickering         | /ˈflɪkərɪŋ/          | nhấp nháy (do refresh lỗi)                   |
| misaligned         | /ˌmɪsəˈlaɪnd/        | bị lệch vị trí                               |
| clipping           | /ˈklɪpɪŋ/            | lỗi hiển thị khi vật thể xuyên qua vật khác  |
| texture stretching | /ˈtekstʃə ˈstretʃɪŋ/ | lỗi giãn kết cấu bề mặt                      |
| rendering issue    | /ˈrendə(r)ɪŋ ˈɪʃuː/  | lỗi dựng hình                                |
| resolution         | /ˌrezəˈluːʃn/        | độ phân giải                                 |
| UI artifact        | /ˌɑːtɪfakt/          | hiện tượng lỗi trên giao diện người dùng     |

---

### ✅ 2. Câu mẫu thực tế

| Câu mẫu                                                            | Dịch nghĩa                                                            |
| ------------------------------------------------------------------ | --------------------------------------------------------------------- |
| The health bar is overlapping with the character name.             | Thanh máu đang chồng lên tên nhân vật.                                |
| There’s a flickering issue when switching between scenes.          | Có hiện tượng nhấp nháy khi chuyển giữa các cảnh.                     |
| Some text appears misaligned on smaller screens.                   | Một số văn bản bị lệch vị trí trên màn hình nhỏ.                      |
| The enemy model clips through the wall during the animation.       | Mô hình kẻ địch xuyên tường trong lúc hoạt ảnh.                       |
| We found a rendering bug that causes stretched textures on mobile. | Chúng tôi phát hiện lỗi dựng hình khiến texture bị giãn trên di động. |

---

### ✅ 3. Bài luyện viết ✍️

**Đề bài:**
Viết một đoạn email hoặc báo cáo lỗi (bug report) mô tả một lỗi hiển thị bạn gặp trong game/app. Bao gồm: tình huống xảy ra, thiết bị nếu có, và mô tả lỗi.

**Mẫu:**

```
Title: UI Overlap Bug on Settings Page

Description:
When opening the settings page on a 5.5-inch mobile screen, the text labels overlap with the toggle buttons. The issue happens in both portrait and landscape mode. It looks like the layout doesn't scale correctly on smaller resolutions.

Steps to Reproduce:
1. Open the app on a small screen device.
2. Go to Settings.
3. Observe the overlapping text.

Expected:
Elements should adjust properly to screen size without overlap.
```

---

### ✅ 4. Bài luyện nói 🎤

**Chủ đề:**
**Describe a visual bug you’ve encountered.**

**Gợi ý trình bày (30–60 giây):**

* What was the bug?
* Where and when did it occur?
* What might have caused it?
* How could it be fixed or improved?

---

### ✅ 5. Ghi chú mở rộng

#### 🐞 **Các lỗi hiển thị phổ biến trong phát triển game/app**

| Lỗi              | Mô tả ngắn gọn                                               |
| ---------------- | ------------------------------------------------------------ |
| Clipping         | Nhân vật xuyên tường hoặc xuyên sàn                          |
| Z-fighting       | Hai bề mặt gần nhau nhấp nháy liên tục do tranh quyền vẽ     |
| Missing texture  | Vật thể bị mất kết cấu, hiển thị màu hồng hoặc đen           |
| UI scaling issue | Giao diện không tự điều chỉnh phù hợp độ phân giải khác nhau |
| Camera jitter    | Camera rung nhẹ, thường do tính toán vị trí sai              |
| Ghosting         | Bóng mờ hoặc dư ảnh khi chuyển động nhanh                    |

#### 🛠️ **Cách ghi chú lỗi hiệu quả:**

* **Rõ ràng:** Nêu đúng hành vi sai khác so với kỳ vọng
* **Có ngữ cảnh:** Nêu rõ khi nào và ở đâu lỗi xảy ra
* **Có bước tái hiện (steps to reproduce)** nếu có thể
* **Có mô tả hình ảnh/video đính kèm** nếu làm báo cáo thực tế

---

Bạn có muốn mình giúp tạo một **template báo cáo lỗi chuyên nghiệp** hoặc viết lại đoạn bug report dưới dạng tiếng Anh thương mại?
