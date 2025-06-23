Dưới đây là nội dung bài giảng **A04 - TypeScript Vocabulary**, trình bày theo định dạng **Markdown (.md)**, bao gồm từ vựng tiếng Anh chuyên ngành TypeScript, phiên âm IPA, nghĩa tiếng Việt, giải thích, ví dụ code, và phần luyện tập.

---

# A04 - TypeScript Vocabulary

## 🎯 Lesson Objective

Learn essential English vocabulary related to **TypeScript**, including pronunciation, Vietnamese meanings, and how these terms are used in real code.

---

## 📌 What Is TypeScript?

**TypeScript** is a superset of JavaScript that adds static type definitions. It helps developers write safer, more predictable code.

---

## 🧩 TypeScript Vocabulary Table

| Term          | IPA Pronunciation | Vietnamese Meaning        | Description (EN)                                        |
| ------------- | ----------------- | ------------------------- | ------------------------------------------------------- |
| type          | /taɪp/            | kiểu dữ liệu              | Specifies the kind of value (string, number, etc.)      |
| interface     | /ˈɪn.tə.feɪs/     | giao diện                 | Defines a contract for object shapes                    |
| union         | /ˈjuː.njən/       | hợp kiểu                  | Allows multiple possible types                          |
| type alias    | /taɪp ˈeɪ.li.əs/  | bí danh kiểu              | A name for a type or union of types                     |
| optional      | /ˈɒp.ʃən.əl/      | tùy chọn                  | A property or parameter that may be undefined           |
| readonly      | /ˈriːd.ən.li/     | chỉ đọc                   | Prevents modification of a property                     |
| enum          | /ˈiː.nʌm/         | kiểu liệt kê              | Named constants grouped under one type                  |
| generic       | /dʒəˈnɛ.rɪk/      | kiểu tổng quát            | Allows type to be passed as a parameter                 |
| assertion     | /əˈsɜː.ʃən/       | khẳng định kiểu           | Forces the compiler to treat a value as a specific type |
| inferred type | /ɪnˈfɜːd taɪp/    | kiểu được suy diễn        | Type guessed by the compiler                            |
| extends       | /ɪkˈstɛndz/       | kế thừa                   | Inherit properties from another interface               |
| keyof         | /ˈkiː ˌɒv/        | khóa của                  | Get union of keys of a type                             |
| typeof        | /ˈtaɪpˌɒv/        | kiểu của giá trị          | Get type from a value                                   |
| never         | /ˈnev.ər/         | không bao giờ (kiểu rỗng) | Type for functions that never return                    |
| any           | /ˈɛ.ni/           | bất kỳ kiểu nào           | Disables type checking                                  |
| unknown       | /ʌnˈnəʊn/         | kiểu không xác định       | Safer alternative to `any`                              |

---

## 🔡 Example Code

```ts
type ID = string | number;

interface User {
  id: ID;
  name: string;
  isActive?: boolean; // optional
}

function getUserName(user: User): string {
  return user.name;
}
```

### Vocabulary in context:

* `type ID = ...` – type alias
* `?:` – optional property
* `User` – interface
* `string | number` – union type

---

## 🗣️ Speaking Practice

Repeat aloud:

* “This property is optional, but must be a boolean if present.”
* “Use a type alias to improve readability.”
* “Generic types make the function more flexible.”

---

## 📝 Mini Quiz

**Match the term to its meaning:**

1. `readonly`
2. `interface`
3. `type alias`
4. `union`
5. `generic`

**Options:**

a. định nghĩa tên đại diện cho kiểu
b. định nghĩa hình dạng của đối tượng
c. ngăn thay đổi giá trị
d. cho phép nhiều kiểu giá trị
e. cho phép truyền kiểu làm tham số

<details>
<summary>🧾 Answers</summary>

1. c
2. b
3. a
4. d
5. e

</details>

---

## 📚 Homework

1. Khai báo `interface Product` có các thuộc tính: `id`, `name`, `price`, `tags?`.
2. Dùng `type alias` cho `ProductID = string | number`.
3. Viết hàm `getProductName(product: Product): string` và thử với một vài giá trị.
4. Viết 3 câu mô tả code bằng tiếng Anh sử dụng từ vựng bài học.

---

Bạn muốn mình tiếp tục với bài **A05 - Git & Version Control Vocabulary**, hay muốn gộp tất cả bài A01–A04 thành 1 file Markdown tổng hợp?
