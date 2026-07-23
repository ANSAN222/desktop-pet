# 🐕 Windows 桌面宠物 - 完整使用指南

## ⚡ 最快开始方式（推荐）

### Windows 用户 - 3秒启动

1. **下载项目**
   ```bash
   git clone https://github.com/ANSAN222/desktop-pet.git
   cd desktop-pet
   ```

2. **双击运行**
   - 直接双击 `run.bat` 文件
   - 程序自动检查环境、安装依赖、生成宠物图片
   - 完成！宠物出现在桌面上

### Mac/Linux 用户

```bash
# 1. 下载项目
git clone https://github.com/ANSAN222/desktop-pet.git
cd desktop-pet

# 2. 赋予执行权限
chmod +x run.sh

# 3. 运行
./run.sh
```

---

## 🎮 使用说明

| 操作 | 效果 |
|------|------|
| **左键单击** 宠物 | 触发随机动画 + 对话 |
| **左键拖动** 宠物 | 移动宠物位置 |
| **鼠标滚轮** | 放大/缩小宠物 |
| **右键点击** | 打开菜单（置顶/退出） |

---

## 🖼️ 自定义你的宠物

### 替换宠物图片

1. 准备一张 PNG 图片（推荐 200x200 或更大）
2. 重命名为 `pet_image.png`
3. 放在项目根目录
4. 重新启动程序

**程序会自动移除白色背景！**

### 修改对话文本

编辑 `main.py`，找到这一段：

```python
self.dialogues = [
    "你好呀~",
    "摸我~",
    "嘿嘿",
    # ... 添加更多对话
]
```

修改后保存，重启程序生效。

---

## 📦 功能特性

✅ **开箱即用** - 下载后直接运行  
✅ **自动生成** - 没有图片时自动生成卡通宠物  
✅ **背景移除** - 自动处理图片白色背景  
✅ **丰富互动** - 跳跃、压扁、抖动三种动画  
✅ **随机对话** - 15句中文对话气泡  
✅ **智能拖动** - 随意移动宠物位置  
✅ **大小调整** - 滚轮快速缩放  
✅ **窗口置顶** - 宠物始终显示在最前面  

---

## 🔧 环境要求

- **Python 3.7+**
- **Windows 10+** （或 macOS、Linux）
- **Pillow 库**（运行脚本会自动安装）

---

## 🐛 常见问题

**Q: 双击 run.bat 没反应？**
- 检查 Windows Defender 是否拦截
- 右键 > 属性 > 解除锁定
- 或者用管理员模式运行

**Q: 怎样让程序开机启动？**
- 将 `run.bat` 快捷方式放在 `C:\Users\[用户名]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

**Q: 怎样修改对话？**
- 编辑 `main.py` 中的 `self.dialogues` 列表

**Q: 宠物图片显示不完全？**
- 确保图片背景是白色或纯色
- 可以用 PS 或在线工具移除背景

---

## 📝 文件说明

```
desktop-pet/
├── main.py                # 主程序（所有功能）
├── requirements.txt       # Python 依赖
├── run.bat               # Windows 一键启动 ⭐
├── run.sh                # Mac/Linux 启动脚本
├── build.bat             # 打包成 EXE（可选）
├── DesktopPet.spec       # 打包配置
└── README.md             # 本文件
```

---

## 🚀 高级使用

### 打包成独立 EXE（无需 Python）

**Windows：**
```bash
build.bat
```

完成后在 `dist/` 文件夹找到 `DesktopPet.exe`

### 修改启动参数

编辑 `main.py` 中的 `DesktopPet` 类初始化部分：

```python
self.pet_size = 200      # 初始大小（像素）
self.pet_x = 100         # 初始 X 位置
self.pet_y = 100         # 初始 Y 位置
```

---

## 💡 创意玩法

- 🎨 用你喜欢的角色图片作为宠物
- 🎤 修改对话为日常提醒词语
- 📱 分享给朋友，一起养宠物
- 🎯 制作自己的专属桌面助手

---

## 📞 获取帮助

- 🐛 发现 Bug：提交 Issue
- 💬 有建议：讨论区或 PR
- 📧 其他问题：查看代码注释

---

## 📄 许可证

MIT License - 自由使用和修改

---

**现在就启动你的桌面宠物吧！🎉**

祝你玩得开心！
