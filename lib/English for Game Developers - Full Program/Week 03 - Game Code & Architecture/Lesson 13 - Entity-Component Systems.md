Dưới đây là nội dung chi tiết cho:

---

# ✅ Lesson 13 – Entity-Component Systems

> 📘 **Mục tiêu bài học:**

* ✅ Làm quen với mô hình **Entity-Component System (ECS)** – kiến trúc phổ biến trong phát triển game hiện đại.
* ✅ Mô tả các thành phần: entity, component, system và cách chúng phối hợp.
* ✅ Tự tin sử dụng từ vựng ECS khi mô tả hoặc trình bày kiến trúc game.

---

## 📚 Từ vựng chính (IPA + nghĩa)

| Từ vựng / Cụm từ        | Phiên âm IPA                      | Nghĩa                                                      |
| ----------------------- | --------------------------------- | ---------------------------------------------------------- |
| entity                  | /ˈen.tə.ti/                       | thực thể – đơn vị độc lập trong game                       |
| component               | /kəmˈpəʊ.nənt/                    | thành phần – dữ liệu mô tả đặc điểm cho entity             |
| system                  | /ˈsɪs.təm/                        | hệ thống – xử lý logic áp dụng cho nhóm entity             |
| entity-component system | /ˈen.tə.ti kəmˈpəʊ.nənt ˈsɪs.təm/ | kiến trúc thực thể-thành phần-hệ thống                     |
| reusable                | /riːˈjuː.zə.bəl/                  | có thể tái sử dụng                                         |
| decoupled               | /ˌdiːˈkʌp.əld/                    | tách biệt – không phụ thuộc vào nhau                       |
| scalable                | /ˈskeɪ.lə.bəl/                    | có thể mở rộng                                             |
| data-driven             | /ˈdeɪ.tə ˈdrɪ.vən/                | điều khiển bởi dữ liệu                                     |
| composition             | /ˌkɒm.pəˈzɪʃ.ən/                  | sự kết hợp                                                 |
| inheritance             | /ɪnˈher.ɪ.təns/                   | kế thừa (so sánh với mô hình hướng đối tượng truyền thống) |

---

## 🗣️ Câu mẫu thực tế

### 1. Mô tả tổng quan:

* Our game uses an **Entity-Component System** architecture for better flexibility.
* Each **entity** is just an ID – it gains behavior through **components**.
* **Systems** operate on entities that match a set of components.

### 2. Chi tiết hoạt động:

* For example, the **MovementSystem** processes entities with both `Position` and `Velocity` components.
* Components are just plain data – no logic inside.
* This design allows for **decoupled** and **scalable** code.

### 3. So sánh:

* Unlike traditional OOP, ECS avoids deep **inheritance** trees.
* The ECS model is more **data-driven** and **composition-based**.

---

## ✍️ Bài luyện viết (Writing Practice)

> Viết đoạn văn ngắn (5–6 câu) mô tả cách ECS được dùng trong game bạn hoặc bạn hiểu như thế nào.

**Gợi ý mẫu:**

> In our project, we use an **Entity-Component-System** architecture.
> Each entity is composed of simple components like `Position`, `Health`, or `Sprite`.
> Systems read and update these components based on game logic.
> For example, the `RenderSystem` draws all entities with `Sprite` and `Position`.
> This makes our code **modular** and easy to maintain.

---

## 🎤 Bài luyện nói (Speaking Practice)

> Trả lời các câu hỏi sau bằng tiếng Anh:

1. What is an Entity-Component-System?
2. How does a system interact with entities?
3. What are the benefits of using ECS over OOP?

**Gợi ý mở đầu:**

* “In ECS, logic is separated from data. Components hold data, and systems apply logic…”
* “One of the biggest advantages is that the architecture is highly **modular** and **scalable**…”

---

## 🧠 Ghi chú mở rộng

* **Ví dụ trực quan:**

```plaintext
Entity: Player #1
→ Components: Position, Velocity, Health

System: MovementSystem
→ Processes all entities with Position + Velocity
```

* **Khi nào nên dùng ECS:**

  * Dự án game có nhiều loại đối tượng động, tái sử dụng logic.
  * Bạn cần tách logic khỏi dữ liệu để dễ bảo trì và kiểm thử.

* **Khác biệt giữa ECS và OOP:**

| ECS                          | OOP                                  |
| ---------------------------- | ------------------------------------ |
| Composition over inheritance | Inheritance-based hierarchy          |
| Systems contain behavior     | Objects contain both data + behavior |
| Data is separated from logic | Data and logic are tightly coupled   |

---

Bạn muốn tiếp tục với **Lesson 14 – Debugging and Logging in English** chứ?
