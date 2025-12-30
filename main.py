import os
import shutil

# 定义我们要整理的目标文件夹（当前目录）
# 你也可以修改为绝对路径，例如: path = '/Users/username/Downloads'
path = os.getcwd()

# 定义文件类型及其对应的扩展名
extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".md"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

def organize_files():
    # 获取当前目录下所有文件
    files = os.listdir(path)
    
    for file in files:
        # 跳过脚本本身和文件夹
        if file == "main.py" or os.path.isdir(file):
            continue
            
        # 获取文件后缀名
        filename, extension = os.path.splitext(file)
        extension = extension.lower()
        
        # 查找该后缀名属于哪个类别
        moved = False
        for folder_name, ext_list in extensions.items():
            if extension in ext_list:
                # 如果文件夹不存在，则创建
                folder_path = os.path.join(path, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                # 移动文件
                old_path = os.path.join(path, file)
                new_path = os.path.join(folder_path, file)
                shutil.move(old_path, new_path)
                print(f"已移动: {file} -> {folder_name}/")
                moved = True
                break
        
        # 如果文件没有匹配的类型，放入 'Others'
        if not moved:
            other_folder = os.path.join(path, "Others")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(os.path.join(path, file), os.path.join(other_folder, file))
            print(f"已移动: {file} -> Others/")

if __name__ == "__main__":
    print(f"正在整理文件夹: {path} ...")
    organize_files()
    print("整理完成！")
