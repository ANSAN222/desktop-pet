# Windows 桌面宠物程序 🐕

一个可爱的Windows桌面宠物程序，支持拖动、互动、对话等功能。

## ✨ 功能特性

- 🎨 **透明无边框窗口** - 美观的桌面宠物显示
- 🐾 **背景移除** - 自动处理图片背景，支持透明效果
- 🎭 **丰富互动** - 支持跳跃、压扁、抖动三种动画
- 💬 **随机对话** - 15句趣味中文对话气泡
- 🖱️ **鼠标操作**：
  - **左键拖动** - 随意移动宠物位置
  - **滚轮缩放** - 调整宠物大小
  - **右键菜单** - 置顶、大小调整、退出选项
- ⭐ **始终置顶** - 宠物始终显示在其他窗口前面
- 📦 **一键运行** - 打包后可直接双击EXE运行

## 🚀 快速开始

### 方式一：直接运行EXE（推荐）

1. 下载 `dist/DesktopPet.exe`
2. 将 `pet_image.png` 放在同一目录
3. 双击 `DesktopPet.exe` 运行

### 方式二：Python源码运行

#### 环境要求
- Python 3.7+
- Windows 系统

#### 安装依赖
```bash
pip install -r requirements.txt
```

#### 运行程序
```bash
python main.py
```

### 方式三：自己打包

#### 安装构建工具
```bash
pip install -r requirements.txt
pip install pyinstaller
```

#### 构建EXE
**Windows:**
```bash
build.bat
```

**Linux/Mac:**
```bash
bash build.sh
```

打包完成后，EXE文件会在 `dist/` 目录下。

## 🎮 使用方法

| 操作 | 功能 |
|------|------|
| **左键单击** | 触发动画 + 显示对话 |
| **左键拖动** | 移动宠物位置 |
| **鼠标滚轮** | 调整宠物大小 |
| **右键点击** | 打开菜单 |
| **菜单 > 置顶开关** | 切换窗口置顶 |
| **菜单 > 退出** | 关闭程序 |

## 📁 文件说明

```
desktop-pet/
├── main.py              # 主程序源码
├── requirements.txt     # Python依赖
├── DesktopPet.spec     # PyInstaller打包配置
├── build.bat           # Windows打包脚本
├── build.sh            # Linux/Mac打包脚本
├── pet_image.png       # 宠物图片（需要自行提供）
└── README.md           # 本文件
```

## 🖼️ 宠物图片

需要将你的宠物图片放在项目根目录，命名为 `pet_image.png`。

**图片要求：**
- 格式：PNG、JPG 等常见格式
- 建议背景为白色或纯色（程序会自动移除）
- 推荐大小：200x200px 及以上

## 🎨 自定义选项

编辑 `main.py` 中的 `self.dialogues` 列表来修改对话文本：

```python
self.dialogues = [
    "你好呀~",
    "摸我~",
    # ... 添加更多对话
]
```

## 🐛 常见问题

**Q: 为什么看不到宠物？**
- 确保 `pet_image.png` 在正确位置
- 检查图片格式是否正确
- 尝试将背景改为白色

**Q: 怎样修改宠物大小？**
- 使用鼠标滚轮调整
- 或右键菜单中选择"调整大小"

**Q: 如何修改对话文本？**
- 编辑 `main.py` 中的 `self.dialogues` 列表

**Q: 能否改变动画速度？**
- 编辑 `main.py` 中 `play_animation()` 方法的 `self.root.after(30, animate)` 参数（单位毫秒）

## 📝 许可证

MIT License

## 👨‍💻 开发

欢迎提交 Issue 和 Pull Request！

---

**祝你玩得开心！🎉**
