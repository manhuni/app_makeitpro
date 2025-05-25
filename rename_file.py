import os
from unidecode import unidecode

def rename_files_replace_space_and_unicode(folder_path):
    for filename in os.listdir(folder_path):
        if ' ' in filename or any(ord(c) > 127 for c in filename):
            # Thay dấu cách bằng dấu _
            new_name = filename.replace(' ', '_')
            # Chuyển unicode sang ASCII gần đúng
            new_name = unidecode(new_name)
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            print(f'Renaming: "{filename}" -> "{new_name}"')
            os.rename(old_path, new_path)
    print('Đổi tên hoàn tất!')

if __name__ == '__main__':
    folder = './lib/ipa/pdf'
    if os.path.isdir(folder):
        rename_files_replace_space_and_unicode(folder)
    else:
        print('Đường dẫn không hợp lệ!')
