Dưới đây là bài giảng **A03 - Cocos Specific Vocabulary** dành cho lập trình viên học tiếng Anh chuyên ngành, đặc biệt là khi làm việc với **Cocos (Cocos2d-x / Cocos Creator)**. Định dạng chuẩn **Markdown (.md)**, có đầy đủ:

* Từ vựng
* Phiên âm (IPA)
* Nghĩa tiếng Việt
* Giải thích tiếng Anh

---

# A03 - Cocos Specific Vocabulary

## 🎯 Lesson Objective

Learn the key English terms that are specific to the **Cocos game engine**, including their pronunciation, Vietnamese meaning, and usage.

---

## 🎮 About Cocos

**Cocos** is a family of open-source game development tools, including **Cocos2d-x** (C++) and **Cocos Creator** (TypeScript + UI editor). It's widely used for 2D mobile games.

---

## 📘 Cocos Engine Vocabulary

| Term               | IPA Pronunciation       | Vietnamese Meaning          | Description (EN)                              |
| ------------------ | ----------------------- | --------------------------- | --------------------------------------------- |
| `Node`             | /nəʊd/                  | nút (đối tượng trong scene) | Basic element in the scene graph              |
| `Scene`            | /siːn/                  | cảnh                        | A container of game objects                   |
| `Component`        | /kəmˈpəʊ.nənt/          | thành phần                  | Attached to nodes to give them behavior       |
| `Prefab`           | /ˈpriː.fæb/             | mẫu dựng sẵn                | A reusable node template                      |
| `Script`           | /skrɪpt/                | mã điều khiển               | TypeScript/JavaScript code attached to nodes  |
| `AnimationClip`    | /ˌæn.ɪˈmeɪ.ʃən klɪp/    | đoạn hoạt ảnh               | Contains animation keyframes                  |
| `Tween`            | /twiːn/                 | nội suy                     | Smooth animation between values               |
| `Touch Event`      | /tʌtʃ ɪˈvent/           | sự kiện chạm                | Handles finger or mouse input                 |
| `BoundingBox`      | /ˈbaʊn.dɪŋ bɒks/        | hộp bao                     | Rectangular area for collision or positioning |
| `Z Index`          | /ziː ˈɪn.deks/          | thứ tự lớp hiển thị         | Layer order for rendering                     |
| `Opacity`          | /əˈpæs.ə.ti/            | độ mờ                       | Transparency level of a node                  |
| `Label`            | /ˈleɪ.bəl/              | nhãn văn bản                | Used to display text                          |
| `SpriteFrame`      | /spraɪt freɪm/          | khung ảnh                   | Single image from a sprite sheet              |
| `Scheduler`        | /ˈʃed.juː.lər/          | bộ lập lịch                 | Calls functions at intervals                  |
| `Director`         | /dəˈrek.tər/            | trình quản lý cảnh          | Controls game scenes and transitions          |
| `Canvas`           | /ˈkæn.vəs/              | nền canvas                  | Root container for 2D rendering               |
| `AudioSource`      | /ˈɔː.di.oʊ sɔːrs/       | nguồn âm thanh              | Plays background music or sound effects       |
| `CollisionManager` | /kəˈlɪʒ.ən ˈmæn.ɪ.dʒər/ | bộ quản lý va chạm          | Detects and processes collisions              |
| `Physics2D`        | /ˈfɪz.ɪks tuː diː/      | vật lý 2D                   | Enables 2D physics simulation                 |
| `Editor`           | /ˈed.ɪ.tər/             | trình chỉnh sửa             | GUI for scene design and property tweaking    |

---

## 🧠 Code Example (Cocos Creator)

```ts
@ccclass('Player')
export class Player extends Component {
    start() {
        this.node.on(Node.EventType.TOUCH_START, this.onTouchStart, this);
    }

    onTouchStart() {
        this.node.setPosition(100, 100);
    }
}
```

### Key terms:

* `@ccclass` – annotation to define a class
* `Component` – base class for script behavior
* `node.on` – listens to input event
* `setPosition` – moves the node

---

## 🗣️ Speaking Practice

Repeat aloud:

* "The player node has a script component."
* "Each scene contains multiple prefabs and labels."
* "Touch events trigger movement using tweens."

---

## 📝 Mini Quiz

Match the term to its Vietnamese meaning:

1. `Prefab`
2. `Scheduler`
3. `BoundingBox`
4. `Canvas`
5. `Director`

**Options:**

a. trình quản lý cảnh
b. hộp bao
c. mẫu dựng sẵn
d. nền canvas
e. bộ lập lịch

<details>
<summary>🧾 Answers</summary>

1. c
2. e
3. b
4. d
5. a

</details>

---

## 📚 Homework

1. Tạo một prefab đơn giản trong Cocos Creator.
2. Gắn một script xử lý `TOUCH_START`.
3. Ghi chú lại: bạn đã dùng bao nhiêu từ trong bảng từ vựng?

---

Bạn muốn tiếp tục với **A04 - Debugging Vocabulary** hay chuyển sang nội dung nâng cao hơn (ví dụ như **Shader Terms**, **Optimization**, v.v.)?
