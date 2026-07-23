@echo off
chcp 65001 >nul
cls

echo ========================================
echo     Windows 桌面宠物程序 - 快速启动
echo ========================================
echo.
echo 正在安装必要的Python库...
echo.

REM 强制更新pip
python -m pip install --upgrade pip -q

REM 安装Pillow
echo 安装 Pillow 图像库...
python -m pip install Pillow --user -q

if %errorlevel% neq 0 (
    echo.
    echo 错误：无法安装Pillow
    echo 请尝试手动安装：
    echo python -m pip install Pillow --user
    echo.
    pause
    exit /b 1
)

echo ✓ 库安装成功
echo.

REM 检查宠物图片
if not exist "pet_image.png" (
    echo 正在生成默认宠物...
    python << 'PYSCRIPT'
from PIL import Image, ImageDraw

img = Image.new('RGBA', (300, 300), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# 绘制头部
draw.ellipse([75, 50, 225, 200], fill=(200, 180, 150, 255), outline=(0, 0, 0, 255), width=3)

# 绘制眼睛
draw.ellipse([110, 100, 140, 130], fill=(0, 0, 0, 255))
draw.ellipse([160, 100, 190, 130], fill=(0, 0, 0, 255))
draw.ellipse([120, 110, 130, 120], fill=(255, 255, 255, 255))
draw.ellipse([170, 110, 180, 120], fill=(255, 255, 255, 255))

# 绘制鼻子
draw.ellipse([145, 145, 155, 155], fill=(0, 0, 0, 255))

# 绘制嘴巴
draw.arc([130, 150, 170, 180], 0, 180, fill=(0, 0, 0, 255), width=2)

# 绘制耳朵
draw.ellipse([70, 50, 110, 100], fill=(200, 180, 150, 255), outline=(0, 0, 0, 255), width=2)
draw.ellipse([190, 50, 230, 100], fill=(200, 180, 150, 255), outline=(0, 0, 0, 255), width=2)

img.save('pet_image.png')
print("✓ 已生成默认宠物图片")
PYSCRIPT
)

echo ✓ 宠物图片已就绪
echo.
echo ========================================
echo 正在启动桌面宠物...
echo 按 Ctrl+C 关闭程序
echo ========================================
echo.

python main.py

if %errorlevel% neq 0 (
    echo.
    echo 程序出错！按任意键继续...
)

pause
