import os
import requests

# Tạo thư mục lưu file
os.makedirs("downloads", exist_ok=True)

# Vòng lặp từ 1 đến 44
for i in range(1, 45):
    url = f"https://thesoundofenglish.org/wp-content/uploads/in5-archives/interactive-ipa-chart-22/Interactive%20IPA%20Chart%2022/assets/media/SOUND%20{i}.mp3"
    filename = f"downloads/SOUND_{i}.mp3"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra lỗi HTTP
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Đã tải: SOUND_{i}.mp3")
    except requests.exceptions.RequestException as e:
        print(f"Lỗi với SOUND_{i}.mp3: {e}")
