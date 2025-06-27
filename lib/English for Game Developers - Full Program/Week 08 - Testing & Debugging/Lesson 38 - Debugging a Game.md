**Lesson 38 - Debugging a Game (Gỡ lỗi một trò chơi)**:

---

## 📘 **Mục tiêu bài học:**

---

### ✅ 1. Từ vựng chính (IPA + nghĩa)

| Từ vựng       | Phiên âm IPA    | Nghĩa tiếng Việt                      |
| ------------- | --------------- | ------------------------------------- |
| debug         | /ˌdiːˈbʌɡ/      | gỡ lỗi, tìm và sửa lỗi trong mã       |
| bug           | /bʌɡ/           | lỗi, sự cố trong phần mềm             |
| glitch        | /ɡlɪtʃ/         | trục trặc nhỏ (thường trong game)     |
| crash         | /kræʃ/          | sập, ngừng hoạt động đột ngột         |
| lag           | /læɡ/           | độ trễ (hiệu suất chậm trong game)    |
| frame rate    | /freɪm reɪt/    | tốc độ khung hình                     |
| breakpoint    | /ˈbreɪkpɔɪnt/   | điểm dừng (trong trình gỡ lỗi)        |
| runtime error | /ˈrʌntaɪm ˈɛrə/ | lỗi xảy ra khi chương trình đang chạy |
| logic error   | /ˈlɒdʒɪk ˈɛrə/  | lỗi logic                             |
| console log   | /ˈkɒnsəʊl lɒɡ/  | ghi log ra bảng điều khiển            |

---

### ✅ 2. Câu mẫu thực tế

| Câu mẫu                                                           | Dịch nghĩa                                                          |
| ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| The game crashes when the player clicks the start button.         | Trò chơi bị sập khi người chơi bấm nút bắt đầu.                     |
| I used breakpoints to trace the issue in the score system.        | Tôi đã dùng breakpoint để lần theo lỗi trong hệ thống điểm.         |
| There’s a glitch in the animation when jumping.                   | Có một lỗi nhỏ trong hoạt ảnh khi nhân vật nhảy.                    |
| The character movement feels laggy on mobile devices.             | Chuyển động của nhân vật bị trễ trên thiết bị di động.              |
| We fixed the bug by resetting the enemy position after collision. | Chúng tôi sửa lỗi bằng cách đặt lại vị trí của kẻ địch sau va chạm. |

---

### ✅ 3. Bài luyện viết ✍️

**Đề bài:**
Mô tả một lỗi trong trò chơi bạn từng gặp hoặc tưởng tượng ra. Bao gồm:

* Hiện tượng lỗi
* Khi nào xảy ra
* Cách bạn tìm ra nguyên nhân
* Cách khắc phục

**Mẫu:**

```
Bug: Player can move while the game is paused.

When: Happens after resuming from pause.

Cause: The pause flag was not checked in the update loop.

Fix: Added a condition to prevent input when isPaused is true.
```

---

### ✅ 4. Bài luyện nói 🎤

**Chủ đề:**
**Talk about how you debugged a game bug.**

**Gợi ý trình bày (30–60 giây):**

* What was the bug?
* How did it affect the game?
* How did you find the cause?
* What tools or techniques did you use (console log, breakpoints, etc.)?
* How did you fix it?

---

### ✅ 5. Ghi chú mở rộng

* **Quy trình gỡ lỗi hiệu quả trong game:**

  1. **Tái tạo lỗi (Reproduce the bug)**: tìm cách tạo lại tình huống xảy ra lỗi.
  2. **Quan sát kết quả đầu ra**: dùng `console.log`, thanh trạng thái, hoặc ghi log.
  3. **Dùng breakpoint** trong IDE hoặc trình gỡ lỗi tích hợp để xem giá trị biến.
  4. **Kiểm tra logic game loop**: lỗi thường xảy ra trong xử lý sự kiện hoặc render.
  5. **Sửa và kiểm thử lại**.

* **Các loại lỗi phổ biến trong game:**

  * Logic sai (đếm điểm sai, sai điều kiện thắng)
  * Va chạm không chính xác
  * Render sai / thiếu khung hình
  * Không đồng bộ sự kiện (event delay)
  * Không phản hồi đầu vào người chơi

---

Bạn muốn mình mô phỏng một đoạn mã bị lỗi để bạn thử mô tả hoặc sửa không? Hoặc bạn có lỗi cụ thể từ dự án game bạn đang làm không?
