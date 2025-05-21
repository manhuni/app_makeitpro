# 📘 Bài học: Quản lý trạng thái với Provider trong Flutter

## 1. Giới thiệu

Khi ứng dụng của bạn trở nên phức tạp hơn, việc truyền dữ liệu giữa các widget trở nên khó khăn. `Provider` là một giải pháp hiệu quả để **quản lý trạng thái** và **chia sẻ dữ liệu** trong cây widget.

---

## 2. Provider là gì?

Provider là một thư viện state management được chính Google đề xuất. Nó dễ học, dễ tích hợp, và phù hợp với các ứng dụng vừa và nhỏ.

> 📦 Gói cần thiết: `provider: ^6.0.5` (hoặc bản mới nhất)

---

## 3. Cài đặt

Thêm vào file `pubspec.yaml`:

```yaml
dependencies:
  flutter:
    sdk: flutter
  provider: ^6.0.5
```

---

## 4. Ví dụ cơ bản

```dart
class Counter with ChangeNotifier {
  int _count = 0;

  int get count => _count;

  void increment() {
    _count++;
    notifyListeners(); // Cập nhật giao diện
  }
}
```

**Khởi tạo Provider:**

```dart
void main() {
  runApp(
    ChangeNotifierProvider(
      create: (_) => Counter(),
      child: MyApp(),
    ),
  );
}
```

**Sử dụng trong widget:**

```dart
Consumer<Counter>(
  builder: (context, counter, _) => Text('${counter.count}'),
),
```

---

## 5. Ghi nhớ quan trọng

✅ Provider hoạt động tốt với ChangeNotifier  
✅ Tránh gọi `notifyListeners()` không cần thiết  
✅ Không nên dùng `BuildContext.read` trong `build()`

---

## 6. Bài tập thực hành

1. Tạo một lớp `TodoList` quản lý danh sách công việc với Provider.  
2. Thêm tính năng xóa và thêm công việc.  
3. Hiển thị danh sách công việc theo `ListView.builder`.

---

## 7. Tài nguyên tham khảo

- [Provider Package - pub.dev](https://pub.dev/packages/provider)
- [State Management - Flutter Docs](https://docs.flutter.dev/data-and-backend/state-mgmt/intro)

---

> 💡 Mẹo: Khi gặp lỗi widget không rebuild, kiểm tra lại vị trí đặt Provider và cách bạn sử dụng `Consumer`.

---

_Tác giả: Thầy Trần Minh • Cập nhật: 04/2025_
