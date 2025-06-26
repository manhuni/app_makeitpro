Rất hay khi bạn hỏi! 👏 Dưới đây là một danh sách **những cú pháp JavaScript/TypeScript hiện đại ít được biết đến** (nhưng rất hữu ích), đặc biệt nếu bạn quen với phong cách cũ hoặc không theo sát chuẩn mới (ES6+ trở đi):

---

## ⚙️ 1. **Dấu gạch dưới trong số** (`_`)

Như bạn vừa phát hiện 😄

```ts
let big = 1_000_000;       // Dễ đọc hơn 1000000
```

---

## ✨ 2. **Optional Chaining (`?.`)**

Tránh lỗi `undefined` khi truy cập sâu vào object:

```ts
let name = user?.profile?.name;
// Thay vì: user && user.profile && user.profile.name
```

---

## ❓ 3. **Nullish Coalescing (`??`)**

Chỉ dùng giá trị mặc định **nếu giá trị bên trái là `null` hoặc `undefined`**:

```ts
let value = input ?? "default"; // Chỉ fallback nếu input là null hoặc undefined
```

**Khác với `||`** (vì `||` cũng coi `0`, `false`, `''` là falsy).

---

## 🔄 4. **Logical Assignment (`&&=`, `||=`, `??=`)**

```ts
a ||= 10;   // a = a || 10
b &&= 5;    // b = b && 5
c ??= "hi"; // c = c ?? "hi"
```

---

## 📦 5. **Destructuring with default value**

```ts
const { name = "Unknown", age } = user;
```

---

## 🧪 6. **Array at()** – lấy phần tử bằng index âm

```ts
const arr = [10, 20, 30];
arr.at(-1); // 30
```

---

## 🔁 7. **Numeric separators trong số thập phân**

```ts
let pi = 3.14_15_92; // Có thể dùng `_` cả trong số thực
```

---

## 🔣 8. **Labeled Tuple Elements (TypeScript)**

```ts
type Point = [x: number, y: number]; // Rõ ràng hơn [number, number]
```

---

## 🔧 9. **`as const` để khóa giá trị**

```ts
const roles = ["admin", "user", "guest"] as const;
// roles[0] sẽ là "admin" (string literal), không phải string chung chung
```

---

## 🧩 10. **Template Literal Types (TypeScript nâng cao)**

```ts
type Lang = "vi" | "en";
type FileName = `file_${Lang}.json`; // "file_vi.json", "file_en.json"
```

---

## ✅ Tổng kết cho bạn:

| Tính năng              | Mục đích chính                 |
| ---------------------- | ------------------------------ |
| `1_000_000`            | Dễ đọc số lớn                  |
| `?.`, `??`, `??=`      | Viết gọn, tránh lỗi null       |
| `at(-1)`               | Truy cập phần tử cuối          |
| `as const`             | Tạo kiểu hằng cho array/object |
| Template literal types | Rất mạnh trong TS nâng cao     |

---

Nếu bạn đang làm TypeScript trong Cocos Creator hoặc React Native, rất nhiều thứ trong này bạn có thể áp dụng **ngay lập tức**.

👉 Muốn mình giúp bạn thử áp dụng mấy cái này vào code bạn đang làm không? Hay làm 1 ví dụ minigame demo nhỏ?
