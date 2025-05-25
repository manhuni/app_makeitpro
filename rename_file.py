import os

def rename_files_replace_space_with_underscore(folder_path):
    for filename in os.listdir(folder_path):
        if ' ' in filename:
            new_name = filename.replace(' ', '_')
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            print(f'Renaming: "{filename}" -> "{new_name}"')
            os.rename(old_path, new_path)
    print('Đổi tên hoàn tất!')

if __name__ == '__main__':
    folder = './lib/ipa/pdf'
    if os.path.isdir(folder):
        rename_files_replace_space_with_underscore(folder)
    else:
        print('Đường dẫn không hợp lệ!')
