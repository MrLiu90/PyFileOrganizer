# 🗂️ PyFileOrganizer (文件整理小助手)

这是一个简单但强大的 Python 脚本，用于自动整理杂乱的文件夹。它会根据文件扩展名，将文件自动归类到 `Images`、`Documents`、`Videos` 等子文件夹中。

## ✨ 功能特点

* **自动化分类**：支持图片、文档、视频、音乐、压缩包等常见格式。
* **零依赖**：只使用 Python 标准库 (`os`, `shutil`)，无需 pip 安装任何东西。
* **兜底处理**：不识别的文件会自动放入 `Others` 文件夹。

## 🚀 如何使用

1.  **克隆仓库**
    ```bash
    git clone [https://github.com/你的用户名/PyFileOrganizer.git](https://github.com/你的用户名/PyFileOrganizer.git)
    cd PyFileOrganizer
    ```

2.  **放置脚本**
    将 `main.py` 放到你需要整理的文件夹中（例如 Downloads 文件夹）。

3.  **运行脚本**
    ```bash
    python main.py
    ```

4.  **查看结果**
    脚本运行后，你会发现所有文件都已整齐地归类到相应的子文件夹中！

## 🛠️ 自定义

你可以打开 `main.py` 并修改 `extensions` 字典来添加更多的文件类型支持。

## 📄 License

MIT License
