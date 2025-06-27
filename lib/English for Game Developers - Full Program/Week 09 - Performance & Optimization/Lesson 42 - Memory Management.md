**Lesson 42 - Memory Management (Quản lý bộ nhớ)**:

---

## 📘 **Mục tiêu bài học:**

---

### ✅ 1. Từ vựng chính (IPA + nghĩa)

| Từ vựng             | Phiên âm IPA         | Nghĩa tiếng Việt                                                |
| ------------------- | -------------------- | --------------------------------------------------------------- |
| memory leak         | /ˈmeməri liːk/       | rò rỉ bộ nhớ (không giải phóng bộ nhớ sau khi dùng)             |
| allocation          | /ˌæləˈkeɪʃən/        | việc cấp phát bộ nhớ                                            |
| deallocation        | /diːˌæləˈkeɪʃən/     | việc giải phóng bộ nhớ                                          |
| garbage collection  | /ˈɡɑːbɪdʒ kəˈlekʃən/ | thu gom bộ nhớ không còn dùng (trong các ngôn ngữ như Java, JS) |
| pointer             | /ˈpɔɪntər/           | con trỏ (địa chỉ vùng nhớ)                                      |
| heap                | /hiːp/               | vùng nhớ heap (cấp phát động)                                   |
| stack               | /stæk/               | vùng nhớ stack (cấp phát tĩnh, theo LIFO)                       |
| fragmentation       | /ˌfræɡmenˈteɪʃən/    | phân mảnh bộ nhớ                                                |
| out of memory (OOM) | /aʊt əv ˈmeməri/     | hết bộ nhớ                                                      |
| memory footprint    | /ˈmeməri ˈfʊtprɪnt/  | dung lượng bộ nhớ mà ứng dụng đang sử dụng                      |

---

### ✅ 2. Câu mẫu thực tế

| Câu mẫu                                                                    | Dịch nghĩa                                                          |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| The app crashes due to a memory leak in the image processing module.       | Ứng dụng bị sập do rò rỉ bộ nhớ trong mô-đun xử lý ảnh.             |
| Garbage collection automatically frees unused memory.                      | Bộ thu gom rác tự động giải phóng bộ nhớ không còn dùng đến.        |
| We optimized the memory footprint by compressing assets.                   | Chúng tôi đã tối ưu dung lượng bộ nhớ bằng cách nén các tài nguyên. |
| Stack memory is used for function calls and local variables.               | Bộ nhớ stack dùng cho lời gọi hàm và biến cục bộ.                   |
| The system threw an "Out of Memory" error after loading too many textures. | Hệ thống báo lỗi "hết bộ nhớ" sau khi tải quá nhiều texture.        |

---

### ✅ 3. Bài luyện viết ✍️

**Đề bài:**
Viết một báo cáo mô tả sự cố về bộ nhớ mà bạn gặp phải trong quá trình phát triển ứng dụng.

**Mẫu:**

```
Issue: Memory usage keeps increasing over time, leading to crashes.

Cause: A memory leak in the game loop where old enemy objects are never cleared.

Fix: Added proper deallocation after enemies are removed from the scene.

Result: Memory usage remains stable after running the game for 30+ minutes.
```

---

### ✅ 4. Bài luyện nói 🎤

**Chủ đề:**
**Talk about how you identified and solved a memory problem.**

**Gợi ý trình bày (30–60 giây):**

* What was the symptom (crash, slow performance, OOM)?
* How did you detect the problem (tool, log, behavior)?
* What was the root cause?
* How did you fix it?
* What did you do to prevent it in the future?

---

### ✅ 5. Ghi chú mở rộng

* **Bộ nhớ gồm 2 phần chính:**

  * **Stack:** dùng cho biến cục bộ, kích thước nhỏ, tự động giải phóng.
  * **Heap:** dùng cho dữ liệu lớn, cấp phát động, cần tự giải phóng (hoặc GC).

* **Ngôn ngữ có garbage collection:**

  * Java, JavaScript, Python → không cần gọi `free()` thủ công.
  * Nhưng vẫn có thể bị **rò rỉ logic** nếu biến còn tham chiếu không cần thiết.

* **Ngôn ngữ quản lý bộ nhớ thủ công:**

  * C, C++ → cần dùng `malloc` / `free` (hoặc `new` / `delete`)

* **Công cụ phát hiện vấn đề bộ nhớ:**

  * **Valgrind**, **Instruments (Xcode)**, **Memory Profiler (Chrome DevTools)**, **Android Studio Profiler**, **Visual Studio Diagnostic Tools**

* **Mẹo phòng tránh memory leak:**

  * Giải phóng tài nguyên đúng lúc (close file, stop timer…)
  * Tránh giữ tham chiếu lâu dài không cần thiết
  * Dùng smart pointers (C++) hoặc `weakRef` khi cần

---

Bạn có muốn mình mô phỏng một đoạn mã có lỗi rò rỉ bộ nhớ để bạn phân tích không? Hoặc tạo bài luyện nói với phản hồi mẫu?
